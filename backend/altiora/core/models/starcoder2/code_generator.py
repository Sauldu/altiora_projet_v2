# backend/altiora/core/models/starcoder2/code_generator.py
"""
Génération de code de test avec templates Starcoder2.
Version améliorée avec support Playwright optimisé.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from altiora.core.models.starcoder2.model_manager import Starcoder2Manager
from altiora.core.models.starcoder2.playwright_templates import (
    PlaywrightTemplates, 
    PlaywrightOptimizer,
    TestType
)


class TestCodeGenerator:
    """Génère des templates de test (pytest, playwright…)."""

    def __init__(self, manager: Starcoder2Manager) -> None:
        self.manager = manager
        self.playwright_templates = PlaywrightTemplates()
        self.playwright_optimizer = PlaywrightOptimizer()

    async def generate_pytest(self, spec_path: Path) -> str:
        """Génère un fichier pytest à partir d'une spec."""
        spec_text = spec_path.read_text(encoding="utf-8")
        description = f"pytest tests for {spec_path.name}: {spec_text[:300]}..."
        return await self.manager.generate_code(
            language="python",
            description=description,
            framework="pytest",
        )

    async def generate_playwright(
        self,
        spec_path: Path,
        test_type: Optional[TestType] = None,
        config: Optional[Dict[str, str]] = None
    ) -> Tuple[str, List[str]]:
        """
        Génère des tests Playwright optimisés.
        
        Args:
            spec_path: Chemin vers la spécification
            test_type: Type de test forcé (sinon détection auto)
            config: Configuration (URLs, auth, etc.)
            
        Returns:
            Tuple (code généré, liste des warnings)
        """
        spec_text = spec_path.read_text(encoding="utf-8")
        
        # Détection automatique du type si non spécifié
        if not test_type:
            test_type = self._detect_test_type(spec_text)
        
        # Extraction des éléments de test depuis la spec
        test_elements = self._extract_test_elements(spec_text)
        
        # Création du prompt optimisé pour StarCoder2
        prompt = PlaywrightTemplates.create_starcoder_prompt(
            test_type=test_type,
            description=f"Tests for {spec_path.stem}: {spec_text[:500]}...",
            context={
                **(config or {}),
                "detected_elements": test_elements,
                "test_count": len(test_elements.get("scenarios", [])),
            }
        )
        
        # Génération via StarCoder2
        raw_code = await self.manager.generate_code(
            language="typescript",
            description=prompt,
            framework="playwright"
        )
        
        # Post-processing et optimisation
        optimized_code = self._post_process_code(raw_code, test_type)
        
        # Validation syntaxique
        warnings = self._validate_playwright_code(optimized_code)
        
        return optimized_code, warnings

    def _detect_test_type(self, spec_text: str) -> TestType:
        """
        Détecte automatiquement le type de test basé sur le contenu.
        
        Args:
            spec_text: Texte de la spécification
            
        Returns:
            Type de test détecté
        """
        spec_lower = spec_text.lower()
        
        # Patterns de détection
        patterns = {
            TestType.API: [
                r"api\s+(endpoint|request|response)",
                r"(get|post|put|delete)\s+/\w+",
                r"status\s+code\s+\d{3}",
                r"json\s+response",
            ],
            TestType.COMPONENT: [
                r"component\s+(test|spec)",
                r"render\s+(button|form|input)",
                r"props\s+validation",
                r"isolated\s+testing",
            ],
            TestType.VISUAL: [
                r"visual\s+(regression|test)",
                r"screenshot\s+comparison",
                r"pixel\s+perfect",
                r"ui\s+consistency",
            ],
            TestType.ACCESSIBILITY: [
                r"(a11y|accessibility)\s+test",
                r"aria\s+(label|role)",
                r"screen\s+reader",
                r"wcag\s+compliance",
            ],
        }
        
        # Comptage des correspondances
        scores = {}
        for test_type, type_patterns in patterns.items():
            score = sum(1 for pattern in type_patterns if re.search(pattern, spec_lower))
            scores[test_type] = score
        
        # Retour du type avec le plus de correspondances
        if max(scores.values()) > 0:
            return max(scores, key=scores.get)
        
        # Par défaut : E2E
        return TestType.E2E

    def _extract_test_elements(self, spec_text: str) -> Dict[str, List[str]]:
        """
        Extrait les éléments testables de la spécification.
        
        Args:
            spec_text: Texte de la spécification
            
        Returns:
            Dictionnaire des éléments extraits
        """
        elements = {
            "scenarios": [],
            "actions": [],
            "validations": [],
            "inputs": [],
            "buttons": [],
        }
        
        # Extraction des scénarios (lignes commençant par nombres ou tirets)
        scenario_patterns = [
            r"^\d+\.\s+(.+)$",  # 1. Scenario
            r"^-\s+(.+)$",      # - Scenario
            r"^Scenario:\s+(.+)$",  # Scenario: description
        ]
        
        for pattern in scenario_patterns:
            scenarios = re.findall(pattern, spec_text, re.MULTILINE)
            elements["scenarios"].extend(scenarios)
        
        # Extraction des actions
        action_keywords = ["click", "fill", "select", "navigate", "submit", "upload"]
        for keyword in action_keywords:
            if keyword in spec_text.lower():
                elements["actions"].append(keyword)
        
        # Extraction des éléments UI
        ui_patterns = {
            "inputs": r"(input|field|textbox)\s+(?:for\s+)?(['\"]?)(\w+)\2",
            "buttons": r"(button|link)\s+(?:labeled\s+)?(['\"]?)(.+?)\2",
        }
        
        for element_type, pattern in ui_patterns.items():
            matches = re.findall(pattern, spec_text, re.IGNORECASE)
            elements[element_type].extend([match[2] for match in matches])
        
        return elements

    def _post_process_code(self, raw_code: str, test_type: TestType) -> str:
        """
        Post-traite et optimise le code généré.
        
        Args:
            raw_code: Code brut de StarCoder2
            test_type: Type de test
            
        Returns:
            Code optimisé
        """
        # Nettoyage des markers StarCoder
        code = raw_code.replace("<|endoftext|>", "")
        code = re.sub(r"<fim_[^>]+>", "", code)
        
        # Application des optimisations
        code = self.playwright_optimizer.add_retry_logic(code)
        code = self.playwright_optimizer.add_error_handling(code)
        code = self.playwright_optimizer.optimize_selectors(code)
        
        # Ajout des imports manquants si nécessaire
        if "import { test, expect }" not in code:
            code = "import { test, expect } from '@playwright/test';\n\n" + code
        
        # Ajout de configuration spécifique au type
        if test_type == TestType.API and "use: {" not in code:
            api_config = """
test.use({
    baseURL: process.env.API_BASE_URL || 'http://localhost:3000',
    extraHTTPHeaders: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    },
});
"""
            code = code.replace("import { test, expect }", 
                              f"import {{ test, expect }} from '@playwright/test';\n{api_config}")
        
        return code

    def _validate_playwright_code(self, code: str) -> List[str]:
        """
        Valide la syntaxe et la structure du code Playwright.
        
        Args:
            code: Code à valider
            
        Returns:
            Liste des warnings
        """
        warnings = []
        
        # Vérifications de base
        if "test(" not in code and "test.describe(" not in code:
            warnings.append("Aucun test trouvé dans le code généré")
        
        if "expect(" not in code:
            warnings.append("Aucune assertion trouvée")
        
        # Vérification des imports
        required_imports = ["@playwright/test"]
        for import_name in required_imports:
            if import_name not in code:
                warnings.append(f"Import manquant : {import_name}")
        
        # Vérification de la structure
        open_braces = code.count("{")
        close_braces = code.count("}")
        if open_braces != close_braces:
            warnings.append(f"Déséquilibre des accolades : {open_braces} ouvertes, {close_braces} fermées")
        
        # Vérification des awaits
        async_calls = re.findall(r"(page\.\w+|expect)\(", code)
        for call in async_calls:
            if not re.search(rf"await\s+{re.escape(call)}", code):
                warnings.append(f"'await' potentiellement manquant pour {call}")
        
        # Vérification des selectors
        selectors = re.findall(r"['\"]([.#]\w+|\/\/|\[)['\"]", code)
        for selector in selectors:
            if selector.startswith((".class", "#id")):
                warnings.append(f"Selector fragile détecté : {selector}. Préférer data-test ou getByRole")
        
        return warnings

    async def generate_test_suite(
        self,
        spec_dir: Path,
        output_dir: Path,
        test_types: Optional[List[TestType]] = None
    ) -> Dict[str, Dict[str, any]]:
        """
        Génère une suite complète de tests depuis un dossier de specs.
        
        Args:
            spec_dir: Dossier contenant les spécifications
            output_dir: Dossier de sortie pour les tests
            test_types: Types de tests à générer (tous par défaut)
            
        Returns:
            Résultats de génération par fichier
        """
        results = {}
        output_dir.mkdir(parents=True, exist_ok=True)
        
        # Parcours des fichiers de spec
        for spec_file in spec_dir.glob("*.{txt,md,json}"):
            file_results = {
                "generated": [],
                "warnings": [],
                "errors": []
            }
            
            try:
                # Détermination des types à générer
                if test_types:
                    types_to_generate = test_types
                else:
                    detected_type = self._detect_test_type(spec_file.read_text())
                    types_to_generate = [detected_type]
                
                # Génération pour chaque type
                for test_type in types_to_generate:
                    output_file = output_dir / f"{spec_file.stem}.{test_type.value}.spec.ts"
                    
                    code, warnings = await self.generate_playwright(
                        spec_file,
                        test_type=test_type
                    )
                    
                    # Écriture du fichier
                    output_file.write_text(code, encoding="utf-8")
                    
                    file_results["generated"].append({
                        "type": test_type.value,
                        "file": str(output_file),
                        "size": len(code)
                    })
                    file_results["warnings"].extend(warnings)
                    
            except Exception as e:
                file_results["errors"].append(str(e))
            
            results[spec_file.name] = file_results
        
        return results


# Configuration des patterns de code fréquents pour cache Redis
COMMON_PATTERNS = {
    "login_flow": {
        "description": "Standard login flow with email/password",
        "code_snippet": """
await page.goto('/login');
await page.fill('[data-test="email-input"]', email);
await page.fill('[data-test="password-input"]', password);
await page.click('[data-test="submit-button"]');
await expect(page).toHaveURL('/dashboard');
"""
    },
    "form_validation": {
        "description": "Form field validation pattern",
        "code_snippet": """
// Test champ requis
await page.click('[data-test="submit-button"]');
await expect(page.locator('.error-message')).toContainText('required');

// Test format email
await page.fill('[data-test="email-input"]', 'invalid-email');
await page.click('[data-test="submit-button"]');
await expect(page.locator('.error-message')).toContainText('valid email');
"""
    },
    "api_auth": {
        "description": "API authentication pattern",
        "code_snippet": """
const token = await getAuthToken();
const response = await request.get('/api/endpoint', {
    headers: {
        'Authorization': `Bearer ${token}`
    }
});
expect(response.status()).toBe(200);
"""
    }
}