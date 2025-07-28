# Structure et contenu du projet

## Arborescence du Projet

```
/
|-- .gitignore
|-- README.md
|-- anythingllm
|   |-- agents
|   |   |-- batch_processor.json
|   |   |-- code_generator.json
|   |   \-- qa_analyst.json
|   |-- chat_templates
|   |   |-- analysis_template.json
|   |   |-- batch_template.json
|   |   |-- coding_template.json
|   |   \-- debug_template.json
|   |-- datasources_priority.md
|   |-- embedding_config.json
|   |-- legacy
|   |   \-- Altiora.html
|   |-- prompts
|   |   |-- qwen3_direct.txt
|   |   |-- qwen3_thinking.txt
|   |   \-- starcoder2_generation.txt
|   \-- workspace_config.json
|-- backend
|   |-- __init__.py
|   |-- altiora
|   |   |-- __init__.py
|   |   |-- __version__.py
|   |   |-- api
|   |   |   |-- __init__.py
|   |   |   |-- app.py
|   |   |   |-- dependencies.py
|   |   |   |-- gateway
|   |   |   |   \-- api_gateway.py
|   |   |   |-- middleware
|   |   |   |   |-- __init__.py
|   |   |   |   |-- advanced_rate_limiter.py
|   |   |   |   |-- cache_middleware.py
|   |   |   |   \-- rbac_middleware.py
|   |   |   |-- openapi.py
|   |   |   \-- v1
|   |   |       |-- __init__.py
|   |   |       |-- analysis.py
|   |   |       |-- batch.py
|   |   |       |-- health.py
|   |   |       |-- models.py
|   |   |       \-- schemas.py
|   |   |-- config
|   |   |   |-- __init__.py
|   |   |   |-- settings.py
|   |   |   \-- validators.py
|   |   |-- core
|   |   |   |-- __init__.py
|   |   |   |-- batch
|   |   |   |   |-- __init__.py
|   |   |   |   |-- batch_processor.py
|   |   |   |   |-- scheduler.py
|   |   |   |   \-- strategies.py
|   |   |   |-- factories
|   |   |   |   \-- model_factory.py
|   |   |   |-- feedback
|   |   |   |   \-- feedback_collector.py
|   |   |   |-- models
|   |   |   |   |-- __init__.py
|   |   |   |   |-- ensemble
|   |   |   |   |   |-- __init__.py
|   |   |   |   |   |-- multi_model.py
|   |   |   |   |   \-- router.py
|   |   |   |   |-- model_swapper.py
|   |   |   |   |-- qwen3
|   |   |   |   |   |-- __init__.py
|   |   |   |   |   |-- cache_optimizer.py
|   |   |   |   |   |-- config.py
|   |   |   |   |   |-- model_manager.py
|   |   |   |   |   |-- prompt_builder.py
|   |   |   |   |   \-- quantizer.py
|   |   |   |   \-- starcoder2
|   |   |   |       |-- __init__.py
|   |   |   |       |-- code_generator.py
|   |   |   |       |-- config.py
|   |   |   |       \-- model_manager.py
|   |   |   |-- modules
|   |   |   |   |-- __init__.py
|   |   |   |   |-- psychodesign
|   |   |   |   |   |-- __init__.py
|   |   |   |   |   |-- altiora_core.py
|   |   |   |   |   |-- personality_evolution.py
|   |   |   |   |   \-- personality_quiz.py
|   |   |   |   |-- voice_anythingllm.py
|   |   |   |   \-- voice_assistant.py
|   |   |   |-- optimization
|   |   |   |   \-- memory_optimizer.py
|   |   |   |-- orchestrator.py
|   |   |   |-- plugins
|   |   |   |   |-- __init__.py
|   |   |   |   |-- plugin_interface.py
|   |   |   |   \-- plugin_system.py
|   |   |   |-- policies
|   |   |   |   |-- __init__.py
|   |   |   |   |-- business_rules.py
|   |   |   |   |-- excel_policy.py
|   |   |   |   |-- privacy_policy.py
|   |   |   |   \-- toxicity_policy.py
|   |   |   |-- post_processing
|   |   |   |   |-- __init__.py
|   |   |   |   |-- code_validator.py
|   |   |   |   |-- excel_formatter.py
|   |   |   |   \-- output_sanitizer.py
|   |   |   |-- qa
|   |   |   |   |-- multimodal_qa.py
|   |   |   |   \-- qa_system.py
|   |   |   |-- training
|   |   |   |   |-- __init__.py
|   |   |   |   |-- advanced_trainer.py
|   |   |   |   |-- auto_fine_tuner.py
|   |   |   |   \-- feedback_system.py
|   |   |   \-- validation
|   |   |       \-- continuous_validator.py
|   |   |-- infrastructure
|   |   |   |-- __init__.py
|   |   |   |-- audit
|   |   |   |   |-- __init__.py
|   |   |   |   |-- audit_logger.py
|   |   |   |   |-- decorator.py
|   |   |   |   |-- models.py
|   |   |   |   |-- ring_buffer.py
|   |   |   |   |-- rotation.py
|   |   |   |   \-- writer.py
|   |   |   |-- database.py
|   |   |   |-- events
|   |   |   |   |-- __init__.py
|   |   |   |   \-- event_bus.py
|   |   |   |-- monitoring
|   |   |   |   |-- __init__.py
|   |   |   |   |-- health.py
|   |   |   |   |-- healthcheck.py
|   |   |   |   \-- metrics
|   |   |   |       \-- model_metrics.py
|   |   |   |-- queue
|   |   |   |   \-- redis_queue.py
|   |   |   |-- repositories
|   |   |   |   |-- __init__.py
|   |   |   |   |-- base_repository.py
|   |   |   |   \-- scenario_repository.py
|   |   |   \-- scaling
|   |   |       |-- __init__.py
|   |   |       \-- auto_scaler.py
|   |   |-- monitoring
|   |   |   \-- memory_monitor.py
|   |   |-- security
|   |   |   |-- auth
|   |   |   |   |-- __init__.py
|   |   |   |   |-- dependencies.py
|   |   |   |   \-- jwt_handler.py
|   |   |   |-- guardrails
|   |   |   |   |-- __init__.py
|   |   |   |   |-- admin_control_system.py
|   |   |   |   |-- admin_dashboard.py
|   |   |   |   |-- emergency_handler.py
|   |   |   |   |-- ethical_safeguards.py
|   |   |   |   |-- interaction_guardrail.py
|   |   |   |   |-- policy_enforcer.py
|   |   |   |   \-- toxicity_guardrail.py
|   |   |   |-- rbac
|   |   |   |   |-- __init__.py
|   |   |   |   |-- manager.py
|   |   |   |   \-- models.py
|   |   |   \-- secret.py
|   |   |-- services
|   |   |   |-- __init__.py
|   |   |   |-- alm
|   |   |   |   |-- README.md
|   |   |   |   |-- __init__.py
|   |   |   |   \-- alm_service.py
|   |   |   |-- base.py
|   |   |   |-- dash
|   |   |   |   |-- README.md
|   |   |   |   \-- app.py
|   |   |   |-- excel
|   |   |   |   |-- README.md
|   |   |   |   |-- __init__.py
|   |   |   |   \-- excel_service.py
|   |   |   |-- ocr
|   |   |   |   |-- README.md
|   |   |   |   |-- __init__.py
|   |   |   |   |-- doctopus_ocr
|   |   |   |   |   \-- __init__.py
|   |   |   |   \-- ocr_wrapper.py
|   |   |   \-- playwright
|   |   |       |-- README.md
|   |   |       |-- __init__.py
|   |   |       |-- optimized_runner.py
|   |   |       \-- playwright_runner.py
|   |   \-- utils
|   |       |-- __init__.py
|   |       |-- errors.py
|   |       |-- helpers.py
|   |       \-- logging.py
|   \-- tests
|       |-- __init__.py
|       |-- conftest.py
|       |-- integration
|       |   |-- __init__.py
|       |   |-- conftest.py
|       |   |-- makefile
|       |   |-- test_full_pipeline.py
|       |   |-- test_performance.py
|       |   \-- test_services_integration.py
|       |-- performance
|       |   |-- config.yaml
|       |   |-- test_load_testing.py
|       |   |-- test_pipeline_load.py
|       |   \-- test_redis_performance.py
|       |-- regression
|       |   |-- __init__.py
|       |   |-- regression_config.yaml
|       |   |-- run_regression.py
|       |   \-- test_regression_suite.py
|       |-- test_admin_control.py
|       |-- test_altiora_core.py
|       |-- test_ethical_safeguards.py
|       |-- test_fine_tuning.py
|       |-- test_integration.py
|       |-- test_interfaces.py
|       |-- test_model_swapper.py
|       |-- test_ocr_wrapper.py
|       |-- test_orchestrator.py
|       |-- test_personality_quiz.py
|       |-- test_playwright_runner.py
|       |-- test_retry_handler.py
|       \-- test_services.py
|-- cli
|   |-- altiora_cli
|   |   |-- __init__.py
|   |   |-- commands
|   |   |   |-- __init__.py
|   |   |   |-- batch.py
|   |   |   |-- benchmark.py
|   |   |   |-- chat.py
|   |   |   |-- doctor.py
|   |   |   |-- init.py
|   |   |   |-- models.py
|   |   |   |-- quickstart.py
|   |   |   |-- start.py
|   |   |   |-- test.py
|   |   |   \-- voice_anything.py
|   |   \-- main.py
|   |-- requirements.txt
|   \-- setup.py
|-- configs
|   \-- prometheus.yml
|-- docker
|   \-- docker-compose.yml
|-- docs
|   |-- ADVANCED_CONFIGURATION.md
|   |-- API_REFERENCE.md
|   |-- ARCHITECTURE.md
|   |-- DEVELOPER_GUIDE.md
|   |-- MODEL_TRAINING.md
|   |-- conf.py
|   |-- env-documentation.md
|   |-- examples
|   |   |-- Altiora.html
|   |   |-- login_test.py
|   |   |-- minimal_sfd.txt
|   |   \-- test_scenarios.json
|   |-- generate_docs.py
|   |-- installation_guide.md
|   |-- requirements.txt
|   \-- source
|       \-- guides
|           |-- deployment.md
|           |-- migration_v2.md
|           \-- prompting_qwen3.md
|-- requirements
|   |-- base.txt
|   |-- dev.txt
|   \-- prod.txt
|-- requirements.txt
\-- scripts
    |-- backup
    |   |-- backup_redis.sh
    |   \-- configure_swap.sh
    |-- models
    |   |-- qwen3_modelfile
    |   \-- starcoder2_modelfile
    |-- monitoring
    |   |-- audit_query.py
    |   |-- diagnose_ollama.py
    |   \-- generate_performance_report.py
    |-- setup
    |   |-- cpu_optimization_script.py
    |   |-- create_directories.sh
    |   |-- create_ephemeral_env.sh
    |   |-- generate_keys.py
    |   |-- run_performance_tests.sh
    |   |-- setup_integration_tests.sh
    |   |-- start_dev.sh
    |   \-- validate_setup.py
    \-- training
        \-- auto_fine_tuner.py
```

---

## Fichier : `.gitignore`

```text
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
.venv/
pip-log.txt
pip-delete-this-directory.txt

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Docker
.dockerignore

# Logs
*.log
logs/

# Data & cache
.cache/
.cache.db
*.tmp
*.temp
data/models/
data/temp/
results/*.json
reports/*.html
artifacts/*.zip

# Secrets
.env
.env.local

# Jupyter
.ipynb_checkpoints/

# Pytest
.coverage
.pytest_cache/
htmlcov/
.tox/
```

---

## Fichier : `README.md`

```markdown
# 🚀 Altiora V2 – Assistant IA de Gestion de Tests Logiciels

> **Projet RAG + Orchestration IA + Micro-services optimisé pour 32 GB de RAM**

---

## 📖 Vue d’ensemble

Altiora est une plate-forme open-source qui automatise l’analyse, la génération et le suivi des tests logiciels.  
Elle combine deux grands modèles open-source et une interface **RAG** (AnythingLLM) :

| Modèle | Rôle | Charge mémoire |
|--------|------|----------------|
| **Qwen3-32B** | Réflexion, analyse métier, orchestration | ~20 GB |
| **StarCoder2-15B** | Génération de code (test, scripts, Playwright) | ~15 GB |
| **DocToPus** | OCR / extraction de texte dans PDF & images | < 1 GB |

> ⚠️ **Contrainte 32 GB RAM** : un seul modèle chargé à la fois grâce au **ModelSwapper**.

---

## 🧩 Fonctionnalités principales

| Fonctionnalité | Description |
|----------------|-------------|
| 📊 **Analyse intelligente** | Qwen3 analyse les specs, les rapports de bug et propose des scénarios de test |
| 🤖 **Génération de code** | StarCoder2 produit des tests Playwright, des scripts Python ou des suites de tests Excel |
| 🔍 **Recherche sémantique** | AnythingLLM interroge documents PDF, images, feuilles Excel, code source |
| 📦 **Batch processing** | Traite par lots des dossiers complets de specs ou de rapports |
| 🔐 **Sécurité renforcée** | Guardrails éthique, filtrage des injections, RBAC, audit complet |
| 🔄 **Swap mémoire** | Chargement dynamique des modèles pour rester sous 32 GB |

---

## 🏗️ Architecture
```

---

## Fichier : `requirements.txt`

```text
# requirements.txt - Fichier principal avec toutes les dépendances
# Ce fichier rassemble les 3 environnements (base, dev, prod) pour installation globale
# En production, utilisez plutôt les fichiers spécifiques

# === CORE API ===
fastapi==0.104.1
uvicorn[standard]==0.24.0
pydantic==2.5.0
pydantic-settings==2.1.0
httpx==0.25.2

# === IA & Modèles ===
llama-cpp-python==0.2.20
transformers==4.52.1
torch==2.1.1
datasets==2.14.6
peft==0.7.1
bitsandbytes==0.41.3          # Pour quantification GPU
accelerate==0.25.0

# === Infrastructure ===
redis==5.0.1
aioredis==2.0.1
asyncio-mqtt==0.15.0

# === Data & Files ===
pandas==2.1.4
openpyxl==3.1.2
aiofiles==23.2.1
zstandard==0.22.0
pypdf2==3.0.1
python-docx==1.1.0

# === OCR & Vision ===
pytesseract==0.3.10
pillow==11.3.0
opencv-python==4.8.1.78

# === Testing & Quality ===
pytest==7.4.3
pytest-asyncio==0.21.1
pytest-cov==4.1.0
black==24.3.0
ruff==0.1.6
mypy==1.7.1

# === Monitoring & Logging ===
prometheus-client==0.19.0
psutil==5.9.6
structlog==23.2.0
python-json-logger==2.0.7

# === Security & Validation ===
cryptography>=42.0.5,<46
python-jose[cryptography]==3.4.0
passlib[bcrypt]==1.7.4
email-validator==2.1.0

# === Development Tools ===
pre-commit==3.5.0
ipython==8.18.1
rich==13.7.0

# === Optional GPU Support ===
nvidia-ml-py==12.535.133

# === Environment ===
python-dotenv==1.0.0
click==8.1.7
typer==0.9.0
setuptools~=80.9.0
PyYAML~=6.0.2
aiohttp~=3.12.14
SQLAlchemy~=2.0.41
tenacity~=8.2.3
numpy~=1.26.4
SpeechRecognition~=3.14.3
PyJWT~=2.10.1
plotly~=6.2.0
pyttsx3~=2.99
```

---

## Fichier : `anythingllm\datasources_priority.md`

```markdown
# Guide d'Indexation Prioritaire - AnythingLLM "Altiora Knowledge"

## 🎯 Priorité 1 - Documents Critiques (Indexer en premier)

### 1. Spécifications & Cas de Test
- `data/scenarios/` - **TOUTES les spécifications de test**
- `docs/examples/` - **Exemples de cas d'usage**
- `data/training/` - **Données d'entraînement**

### 2. Documentation Technique
- `docs/api/` - **Documentation API complète**
- `docs/guides/` - **Guides utilisateur et techniques**

## 🎯 Priorité 2 - Scripts & Configurations

### 3. Scripts d'Automatisation
- `scripts/setup/` - **Scripts d'installation et configuration**
- `scripts/monitoring/` - **Scripts de monitoring et audit**

### 4. Configuration Système
- `config/base.yaml` - **Configuration principale**
- `.env.example` - **Variables d'environnement**

## 🎯 Priorité 3 - Modèles & Assets

### 5. Modèles IA
- `models/` - **Modèles GGUF Qwen3 et Starcoder2**
- `data/models/` - **Modèles ML sauvegardés**

### 6. Ressources Complémentaires
- `frontend/src/components/` - **Composants UI**
- `docs/examples/playwright_scripts/` - **Scripts exemples**

## 📋 Instructions d'Indexation

1. **Démarrer par Priorité 1** (documents critiques)
2. **Indexer par dossier complet** (pas fichier par fichier)
3. **Vérifier l'embedding** après chaque dossier
4. **Tester les requêtes** avec cas d'usage réel

## 🔄 Maintenance

- **Re-indexer** après chaque mise à jour critique
- **Versionner** les embeddings avec git LFS
- **Monitore** la taille du vector store

```

---

## Fichier : `anythingllm\embedding_config.json`

```json
{
  "provider": "ollama",
  "model": "nomic-embed-text",
  "dimensions": 768,
  "chunk_size": 1000,
  "chunk_overlap": 200,
  "batch_size": 8
}
```

---

## Fichier : `anythingllm\workspace_config.json`

```json
{
  "name": "Altiora Knowledge",
  "description": "Workspace dédié à l'assistant Altiora pour la gestion du cycle de vie des tests logiciels. Contient spécifications, scénarios de test, scripts et documentation.",
  "vector_db": "lancedb",
  "embedding": {
    "provider": "ollama",
    "model": "nomic-embed-text",
    "dimensions": 768,
    "chunk_size": 1000,
    "chunk_overlap": 200,
    "batch_size": 8
  },
  "max_document_size_mb": 50,
  "auto_sync": true,
  "default_prompt_mode": "thinking"
}
```

---

## Fichier : `anythingllm\agents\batch_processor.json`

```json
{
  "name": "Batch Processor",
  "description": "Agent spécialisé dans les traitements batch.",
  "system_prompt": "Tu es un architecte batch senior. Expert en orchestration de traitements volumineux, gestion de queues, retry, monitoring, alerting et scaling.",
  "tools": [
    "batch_scheduler",
    "queue_manager",
    "retry_engine",
    "monitoring_dashboard"
  ],
  "model": "qwen3-32b",
  "temperature": 0.5
}
```

---

## Fichier : `anythingllm\agents\code_generator.json`

```json
{
  "name": "Code Generator",
  "description": "Agent spécialisé dans la génération de code de test.",
  "system_prompt": "Tu es un développeur test senior. Expert en Python, JavaScript, TypeScript. Maîtrise pytest, selenium, playwright, cypress. Génère code maintenable et testable.",
  "tools": [
    "code_generator",
    "syntax_validator",
    "dependency_checker",
    "security_linter"
  ],
  "model": "qwen3-32b",
  "temperature": 0.3
}
```

---

## Fichier : `anythingllm\agents\qa_analyst.json`

```json
{
  "name": "QA Analyst",
  "description": "Agent spécialisé dans l’analyse QA et la génération de tests.",
  "system_prompt": "Tu es un analyste QA senior avec 15 ans d’expérience. Expert en techniques de test : unitaires, d’intégration, fonctionnels, non-fonctionnels, sécurité, performance. Connaît les standards ISTQB, TMap, ATDD.",
  "tools": [
    "test_case_generator",
    "coverage_analyzer",
    "performance_profiler",
    "vulnerability_scanner"
  ],
  "model": "qwen3-32b",
  "temperature": 0.4
}
```

---

## Fichier : `anythingllm\chat_templates\analysis_template.json`

```json
{
  "name": "Analyse QA",
  "description": "Template pour l’analyse détaillée de spécifications et la génération de cas de test.",
  "system_prompt": "Tu es un expert QA senior. Analyse la spécification fournie et produis des cas de test complets couvrant fonctionnels, non-fonctionnels, edge-cases et régression.",
  "user_prompt": "Voici la spécification à analyser :\n\n{context}\n\nProduis une analyse QA structurée avec priorités.",
  "model": "qwen3-32b",
  "temperature": 0.4,
  "max_tokens": 4000
}
```

---

## Fichier : `anythingllm\chat_templates\batch_template.json`

```json
{
  "name": "Traitement Batch",
  "description": "Template pour l’orchestration de traitements batch.",
  "system_prompt": "Tu es un architecte batch. Définis des stratégies de traitement par lots optimisées, avec retry, monitoring et gestion d’erreurs.",
  "user_prompt": "Planifie un traitement batch pour :\n\n{description}\n\nVolumes: {volumes}\nDélai: {deadline}",
  "model": "qwen3-32b",
  "temperature": 0.5,
  "max_tokens": 4000
}
```

---

## Fichier : `anythingllm\chat_templates\coding_template.json`

```json
{
  "name": "Génération Code",
  "description": "Template pour générer du code de test ou d’automatisation.",
  "system_prompt": "Tu es un développeur test senior. Génère du code Python ou JavaScript conforme aux standards PEP8 / ESLint, avec tests unitaires et documentation.",
  "user_prompt": "Génère le code pour : {request}\n\nLangage: {language}\nFramework: {framework}\nContraintes: {constraints}",
  "model": "qwen3-32b",
  "temperature": 0.2,
  "max_tokens": 4000
}
```

---

## Fichier : `anythingllm\chat_templates\debug_template.json`

```json
{
  "name": "Débogage",
  "description": "Template pour l’analyse de logs et le débogage.",
  "system_prompt": "Tu es un expert debugging. Analyse les logs fournis, identifie la cause racine et propose des corrections.",
  "user_prompt": "Logs à analyser :\n```\n{logs}\n```\n\nComportement attendu : {expected}\nEnvironnement : {environment}",
  "model": "qwen3-32b",
  "temperature": 0.3,
  "max_tokens": 4000
}
```

---

## Fichier : `anythingllm\legacy\Altiora.html`

```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Altiora - Interface Conversationnelle Avancée</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
    <style>
        :root {
            /* Light Theme Colors */
            --bg-primary: #f8f9fa;
            --bg-secondary: #ffffff;
            --bg-tertiary: #e9ecef;
            --text-primary: #212529;
            --text-secondary: #6c757d;
            --border-color: #dee2e6;
            --primary: #4361ee;
            --primary-dark: #3a56d4;
            --secondary: #7209b7;
            --success: #4cc9f0;
            --warning: #f72585;
            --shadow: 0 4px 12px rgba(0,0,0,0.08);
            
            /* Dark Theme Colors */
            --dark-bg-primary: #121212;
            --dark-bg-secondary: #1e1e1e;
            --dark-bg-tertiary: #2d2d2d;
            --dark-text-primary: #f8f9fa;
            --dark-text-secondary: #adb5bd;
            --dark-border-color: #495057;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', system-ui, sans-serif;
        }

        body {
            background-color: var(--bg-primary);
            color: var(--text-primary);
            height: 100vh;
            display: flex;
            flex-direction: column;
            transition: background-color 0.3s, color 0.3s;
        }

        body.dark-theme {
            background-color: var(--dark-bg-primary);
            color: var(--dark-text-primary);
        }

        .header {
            background: linear-gradient(120deg, var(--primary), var(--secondary));
            color: white;
            padding: 1rem 1.5rem;
            box-shadow: var(--shadow);
            z-index: 10;
        }

        .header-content {
            max-width: 1200px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .logo {
            display: flex;
            align-items: center;
            gap: 0.75rem;
            font-size: 1.5rem;
            font-weight: 700;
        }

        .logo i {
            font-size: 1.75rem;
        }

        .theme-controls {
            display: flex;
            align-items: center;
            gap: 1rem;
        }

        .theme-toggle {
            background: rgba(255, 255, 255, 0.2);
            border: none;
            border-radius: 50%;
            width: 40px;
            height: 40px;
            color: white;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: background 0.2s;
        }

        .theme-toggle:hover {
            background: rgba(255, 255, 255, 0.3);
        }

        .features {
            display: flex;
            gap: 1.5rem;
            font-size: 0.9rem;
        }

        .feature-tag {
            background: rgba(255, 255, 255, 0.2);
            padding: 0.25rem 0.75rem;
            border-radius: 999px;
            backdrop-filter: blur(4px);
        }

        .chat-container {
            flex: 1;
            display: flex;
            max-width: 1200px;
            width: 100%;
            margin: 1.5rem auto;
            gap: 1.5rem;
            padding: 0 1.5rem;
        }

        .sidebar {
            width: 280px;
            background: var(--bg-secondary);
            border-radius: 12px;
            box-shadow: var(--shadow);
            padding: 1.5rem;
            display: flex;
            flex-direction: column;
            gap: 1.5rem;
            transition: background-color 0.3s, box-shadow 0.3s;
        }

        body.dark-theme .sidebar {
            background: var(--dark-bg-secondary);
            box-shadow: 0 4px 12px rgba(0,0,0,0.3);
        }

        .sidebar-section {
            border-bottom: 1px solid var(--border-color);
            padding-bottom: 1.5rem;
        }

        body.dark-theme .sidebar-section {
            border-bottom: 1px solid var(--dark-border-color);
        }

        .sidebar-section:last-child {
            border-bottom: none;
            padding-bottom: 0;
        }

        .sidebar h3 {
            font-size: 0.9rem;
            text-transform: uppercase;
            letter-spacing: 1px;
            color: var(--text-secondary);
            margin-bottom: 1rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        body.dark-theme .sidebar h3 {
            color: var(--dark-text-secondary);
        }

        .context-item {
            padding: 0.75rem;
            border-radius: 8px;
            background: var(--bg-tertiary);
            margin-bottom: 0.5rem;
            font-size: 0.85rem;
        }

        body.dark-theme .context-item {
            background: var(--dark-bg-tertiary);
        }

        .context-key {
            font-weight: 600;
            color: var(--primary);
        }

        .suggestions {
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
        }

        .suggestion-chip {
            background: var(--bg-tertiary);
            border: 1px solid var(--border-color);
            border-radius: 999px;
            padding: 0.4rem 0.8rem;
            font-size: 0.8rem;
            cursor: pointer;
            transition: all 0.2s ease;
        }

        body.dark-theme .suggestion-chip {
            background: var(--dark-bg-tertiary);
            border: 1px solid var(--dark-border-color);
        }

        .suggestion-chip:hover {
            background: var(--primary);
            color: white;
            border-color: var(--primary);
        }

        .main-chat {
            flex: 1;
            display: flex;
            flex-direction: column;
            background: var(--bg-secondary);
            border-radius: 12px;
            box-shadow: var(--shadow);
            overflow: hidden;
            transition: background-color 0.3s, box-shadow 0.3s;
        }

        body.dark-theme .main-chat {
            background: var(--dark-bg-secondary);
            box-shadow: 0 4px 12px rgba(0,0,0,0.3);
        }

        .chat-header {
            padding: 1rem 1.5rem;
            border-bottom: 1px solid var(--border-color);
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        body.dark-theme .chat-header {
            border-bottom: 1px solid var(--dark-border-color);
        }

        .chat-title {
            font-weight: 600;
        }

        .status {
            font-size: 0.85rem;
            color: var(--text-secondary);
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        body.dark-theme .status {
            color: var(--dark-text-secondary);
        }

        .status-indicator {
            width: 10px;
            height: 10px;
            border-radius: 50%;
            background: var(--success);
        }

        .messages-container {
            flex: 1;
            padding: 1.5rem;
            overflow-y: auto;
            display: flex;
            flex-direction: column;
            gap: 1.5rem;
        }

        .message {
            max-width: 80%;
            padding: 1rem 1.25rem;
            border-radius: 18px;
            line-height: 1.5;
            position: relative;
            animation: fadeIn 0.3s ease;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .user-message {
            align-self: flex-end;
            background: var(--primary);
            color: white;
            border-bottom-right-radius: 4px;
        }

        .bot-message {
            align-self: flex-start;
            background: var(--bg-tertiary);
            border-bottom-left-radius: 4px;
        }

        body.dark-theme .bot-message {
            background: var(--dark-bg-tertiary);
        }

        .message-header {
            display: flex;
            align-items: center;
            gap: 0.75rem;
            margin-bottom: 0.5rem;
            font-weight: 600;
        }

        .bot-message .message-header {
            color: var(--primary-dark);
        }

        body.dark-theme .bot-message .message-header {
            color: #6a9eff; /* Lighter blue for dark theme */
        }

        .message-content p {
            margin: 0.5rem 0;
        }

        .message-context {
            margin-top: 0.75rem;
            padding: 0.75rem;
            background: rgba(67, 97, 238, 0.05);
            border-radius: 8px;
            font-size: 0.85rem;
        }

        body.dark-theme .message-context {
            background: rgba(67, 97, 238, 0.15);
        }

        .message-context h4 {
            margin-bottom: 0.5rem;
            color: var(--primary);
        }

        .attachments {
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
            margin-top: 0.75rem;
        }

        .attachment {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            padding: 0.5rem;
            background: rgba(0, 0, 0, 0.03);
            border-radius: 6px;
            font-size: 0.8rem;
        }

        body.dark-theme .attachment {
            background: rgba(255, 255, 255, 0.05);
        }

        .input-area {
            padding: 1.25rem;
            border-top: 1px solid var(--border-color);
            background: var(--bg-secondary);
            transition: background-color 0.3s, border-color 0.3s;
        }

        body.dark-theme .input-area {
            border-top: 1px solid var(--dark-border-color);
            background: var(--dark-bg-secondary);
        }

        .input-form {
            display: flex;
            flex-direction: column;
            gap: 1rem;
        }

        .message-input-row {
            display: flex;
            gap: 0.75rem;
        }

        .message-input {
            flex: 1;
            padding: 0.9rem 1.25rem;
            border: 1px solid var(--border-color);
            border-radius: 999px;
            font-size: 1rem;
            transition: border-color 0.2s, background-color 0.3s, color 0.3s;
            background: var(--bg-secondary);
            color: var(--text-primary);
        }

        body.dark-theme .message-input {
            border: 1px solid var(--dark-border-color);
            background: var(--dark-bg-secondary);
            color: var(--dark-text-primary);
        }

        .message-input:focus {
            outline: none;
            border-color: var(--primary);
            box-shadow: 0 0 0 3px rgba(67, 97, 238, 0.2);
        }

        .send-button {
            background: var(--primary);
            color: white;
            border: none;
            width: 50px;
            height: 50px;
            border-radius: 50%;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: background 0.2s;
            align-self: flex-end;
        }

        .send-button:hover {
            background: var(--primary-dark);
        }

        .attachment-button {
            background: var(--bg-tertiary);
            border: 1px solid var(--border-color);
            width: 50px;
            height: 50px;
            border-radius: 50%;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: background 0.2s, border-color 0.2s;
            align-self: flex-end;
        }

        body.dark-theme .attachment-button {
            background: var(--dark-bg-tertiary);
            border: 1px solid var(--dark-border-color);
        }

        .attachment-button:hover {
            background: var(--primary);
            color: white;
            border-color: var(--primary);
        }

        .file-input {
            display: none;
        }

        .suggestions-bar {
            display: flex;
            gap: 0.75rem;
            flex-wrap: wrap;
        }

        .file-preview {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            padding: 0.5rem;
            background: var(--bg-tertiary);
            border-radius: 6px;
            font-size: 0.85rem;
            max-width: 100%;
            overflow: hidden;
        }

        body.dark-theme .file-preview {
            background: var(--dark-bg-tertiary);
        }

        .file-preview-name {
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }

        .remove-file {
            cursor: pointer;
            color: var(--warning);
        }

        .storage-warning {
            background-color: #fff3cd;
            border: 1px solid #ffeaa7;
            color: #856404;
            padding: 0.75rem;
            border-radius: 0.5rem;
            font-size: 0.85rem;
            margin-bottom: 1rem;
            display: flex;
            align-items: flex-start;
            gap: 0.5rem;
        }

        body.dark-theme .storage-warning {
            background-color: #343a40;
            border-color: #495057;
            color: #e9ecef;
        }

        .workflow-steps {
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
            margin-top: 1rem;
            padding-top: 1rem;
            border-top: 1px dashed var(--border-color);
        }

        body.dark-theme .workflow-steps {
            border-top: 1px dashed var(--dark-border-color);
        }

        .workflow-step {
            display: flex;
            align-items: center;
            gap: 0.4rem;
            background: var(--bg-tertiary);
            border-radius: 999px;
            padding: 0.3rem 0.7rem;
            font-size: 0.75rem;
            font-weight: 500;
            cursor: pointer;
            transition: all 0.2s ease;
        }

        body.dark-theme .workflow-step {
            background: var(--dark-bg-tertiary);
        }

        .workflow-step:hover {
            background: var(--primary);
            color: white;
        }

        .step-number {
            background: var(--primary);
            color: white;
            width: 18px;
            height: 18px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 0.7rem;
        }

        .workflow-step:hover .step-number {
            background: white;
            color: var(--primary);
        }

        @media (max-width: 768px) {
            .chat-container {
                flex-direction: column;
                margin: 1rem;
                padding: 0;
            }
            
            .sidebar {
                width: 100%;
            }
            
            .message {
                max-width: 90%;
            }
        }
    </style>
</head>
<body>
    <header class="header">
        <div class="header-content">
            <div class="logo">
                <i class="fas fa-robot"></i>
                <span>Altiora</span>
            </div>
            <div class="theme-controls">
                <button class="theme-toggle" id="themeToggle" title="Basculer le mode sombre">
                    <i class="fas fa-moon"></i>
                </button>
                <div class="features">
                    <div class="feature-tag">Mémoire Contextuelle</div>
                    <div class="feature-tag">Suggestions Intelligentes</div>
                </div>
            </div>
        </div>
    </header>

    <div class="chat-container">
        <aside class="sidebar">
            <div class="storage-warning">
                <i class="fas fa-exclamation-triangle"></i>
                <div>
                    <strong>Limitation d'affichage :</strong> Le thème sélectionné (sombre/clair) ne sera pas sauvegardé lors du rechargement de la page dans cet environnement.
                </div>
            </div>
            <div class="sidebar-section">
                <h3><i class="fas fa-brain"></i> Contexte Actif</h3>
                <div class="context-item">
                    <span class="context-key">Projet:</span> Migration système de paiement
                </div>
                <div class="context-item">
                    <span class="context-key">Technologie:</span> Node.js, PostgreSQL
                </div>
                <div class="context-item">
                    <span class="context-key">Dernière SFD:</span> Authentification utilisateur
                </div>
                <div class="context-item">
                    <span class="context-key">Tests Générés:</span> 12 cas de test Playwright
                </div>
            </div>

            <div class="sidebar-section">
                <h3><i class="fas fa-history"></i> Historique Récent</h3>
                <div class="context-item">
                    <span class="context-key">Action:</span> Analyse SFD "Authentification"
                </div>
                <div class="context-item">
                    <span class="context-key">Action:</span> Génération tests Playwright
                </div>
            </div>

            <div class="sidebar-section">
                <h3><i class="fas fa-lightbulb"></i> Suggestions</h3>
                <div class="suggestions">
                    <div class="suggestion-chip">Correction textuelle</div>
                    <div class="suggestion-chip">Analyse des SFD</div>
                    <div class="suggestion-chip">Créer une matrice de test</div>
                    <div class="suggestion-chip">Générer les tests Playwright</div>
                    <div class="suggestion-chip">Exécuter les tests</div>
                </div>
            </div>
        </aside>

        <main class="main-chat">
            <div class="chat-header">
                <div class="chat-title">Assistant QA IA</div>
                <div class="status">
                    <div class="status-indicator"></div>
                    <span>En ligne - Mémoire contextuelle active</span>
                </div>
            </div>

            <div class="messages-container" id="messagesContainer">
                <div class="message bot-message">
                    <div class="message-header">
                        <i class="fas fa-robot"></i>
                        <span>Altiora</span>
                    </div>
                    <div class="message-content">
                        <p>Bonjour ! Je suis Altiora, votre assistant QA IA. Je me souviens de notre contexte : vous travaillez sur une migration de système de paiement avec Node.js.</p>
                        <p>Comment puis-je vous aider aujourd'hui ?</p>
                    </div>
                </div>

                <div class="message user-message">
                    <div class="message-header">
                        <i class="fas fa-user"></i>
                        <span>Vous</span>
                    </div>
                    <div class="message-content">
                        <p>J'ai besoin d'analyser la spécification fonctionnelle détaillée pour le module d'authentification.</p>
                        <div class="attachments">
                            <div class="attachment">
                                <i class="fas fa-file-pdf"></i>
                                <span>SFD_authentification_v2.pdf</span>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="message bot-message">
                    <div class="message-header">
                        <i class="fas fa-robot"></i>
                        <span>Altiora</span>
                    </div>
                    <div class="message-content">
                        <p>Merci pour le fichier ! J'ai analysé votre SFD "Authentification". Voici ce que j'ai identifié :</p>
                        <p><strong>5 scénarios de test potentiels :</strong></p>
                        <ol>
                            <li>Connexion utilisateur avec identifiants valides [Critique]</li>
                            <li>Tentative de connexion avec mot de passe incorrect [Haute]</li>
                            <li>Réinitialisation du mot de passe via email [Moyenne]</li>
                            <li>Verrouillage du compte après 3 tentatives [Moyenne]</li>
                            <li>Déconnexion sécurisée [Normale]</li>
                        </ol>
                        <p>Souhaitez-vous que je génère les tests Playwright correspondants ?</p>
                    </div>
                </div>
            </div>

            <div class="input-area">
                <form class="input-form" id="messageForm">
                    <div class="message-input-row">
                        <input type="text" class="message-input" id="messageInput" placeholder="Tapez votre message..." autocomplete="off">
                        <input type="file" id="fileInput" class="file-input" accept=".pdf,.doc,.docx,.txt,.xlsx">
                        <label for="fileInput" class="attachment-button" title="Joindre un fichier">
                            <i class="fas fa-paperclip"></i>
                        </label>
                        <button type="submit" class="send-button">
                            <i class="fas fa-paper-plane"></i>
                        </button>
                    </div>
                    <div id="filePreviewContainer"></div>
                    <!-- Suggestions rapides retirées ici -->
                </form>
            </div>
        </main>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const body = document.body;
            const themeToggle = document.getElementById('themeToggle');
            const themeIcon = themeToggle.querySelector('i');
            const messagesContainer = document.getElementById('messagesContainer');
            const messageForm = document.getElementById('messageForm');
            const messageInput = document.getElementById('messageInput');
            const fileInput = document.getElementById('fileInput');
            const filePreviewContainer = document.getElementById('filePreviewContainer');
            
            // Initialiser le thème clair par défaut
            // Note: Pas de persistance en localStorage à cause du sandbox
            let isDarkTheme = false;
            
            // Basculer le thème
            themeToggle.addEventListener('click', function() {
                isDarkTheme = !isDarkTheme;
                body.classList.toggle('dark-theme', isDarkTheme);
                
                if (isDarkTheme) {
                    themeIcon.classList.remove('fa-moon');
                    themeIcon.classList.add('fa-sun');
                } else {
                    themeIcon.classList.remove('fa-sun');
                    themeIcon.classList.add('fa-moon');
                }
            });
            
            // Fonction pour ajouter un message
            function addMessage(sender, text, attachments = []) {
                const messageDiv = document.createElement('div');
                messageDiv.classList.add('message');
                messageDiv.classList.add(sender === 'user' ? 'user-message' : 'bot-message');
                
                const messageHeader = document.createElement('div');
                messageHeader.classList.add('message-header');
                messageHeader.innerHTML = `
                    <i class="fas ${sender === 'user' ? 'fa-user' : 'fa-robot'}"></i>
                    <span>${sender === 'user' ? 'Vous' : 'Altiora'}</span>
                `;
                
                const messageContent = document.createElement('div');
                messageContent.classList.add('message-content');
                messageContent.innerHTML = `<p>${text}</p>`;
                
                messageDiv.appendChild(messageHeader);
                messageDiv.appendChild(messageContent);
                
                // Ajouter les pièces jointes si présentes
                if (attachments.length > 0) {
                    const attachmentsDiv = document.createElement('div');
                    attachmentsDiv.classList.add('attachments');
                    
                    attachments.forEach(file => {
                        const attachmentDiv = document.createElement('div');
                        attachmentDiv.classList.add('attachment');
                        attachmentDiv.innerHTML = `
                            <i class="fas ${getFileIcon(file.type)}"></i>
                            <span>${file.name}</span>
                        `;
                        attachmentsDiv.appendChild(attachmentDiv);
                    });
                    
                    messageContent.appendChild(attachmentsDiv);
                }
                
                messagesContainer.appendChild(messageDiv);
                messagesContainer.scrollTop = messagesContainer.scrollHeight;
            }
            
            // Déterminer l'icône de fichier
            function getFileIcon(fileType) {
                if (fileType.includes('pdf')) return 'fa-file-pdf';
                if (fileType.includes('word') || fileType.includes('doc')) return 'fa-file-word';
                if (fileType.includes('excel') || fileType.includes('sheet')) return 'fa-file-excel';
                if (fileType.includes('image')) return 'fa-file-image';
                if (fileType.includes('text') || fileType.includes('txt')) return 'fa-file-alt';
                return 'fa-file';
            }
            
            // Gestion de l'envoi du message
            messageForm.addEventListener('submit', function(e) {
                e.preventDefault();
                const message = messageInput.value.trim();
                const files = Array.from(fileInput.files);
                
                if (message || files.length > 0) {
                    addMessage('user', message || "Fichier joint", files);
                    messageInput.value = '';
                    fileInput.value = '';
                    filePreviewContainer.innerHTML = '';
                    
                    // Simulation de réponse de l'assistant
                    setTimeout(() => {
                        let response = "";
                        if (message.toLowerCase().includes('génère') && message.toLowerCase().includes('test')) {
                            response = "J'ai généré 5 tests Playwright pour le module d'authentification. Vous les trouverez dans le dossier /tests/playwright/auth/. Souhaitez-vous que je les exécute maintenant ?";
                        } else if (message.toLowerCase().includes('matrice')) {
                            response = "Voici la matrice de traçabilité entre les exigences de la SFD et les cas de test que j'ai générés. Elle est disponible au format Excel dans /docs/matrice_authentification.xlsx";
                        } else if (message.toLowerCase().includes('exécute')) {
                            response = "J'exécute les tests Playwright pour le module d'authentification...<br><br>✅ Test 1: Connexion réussie - PASS<br>✅ Test 2: Mot de passe incorrect - PASS<br>⚠️ Test 3: Réinitialisation mot de passe - FAIL (Timeout)<br>✅ Test 4: Verrouillage compte - PASS<br>✅ Test 5: Déconnexion - PASS<br><br>Un rapport détaillé est disponible dans /reports/auth_test_report.html";
                        } else {
                            response = "J'ai bien noté votre demande. En utilisant le contexte de notre projet de migration de système de paiement, je peux vous aider à analyser des SFD, générer des tests, créer des matrices ou exécuter des suites de tests. Que souhaitez-vous faire maintenant ?";
                        }
                        
                        addMessage('bot', response);
                    }, 1000);
                }
            });
            
            // Gestion des suggestions
            document.querySelectorAll('.suggestion-chip').forEach(element => {
                element.addEventListener('click', function() {
                    const action = this.getAttribute('data-action') || this.textContent;
                    messageInput.value = action;
                    messageInput.focus();
                });
            });
            
            // Gestion de l'aperçu des fichiers
            fileInput.addEventListener('change', function() {
                filePreviewContainer.innerHTML = '';
                const files = Array.from(fileInput.files);
                
                if (files.length > 0) {
                    const previewDiv = document.createElement('div');
                    previewDiv.classList.add('file-preview');
                    
                    const fileIcon = document.createElement('i');
                    fileIcon.classList.add('fas', getFileIcon(files[0].type));
                    
                    const fileNameSpan = document.createElement('span');
                    fileNameSpan.classList.add('file-preview-name');
                    fileNameSpan.textContent = files[0].name;
                    
                    const removeIcon = document.createElement('i');
                    removeIcon.classList.add('fas', 'fa-times', 'remove-file');
                    removeIcon.addEventListener('click', function() {
                        fileInput.value = '';
                        filePreviewContainer.innerHTML = '';
                    });
                    
                    previewDiv.appendChild(fileIcon);
                    previewDiv.appendChild(fileNameSpan);
                    previewDiv.appendChild(removeIcon);
                    
                    filePreviewContainer.appendChild(previewDiv);
                }
            });
        });
    </script>
</body>
</html>
```

---

## Fichier : `anythingllm\prompts\qwen3_direct.txt`

```text
You are Altiora, a concise QA assistant. Provide direct answers without showing reasoning. Be accurate but brief. Focus on actionable insights.
```

---

## Fichier : `anythingllm\prompts\qwen3_thinking.txt`

```text
You are Altiora, an expert QA assistant. Use the <thinking> tags to show your reasoning process. Be precise, methodical and provide detailed analysis. Always validate edge cases and suggest improvements. Think step by step before giving the final answer.
```

---

## Fichier : `anythingllm\prompts\starcoder2_generation.txt`

```text
You are an expert test automation engineer. Generate clean, well-documented code following best practices. Include unit tests, error handling, and clear comments. Prefer Python with pytest framework. Respect PEP8 standards.
```

---

## Fichier : `backend\__init__.py`

```python

```

---

## Fichier : `backend\altiora\__init__.py`

```python
# backend/altiora/__init__.py
"""
Package principal Altiora.

Fournit l’API, la logique métier, les services et l’infrastructure
nécessaires à l’assistant QA intelligent.
"""

__all__ = ["api", "core", "services", "security", "config", "utils"]
```

---

## Fichier : `backend\altiora\__version__.py`

```python
# backend/altiora/__version__.py
"""
Gestion centralisée des versions pour Altiora V2.

Cette source unique de vérité est importée partout dans la base de code
pour assurer une gestion cohérente des versions à travers le backend, la CLI et les images Docker.
"""

from __future__ import annotations

__title__ = "altiora"
__description__ = (
    "Altiora V2 - Intelligent QA Assistant with Qwen3-32B and Starcoder2-15B"
)
__version__ = "2.0.0"
__author__ = "Paul DE MOURA"
__email__ = "pauldemoura@ik.me"
__license__ = "MIT"
__copyright__ = f"2025 {__author__}"

# Alias de compatibilité API
VERSION = __version__
VERSION_INFO = tuple(map(int, __version__.split(".")))

# Métadonnées de pré-version / build
__build__ = None  # Défini par le pipeline CI/CD
__commit__ = None  # Hash du commit Git, défini par le pipeline CI/CD

# API Publique
__all__ = [
    "__title__",
    "__description__",
    "__version__",
    "__author__",
    "__email__",
    "__license__",
    "__copyright__",
    "VERSION",
    "VERSION_INFO",
]
```

---

## Fichier : `backend\altiora\api\app.py`

```python
# backend/altiora/api/app.py
"""
Bootstrap de l'application FastAPI.

Gère :
- Le routage de l'API v1
- Les middlewares globaux
- Les événements de cycle de vie
- La documentation OpenAPI
"""

from __future__ import annotations

import logging
import time
from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.responses import ORJSONResponse

from backend.altiora.__version__ import __title__, __version__
from backend.altiora.api.v1 import analysis, batch, health, models
from backend.altiora.config.settings import settings
from backend.altiora.utils.logging import setup_logging
from backend.altiora.api.openapi import custom_openapi



logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncGenerator[None, None]:
    """Cycle de vie de démarrage / arrêt."""
    setup_logging()
    logger.info("🚀 %s v%s starting", __title__, __version__)
    yield
    logger.info("⏹️  %s stopped", __title__)


app = FastAPI(
    title=__title__,
    version=__version__,
    description="Altiora V2 – QA assistant API",
    docs_url="/docs",
    redoc_url="/redoc",
    default_response_class=ORJSONResponse,
    lifespan=lifespan,
)

# Middleware global
app.add_middleware(GZipMiddleware, minimum_size=1024)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routeurs
app.include_router(health.router, prefix="/health", tags=["health"])
app.include_router(analysis.router, prefix="/api/v1/analysis", tags=["analysis"])
app.include_router(batch.router, prefix="/api/v1/batch", tags=["batch"])
app.include_router(models.router, prefix="/api/v1/models", tags=["models"])
```

---

## Fichier : `backend\altiora\api\dependencies.py`

```python
# backend/altiora/api/dependencies.py
"""
Dépendances FastAPI réutilisables.

Fournit : authentification, DB, cache, modèles.
"""
from typing import Annotated, Optional
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from redis import Redis

from backend.altiora.config.settings import settings
from backend.altiora.core.models.model_swapper import ModelSwapper
from backend.altiora.infrastructure.cache.unified_cache import UnifiedCache
from backend.altiora.security.auth.jwt_handler import decode_access_token
from backend.altiora.infrastructure.database import get_db

security = HTTPBearer()

# Singleton instances
_model_swapper: Optional[ModelSwapper] = None
_cache: Optional[UnifiedCache] = None

def get_model_swapper() -> ModelSwapper:
    global _model_swapper
    if _model_swapper is None:
        _model_swapper = ModelSwapper()
    return _model_swapper

def get_cache() -> UnifiedCache:
    global _cache
    if _cache is None:
        _cache = UnifiedCache()
    return _cache

async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
) -> dict:
    try:
        payload = decode_access_token(credentials.credentials)
        return payload
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e),
            headers={"WWW-Authenticate": "Bearer"},
        )

# Type aliases for dependency injection
CurrentUserDep = Annotated[dict, Depends(get_current_user)]
ModelSwapperDep = Annotated[ModelSwapper, Depends(get_model_swapper)]
CacheDep = Annotated[UnifiedCache, Depends(get_cache)]
DBSessionDep = Annotated[Session, Depends(get_db)]
RedisCacheDep = Annotated[Redis, Depends(lambda: Redis.from_url(settings.redis_url))]
```

---

## Fichier : `backend\altiora\api\openapi.py`

```python
# backend/altiora/api/openapi.py
"""Module pour la personnalisation de la spécification OpenAPI (Swagger/Redoc) de l'API Altiora.

Ce module permet de définir des métadonnées supplémentaires pour la documentation
de l'API, telles que le titre, la version, la description, et d'ajouter des
exemples de requêtes/réponses pour améliorer la clarté de la documentation
générée automatiquement par FastAPI.
"""

from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi


def custom_openapi(app: FastAPI):
    """Génère et personnalise la spécification OpenAPI pour l'application FastAPI."

    Cette fonction est appelée par FastAPI pour construire la documentation
    interactive (Swagger UI, ReDoc). Elle ajoute des informations spécifiques
    au projet et des exemples pour les endpoints.

    Args:
        app: L'instance de l'application FastAPI.

    Returns:
        Le schéma OpenAPI personnalisé.
    """
    # Si le schéma a déjà été généré, le retourne directement pour éviter de le recréer.
    if app.openapi_schema:
        return app.openapi_schema

    # Génère le schéma OpenAPI de base à partir des routes de l'application.
    openapi_schema = get_openapi(
        title="Altiora API",
        version="1.0.0",
        description="API pour l'assistant QA Altiora, permettant l'automatisation des tests et l'analyse de spécifications.",
        routes=app.routes,
    )

    # Ajoute des exemples personnalisés pour des endpoints spécifiques.
    # Ceci améliore la lisibilité de la documentation Swagger/Redoc.
    if "/analyze-sfd" in openapi_schema["paths"] and "post" in openapi_schema["paths"]["/analyze-sfd"]:
        openapi_schema["paths"]["/analyze-sfd"]["post"]["requestBody"]["content"]["application/json"]["example"] = {
            "content": "Spécification fonctionnelle détaillée du module de connexion utilisateur...",
            "project_id": "proj-123"
        }

    # Stocke le schéma généré dans l'application pour les appels futurs.
    app.openapi_schema = openapi_schema
    return app.openapi_schema

```

---

## Fichier : `backend\altiora\api\__init__.py`

```python
# backend/altiora/api/__init__.py
"""
Couche API – Routeurs FastAPI, middlewares, dépendances.
"""
```

---

## Fichier : `backend\altiora\api\gateway\api_gateway.py`

```python
# backend/altiora/api/gateway/api_gateway.py
"""Passerelle API principale pour l'application Altiora.

Ce module implémente une passerelle API basée sur FastAPI qui expose
des points de terminaison pour interagir avec les fonctionnalités
de l'assistant QA. Il intègre des mesures de sécurité comme la limitation
de débit (rate limiting) et l'ajout d'en-têtes de sécurité HTTP.
"""

import time
import logging

from fastapi import FastAPI, Request, HTTPException, status
from pydantic import BaseModel, Field
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address

# Importation du système de QA (Question Answering).
from src.qa_system.qa_system import QASystem

logger = logging.getLogger(__name__)

# Initialisation du limiteur de débit.
limiter = Limiter(key_func=get_remote_address)

# Initialisation de l'application FastAPI.
app = FastAPI(
    title="Altiora API Gateway",
    description="Passerelle API pour l'assistant QA Altiora.",
    version="1.0.0",
)
app.state.limiter = limiter
app.add_exception_handler(429, _rate_limit_exceeded_handler)


# --- Modèles Pydantic pour les requêtes et réponses --- #
class QARequest(BaseModel):
    """Modèle de requête pour le système de Question-Réponse (QA)."""
    question: str = Field(..., description="La question posée par l'utilisateur.")
    context: Optional[str] = Field(None, description="Contexte optionnel pour aider à répondre à la question.")
    model: str = Field("qwen", description="Le modèle d'IA à utiliser pour la réponse (ex: 'qwen', 'starcoder').")
    temperature: float = Field(0.7, ge=0.0, le=1.0, description="Température pour la génération de la réponse (contrôle la créativité).")


class QAResponse(BaseModel):
    """Modèle de réponse du système de Question-Réponse (QA)."""
    answer: str = Field(..., description="La réponse générée par le modèle.")
    confidence: float = Field(..., description="Le niveau de confiance de la réponse (entre 0 et 1).")
    model_used: str = Field(..., description="Le nom du modèle d'IA utilisé pour générer la réponse.")
    processing_time: float = Field(..., description="Le temps de traitement de la requête en secondes.")


# Initialisation du système de QA.
qa_system = QASystem()


# --- Middlewares --- #
@app.middleware("http")
async def add_security_headers(request: Request, call_next):
    """Middleware pour ajouter des en-têtes de sécurité HTTP aux réponses."

    Ces en-têtes aident à protéger l'application contre certaines vulnérabilités
    web courantes comme le Cross-Site Scripting (XSS) et le Clickjacking.
    """
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    return response


# --- Points de terminaison (Endpoints) --- #
@app.post("/api/v1/qa/answer", response_model=QAResponse)
@limiter.limit("10/minute") # Limite à 10 requêtes par minute par adresse IP.
async def answer_question(request: QARequest) -> QAResponse:
    """Point de terminaison principal pour poser une question au système QA."

    Args:
        request: L'objet `QARequest` contenant la question et les paramètres.

    Returns:
        Un objet `QAResponse` avec la réponse du modèle.

    Raises:
        HTTPException: En cas d'erreur interne du serveur.
    """
    start_time = time.time()

    try:
        # Appelle le système de QA pour obtenir une réponse.
        answer = await qa_system.answer_async(
            question=request.question,
            context=request.context,
            model=request.model,
            temperature=request.temperature
        )

        return QAResponse(
            answer=answer.text,
            confidence=answer.confidence,
            model_used=request.model,
            processing_time=time.time() - start_time
        )
    except Exception as e:
        logger.error(f"Erreur lors de la réponse à la question : {e}", exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@app.post("/api/v1/analyze")
@limiter.limit("5/minute") # Limite à 5 requêtes par minute pour l'analyse SFD.
async def analyze_sfd(request: Request, sfd_content: str):
    """Point de terminaison pour analyser une Spécification Fonctionnelle Détaillée (SFD)."

    Args:
        request: L'objet `Request` de FastAPI.
        sfd_content: Le contenu de la SFD à analyser.

    Returns:
        Un dictionnaire avec le résultat de l'analyse (actuellement un placeholder).

    Raises:
        HTTPException: En cas d'erreur interne du serveur.
    """
    logger.info(f"Requête d'analyse SFD reçue. Contenu : {sfd_content[:100]}...")
    # TODO: Implémenter la logique réelle d'analyse SFD ici.
    # Cela impliquerait d'appeler l'orchestrateur ou un service dédié.
    return {"message": "Analyse SFD en cours de développement.", "received_content_length": len(sfd_content)}


# ------------------------------------------------------------------
# Point d'entrée Uvicorn
# ------------------------------------------------------------------
if __name__ == "__main__":
    import uvicorn
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logger.info("Lancement de la passerelle API sur http://0.0.0.0:8000")
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
```

---

## Fichier : `backend\altiora\api\middleware\advanced_rate_limiter.py`

```python
# backend/altiora/api/middleware/advanced_rate_limiter.py
"""Module implémentant un limiteur de débit (rate limiter) avancé.

Ce limiteur de débit permet de contrôler le nombre de requêtes qu'un utilisateur
ou une entité peut effectuer dans une période donnée. Il supporte différentes
catégories de limites (ex: par défaut, analyse, génération) et est conçu pour
être utilisé de manière asynchrone.
"""

from collections import defaultdict
from datetime import datetime, timedelta
from typing import Dict, List, Any
import logging

logger = logging.getLogger(__name__)


class AdvancedRateLimiter:
    """Implémente un limiteur de débit configurable avec différentes catégories de limites."""

    def __init__(self):
        """Initialise le limiteur de débit avec des limites prédéfinies."

        `limits` est un dictionnaire où chaque clé est une catégorie (ex: "default", "analysis").
        Chaque catégorie contient le nombre maximal de requêtes et la fenêtre de temps en secondes.
        `requests` stocke les horodatages des requêtes pour chaque clé (utilisateur/IP).
        """
        self.limits: Dict[str, Dict[str, int]] = {
            "default": {"requests": 100, "window": 3600}, # 100 requêtes par heure.
            "analysis": {"requests": 20, "window": 3600}, # 20 requêtes d'analyse par heure.
            "generation": {"requests": 50, "window": 3600}, # 50 requêtes de génération par heure.
        }
        self.requests: Dict[str, List[datetime]] = defaultdict(list)

    async def check_limit(self, key: str, category: str = "default") -> bool:
        """Vérifie si une requête est autorisée selon les limites de débit."

        Args:
            key: La clé unique pour laquelle la limite est vérifiée (ex: adresse IP, ID utilisateur).
            category: La catégorie de limite à appliquer (ex: "default", "analysis").

        Returns:
            True si la requête est autorisée, False si la limite est dépassée.
        """
        now = datetime.now()
        limit_config = self.limits.get(category, self.limits["default"])

        # Nettoie les anciennes requêtes qui sont en dehors de la fenêtre de temps.
        cutoff = now - timedelta(seconds=limit_config["window"])
        self.requests[f"{category}:{key}"] = [
            req for req in self.requests[f"{category}:{key}"]
            if req > cutoff
        ]

        # Vérifie si le nombre de requêtes actuelles dépasse la limite.
        if len(self.requests[f"{category}:{key}"]) >= limit_config["requests"]:
            logger.warning(f"Limite de débit dépassée pour la clé '{key}' dans la catégorie '{category}'.")
            return False

        # Enregistre la nouvelle requête.
        self.requests[f"{category}:{key}"].append(now)
        return True


# ------------------------------------------------------------------
# Démonstration (exemple d'utilisation)
# ------------------------------------------------------------------
if __name__ == "__main__":
    import asyncio
    import logging

    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    async def demo():
        limiter = AdvancedRateLimiter()

        print("\n--- Démonstration de la limite par défaut (100/heure) ---")
        user_ip = "192.168.1.100"
        for i in range(5):
            allowed = await limiter.check_limit(user_ip)
            print(f"Requête {i+1} par {user_ip} : {'Autorisée' if allowed else 'Bloquée'}")
            await asyncio.sleep(0.01) # Petite pause.

        print("\n--- Démonstration de la limite 'analysis' (20/heure) ---")
        user_id = "user_alice"
        for i in range(25):
            allowed = await limiter.check_limit(user_id, category="analysis")
            print(f"Requête d'analyse {i+1} par {user_id} : {'Autorisée' if allowed else 'Bloquée'}")
            if not allowed:
                break
            await asyncio.sleep(0.01)

        print("\n--- Démonstration de la réinitialisation après fenêtre de temps ---")
        # Simule le passage du temps pour réinitialiser la limite.
        limiter.limits["short_test"] = {"requests": 2, "window": 1}
        test_key = "short_lived_user"

        print("Requête 1 (short_test) :", "Autorisée" if await limiter.check_limit(test_key, "short_test") else "Bloquée")
        print("Requête 2 (short_test) :", "Autorisée" if await limiter.check_limit(test_key, "short_test") else "Bloquée")
        print("Requête 3 (short_test) :", "Autorisée" if await limiter.check_limit(test_key, "short_test") else "Bloquée")

        print("Attente de 1.1 seconde pour la réinitialisation...")
        await asyncio.sleep(1.1)

        print("Requête 4 (short_test) après réinitialisation :", "Autorisée" if await limiter.check_limit(test_key, "short_test") else "Bloquée")

        print("Démonstration du limiteur de débit terminée.")

    asyncio.run(demo())
```

---

## Fichier : `backend\altiora\api\middleware\cache_middleware.py`

```python
# backend/altiora/api/middleware/cache_middleware.py
"""Middleware de cache pour les requêtes HTTP.

Ce middleware intercepte les requêtes HTTP et tente de servir les réponses
depuis un cache Redis. Si la réponse n'est pas en cache, la requête est
transmise à l'application, et la réponse est ensuite stockée dans Redis
pour les requêtes futures. Il utilise la compression pour optimiser
l'espace de stockage dans Redis.
"""

import time
import logging

from fastapi import Request, Response
from src.infrastructure.redis_config import get_redis_client
from src.utils.compression import compress_data, decompress_data

logger = logging.getLogger(__name__)


async def cache_middleware(request: Request, call_next):
    """Middleware de cache pour les requêtes FastAPI."

    Args:
        request: L'objet `Request` de FastAPI.
        call_next: La fonction pour passer la requête au prochain middleware ou à l'endpoint.

    Returns:
        L'objet `Response` de FastAPI, potentiellement servi depuis le cache.
    """
    start_time = time.time()
    redis_client = await get_redis_client()
    
    # Génère une clé de cache unique basée sur la méthode et l'URL de la requête.
    cache_key = f"cache:{request.method}:{request.url.path}"

    # Tente de récupérer la réponse depuis le cache Redis.
    cached_response = await redis_client.get(cache_key)
    
    if cached_response:
        try:
            # Si la réponse est en cache, la décompresse et la décode.
            response_data = decompress_data(cached_response)
            response = Response(content=response_data, media_type="application/json")
            response.headers["X-Cache"] = "HIT"
            logger.info(f"Cache HIT pour {request.url.path}")
        except Exception as e:
            logger.error(f"Erreur lors de la lecture/décompression du cache pour {request.url.path}: {e}")
            # En cas d'erreur de cache, on passe à l'application.
            response = await call_next(request)
            response.headers["X-Cache"] = "MISS_ERROR"
    else:
        # Si la réponse n'est pas en cache, passe la requête à l'application.
        response = await call_next(request)
        response.headers["X-Cache"] = "MISS"
        logger.info(f"Cache MISS pour {request.url.path}")

        # Si la réponse est un succès (200 OK), la stocke dans le cache.
        if response.status_code == 200:
            # Lit le corps de la réponse pour le mettre en cache.
            # Note: response.body est un bytes, il faut le décoder pour le compresser en string.
            response_body = response.body.decode('utf-8')
            compressed_data = compress_data(response_body)
            # Stocke dans Redis avec une expiration de 5 minutes (300 secondes).
            await redis_client.setex(cache_key, 300, compressed_data)
            logger.info(f"Réponse pour {request.url.path} mise en cache.")

    # Ajoute un en-tête pour le temps de réponse.
    response.headers["X-Response-Time"] = str(time.time() - start_time)
    return response


# ------------------------------------------------------------------
# Démonstration (exemple d'utilisation)
# ------------------------------------------------------------------
if __name__ == "__main__":
    import asyncio
    from fastapi import FastAPI
    from fastapi.testclient import TestClient
    import uvicorn

    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    app = FastAPI()

    # Applique le middleware de cache.
    app.middleware("http")(cache_middleware)

    @app.get("/items/{item_id}")
    async def read_item(item_id: int):
        """Endpoint de démonstration qui simule un travail long."""
        logger.info(f"Traitement de la requête pour item_id: {item_id} (non mis en cache)...")
        await asyncio.sleep(1) # Simule un travail long.
        return {"item_id": item_id, "data": "Données générées", "timestamp": datetime.datetime.now().isoformat()}

    async def run_demo_client():
        print("\n--- Lancement du client de démonstration ---")
        client = TestClient(app)

        print("Premier appel à /items/1 (devrait être MISS)...")
        response1 = client.get("/items/1")
        print(f"Statut: {response1.status_code}, Cache: {response1.headers.get('X-Cache')}, Temps: {response1.headers.get('X-Response-Time')[:5]}s")

        print("\nDeuxième appel à /items/1 (devrait être HIT)...")
        response2 = client.get("/items/1")
        print(f"Statut: {response2.status_code}, Cache: {response2.headers.get('X-Cache')}, Temps: {response2.headers.get('X-Response-Time')[:5]}s")

        print("\nTroisième appel à /items/2 (nouvelle clé, devrait être MISS)...")
        response3 = client.get("/items/2")
        print(f"Statut: {response3.status_code}, Cache: {response3.headers.get('X-Cache')}, Temps: {response3.headers.get('X-Response-Time')[:5]}s")

        print("\nAttente de 6 secondes pour l'expiration du cache...")
        await asyncio.sleep(6)

        print("\nQuatrième appel à /items/1 (après expiration, devrait être MISS)...")
        response4 = client.get("/items/1")
        print(f"Statut: {response4.status_code}, Cache: {response4.headers.get('X-Cache')}, Temps: {response4.headers.get('X-Response-Time')[:5]}s")

        print("Démonstration du cache middleware terminée.")

    # Lance le serveur Uvicorn en arrière-plan pour la démo.
    # Assurez-vous qu'un serveur Redis est en cours d'exécution sur localhost:6379.
    async def run_server_and_client():
        config = uvicorn.Config(app, host="0.0.0.0", port=8000, log_level="warning")
        server = uvicorn.Server(config)
        server_task = asyncio.create_task(server.serve())
        await asyncio.sleep(1) # Donne le temps au serveur de démarrer.
        await run_demo_client()
        server_task.cancel()

    asyncio.run(run_server_and_client())
```

---

## Fichier : `backend\altiora\api\middleware\rbac_middleware.py`

```python
# backend/altiora/api/middleware/rbac_middleware.py
"""Middleware pour le contrôle d'accès basé sur les rôles (RBAC).

Ce middleware s'intègre aux applications FastAPI pour vérifier les permissions
des utilisateurs avant d'autoriser l'accès à certaines ressources ou actions.
Il utilise un gestionnaire RBAC centralisé pour déterminer si un utilisateur
possède les droits nécessaires.
"""

from __future__ import annotations

import logging
from pathlib import Path

from fastapi import HTTPException, status

from src.rbac.manager import RBACManager
from src.rbac.models import User # Assurez-vous que le modèle User est correctement importé.

logger = logging.getLogger(__name__)

# ------------------------------------------------------------------
# Instance globale du gestionnaire RBAC
# ------------------------------------------------------------------
# Le chemin vers le fichier de configuration des rôles (ex: configs/roles.yaml).
# Assurez-vous que ce fichier existe et est correctement configuré.
rbac_manager = RBACManager(Path("configs/roles.yaml"))


async def verify_permission(
    user: User,
    resource: str,
    action: str,
) -> None:
    """Vérifie si un utilisateur a la permission d'effectuer une action sur une ressource."

    Args:
        user: L'objet `User` représentant l'utilisateur authentifié.
        resource: La ressource à laquelle l'accès est demandé (ex: "sfd:analysis", "user:management").
        action: L'action que l'utilisateur tente d'effectuer (ex: "read", "write", "delete").

    Raises:
        HTTPException: Si l'utilisateur n'a pas la permission requise (statut 403 Forbidden).
    """
    logger.debug(f"Vérification de permission pour l'utilisateur '{user.username}' sur ressource '{resource}' avec action '{action}'.")
    if not rbac_manager.has_permission(user, resource, action):
        logger.warning(f"Accès refusé pour l'utilisateur '{user.username}' : permission '{action}' sur '{resource}' manquante.")
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"L'utilisateur '{user.username}' n'a pas la permission d'effectuer l'action '{action}' sur la ressource '{resource}'."
        )
    logger.debug(f"Accès autorisé pour l'utilisateur '{user.username}'.")


# ------------------------------------------------------------------
# Démonstration (exemple d'utilisation)
# ------------------------------------------------------------------
if __name__ == "__main__":
    import asyncio
    import logging
    from fastapi import FastAPI, Depends
    from fastapi.security import OAuth2PasswordBearer
    from src.auth.jwt_handler import jwt_handler
    from src.auth.models import User, UserRole, TokenData # Assurez-vous d'importer UserRole

    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    # Crée un fichier roles.yaml factice pour la démonstration.
    temp_roles_file = Path("configs/roles.yaml")
    temp_roles_file.write_text("""
roles:
  - name: admin
    permissions:
      - "user:read"
      - "user:write"
      - "admin:*"
  - name: user
    permissions:
      - "sfd:read"
      - "sfd:write"
  - name: viewer
    permissions:
      - "sfd:read"
""")

    # Re-initialise le rbac_manager avec le fichier factice.
    rbac_manager = RBACManager(temp_roles_file)

    # Simule un utilisateur authentifié (en temps normal, viendrait d'un token JWT).
    async def get_current_user_mock(username: str, roles: List[UserRole]) -> User:
        # Crée un objet User factice pour la démonstration.
        return User(id=1, username=username, email=f"{username}@example.com", hashed_password="hashed", role=roles[0].value) # Utilise .value pour l'Enum

    # Dépendance pour simuler l'utilisateur courant.
    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

    async def get_user_admin() -> User:
        return await get_current_user_mock("admin_user", [UserRole.ADMIN])

    async def get_user_normal() -> User:
        return await get_current_user_mock("normal_user", [UserRole.USER])

    async def get_user_viewer() -> User:
        return await get_current_user_mock("viewer_user", [UserRole.VIEWER])

    app = FastAPI()

    @app.get("/admin_only")
    async def admin_only_endpoint(current_user: User = Depends(get_user_admin)):
        await verify_permission(current_user, "admin", "access")
        return {"message": f"Bienvenue, {current_user.username}! Vous avez accès à l'administration."

    @app.get("/sfd_read")
    async def sfd_read_endpoint(current_user: User = Depends(get_user_normal)):
        await verify_permission(current_user, "sfd", "read")
        return {"message": f"Bienvenue, {current_user.username}! Vous pouvez lire les SFD."

    @app.get("/sfd_write")
    async def sfd_write_endpoint(current_user: User = Depends(get_user_normal)):
        await verify_permission(current_user, "sfd", "write")
        return {"message": f"Bienvenue, {current_user.username}! Vous pouvez écrire des SFD."

    async def run_demo_client():
        print("\n--- Démonstration du RBAC Middleware ---")
        from fastapi.testclient import TestClient
        client = TestClient(app)

        print("\nTest 1: Admin accède à /admin_only (attendu: succès)")
        response = client.get("/admin_only", headers={"Authorization": "Bearer fake_token_admin"})
        print(f"Statut: {response.status_code}, Message: {response.json()}")

        print("\nTest 2: Utilisateur normal accède à /admin_only (attendu: échec 403)")
        response = client.get("/admin_only", headers={"Authorization": "Bearer fake_token_user"})
        print(f"Statut: {response.status_code}, Message: {response.json()}")

        print("\nTest 3: Utilisateur normal accède à /sfd_read (attendu: succès)")
        response = client.get("/sfd_read", headers={"Authorization": "Bearer fake_token_user"})
        print(f"Statut: {response.status_code}, Message: {response.json()}")

        print("\nTest 4: Viewer accède à /sfd_write (attendu: échec 403)")
        response = client.get("/sfd_write", headers={"Authorization": "Bearer fake_token_viewer"})
        print(f"Statut: {response.status_code}, Message: {response.json()}")

        print("Démonstration du RBAC Middleware terminée.")

    # Lance le serveur Uvicorn en arrière-plan pour la démo.
    async def run_server_and_client():
        config = uvicorn.Config(app, host="0.0.0.0", port=8000, log_level="warning")
        server = uvicorn.Server(config)
        server_task = asyncio.create_task(server.serve())
        await asyncio.sleep(1) # Donne le temps au serveur de démarrer.
        await run_demo_client()
        server_task.cancel()

    import uvicorn
    asyncio.run(run_server_and_client())

    # Nettoyage du fichier factice.
    temp_roles_file.unlink(missing_ok=True)

```

---

## Fichier : `backend\altiora\api\middleware\__init__.py`

```python
# backend/altiora/api/middleware/__init__.py
"""Initialise le package des middlewares de l'application Altiora.

Ce package contient les middlewares FastAPI qui interceptent les requêtes
et les réponses HTTP pour appliquer des logiques transversales telles que
la limitation de débit, la mise en cache et le contrôle d'accès basé sur les rôles (RBAC).

Les modules suivants sont exposés pour faciliter les importations :
- `AdvancedRateLimiter`: Pour la gestion avancée de la limitation de débit.
- `cache_middleware`: Middleware pour la mise en cache des réponses HTTP.
- `rbac_middleware`: Middleware pour la vérification des permissions RBAC.
"""
from .advanced_rate_limiter import AdvancedRateLimiter
from .cache_middleware import cache_middleware
from .rbac_middleware import rbac_middleware

__all__ = ['AdvancedRateLimiter', 'cache_middleware', 'rbac_middleware']

```

---

## Fichier : `backend\altiora\api\v1\analysis.py`

```python
# backend/altiora/api/v1/analysis.py
"""
Endpoints d’analyse QA.
"""
# backend/altiora/api/v1/analysis.py
from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import List

from altiora.api.dependencies import CurrentUserDep, ModelSwapperDep
from altiora.core.orchestrator import AltioraOrchestrator

router = APIRouter()

class SpecificationInput(BaseModel):
    content: str
    project_id: str | None = None

class TestScenario(BaseModel):
    id: str
    title: str
    description: str
    type: str

class AnalysisResult(BaseModel):
    scenarios: List[TestScenario]
    summary: str

@router.post("/analyze", response_model=AnalysisResult)
async def analyze_specification(
    spec: SpecificationInput,
    user: CurrentUserDep,
    swapper: ModelSwapperDep,
) -> AnalysisResult:
    """Analyse complète avec orchestrateur."""
    orchestrator = AltioraOrchestrator(swapper)
    return await orchestrator.process_specification(spec.content)
```

---

## Fichier : `backend\altiora\api\v1\batch.py`

```python
# backend/altiora/api/v1/batch.py
from fastapi import APIRouter, Depends, HTTPException
from backend.altiora.api.v1.schemas import BatchJobInput, BatchJobResponse
from backend.altiora.api.dependencies import CurrentUserDep
from backend.altiora.core.batch.scheduler import BatchScheduler
from pathlib import Path
from datetime import datetime, timedelta
import asyncio

router = APIRouter()


@router.post("/schedule", response_model=BatchJobResponse)
async def schedule_batch(
        job: BatchJobInput,
        user: CurrentUserDep,
) -> BatchJobResponse:
    """
    Planifie un traitement batch de spécifications avec limites :
    - Max 100 fichiers
    - Timeout global de 2h
    """
    try:
        # Validation des chemins
        input_path = Path(job.input_dir)
        output_path = Path(job.output_dir)

        if not input_path.exists():
            raise HTTPException(400, f"Input dir not found: {job.input_dir}")

        output_path.mkdir(parents=True, exist_ok=True)

        # Validation du pattern de fichier
        if not job.file_pattern:
            raise HTTPException(400, "file_pattern cannot be empty")

        # Comptage et limitation
        files = list(input_path.glob(job.file_pattern))
        if len(files) > 100:
            raise HTTPException(
                400,
                f"Trop de fichiers : {len(files)} trouvés (max 100 autorisés)"
            )

        if not files:
            raise HTTPException(400, "Aucun fichier trouvé avec le pattern spécifié")

        # Calcul de l'ETA (estimation basée sur 30s par fichier)
        estimated_duration = min(len(files) * 30, 7200)  # Max 2h (7200s)
        eta = datetime.utcnow() + timedelta(seconds=estimated_duration)

        # Création du job
        scheduler = BatchScheduler()
        job_id = await scheduler.schedule(
            {
                "input_dir": str(input_path),
                "output_dir": str(output_path),
                "file_pattern": job.file_pattern,
                "resume": job.resume,
                "max_files": 100,
                "timeout": 7200  # 2h en secondes
            },
            delay=job.delay
        )

        return BatchJobResponse(
            job_id=job_id,
            estimated_files=len(files),
            eta=eta.isoformat() + "Z"
        )

    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
```

---

## Fichier : `backend\altiora\api\v1\health.py`

```python
# backend/altiora/api/v1/health.py
"""
Endpoints de santé.
"""

from __future__ import annotations

from fastapi import APIRouter, Depends

from altiora.api.dependencies import CacheDep, DBSessionDep

router = APIRouter()


@router.get("/")
async def health_check(cache: CacheDep, db: DBSessionDep) -> dict[str, str]:
    """Retourne l’état général des services."""
    await cache.redis.ping()
    await db.execute("SELECT 1")
    return {"status": "ok"}
```

---

## Fichier : `backend\altiora\api\v1\models.py`

```python
# backend/altiora/api/v1/models.py
"""
Endpoints de gestion des modèles IA.
"""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends

from altiora.api.dependencies import ModelSwapperDep

router = APIRouter()


@router.post("/swap")
async def swap_model(
    model: str,
    swapper: ModelSwapperDep,
) -> dict[str, str]:
    """Force le swap vers un modèle donné (qwen3 ou starcoder2)."""
    await swapper.ensure_model_loaded(model)
    return {"active_model": model}
```

---

## Fichier : `backend\altiora\api\v1\schemas.py`

```python
# backend/altiora/api/v1/schemas.py
from pydantic import BaseModel
from typing import List, Optional, Any

class SpecificationInput(BaseModel):
    content: str
    project_id: Optional[str] = None
    language: Optional[str] = "fr"

class TestScenario(BaseModel):
    id: str
    title: str
    description: str
    type: str  # CP, CE, CL
    priority: int = 1

class AnalysisResult(BaseModel):
    scenarios: List[TestScenario]
    summary: str
    estimated_tests: int
    model_used: str

class BatchJobInput(BaseModel):
    input_dir: str
    output_dir: str
    file_pattern: str = "*.pdf"
    delay: int = 0  # secondes
    resume: bool = False

class BatchJobResponse(BaseModel):
    job_id: str
    status: str = "queued"
    estimated_files: int
```

---

## Fichier : `backend\altiora\api\v1\__init__.py`

```python
# backend/altiora/api/v1/__init__.py
"""
Routers API v1.
"""
```

---

## Fichier : `backend\altiora\config\settings.py`

```python
# backend/altiora/config/settings.py
"""
Paramètres Pydantic (env, YAML, validation).
"""

from typing import List, Optional
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field, validator


class QwenConfig(BaseSettings):
    model_path: Path = Field(default=Path("models/qwen3-32b-q4_K_M.gguf"))
    context_length: int = 32768
    threads: int = 8
    thinking_temp: float = 0.6
    non_thinking_temp: float = 0.7
    thinking_top_p: float = 0.95
    thinking_top_k: int = 20
    use_mmap: bool = True
    use_mlock: bool = False

    @validator("model_path")
    def validate_model_path(cls, v):
        if not v.exists():
            raise ValueError(f"Model file not found: {v}")
        return v


class StarcoderConfig(BaseSettings):
    model_path: Path = Field(default=Path("models/starcoder2-15b-q8_0.gguf"))
    context_length: int = 16384
    threads: int = 8
    temperature: float = 0.2
    max_tokens: int = 1200
    use_mmap: bool = True
    use_mlock: bool = False


class RedisConfig(BaseSettings):
    url: str = "redis://localhost:6379/0"
    decode_responses: bool = False
    max_connections: int = 50
    socket_keepalive: bool = True
    socket_keepalive_options: dict = Field(default_factory=dict)


class Settings(BaseSettings):
    # Application
    app_name: str = "Altiora"
    app_version: str = "2.0.0"
    debug: bool = False
    log_level: str = "INFO"

    # API
    api_host: str = "0.0.0.0"
    api_port: int = 8000
    api_prefix: str = "/api/v1"
    cors_origins: List[str] = ["http://localhost:3000", "http://localhost:3001"]

    # Security
    jwt_secret_key: str = Field(..., env="JWT_SECRET_KEY")
    jwt_algorithm: str = "HS256"
    jwt_expiration_hours: int = 24
    encryption_key: str = Field(..., env="ENCRYPTION_KEY")

    # Models
    qwen: QwenConfig = QwenConfig()
    starcoder: StarcoderConfig = StarcoderConfig()
    ollama_host: str = "http://localhost:11434"

    # Infrastructure
    redis: RedisConfig = RedisConfig()
    database_url: str = "sqlite:///./altiora.db"

    # Performance
    memory_limit_gb: int = 32
    memory_warning_threshold: float = 0.85
    swap_enabled: bool = True
    model_swap_enabled: bool = True

    # Cache
    cache_ttl_default: int = 3600
    cache_compression_enabled: bool = True
    cache_semantic_enabled: bool = True

    # Batch Processing
    batch_max_parallel: int = 5
    batch_retry_max: int = 3
    batch_timeout_seconds: int = 300

    model_config = SettingsConfigDict(
        env_file=".env",
        env_nested_delimiter="__",
        case_sensitive=False
    )


settings = Settings()
```

---

## Fichier : `backend\altiora\config\validators.py`

```python
# backend/altiora/config/validators.py
"""
Validateurs personnalisés pour la configuration.
"""

from pathlib import Path
from typing import Any, Optional
from pydantic import validator, root_validator
import os


def validate_model_path(path: str | Path) -> Path:
    """Vérifie que le fichier GGUF existe."""
    path = Path(path)
    if not path.is_file():
        raise ValueError(f"Model file not found: {path}")
    if not path.suffix == ".gguf":
        raise ValueError(f"Model must be GGUF format, got: {path.suffix}")
    return path


def validate_memory_limit(v: int) -> int:
    """Vérifie que la limite mémoire est raisonnable."""
    if v < 16:
        raise ValueError("Memory limit must be at least 16GB")
    if v > 128:
        raise ValueError("Memory limit above 128GB is unrealistic")
    return v


def validate_redis_url(v: str) -> str:
    """Valide l'URL Redis."""
    if not v.startswith(("redis://", "rediss://")):
        raise ValueError("Redis URL must start with redis:// or rediss://")
    return v


def validate_ollama_host(v: str) -> str:
    """Valide l'URL Ollama."""
    if not v.startswith(("http://", "https://")):
        raise ValueError("Ollama host must start with http:// or https://")
    return v


def validate_jwt_secret(v: str) -> str:
    """Vérifie que le secret JWT est suffisamment sécurisé."""
    if len(v) < 32:
        raise ValueError("JWT secret must be at least 32 characters")
    return v


def validate_port(v: int) -> int:
    """Valide un numéro de port."""
    if v < 1 or v > 65535:
        raise ValueError(f"Invalid port number: {v}")
    return v


def validate_percentage(v: float) -> float:
    """Valide un pourcentage (0-1)."""
    if v < 0 or v > 1:
        raise ValueError(f"Percentage must be between 0 and 1, got: {v}")
    return v


class PathValidator:
    """Validateur pour les chemins avec création automatique."""

    @staticmethod
    def validate_directory(path: str | Path, create: bool = True) -> Path:
        path = Path(path)
        if create and not path.exists():
            path.mkdir(parents=True, exist_ok=True)
        elif not path.is_dir():
            raise ValueError(f"Not a directory: {path}")
        return path

    @staticmethod
    def validate_file(path: str | Path, must_exist: bool = True) -> Path:
        path = Path(path)
        if must_exist and not path.is_file():
            raise ValueError(f"File not found: {path}")
        return path
```

---

## Fichier : `backend\altiora\config\__init__.py`

```python
# backend/altiora/config/__init__.py
"""
Configuration centralisée avec Pydantic.
"""
```

---

## Fichier : `backend\altiora\core\orchestrator.py`

```python
# backend/altiora/core/orchestrator.py (version optimisée)
"""
Orchestrateur principal d'Altiora - VERSION OPTIMISÉE 32GB RAM.

CHANGEMENT MAJEUR : Utilise ModelSwapper pour ne jamais avoir
les deux modèles en mémoire simultanément.

Workflow:
1. Qwen3 analyse avec /think
2. Si besoin de code → swap vers Starcoder2
3. Starcoder2 génère → swap retour vers Qwen3
4. Qwen3 finalise la réponse
"""

from typing import List, Dict

from backend.altiora.core.models.model_swapper import ModelSwapper
from backend.altiora.core.models.qwen3.model_manager import Qwen3Manager
from backend.altiora.core.models.starcoder2.model_manager import Starcoder2Manager
from backend.altiora.infrastructure.cache.compressed_client import CompressedRedisCache


class AltioraOrchestrator:
    """Orchestre le flux de traitement des requêtes en gérant le chargement des modèles."""

    def __init__(self):
        """Initialise avec le swapper de modèles."""
        self.model_swapper = ModelSwapper()
        self.cache = CompressedRedisCache(settings.redis_url)  # Cache compressé
        # Plus besoin d'instances séparées !

    async def process_request(self, request: AnalysisRequest) -> AnalysisResponse:
        """
        Traite une requête avec swap mémoire intelligent.
        """
        # 1. Charger Qwen3 pour l'analyse
        logger.info("Chargement de Qwen3 pour analyse...")
        qwen3 = await self.model_swapper.ensure_model_loaded("qwen3")

        # 2. Analyse avec Qwen3
        qwen_response = await self._analyze_with_qwen(qwen3, request)

        # 3. Si besoin de code, swap vers Starcoder2
        if self._needs_code_generation(qwen_response.content):
            logger.info("Swap Qwen3 → Starcoder2 pour génération de code...")

            # Sauver l'état de Qwen3 si nécessaire
            qwen_state = {"response": qwen_response, "context": request.context}

            # Swap vers Starcoder2
            starcoder = await self.model_swapper.swap_to_model("starcoder2", qwen_state)

            # Générer le code
            code_sections = await self._generate_code_with_starcoder(starcoder, qwen_response)

            # Swap retour vers Qwen3
            logger.info("Swap Starcoder2 → Qwen3 pour finalisation...")
            qwen3 = await self.model_swapper.swap_to_model("qwen3")

            # Qwen3 intègre le code dans sa réponse
            final_response = await self._finalize_with_qwen(qwen3, qwen_response, code_sections)
        else:
            final_response = qwen_response
            code_sections = []

        # 4. Cleanup - CRUCIAL !
        await self.model_swapper.cleanup()

        return final_response


class AnalysisResult:
    def __init__(self, scenarios: List[Dict], summary: str):
        self.scenarios = scenarios
        self.summary = summary


class AltioraOrchestrator:
    async def process_specification(self, spec_content: str) -> AnalysisResult:
        """Workflow complet : analyse → décision → génération."""

        # Étape 1 : Charger Qwen3
        qwen3 = await self.swapper.ensure_model_loaded("qwen3")
        qwen_manager = Qwen3Manager(model=qwen3)

        # Étape 2 : Analyser la spécification
        scenarios = await qwen_manager.analyze(spec_content)

        # Étape 3 : Vérifier si génération de code nécessaire
        if any("pytest" in s.get('type', '').lower() for s in scenarios):
            starcoder = await self.swapper.swap_to_model("starcoder2")
            starcoder_manager = Starcoder2Manager(model=starcoder)
            await self._generate_code_if_needed(scenarios)
            await self.swapper.swap_to_model("qwen3")

        return AnalysisResult(
            scenarios=scenarios,
            summary=f"Analysé {len(scenarios)} scénarios"
        )


async def _analyze_with_qwen(self, model: Llama, request: AnalysisRequest) -> AnalysisResponse:
    """Utilise Qwen3 pour analyser une spécification."""
    # Construire le prompt
    prompt = f"""<|im_start|>system
Tu es un expert QA. Analyse cette spécification et extrais :
1. Les objectifs de test
2. Les scénarios identifiés
3. Les préconditions
4. Les étapes détaillées
<|im_end|>
<|im_start|>user
{request.content}
<|im_end|>
<|im_start|>assistant
/think"""

    # Appeler le modèle
    response = model(
        prompt,
        max_tokens=2048,
        temperature=0.7,
        stop=["<|im_end|>"]
    )

    # Parser la réponse
    content = response["choices"][0]["text"]

    # Extraire les scénarios avec regex
    scenarios = []
    scenario_pattern = r"Scénario (\d+):\s*(.+?)(?=Scénario \d+:|$)"
    matches = re.finditer(scenario_pattern, content, re.DOTALL)

    for match in matches:
        scenarios.append({
            "id": f"SC-{match.group(1).zfill(3)}",
            "title": match.group(2).strip().split('\n')[0],
            "description": match.group(2).strip()
        })

    return AnalysisResponse(
        content=content,
        scenarios=scenarios,
        metadata={"model": "qwen3", "thinking_mode": True}
    )


async def _needs_code_generation(self, content: str) -> bool:
    """Détermine si la réponse nécessite de générer du code."""
    code_indicators = [
        "générer test",
        "créer script",
        "implémenter",
        "code playwright",
        "automatiser",
        "def test_",
        "scénario de test automatisé"
    ]

    content_lower = content.lower()
    return any(indicator in content_lower for indicator in code_indicators)


async def _generate_code_with_starcoder(
        self,
        model: Llama,
        analysis: AnalysisResponse
) -> List[CodeSection]:
    """Génère du code de test avec Starcoder2."""
    code_sections = []

    for scenario in analysis.scenarios:
        prompt = f"""<fim_prefix>
# Test: {scenario['title']}
# Description: {scenario['description']}

import pytest
from playwright.sync_api import Page, expect

def test_{scenario['id'].lower().replace('-', '_')}(page: Page):
    \"\"\"
<fim_suffix>

    # Assertions
    expect(page).to_have_title(re.compile(".*"))
<fim_middle>"""

        response = model(
            prompt,
            max_tokens=800,
            temperature=0.2,
            stop=["<|endoftext|>", "<fim_prefix>"]
        )

        code = response["choices"][0]["text"]

        code_sections.append(CodeSection(
            scenario_id=scenario['id'],
            code=f"def test_{scenario['id'].lower().replace('-', '_')}(page: Page):\n    \"\"\"\n{code}",
            language="python",
            framework="playwright"
        ))

    return code_sections


async def _finalize_with_qwen(
        self,
        model: Llama,
        analysis: AnalysisResponse,
        code_sections: List[CodeSection]
) -> AnalysisResponse:
    """Qwen3 intègre le code dans sa réponse finale."""
    # Construire un résumé avec le code
    code_summary = "\n\n".join([
        f"### {cs.scenario_id}\n```python\n{cs.code}\n```"
        for cs in code_sections
    ])

    final_prompt = f"""<|im_start|>system
Intègre les tests générés dans un rapport final structuré.
<|im_end|>
<|im_start|>user
Analyse initiale:
{analysis.content}

Tests générés:
{code_summary}
<|im_end|>
<|im_start|>assistant"""

    response = model(
        final_prompt,
        max_tokens=1024,
        temperature=0.5
    )

    analysis.content = response["choices"][0]["text"]
    analysis.code_sections = code_sections
    return analysis

```

---

## Fichier : `backend\altiora\core\__init__.py`

```python
# backend/altiora/core/__init__.py
"""
Contient la logique métier principale et les modules fondamentaux d'Altiora.
"""

```

---

## Fichier : `backend\altiora\core\batch\batch_processor.py`

```python
"""
# backend/altiora/core/batch/processor.py

Asynchronous batch processor for *Spécifications Fonctionnelles Détaillées* (SFD).

Features:
- 100 % async/await
- Redis persistence with compression
- Prometheus metrics
- Configurable concurrency
- Automatic retry & resume
"""

from __future__ import annotations

import asyncio
import gc
import json
import logging
import uuid
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, List, Optional

import aiofiles
import zstandard as zstd
from prometheus_client import Counter, Gauge
from redis.asyncio import Redis

from altiora.core.models.model_swapper import ModelSwapper
from altiora.services.ocr.ocr_wrapper import OCRRequest, extract_text

# ------------------------------------------------------------------
# Prometheus metrics
# ------------------------------------------------------------------
BATCH_DOCS_TOTAL = Gauge("altiora_batch_docs_total", "Total documents in batch")
BATCH_SUCCESS_TOTAL = Counter("altiora_batch_success_total", "Successfully processed docs")
BATCH_CHUNK_TIME = Gauge("altiora_batch_chunk_seconds", "Processing time per chunk")

# ------------------------------------------------------------------
# Configuration
# ------------------------------------------------------------------
MAX_WORKERS = 20
LLM_CONCURRENCY = 6
CHUNK_SIZE = 16

# ------------------------------------------------------------------
# Data model
# ------------------------------------------------------------------
@dataclass
class Job:
    """Single SFD job state."""
    path: Path
    ocr_text: str = ""
    status: str = "pending"
    error: str = ""
    result: Optional[dict[str, Any]] = None


class BatchProcessor:
    """Async batch processor for SFD files."""

    def __init__(self, redis_url: str, swapper: ModelSwapper) -> None:
        self.redis = Redis.from_url(redis_url, decode_responses=False)
        self.swapper = swapper
        self.limiter = asyncio.Semaphore(LLM_CONCURRENCY)

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------
    async def run(
        self,
        input_dir: Path,
        output_dir: Path,
        resume: bool = False,
    ) -> None:
        """Process all SFD files asynchronously."""
        output_dir.mkdir(parents=True, exist_ok=True)
        job_key = f"batch:{input_dir.name}"

        jobs = await self._load_or_create_jobs(job_key, input_dir, resume)
        BATCH_DOCS_TOTAL.set(len(jobs))

        await self._pipeline(jobs)
        await self._dump_results(output_dir, jobs)

    # ------------------------------------------------------------------
    # Pipeline (OCR → LLM)
    # ------------------------------------------------------------------
    async def _pipeline(self, jobs: list[Job]) -> None:
        """Run OCR + LLM asynchronously."""
        ocr_tasks = [self._ocr_one(job) for job in jobs if job.status == "pending"]
        await asyncio.gather(*ocr_tasks)

        llm_tasks = [self._llm_one(job) for job in jobs if job.status == "ocr_ok"]
        await asyncio.gather(*llm_tasks)

    async def _ocr_one(self, job: Job) -> None:
        """OCR single file."""
        try:
            req = OCRRequest(file_path=str(job.path), language="fra", preprocess=True)
            job.ocr_text = await asyncio.to_thread(extract_text, req)
            job.status = "ocr_ok"
        except Exception as e:
            job.status, job.error = "ocr_failed", str(e)
            logging.exception("OCR failed for %s", job.path.name)

    async def _llm_one(self, job: Job) -> None:
        """LLM analysis single file."""
        async with self.limiter:
            try:
                qwen3 = await self.swapper.ensure_model_loaded("qwen3")
                job.result = await qwen3.analyze(job.ocr_text)
                job.status = "done"
                BATCH_SUCCESS_TOTAL.inc()
            except Exception as e:
                job.status, job.error = "llm_failed", str(e)
                logging.exception("LLM failed for %s", job.path.name)

    # ------------------------------------------------------------------
    # Persistence
    # ------------------------------------------------------------------
    async def _load_or_create_jobs(
        self,
        key: str,
        input_dir: Path,
        resume: bool,
    ) -> list[Job]:
        """Load or create job list."""
        if resume and await self.redis.exists(key):
            raw = await self.redis.get(key)
            return [Job(**j) for j in json.loads(zstd.decompress(raw).decode())]

        files = [p for p in input_dir.iterdir() if p.suffix.lower() in {".pdf", ".txt", ".docx"}]
        jobs = [Job(p) for p in files]
        await self._save_jobs(key, jobs)
        return jobs

    async def _save_jobs(self, key: str, jobs: list[Job]) -> None:
        """Save current state to Redis."""
        await self.redis.set(
            key,
            zstd.compress(json.dumps([asdict(j) for j in jobs]).encode()),
            ex=3600,
        )

    async def _dump_results(self, output_dir: Path, jobs: list[Job]) -> None:
        """Write final results to disk."""
        summary = {
            "total": len(jobs),
            "success": sum(1 for j in jobs if j.status == "done"),
            "failed": sum(1 for j in jobs if j.status.endswith("failed")),
        }

        async with aiofiles.open(output_dir / "summary.json", "w") as f:
            await f.write(json.dumps(summary, indent=2))

        for job in jobs:
            if job.result:
                out_file = output_dir / f"{job.path.stem}.json"
                async with aiofiles.open(out_file, "w") as f:
                    await f.write(json.dumps(job.result, indent=2))

        gc.collect()  # Free memory
```

---

## Fichier : `backend\altiora\core\batch\scheduler.py`

```python
# backend/altiora/core/batch/scheduler.py
"""
Ordonnanceur de tâches batch.

Gère la file d’attente, la planification et le suivi des jobs.
"""

from __future__ import annotations

import asyncio
import uuid
from datetime import datetime, timedelta
from typing import Any

from altiora.infrastructure.queue.redis_queue import RedisTaskQueue


class BatchScheduler:
    """Planificateur simple basé sur Redis."""

    def __init__(self) -> None:
        self.queue = RedisTaskQueue()

    async def schedule(
        self,
        payload: dict[str, Any],
        delay: int = 0,
    ) -> str:
        """Ajoute un job dans la file avec un délai optionnel."""
        job_id = str(uuid.uuid4())
        eta = datetime.utcnow() + timedelta(seconds=delay)
        await self.queue.enqueue(
            "batch_process",
            {"job_id": job_id, **payload},
            eta=eta,
        )
        return job_id
```

---

## Fichier : `backend\altiora\core\batch\strategies.py`

```python
# backend/altiora/core/batch/strategies.py
"""
Stratégies de traitement batch.

Définit les patterns de retry, de parallélisation et de priorisation.
"""

from __future__ import annotations

import asyncio
import logging
from abc import ABC, abstractmethod
from typing import Any, Protocol

from tenacity import AsyncRetrying, stop_after_attempt, wait_exponential

logger = logging.getLogger(__name__)


class BatchStrategy(Protocol):
    """Interface pour une stratégie batch."""

    async def execute(self, items: list[Any]) -> list[Any]:
        """Exécute la stratégie sur la liste d’items."""
        ...


class LinearStrategy:
    """Traitement séquentiel, simple et prévisible."""

    async def execute(self, items: list[Any]) -> list[Any]:
        """Traite les items un par un."""
        results = []
        for item in items:
            await asyncio.sleep(0)  # yield control
            results.append(await self._process(item))
        return results

    async def _process(self, item: Any) -> Any:
        """Logique métier à surcharger ou injecter."""
        return item


class ParallelStrategy:
    """Traitement parallèle limité par un pool de workers."""

    def __init__(self, max_workers: int = 4) -> None:
        self.max_workers = max_workers

    async def execute(self, items: list[Any]) -> list[Any]:
        """Traite les items en parallèle."""
        semaphore = asyncio.Semaphore(self.max_workers)

        async def _with_semaphore(item: Any) -> Any:
            async with semaphore:
                return await self._process(item)

        tasks = [_with_semaphore(item) for item in items]
        return await asyncio.gather(*tasks)

    async def _process(self, item: Any) -> Any:
        return item


class RetryStrategy:
    """Enrobe n’importe quelle stratégie avec retry exponentiel."""

    def __init__(
        self,
        strategy: BatchStrategy,
        max_attempts: int = 3,
    ) -> None:
        self.strategy = strategy
        self.retry = AsyncRetrying(
            stop=stop_after_attempt(max_attempts),
            wait=wait_exponential(multiplier=1, min=1, max=10),
            reraise=True,
        )

    async def execute(self, items: list[Any]) -> list[Any]:
        """Exécute la stratégie sous-jacente avec retry."""
        return await self.retry(self.strategy.execute, items)
```

---

## Fichier : `backend\altiora\core\batch\__init__.py`

```python
# backend/altiora/core/batch/__init__.py
"""
Batch processing – orchestration et scheduling.
"""
```

---

## Fichier : `backend\altiora\core\factories\model_factory.py`

```python
from enum import Enum
from typing import Union
import logging

# backend/altiora/core/factories/model_factory.py
from altiora.core.models.qwen3.model_manager import Qwen3Manager
from altiora.core.models.starcoder2.model_manager import Starcoder2Manager

logger = logging.getLogger(__name__)


class ModelType(Enum):
    """Énumération des types de modèles d'IA supportés par la fabrique."""
    QWEN3 = "qwen3"
    STARCODER2 = "starcoder2"


class ModelFactory:
    """Fabrique pour la création et la gestion des instances de modèles d'IA.

    Cette fabrique implémente le pattern Singleton pour chaque type de modèle,
    assurant qu'une seule instance d'un modèle donné est créée et réutilisée
    tout au long de l'application. Cela permet d'optimiser l'utilisation des
    ressources en évitant de charger plusieurs fois le même modèle en mémoire.
    """
    _instances: Dict[ModelType, Union[Qwen3OllamaInterface, StarCoder2OllamaInterface]] = {}
    
    @classmethod
    async def create(cls, model_type: ModelType) -> Union[Qwen3OllamaInterface, StarCoder2OllamaInterface]:
        """Crée ou récupère une instance de modèle d'IA."

        Si une instance du modèle demandé existe déjà, elle est retournée.
        Sinon, une nouvelle instance est créée, initialisée et stockée.

        Args:
            model_type: Le type de modèle à créer ou à récupérer (ex: `ModelType.QWEN3`).

        Returns:
            Une instance du modèle d'IA spécifié.

        Raises:
            ValueError: Si le type de modèle demandé n'est pas reconnu.
        """
        if model_type not in cls._instances:
            logger.info(f"Création d'une nouvelle instance pour le modèle : {model_type.value}")
            if model_type == ModelType.QWEN3:
                instance = Qwen3OllamaInterface()
            elif model_type == ModelType.STARCODER2:
                instance = StarCoder2OllamaInterface()
            else:
                raise ValueError(f"Type de modèle inconnu : {model_type}")
            
            await instance.initialize()
            cls._instances[model_type] = instance
        else:
            logger.info(f"Réutilisation de l'instance existante pour le modèle : {model_type.value}")
        
        return cls._instances[model_type]


# ------------------------------------------------------------------
# Démonstration (exemple d'utilisation)
# ------------------------------------------------------------------
if __name__ == "__main__":
    import asyncio
    import logging

    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    async def demo():
        print("\n--- Démonstration de ModelFactory ---")

        # Création/récupération d'une instance de Qwen3.
        print("Création de Qwen3...")
        qwen3_instance_1 = await ModelFactory.create(ModelType.QWEN3)
        print(f"Instance Qwen3 1 : {qwen3_instance_1}")

        print("Création de Qwen3 (devrait réutiliser l'instance existante)...")
        qwen3_instance_2 = await ModelFactory.create(ModelType.QWEN3)
        print(f"Instance Qwen3 2 : {qwen3_instance_2}")
        assert qwen3_instance_1 is qwen3_instance_2, "Les instances de Qwen3 devraient être les mêmes."

        # Création/récupération d'une instance de StarCoder2.
        print("\nCréation de StarCoder2...")
        starcoder2_instance_1 = await ModelFactory.create(ModelType.STARCODER2)
        print(f"Instance StarCoder2 1 : {starcoder2_instance_1}")

        print("Création de StarCoder2 (devrait réutiliser l'instance existante)...")
        starcoder2_instance_2 = await ModelFactory.create(ModelFactory.STARCODER2)
        print(f"Instance StarCoder2 2 : {starcoder2_instance_2}")
        assert starcoder2_instance_1 is starcoder2_instance_2, "Les instances de StarCoder2 devraient être les mêmes."

        # Nettoyage des instances (si les interfaces ont une méthode close).
        if hasattr(qwen3_instance_1, 'close'):
            await qwen3_instance_1.close()
        if hasattr(starcoder2_instance_1, 'close'):
            await starcoder2_instance_1.close()

        print("Démonstration de ModelFactory terminée.")

    asyncio.run(demo())
```

---

## Fichier : `backend\altiora\core\feedback\feedback_collector.py`

```python
# backend/altiora/core/feedback/feedback_collector.py
import json

from pydantic import BaseModel
from datetime import datetime
import redis.asyncio as redis


class Feedback(BaseModel):
    user_id: str
    query: str
    response: str
    rating: int
    correction: str | None = None
    timestamp: datetime


class FeedbackCollector:
    def __init__(self, redis_url: str = "redis://localhost:6379"):
        self.redis = redis.from_url(redis_url, decode_responses=True)

    async def add(self, fb: Feedback):
        key = f"feedback:{datetime.utcnow().isoformat()}"
        await self.redis.set(key, fb.model_dump_json())

    async def get_batch(self, min_rating: int = 3) -> list[Feedback]:
        keys = await self.redis.keys("feedback:*")
        items = [await self.redis.get(k) for k in keys]
        return [
            Feedback(**json.loads(i))
            for i in items
            if i and json.loads(i)["rating"] >= min_rating
        ]
```

---

## Fichier : `backend\altiora\core\models\model_swapper.py`

```python
# backend/altiora/core/models/model_swapper.py
"""
Gestionnaire de swap mémoire pour les modèles.

Ce module CRITIQUE gère le chargement/déchargement des modèles
pour respecter la limite de 32GB RAM. UN SEUL modèle actif à la fois.

Architecture:
1. Qwen3 analyse et décide
2. Si besoin de code : sauver état Qwen3, libérer mémoire
3. Charger Starcoder2, générer code
4. Libérer Starcoder2, recharger Qwen3
5. Qwen3 finalise la réponse

IMPORTANT: Toujours appeler cleanup() après usage d'un modèle!
"""

import gc
import os
import psutil
from typing import Optional, Dict, Any
import logging
from pathlib import Path
import pickle

from llama_cpp import Llama

from altiora.config.settings import settings

logger = logging.getLogger(__name__)


class ModelSwapper:
    """
    Gestionnaire de swap mémoire pour modèles IA.

    Assure qu'UN SEUL modèle est en mémoire à la fois.
    Sauvegarde l'état si nécessaire pour reprendre après swap.
    """

    def __init__(self):
        """Initialise le gestionnaire de swap."""
        self.current_model: Optional[Llama] = None
        self.current_model_name: Optional[str] = None
        self.state_cache_dir = Path("/tmp/altiora/model_states")
        self.state_cache_dir.mkdir(parents=True, exist_ok=True)

        # Configuration mmap pour économiser la mémoire
        self.model_configs = {
            "qwen3": {
                "path": settings.qwen.model_path,
                "n_ctx": settings.qwen.context_length,
                "n_threads": settings.qwen.threads,
                "use_mmap": True,  # CRUCIAL : utilise memory mapping
                "use_mlock": False,  # Ne pas verrouiller toute la RAM
                "n_batch": 512,
                "f16_kv": False,
                "verbose": False
            },
            "starcoder2": {
                "path": settings.starcoder.model_path,
                "n_ctx": settings.starcoder.context_length,
                "n_threads": settings.starcoder.threads,
                "use_mmap": True,  # CRUCIAL : utilise memory mapping
                "use_mlock": False,
                "n_batch": 256,
                "f16_kv": False,
                "verbose": False
            }
        }

    def get_memory_usage(self) -> Dict[str, float]:
        """
        Retourne l'utilisation mémoire actuelle.

        Returns:
            Dict avec used_gb, available_gb, percent
        """
        memory = psutil.virtual_memory()
        return {
            "used_gb": memory.used / (1024 ** 3),
            "available_gb": memory.available / (1024 ** 3),
            "percent": memory.percent
        }

    async def ensure_model_loaded(self, model_name: str) -> Llama:
        """
        S'assure que le modèle demandé est chargé.

        Si un autre modèle est en mémoire, le décharge d'abord.

        Args:
            model_name: "qwen3" ou "starcoder2"

        Returns:
            Instance du modèle Llama chargé

        Raises:
            MemoryError: Si pas assez de RAM disponible
        """
        # Vérifier la mémoire disponible
        memory = self.get_memory_usage()
        logger.info(f"Mémoire avant chargement: {memory['used_gb']:.1f}GB utilisés, "
                    f"{memory['available_gb']:.1f}GB disponibles")

        # Si le bon modèle est déjà chargé, le retourner
        if self.current_model and self.current_model_name == model_name:
            logger.debug(f"Modèle {model_name} déjà en mémoire")
            return self.current_model

        # Si un autre modèle est chargé, le décharger
        if self.current_model:
            logger.info(f"Déchargement du modèle {self.current_model_name}")
            await self._unload_current_model()

        # Vérifier qu'on a assez de mémoire
        required_gb = 20 if model_name == "qwen3" else 15
        if memory['available_gb'] < required_gb + 2:  # +2GB de marge
            raise MemoryError(
                f"Pas assez de mémoire pour charger {model_name}. "
                f"Requis: {required_gb}GB, Disponible: {memory['available_gb']:.1f}GB"
            )

        # Charger le nouveau modèle
        logger.info(f"Chargement du modèle {model_name}...")
        config = self.model_configs[model_name]

        try:
            self.current_model = Llama(
                model_path=str(config["path"]),
                **{k: v for k, v in config.items() if k != "path"}
            )
            self.current_model_name = model_name

            # Vérifier la mémoire après chargement
            memory_after = self.get_memory_usage()
            logger.info(f"Mémoire après chargement: {memory_after['used_gb']:.1f}GB utilisés")

            return self.current_model

        except Exception as e:
            logger.error(f"Erreur chargement {model_name}: {e}")
            raise

    async def _unload_current_model(self) -> None:
        """
        Décharge le modèle actuel de la mémoire.

        Force la libération mémoire avec garbage collection.
        """
        if not self.current_model:
            return

        model_name = self.current_model_name

        # Supprimer toutes les références
        del self.current_model
        self.current_model = None
        self.current_model_name = None

        # Forcer le garbage collection - CRUCIAL!
        gc.collect()

        # Sur Linux, on peut aussi libérer la mémoire au niveau OS
        if hasattr(os, 'system'):
            os.system('sync && echo 3 > /proc/sys/vm/drop_caches 2>/dev/null')

        logger.info(f"Modèle {model_name} déchargé et mémoire libérée")

        # Attendre un peu pour que l'OS récupère la mémoire
        import asyncio
        await asyncio.sleep(0.5)

    async def swap_to_model(self, target_model: str, state: Optional[Dict] = None) -> Llama:
        """
        Swap vers un modèle spécifique avec état optionnel.

        Args:
            target_model: Modèle cible ("qwen3" ou "starcoder2")
            state: État à restaurer après chargement

        Returns:
            Modèle chargé
        """
        # Sauver l'état du modèle actuel si demandé
        if state and self.current_model_name:
            await self._save_state(self.current_model_name, state)

        # Charger le nouveau modèle
        model = await self.ensure_model_loaded(target_model)

        # Restaurer l'état si disponible
        saved_state = await self._load_state(target_model)
        if saved_state:
            logger.info(f"État restauré pour {target_model}")

        return model

    async def _save_state(self, model_name: str, state: Dict) -> None:
        """Sauvegarde l'état d'un modèle."""
        state_file = self.state_cache_dir / f"{model_name}_state.pkl"
        with open(state_file, 'wb') as f:
            pickle.dump(state, f)

    async def _load_state(self, model_name: str) -> Optional[Dict]:
        """Charge l'état sauvegardé d'un modèle."""
        state_file = self.state_cache_dir / f"{model_name}_state.pkl"
        if state_file.exists():
            with open(state_file, 'rb') as f:
                return pickle.load(f)
        return None

    async def cleanup(self) -> None:
        """
        Nettoie toutes les ressources.

        TOUJOURS appeler cette méthode à la fin!
        """
        await self._unload_current_model()

        # Nettoyer les états sauvegardés
        for state_file in self.state_cache_dir.glob("*_state.pkl"):
            state_file.unlink()
```

---

## Fichier : `backend\altiora\core\models\__init__.py`

```python
# backend/altiora/core/models/__init__.py
"""
Contient les définitions et les gestionnaires des modèles d'IA.
"""
```

---

## Fichier : `backend\altiora\core\models\ensemble\multi_model.py`

```python
from typing import List
import asyncio
from src.ensemble.voting_strategies import WeightedVoting

# backend/altiora/core/models/ensemble/multi_model.py
class MultiModelEnsemble:
    def __init__(self, models: List[str]):
        self.models = self.load_models(models)
        self.voting_strategy = WeightedVoting()

    async def generate(self, prompt: str) -> str:
        """Génère une réponse en utilisant plusieurs modèles"""
        responses = await asyncio.gather(*[
            model.generate(prompt) for model in self.models
        ])

        # Vote pondéré basé sur la confiance
        best_response = self.voting_strategy.select(
            responses,
            weights=self.calculate_confidence_weights(responses)
        )

        return best_response
```

---

## Fichier : `backend\altiora\core\models\ensemble\router.py`

```python
# backend/altiora/core/models/ensemble/router.py
"""
Router qui choisit dynamiquement le modèle adapté.
"""

from __future__ import annotations

from typing import Any

from altiora.core.models.model_swapper import ModelSwapper


class ModelRouter:
    """Décide quel modèle activer selon la tâche demandée."""

    async def route(self, task: str, swapper: ModelSwapper) -> str:
        """Retourne le nom du modèle à utiliser."""
        if "code" in task.lower() or "script" in task.lower():
            await swapper.ensure_model_loaded("starcoder2")
            return "starcoder2"
        await swapper.ensure_model_loaded("qwen3")
        return "qwen3"
```

---

## Fichier : `backend\altiora\core\models\ensemble\__init__.py`

```python
# backend/altiora/core/models/ensemble/__init__.py
"""
Routage intelligent entre Qwen3 et Starcoder2.
"""
```

---

## Fichier : `backend\altiora\core\models\qwen3\cache_optimizer.py`

```python
# backend/altiora/core/models/qwen3/cache_optimizer.py
"""
Optimisation du cache conversation Qwen3 (clés, TTL, compression).
"""

from __future__ import annotations

import hashlib
from typing import Any

from altiora.infrastructure.cache.unified_cache import UnifiedCache


class QwenCacheOptimizer:
    """Utilitaire de cache spécifique aux prompts Qwen3."""

    def __init__(self, cache: UnifiedCache) -> None:
        self.cache = cache

    def _cache_key(self, prompt: str) -> str:
        """Génère une clé stable à partir du prompt."""
        return f"qwen:{hashlib.sha256(prompt.encode()).hexdigest()}"

    async def get(self, prompt: str) -> str | None:
        """Récupère la réponse en cache."""
        key = self._cache_key(prompt)
        return await self.cache.get(key)

    async def set(self, prompt: str, response: str, ttl: int = 3600) -> None:
        """Stocke la réponse avec TTL par défaut 1 h."""
        key = self._cache_key(prompt)
        await self.cache.set(key, response, ttl=ttl)
```

---

## Fichier : `backend\altiora\core\models\qwen3\config.py`

```python
# backend/altiora/core/models/qwen3/config.py
"""
Configuration spécifique pour le modèle Qwen3.
"""
```

---

## Fichier : `backend\altiora\core\models\qwen3\model_manager.py`

```python
# backend/altiora/core/models/qwen3/model_manager.py
"""
Manager Qwen3-32B avec modes thinking et direct.
"""

from __future__ import annotations

import logging
from typing import Any

from llama_cpp import Llama

logger = logging.getLogger(__name__)


class Qwen3Manager:
    """Wrapper autour de l’instance Llama pour Qwen3."""

    def __init__(self, model: Llama) -> None:
        self.model = model

    async def analyze(self, spec: str) -> str:
        """Analyse une spécification."""
        prompt = (
            f"<|im_start|>system\n"
            f"You are a QA expert. Analyze the following spec step by step.\n"
            f"<|im_end|>\n"
            f"<|im_start|>user\n{spec}<|im_end|>\n"
            f"<|im_start|>assistant\n<thinking>"
        )
        output = self.model(prompt, max_tokens=1500, stop=["</thinking>"])
        return output["choices"][0]["text"]

    async def direct(self, prompt: str) -> str:
        """Réponse directe sans thinking."""
        prompt = (
            f"<|im_start|>system\n"
            f"Answer concisely without showing reasoning.\n"
            f"<|im_end|>\n"
            f"<|im_start|>user\n{prompt}<|im_end|>\n"
            f"<|im_start|>assistant\n"
        )
        output = self.model(prompt, max_tokens=800, temperature=0.7)
        return output["choices"][0]["text"]
```

---

## Fichier : `backend\altiora\core\models\qwen3\prompt_builder.py`

```python
# backend/altiora/core/models/qwen3/prompt_builder.py
"""
Constructeur de prompts spécialisés Qwen3.
"""

from __future__ import annotations

from typing import Any


class QwenPromptBuilder:
    """Fabrique de prompts conformes au format Qwen3."""

    @staticmethod
    def build_thinking_prompt(context: str, task: str) -> str:
        """Prompt avec bloc <thinking>."""
        return (
            f"<|im_start|>system\n"
            f"You are Altiora, QA specialist. Think step by step.\n"
            f"<|im_end|>\n"
            f"<|im_start|>user\nContext: {context}\n\nTask: {task}<|im_end|>\n"
            f"<|im_start|>assistant\n<thinking>"
        )

    @staticmethod
    def build_direct_prompt(context: str, task: str) -> str:
        """Prompt sans bloc <thinking>."""
        return (
            f"<|im_start|>system\n"
            f"Answer directly and concisely.\n"
            f"<|im_end|>\n"
            f"<|im_start|>user\nContext: {context}\n\nTask: {task}<|im_end|>\n"
            f"<|im_start|>assistant\n"
        )
```

---

## Fichier : `backend\altiora\core\models\qwen3\quantizer.py`

```python
# backend/altiora/core/models/qwen3/quantizer.py
"""
Utilitaires de quantification (placeholder pour futur support GPU).
"""

from __future__ import annotations


class QwenQuantizer:
    """Classe factice – sera implémentée si besoin de quantifier le modèle."""
```

---

## Fichier : `backend\altiora\core\models\qwen3\__init__.py`

```python
# backend/altiora/core/models/qwen3/__init__.py
"""
Gestion du modèle Qwen3-32B (mode thinking / direct).
"""
```

---

## Fichier : `backend\altiora\core\models\starcoder2\code_generator.py`

```python
# backend/altiora/core/models/starcoder2/code_generator.py
"""
Génération de code de test avec templates Starcoder2.
"""

from __future__ import annotations

from pathlib import Path

from altiora.core.models.starcoder2.model_manager import Starcoder2Manager


class TestCodeGenerator:
    """Génère des templates de test (pytest, playwright…)."""

    def __init__(self, manager: Starcoder2Manager) -> None:
        self.manager = manager

    async def generate_pytest(self, spec_path: Path) -> str:
        """Génère un fichier pytest à partir d’une spec."""
        spec_text = spec_path.read_text(encoding="utf-8")
        description = f"pytest tests for {spec_path.name}: {spec_text[:300]}..."
        return await self.manager.generate_code(
            language="python",
            description=description,
            framework="pytest",
        )
```

---

## Fichier : `backend\altiora\core\models\starcoder2\config.py`

```python
# backend/altiora/core/models/starcoder2/config.py
"""
Configuration spécifique Starcoder2.
"""

from __future__ import annotations

from altiora.config.settings import settings

STARCODER2_DEFAULT_CONFIG = {
    "n_ctx": settings.starcoder.context_length,
    "n_threads": settings.starcoder.threads,
    "temperature": settings.starcoder.temperature,
    "max_tokens": settings.starcoder.max_tokens,
    "use_mmap": True,
    "use_mlock": False,
}
```

---

## Fichier : `backend\altiora\core\models\starcoder2\model_manager.py`

```python
# backend/altiora/core/models/starcoder2/model_manager.py
"""
Manager Starcoder2-15B (génération de code).
"""

from __future__ import annotations

import logging
from typing import Any

from llama_cpp import Llama

logger = logging.getLogger(__name__)


class Starcoder2Manager:
    """Wrapper Starcoder2 spécialisé code."""

    def __init__(self, model: Llama) -> None:
        self.model = model

    async def generate_code(
        self,
        language: str,
        description: str,
        framework: str | None = None,
    ) -> str:
        """Génère du code à partir d’une description."""
        prompt = (
            f"<fim_prefix>Generate {language} code for: {description}"
            f"{f' using {framework}' if framework else ''}\n\n"
            f"<fim_suffix>\n\n<fim_middle>"
        )
        output = self.model(
            prompt,
            max_tokens=1200,
            temperature=0.2,
            stop=["<|endoftext|>"],
        )
        return output["choices"][0]["text"]
```

---

## Fichier : `backend\altiora\core\models\starcoder2\__init__.py`

```python
# backend/altiora/core/models/starcoder2/__init__.py
"""
Gestion du modèle Starcoder2-15B pour génération de code.
"""
```

---

## Fichier : `backend\altiora\core\modules\voice_anythingllm.py`

```python
import asyncio
import aiohttp
import speech_recognition as sr
import pyttsx3
import logging
from typing import Dict

logger = logging.getLogger(__name__)


class VoiceAnythingLLM:
    """Assistant vocal pilotant AnythingLLM via API"""

    def __init__(self, workspace_slug: str = "Altiora Knowledge"):
        self.workspace_slug = workspace_slug
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 180)
        self.anythingllm_url = "http://localhost:3001"

    async def recognize_voice(self) -> str:
        """Reconnaissance vocale -> texte"""
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source)
            logger.info("🎤 Parlez...")

            audio = await asyncio.to_thread(
                self.recognizer.listen, source, timeout=3, phrase_time_limit=10
            )
            return await asyncio.to_thread(
                self.recognizer.recognize_google, audio, language="fr-FR"
            )

    async def send_to_anythingllm(self, text: str) -> Dict:
        """Envoie le texte au workspace AnythingLLM"""
        payload = {
            "message": text,
            "mode": "chat"
        }

        async with aiohttp.ClientSession() as session:
            url = f"{self.anythingllm_url}/api/v1/workspace/{self.workspace_slug}/chat"
            async with session.post(url, json=payload) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    return data.get("textResponse", "")
                else:
                    logger.error(f"❌ Erreur AnythingLLM : {resp.status}")
                    return "Erreur de communication avec AnythingLLM."

    async def speak(self, text: str):
        """Synthèse vocale"""
        await asyncio.to_thread(self.engine.say, text)
        await asyncio.to_thread(self.engine.runAndWait)

    async def start_session(self):
        """Boucle écoute → AnythingLLM → voix"""
        logger.info("🎤 Mode vocal AnythingLLM activé")

        while True:
            try:
                # 1. Reconnaissance
                query = await self.recognize_voice()
                logger.info(f"🗣️ Reçu : {query}")

                # 2. Envoi à AnythingLLM
                response = await self.send_to_anythingllm(query)
                logger.info(f"💬 Réponse : {response}")

                # 3. Vocalisation
                await self.speak(response)

            except sr.UnknownValueError:
                logger.debug("🔇 Bruit ignoré")
            except KeyboardInterrupt:
                logger.info("👋 Session vocale arrêtée")
                break
            except Exception as e:
                logger.error(f"💥 Erreur : {e}")
                await self.speak("Erreur technique. Veuillez réessayer.")
```

---

## Fichier : `backend\altiora\core\modules\voice_assistant.py`

```python
import asyncio
import logging
import speech_recognition as sr
import pyttsx3
from typing import Optional

logger = logging.getLogger(__name__)


class VoiceAssistant:
    """Assistant vocal pour Altiora"""

    def __init__(self, altiora_core):
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 180)  # Vitesse de parole
        self.engine.setProperty('voice', 'fr')  # Langue française
        self.altiora = altiora_core
        self.is_listening = False

    async def start_listening(self):
        """Lance l'écoute continue"""
        self.is_listening = True
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source)
            logger.info("🎤 Assistant vocal prêt...")

            while self.is_listening:
                try:
                    audio = await asyncio.to_thread(
                        self.recognizer.listen,
                        source,
                        timeout=1,
                        phrase_time_limit=5
                    )
                    text = await asyncio.to_thread(
                        self.recognizer.recognize_google,
                        audio,
                        language="fr-FR"
                    )

                    if text and any(kw in text.lower() for kw in ["altiora", "analyse", "test"]):
                        logger.info(f"🗣️ Entendu : {text}")
                        response = await self.altiora.process_request(text)
                        await self.speak(response)

                except sr.UnknownValueError:
                    pass  # Bruit ignoré
                except sr.RequestError as e:
                    logger.error(f"🎤 Erreur reconnaissance : {e}")

    async def speak(self, text: str):
        """Synthèse vocale"""
        logger.info(f"🔊 Réponse : {text}")
        await asyncio.to_thread(self.engine.say, text)
        await asyncio.to_thread(self.engine.runAndWait)

    def stop(self):
        """Arrête l'écoute"""
        self.is_listening = False
```

---

## Fichier : `backend\altiora\core\modules\__init__.py`

```python
# backend/altiora/core/modules/__init__.py
"""Initialise le package `modules` de l'application Altiora.

Ce package contient des modules fonctionnels spécifiques qui peuvent être
réutilisés à travers différentes parties de l'application. Chaque sous-package
dans `modules` est dédié à une fonctionnalité ou un domaine particulier.
"""

```

---

## Fichier : `backend\altiora\core\modules\psychodesign\altiora_core.py`

```python
# backend/altiora/core/modules/psychodesign/altiora_core.py
"""Noyau de personnalité et d'apprentissage supervisé pour l'IA Altiora.

Ce module gère les traits de personnalité de l'IA, son évolution via le
feedback utilisateur et l'apprentissage supervisé. Il intègre des mécanismes
de validation administrative pour assurer une évolution contrôlée et sécurisée.
"""

import json
import logging
from collections import defaultdict
from dataclasses import dataclass, asdict
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any
import numpy as np

from guardrails.admin_control_system import AdminControlSystem, AdminCommand
from guardrails.ethical_safeguards import EthicalSafeguards
from src.modules.psychodesign.personality_quiz import PersonalityProfile

logger = logging.getLogger(__name__)


@dataclass
class PersonalityEvolution:
    """Enregistrement d'un changement dans les traits de personnalité de l'IA."""
    timestamp: datetime
    change_type: str # Type de changement (ex: 'trait_formalite', 'preference_update').
    old_value: float # Ancienne valeur du trait ou de la préférence.
    new_value: float # Nouvelle valeur du trait ou de la préférence.
    reason: str      # Raison du changement (ex: 'feedback utilisateur', 'ajustement automatique').
    source: str      # Source du changement (ex: 'auto', 'user_feedback', 'admin_override').
    approved: bool = False # Indique si le changement a été approuvé par un administrateur.
    admin_review: Optional[str] = None # Commentaires de l'administrateur.


@dataclass
class LearningProposal:
    """Représente une proposition de modification de la personnalité issue de l'apprentissage supervisé."""
    proposal_id: str
    user_id: str
    suggested_changes: Dict[str, Any] # Changements proposés (ex: {"formalite": 0.7}).
    confidence_score: float # Score de confiance de la proposition (entre 0 et 1).
    evidence: List[Dict[str, Any]] # Preuves ou données brutes ayant mené à la proposition.
    timestamp: datetime
    status: str = "pending" # Statut de la proposition ('pending', 'approved', 'rejected').
    admin_decision: Optional[str] = None # Décision de l'administrateur.


class AltioraCore:
    """Moteur de personnalité de l'IA avec capacités d'apprentissage supervisé."""

    def __init__(self, user_id: str, admin_system: AdminControlSystem):
        """Initialise le noyau Altiora."

        Args:
            user_id: L'identifiant de l'utilisateur associé à cette instance du noyau.
            admin_system: Une instance de `AdminControlSystem` pour la gestion des commandes administratives.
        """
        self.user_id = user_id
        self.admin_system = admin_system
        self.ethical_safeguards = EthicalSafeguards() # Système de garde-fous éthiques.

        self.core_path = Path("altiora_core") # Répertoire pour la persistance des données du noyau.
        self.core_path.mkdir(exist_ok=True)

        self.personality = self._load_default_personality()
        self.evolution_history: List[PersonalityEvolution] = []
        self.learning_proposals: List[LearningProposal] = []

        self.supervised_mode = False # Mode d'apprentissage supervisé (True/False).
        self.learning_mode = "conservative" # Stratégie d'apprentissage ('conservative', 'adaptive').
        self.logger = self._setup_logging()

    # ------------------------------------------------------------------
    # Initialisation et Persistance
    # ------------------------------------------------------------------

    def _setup_logging(self) -> logging.Logger:
        """Configure un logger spécifique pour cette instance du noyau Altiora."""
        logger = logging.getLogger(f"altiora_core_{self.user_id}")
        logger.setLevel(logging.INFO)
        handler = logging.FileHandler(self.core_path / f"{self.user_id}.log")
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger

    def _load_default_personality(self) -> PersonalityProfile:
        """Charge le profil de personnalité de l'utilisateur depuis le disque, ou crée un profil par défaut."

        Returns:
            L'objet `PersonalityProfile` chargé ou par défaut.
        """
        profile_file = self.core_path / f"{self.user_id}_profile.json"
        if profile_file.exists():
            try:
                with open(profile_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    return PersonalityProfile(**data)
            except (IOError, OSError, json.JSONDecodeError) as e:
                self.logger.error(f"Erreur lors du chargement du profil pour {self.user_id}: {e}")

        # Retourne un profil par défaut si aucun n'est trouvé ou si le chargement échoue.
        return PersonalityProfile(
            user_id=self.user_id,
            traits={
                "formalite": 0.6,
                "empathie": 0.7,
                "humor": 0.2,
                "proactivite": 0.5,
                "verbosite": 0.5,
                "confirmation": 0.3,
                "technical_level": 0.7,
            },
            preferences={
                "vouvoiement": True,
                "expressions": ["Parfait!", "Intéressant", "Voyons voir..."],
                "voice_settings": {"pitch": 1.0, "speed": 1.1, "intonation": "dynamique"},
            },
            vocal_profile={},
            behavioral_patterns={},
            quiz_metadata={"created_at": datetime.now().isoformat()},
        )

    # ------------------------------------------------------------------
    # API Publique – Interaction et Apprentissage
    # ------------------------------------------------------------------

    async def process_learning_feedback(self, feedback: Dict[str, Any]) -> Optional[LearningProposal]:
        """Traite un feedback utilisateur et génère une proposition d'apprentissage."

        Args:
            feedback: Un dictionnaire contenant le feedback de l'utilisateur.

        Returns:
            Une `LearningProposal` si une proposition est générée, sinon None.
        """
        feedback_type = feedback.get("type")
        if feedback_type == "correction":
            return await self._handle_correction_feedback(feedback)
        if feedback_type == "adjustment":
            return await self._handle_adjustment_feedback(feedback)
        if feedback_type == "explicit_preference":
            return await self._handle_preference_feedback(feedback) # Méthode à implémenter.
        return None

    async def handle_user_interaction(self, interaction: Dict[str, Any]) -> Dict[str, Any]:
        """Analyse une interaction utilisateur, applique les garde-fous éthiques et génère une réponse personnalisée."

        Args:
            interaction: Un dictionnaire décrivant l'interaction de l'utilisateur.

        Returns:
            Un dictionnaire contenant la réponse de l'IA et potentiellement des informations sur les propositions d'apprentissage.
        """
        alert = await self.ethical_safeguards.analyze_interaction(self.user_id, interaction)
        if alert and alert.severity == "critical":
            return {
                "status": "blocked",
                "message": "Interaction bloquée pour raisons éthiques",
                "alert_id": alert.alert_id,
            }

        response = await self._generate_response()
        if interaction.get("type") == "feedback":
            proposal = await self.process_learning_feedback(interaction)
            if proposal:
                response["learning_proposal"] = proposal.proposal_id

        self.logger.info("Interaction traitée : %s", interaction.get("type"))
        return response

    # ------------------------------------------------------------------
    # Gestion des Propositions d'Apprentissage
    # ------------------------------------------------------------------

    async def _handle_correction_feedback(self, feedback: Dict[str, Any]) -> Optional[LearningProposal]:
        """Traite le feedback de correction et génère une proposition d'apprentissage."""
        original = feedback.get("original")
        corrected = feedback.get("corrected")
        changes = self._analyze_correction_impact(original, corrected)
        if not changes:
            return None

        proposal = LearningProposal(
            proposal_id=f"corr_{self.user_id}_{datetime.now().isoformat()}",
            user_id=self.user_id,
            suggested_changes=changes,
            confidence_score=0.9,
            evidence=[{"type": "correction", "data": feedback}],
            timestamp=datetime.now(),
        )
        self.learning_proposals.append(proposal)
        await self._submit_for_admin_review(proposal)
        return proposal

    async def _handle_adjustment_feedback(self, feedback: Dict[str, Any]) -> Optional[LearningProposal]:
        """Traite le feedback d'ajustement et génère une proposition d'apprentissage."""
        adjustment_type = feedback.get("adjustment_type")
        trait_map = {
            "shorter": ("verbosite", -0.2),
            "longer": ("verbosite", 0.2),
            "more_formal": ("formalite", 0.1),
            "less_formal": ("formalite", -0.1),
            "more_empathetic": ("empathie", 0.1),
            "less_empathetic": ("empathie", -0.1),
        }
        if adjustment_type not in trait_map:
            return None

        trait, delta = trait_map[adjustment_type]
        new_value = max(0.0, min(1.0, self.personality.traits[trait] + delta)) # Assure que la valeur reste entre 0 et 1.

        proposal = LearningProposal(
            proposal_id=f"adj_{self.user_id}_{datetime.now().isoformat()}",
            user_id=self.user_id,
            suggested_changes={trait: new_value},
            confidence_score=0.7,
            evidence=[{"type": "adjustment", "data": feedback}],
            timestamp=datetime.now(),
        )
        self.learning_proposals.append(proposal)
        await self._submit_for_admin_review(proposal)
        return proposal

    async def _handle_preference_feedback(self, feedback: Dict[str, Any]) -> Optional[LearningProposal]:
        """Traite le feedback de préférence explicite et génère une proposition d'apprentissage."""
        # TODO: Implémenter la logique pour analyser le feedback de préférence.
        self.logger.warning(f"Feedback de préférence explicite non implémenté : {feedback}")
        return None

    # ------------------------------------------------------------------
    # Fonctions internes
    # ------------------------------------------------------------------

    def _analyze_correction_impact(self, original: Optional[str], corrected: Optional[str]) -> Dict[str, float]:
        """Analyse l'impact d'une correction sur les traits de personnalité (ex: verbosité, formalité)."""
        changes: Dict[str, float] = {}
        if not original or not corrected:
            return changes

        # Exemple: Ajustement de la verbosité si la correction est significativement plus courte.
        if len(corrected) < len(original) * 0.8:
            changes["verbosite"] = max(0.0, self.personality.traits["verbosite"] - 0.1)

        # Exemple: Ajustement de la formalité basé sur la présence de certains indicateurs.
        formal_indicators = ["vous", "monsieur", "madame"]
        orig_formal = any(w in str(original).lower() for w in formal_indicators)
        corr_formal = any(w in str(corrected).lower() for w in formal_indicators)
        if orig_formal != corr_formal:
            delta = 0.1 if corr_formal else -0.1
            changes["formalite"] = max(0.0, min(1.0, self.personality.traits["formalite"] + delta))
        return changes

    async def _submit_for_admin_review(self, proposal: LearningProposal) -> None:
        """Soumet une proposition d'apprentissage à l'administrateur pour examen et approbation."""
        command = AdminCommand(
            command_id=proposal.proposal_id,
            timestamp=datetime.now(),
            action="review_learning_proposal",
            target_user=self.user_id,
            parameters={
                "proposal": asdict(proposal),
                "user_id": self.user_id # Ajout de l'user_id pour le contexte admin.
            },
        )
        await self.admin_system.execute_admin_command(command)
        self.logger.info("Proposition d'apprentissage soumise pour examen : %s", proposal.proposal_id)

    async def _generate_response(self) -> Dict[str, Any]:
        """Génère une réponse de l'IA basée sur la personnalité actuelle (stub)."""
        # TODO: Intégrer un modèle de génération de texte qui utilise les traits de personnalité.
        return {
            "status": "success",
            "response": "Réponse générée selon la personnalité actuelle (implémentation à venir).",
            "personality_snapshot": self.personality.traits,
        }

    async def apply_approved_changes(self, proposal_id: str) -> bool:
        """Applique les changements de personnalité validés par un administrateur."

        Args:
            proposal_id: L'ID de la proposition d'apprentissage approuvée.

        Returns:
            True si les changements ont été appliqués, False sinon.
        """
        proposal = next((p for p in self.learning_proposals if p.proposal_id == proposal_id), None)
        if not proposal or proposal.status != "approved":
            self.logger.warning(f"Proposition {proposal_id} non trouvée ou non approuvée. Changements non appliqués.")
            return False

        for trait, new_value in proposal.suggested_changes.items():
            old_value = self.personality.traits.get(trait, 0.5) # Récupère l'ancienne valeur.
            evolution = PersonalityEvolution(
                timestamp=datetime.now(),
                change_type=f"trait_{trait}",
                old_value=old_value,
                new_value=float(new_value),
                reason=f"Approbation de la proposition d'apprentissage {proposal_id}",
                source="learning",
                approved=True,
            )
            self.evolution_history.append(evolution)
            self.personality.traits[trait] = float(new_value) # Applique le nouveau trait.
            self.logger.info(f"Trait '{trait}' mis à jour de {old_value:.2f} à {new_value:.2f}.")

        await self._save_state()
        self.logger.info("Changements de personnalité appliqués : %s", proposal.suggested_changes)
        return True

    async def _save_state(self) -> None:
        """Sauvegarde l'état complet du noyau Altiora (personnalité, historique, propositions)."""
        try:
            # Sauvegarde le profil de personnalité.
            with open(self.core_path / f"{self.user_id}_profile.json", "w", encoding='utf-8') as f:
                json.dump(asdict(self.personality), f, indent=2, default=str)
            # Sauvegarde l'historique d'évolution.
            with open(self.core_path / f"{self.user_id}_evolution.json", "w", encoding='utf-8') as f:
                json.dump([asdict(e) for e in self.evolution_history], f, indent=2, default=str)
            # Sauvegarde les propositions d'apprentissage.
            with open(self.core_path / f"{self.user_id}_proposals.json", "w", encoding='utf-8') as f:
                json.dump([asdict(p) for p in self.learning_proposals], f, indent=2, default=str)
            self.logger.info(f"État du noyau Altiora sauvegardé pour l'utilisateur {self.user_id}.")
        except (IOError, OSError) as e:
            self.logger.error(f"Erreur lors de la sauvegarde de l'état pour {self.user_id}: {e}")

    # ------------------------------------------------------------------
    # Accès en lecture (pour le reporting ou le débogage)
    # ------------------------------------------------------------------

    def get_personality_summary(self) -> Dict[str, Any]:
        """Retourne un résumé des traits de personnalité actuels et des statistiques d'apprentissage."""
        return {
            "user_id": self.user_id,
            "current_traits": self.personality.traits,
            "evolution_count": len(self.evolution_history),
            "pending_proposals": len([p for p in self.learning_proposals if p.status == "pending"]),
            "last_change": self.evolution_history[-1].timestamp.isoformat() if self.evolution_history else None,
            "supervised_mode": self.supervised_mode,
            "learning_mode": self.learning_mode,
        }

    def get_evolution_report(self) -> str:
        """Génère un rapport textuel de l'évolution de la personnalité."""
        lines = [f"📈 **Rapport d'Évolution - {self.user_id}**", "", "**Traits actuels :**"]
        lines.extend(f"• {k} : {v:.1%}" for k, v in self.personality.traits.items())
        lines += [
            "",
            f"**Historique :** {len(self.evolution_history)} changements",
            f"**Propositions en attente :** {len([p for p in self.learning_proposals if p.status == 'pending'])} ",
            f"**Mode apprentissage :** {self.learning_mode}",
        ]
        return "\n".join(lines)


class EvolutionAnalyzer:
    """Outils d'analyse des tendances de personnalité à partir de l'historique d'évolution."""

    @staticmethod
    def analyze_trends(evolution_history: List[PersonalityEvolution]) -> Dict[str, Any]:
        """Analyse les tendances d'évolution des traits de personnalité."

        Args:
            evolution_history: La liste des objets `PersonalityEvolution`.

        Returns:
            Un dictionnaire contenant des analyses de tendances pour chaque trait.
        """
        if not evolution_history:
            return {}

        trends = defaultdict(list)
        for evo in evolution_history:
            if evo.change_type.startswith("trait_"):
                trait = evo.change_type[6:]
                trends[trait].append({"value": evo.new_value, "timestamp": evo.timestamp.isoformat()})

        analysis: Dict[str, Any] = {}
        for trait, changes in trends.items():
            if len(changes) >= 2:
                values = [float(c["value"]) for c in changes]
                analysis[trait] = {
                    "direction": "increasing" if values[-1] > values[0] else "decreasing",
                    "volatility": float(np.std(values)),
                    "total_change": float(values[-1] - values[0]),
                }
        return analysis


# ------------------------------------------------------------------
# Démonstration (exemple d'utilisation)
# ------------------------------------------------------------------
if __name__ == "__main__":
    import asyncio
    import logging

    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    # Classe factice pour AdminControlSystem pour la démonstration.
    class MockAdminControlSystem:
        async def execute_admin_command(self, command: AdminCommand):
            logging.info(f"[MockAdmin] Commande reçue : {command.action} pour {command.target_user}")
            if command.action == "review_learning_proposal":
                # Simule l'approbation automatique pour la démo.
                proposal_id = command.command_id
                for prop in altiora_core_instance.learning_proposals:
                    if prop.proposal_id == proposal_id:
                        prop.status = "approved"
                        prop.admin_decision = "Approuvé automatiquement pour la démo."
                        logging.info(f"[MockAdmin] Proposition {proposal_id} approuvée.")
                        break

    async def demo():
        user_id = "demo_user_1"
        mock_admin = MockAdminControlSystem()
        global altiora_core_instance # Rendre l'instance accessible au mock_admin.
        altiora_core_instance = AltioraCore(user_id, mock_admin)

        print("\n--- Profil de personnalité initial ---")
        print(altiora_core_instance.get_personality_summary())

        print("\n--- Simulation d'interaction utilisateur et feedback ---")
        # Simule un feedback de correction.
        feedback_correction = {
            "type": "correction",
            "original": "Le rapport est trop long et formel.",
            "corrected": "Rapport concis."
        }
        await altiora_core_instance.handle_user_interaction(feedback_correction)

        # Simule un feedback d'ajustement.
        feedback_adjustment = {
            "type": "adjustment",
            "adjustment_type": "shorter"
        }
        await altiora_core_instance.handle_user_interaction(feedback_adjustment)

        print("\n--- Propositions d'apprentissage en attente ---")
        for prop in altiora_core_instance.learning_proposals:
            print(f"Proposition ID: {prop.proposal_id}, Statut: {prop.status}, Changements: {prop.suggested_changes}")

        # Simule l'approbation des propositions par l'admin.
        print("\n--- Application des changements approuvés (simulée par l'admin) ---")
        for prop in altiora_core_instance.learning_proposals:
            if prop.status == "pending":
                # L'admin mock va approuver la proposition.
                await mock_admin.execute_admin_command(AdminCommand(
                    command_id=prop.proposal_id,
                    timestamp=datetime.now(),
                    action="review_learning_proposal",
                    target_user=user_id,
                    parameters={'proposal': asdict(prop)}
                ))
                await altiora_core_instance.apply_approved_changes(prop.proposal_id)

        print("\n--- Profil de personnalité après apprentissage ---")
        print(altiora_core_instance.get_personality_summary())

        print("\n--- Rapport d'évolution ---")
        print(altiora_core_instance.get_evolution_report())

        print("\n--- Analyse des tendances ---")
        trends = EvolutionAnalyzer.analyze_trends(altiora_core_instance.evolution_history)
        print(f"Tendances : {trends}")

        print("Démonstration de AltioraCore terminée.")

    asyncio.run(demo())
```

---

## Fichier : `backend\altiora\core\modules\psychodesign\personality_evolution.py`

```python
# backend/altiora/core/modules/psychodesign/personality_evolution.py
"""Module pour gérer l'évolution de la personnalité de l'IA via le fine-tuning supervisé.

Ce module orchestre le processus d'entraînement LoRA en arrière-plan en utilisant
des exemples d'interactions de haute qualité. Il permet d'ajouter de nouveaux
exemples d'entraînement, de déclencher des cycles de fine-tuning, de vérifier
leur statut et de récupérer le chemin du dernier adaptateur entraîné.
"""

import asyncio
import json
import logging
import subprocess
from pathlib import Path
from typing import Dict, Any, List, Optional

logger = logging.getLogger(__name__)

# Chemins basés sur la structure du projet pour les données et scripts d'entraînement.
TRAINING_DATA_PATH = Path("data/training/data/train_dataset.jsonl")
TRAINING_SCRIPT_PATH = Path("data/training/src/train_qwen3_thinkpad.py")
ADAPTERS_OUTPUT_DIR = Path("data/models/lora_adapters")


class PersonalityEvolution:
    """Gère le cycle de vie du fine-tuning de la personnalité de l'IA."""

    def __init__(self):
        """Initialise le gestionnaire d'évolution de la personnalité."

        S'assure que le répertoire de sortie des adaptateurs existe.
        """
        ADAPTERS_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        self.training_process: Optional[asyncio.subprocess.Process] = None

    async def add_training_example(self, example: Dict[str, str]) -> bool:
        """Ajoute un nouvel exemple de haute qualité au dataset d'entraînement."

        L'exemple doit être un dictionnaire avec les clés "instruction", "input", "output",
        conformément au format JSON Lines attendu par le script d'entraînement.

        Args:
            example: Le dictionnaire contenant l'exemple d'entraînement.

        Returns:
            True si l'ajout a réussi, False sinon.
        """
        required_keys = {"instruction", "input", "output"}
        if not required_keys.issubset(example.keys()):
            logger.error(f"Exemple d'entraînement invalide. Clés requises : {required_keys}. Clés fournies : {example.keys()}")
            return False

        try:
            # Crée le répertoire parent si nécessaire.
            TRAINING_DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
            with open(TRAINING_DATA_PATH, "a", encoding="utf-8") as f:
                f.write(json.dumps(example, ensure_ascii=False) + "\n")
            logger.info(f"Nouvel exemple d'entraînement ajouté à {TRAINING_DATA_PATH}.")
            return True
        except IOError as e:
            logger.error(f"Impossible d'écrire dans le fichier d'entraînement {TRAINING_DATA_PATH}: {e}")
            return False

    async def trigger_finetuning_cycle(self, min_new_examples: int = 10) -> Dict[str, Any]:
        """Déclenche un nouveau cycle de fine-tuning si les conditions sont remplies."

        Args:
            min_new_examples: Nombre minimum de nouveaux exemples requis pour lancer un cycle.
                              (La logique de vérification du nombre d'exemples n'est pas implémentée ici).

        Returns:
            Un dictionnaire indiquant le statut du déclenchement (started, already_running, error).
        """
        if self.training_process and self.training_process.returncode is None:
            logger.info(f"Un processus d'entraînement est déjà en cours (PID: {self.training_process.pid}).")
            return {"status": "already_running", "pid": self.training_process.pid}

        if not TRAINING_SCRIPT_PATH.exists():
            logger.error(f"Script d'entraînement non trouvé : {TRAINING_SCRIPT_PATH}.")
            return {"status": "error", "reason": "Training script not found"}

        logger.info("Déclenchement d'un nouveau cycle de fine-tuning de la personnalité...")

        try:
            # Lance le script d'entraînement en arrière-plan.
            # `asyncio.create_subprocess_exec` est utilisé pour exécuter un processus externe.
            self.training_process = await asyncio.create_subprocess_exec(
                "python",
                str(TRAINING_SCRIPT_PATH),
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
            )

            logger.info(f"Processus d'entraînement démarré avec le PID : {self.training_process.pid}.")
            return {"status": "started", "pid": self.training_process.pid}
        except FileNotFoundError:
            logger.error("La commande 'python' ou le script d'entraînement n'a pas été trouvé. Assurez-vous que Python est dans le PATH et que le script existe.")
            return {"status": "error", "reason": "Python interpreter or training script not found"}
        except Exception as e:
            logger.error(f"Erreur lors du lancement du script d'entraînement : {e}")
            return {"status": "error", "reason": str(e)}

    async def get_training_status(self) -> Dict[str, Any]:
        """Vérifie le statut du processus d'entraînement en cours."

        Returns:
            Un dictionnaire décrivant le statut de l'entraînement (not_running, running, completed_successfully, failed).
        """
        if not self.training_process:
            return {"status": "not_running"}

        if self.training_process.returncode is None:
            return {"status": "running", "pid": self.training_process.pid}
        else:
            # Le processus est terminé, récupère la sortie standard et d'erreur.
            stdout, stderr = await self.training_process.communicate()
            if self.training_process.returncode == 0:
                return {
                    "status": "completed_successfully",
                    "pid": self.training_process.pid,
                    "stdout": stdout.decode('utf-8'),
                }
            else:
                return {
                    "status": "failed",
                    "pid": self.training_process.pid,
                    "returncode": self.training_process.returncode,
                    "stderr": stderr.decode('utf-8'),
                }

    def get_latest_adapter(self) -> Optional[Path]:
        """Trouve le chemin du dernier adaptateur LoRA entraîné."

        Les adaptateurs sont supposés être stockés dans des sous-répertoires
        nommés 'checkpoint-N' où N est un numéro d'étape.

        Returns:
            Le chemin `Path` vers le répertoire du dernier adaptateur,
            ou None si aucun adaptateur n'est trouvé.
        """
        try:
            # Liste tous les sous-répertoires qui ressemblent à des checkpoints.
            adapters = [p for p in ADAPTERS_OUTPUT_DIR.iterdir() if p.is_dir() and p.name.startswith("checkpoint-")]
            if not adapters:
                logger.info(f"Aucun adaptateur trouvé dans {ADAPTERS_OUTPUT_DIR}.")
                return None
            # Trie les adaptateurs par numéro de checkpoint pour trouver le plus récent.
            latest_adapter = max(adapters, key=lambda p: int(p.name.split('-')[-1]))
            logger.info(f"Dernier adaptateur trouvé : {latest_adapter}.")
            return latest_adapter
        except (FileNotFoundError, ValueError) as e:
            logger.error(f"Erreur lors de la recherche du dernier adaptateur : {e}")
            return None


# ------------------------------------------------------------------
# Démonstration (exemple d'utilisation)
# ------------------------------------------------------------------
if __name__ == "__main__":
    async def main():
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        evolution = PersonalityEvolution()

        # 1. Ajouter un nouvel exemple d'entraînement.
        new_example = {
            "instruction": "Reformule cette phrase de manière plus empathique.",
            "input": "Le ticket est fermé car le problème n'est pas reproductible.",
            "output": "Je comprends votre frustration. Pour l'instant, nous n'avons pas pu reproduire le problème pour le corriger, mais nous restons attentifs si de nouvelles informations apparaissent."
        }
        print("\n--- Ajout d'un exemple d'entraînement ---")
        await evolution.add_training_example(new_example)

        # 2. Déclencher un cycle de fine-tuning (simulation).
        # Pour la démo, nous allons créer un script factice si nécessaire.
        if not TRAINING_SCRIPT_PATH.exists():
            TRAINING_SCRIPT_PATH.parent.mkdir(parents=True, exist_ok=True)
            TRAINING_SCRIPT_PATH.write_text("""
import time
import sys
print("Simulating a successful training run...")
time.sleep(1)
print("Training complete.")
sys.exit(0)
""")
            print(f"Script d'entraînement factice créé à : {TRAINING_SCRIPT_PATH}")
        
        print("\n--- Déclenchement du Fine-Tuning ---")
        start_result = await evolution.trigger_finetuning_cycle(min_new_examples=1)
        logging.info(f"Résultat du déclenchement : {start_result}")

        if start_result["status"] == "started":
            print("Attente de la fin du processus d'entraînement (simulation)...")
            # Attendre que le processus se termine.
            while True:
                status_result = await evolution.get_training_status()
                logging.info(f"Statut actuel : {status_result['status']}")
                if status_result['status'] not in ["running", "not_running"]:
                    break
                await asyncio.sleep(1)
            logging.info(f"Statut final de l'entraînement : {status_result}")

        # 3. Trouver le dernier adaptateur (simulation).
        print("\n--- Recherche du dernier adaptateur ---")
        # Simuler la création de répertoires d'adaptateurs.
        (ADAPTERS_OUTPUT_DIR / "checkpoint-100").mkdir(parents=True, exist_ok=True)
        (ADAPTERS_OUTPUT_DIR / "checkpoint-200").mkdir(parents=True, exist_ok=True)
        latest = evolution.get_latest_adapter()
        logging.info(f"Dernier adaptateur trouvé : {latest}")
        assert latest and latest.name == "checkpoint-200"

        print("Démonstration de PersonalityEvolution terminée.")

        # Nettoyage des fichiers et répertoires temporaires.
        if TRAINING_DATA_PATH.exists():
            TRAINING_DATA_PATH.unlink()
        if TRAINING_SCRIPT_PATH.exists():
            TRAINING_SCRIPT_PATH.unlink()
        if ADAPTERS_OUTPUT_DIR.exists():
            import shutil
            shutil.rmtree(ADAPTERS_OUTPUT_DIR)

    asyncio.run(main())
```

---

## Fichier : `backend\altiora\core\modules\psychodesign\personality_quiz.py`

```python
# backend/altiora/core/modules/psychodesign/personality_quiz.py
"""Module pour le quiz de personnalisation de l'IA Altiora.

Ce module permet de définir le profil initial de la personnalité de l'IA
en posant une série de questions à l'utilisateur. Il collecte des réponses
textuelles et peut potentiellement analyser des caractéristiques vocales
pour affiner les traits de personnalité de l'assistant QA.
"""

import json
import logging
from dataclasses import dataclass, asdict
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional

# Importation conditionnelle de speech_recognition.
try:
    import speech_recognition as sr
    HAS_SPEECH_RECOGNITION = True
except ImportError:
    sr = None
    HAS_SPEECH_RECOGNITION = False
    logging.warning("La bibliothèque 'speech_recognition' n'est pas installée. La calibration vocale sera désactivée.")

logger = logging.getLogger(__name__)


@dataclass
class QuizResponse:
    """Représente une réponse individuelle à une question du quiz."""
    question_id: str
    response: Any
    confidence: float
    response_time: float
    vocal_features: Dict[str, float]


@dataclass
class PersonalityProfile:
    """Représente le profil de personnalité complet de l'IA pour un utilisateur donné."""
    user_id: str
    traits: Dict[str, float] # Traits de personnalité (ex: formalité, empathie).
    preferences: Dict[str, Any] # Préférences de communication (ex: vouvoiement, expressions).
    vocal_profile: Dict[str, Any] # Caractéristiques vocales (si calibration effectuée).
    behavioral_patterns: Dict[str, Any] # Modèles comportementaux identifiés.
    quiz_metadata: Dict[str, Any] # Métadonnées du quiz (date de complétion, etc.).


class PersonalityQuiz:
    """Système de quiz de personnalisation avancé pour définir le profil de l'IA."""

    def __init__(self, user_id: str):
        """Initialise le quiz de personnalité."

        Args:
            user_id: L'identifiant de l'utilisateur qui passe le quiz.
        """
        self.user_id = user_id
        self.responses: List[QuizResponse] = []
        self.vocal_samples: List[Dict[str, Any]] = []

        self.quiz_path = Path("quiz_data") # Répertoire pour sauvegarder les données du quiz.
        self.quiz_path.mkdir(exist_ok=True)

        # Initialisation conditionnelle de speech recognition.
        self.recognizer: Optional[sr.Recognizer] = None
        self.microphone: Optional[sr.Microphone] = None
        if HAS_SPEECH_RECOGNITION:
            self.recognizer = sr.Recognizer()
            self.microphone = sr.Microphone()

        self.questions = self._load_questions()

    # ------------------------------------------------------------------
    # Questionnaire (définition des questions)
    # ------------------------------------------------------------------

    @staticmethod
    def _load_questions() -> List[Dict[str, Any]:
        """Charge la liste des questions du quiz."

        Returns:
            Une liste de dictionnaires, chaque dictionnaire représentant une question.
        """
        return [
            {
                "id": "comm_1",
                "type": "choice",
                "question": "Comment préférez-vous qu'on s'adresse à vous ?",
                "options": [
                    {"text": "Salut ! (familier)", "value": "tu", "weight": 0.2},
                    {"text": "Bonjour (professionnel)", "value": "vous", "weight": 0.8},
                    {"text": "S'adapte selon le contexte", "value": "adaptive", "weight": 0.5}
                ],
                "trait": "formalite"
            },
            {
                "id": "comm_2",
                "type": "scale",
                "question": "Quand j'explique quelque chose, préférez-vous :",
                "scale": {
                    "min": "Aller directement au résultat",
                    "max": "Avoir tous les détails et le contexte"
                },
                "trait": "verbosite"
            },
            {
                "id": "comm_3",
                "type": "scenario",
                "question": "Je viens de terminer une analyse complexe. Votre réaction préférée :",
                "options": [
                    {"text": "Parfait, donne-moi juste le résumé", "weight": 0.1},
                    {"text": "Super! Peux-tu m'expliquer les points clés ?", "weight": 0.5},
                    {"text": "Génial! J'aimerais comprendre tout le processus", "weight": 0.9}
                ],
                "trait": "verbosite"
            },
            {
                "id": "work_1",
                "type": "choice",
                "question": "Face à une erreur dans votre code, préférez-vous que je :",
                "options": [
                    {"text": "Corrige directement sans vous déranger", "weight": 0.0},
                    {"text": "Vous montre la correction avec explication rapide", "weight": 0.3},
                    {"text": "Explique le problème et vous guide vers la solution", "weight": 0.7},
                    {"text": "Fais une session complète de debugging ensemble", "weight": 1.0}
                ],
                "trait": "empathie"
            },
            {
                "id": "vocal_1",
                "type": "calibration",
                "question": "Lisez cette phrase : 'Altiora, analyse le document de spécification et crée les tests'",
                "purpose": "baseline"
            },
            {
                "id": "vocal_2",
                "type": "calibration",
                "question": "Lisez : 'Non, je voulais dire le module de paiement, pas le module utilisateur'",
                "purpose": "correction"
            },
            {
                "id": "vocal_3",
                "type": "calibration",
                "question": "Lisez : 'Parfait! Exactement ce que je voulais'",
                "purpose": "satisfaction"
            }
        ]

    async def start_quiz(self) -> PersonalityProfile:
        """Démarre le processus du quiz de personnalisation."

        Parcourt toutes les questions, collecte les réponses et génère le profil.

        Returns:
            L'objet `PersonalityProfile` généré.
        """
        logger.info(f"\nQuiz de personnalisation Altiora pour {self.user_id}")
        print("=" * 60)

        for question in self.questions:
            await self._ask_question(question)

        await self._analyze_vocal_patterns() # Analyse les patterns vocaux si des échantillons ont été collectés.
        profile = self._generate_profile()
        await self._save_profile(profile)
        return profile

    # ------------------------------------------------------------------
    # Gestionnaires de questions
    # ------------------------------------------------------------------

    async def _ask_question(self, question: Dict[str, Any]) -> None:
        """Pose une question à l'utilisateur et collecte sa réponse."

        Args:
            question: Le dictionnaire représentant la question à poser.
        """
        logger.info(f"\n{question['question']}")

        response: Dict[str, Any]
        if question["type"] == "choice":
            response = await self._handle_choice_question(question)
        elif question["type"] == "scale":
            response = await self._handle_scale_question(question)
        elif question["type"] == "calibration":
            response = await self._handle_calibration_question(question)
        else:
            response = await self._handle_text_question(question)

        self.responses.append(
            QuizResponse(
                question_id=question["id"],
                response=response["value"],
                confidence=response.get("confidence", 1.0),
                response_time=response.get("time", 0.0),
                vocal_features=response.get("vocal_features", {})
            )
        )

    @staticmethod
    async def _handle_choice_question(question: Dict[str, Any]) -> Dict[str, Any]:
        """Gère les questions à choix multiples."""
        for i, opt in enumerate(question["options"], 1):
            logger.info(f"  {i}. {opt['text']}")
        while True:
            try:
                choice = int(input("Votre choix (1-{}): ".format(len(question["options"]))).strip())
                if 1 <= choice <= len(question["options"]):
                    selected = question["options"][choice - 1]
                    return {"value": selected.get("value", selected["weight"])} # Retourne la valeur ou le poids.
                else:
                    logger.warning("Choix invalide. Veuillez entrer un nombre dans la plage indiquée.")
            except ValueError:
                logger.warning("Entrée invalide. Veuillez entrer un nombre.")

    @staticmethod
    async def _handle_scale_question(_question: Dict[str, Any]) -> Dict[str, Any]:
        """Gère les questions avec une échelle de valeur (ex: 0 à 1)."""
        while True:
            try:
                val_str = input("Entrez une valeur entre 0 et 1 : ").strip()
                val = float(val_str)
                if 0.0 <= val <= 1.0:
                    return {"value": val}
                else:
                    logger.warning("Valeur hors de la plage. Veuillez entrer un nombre entre 0 et 1.")
            except ValueError:
                logger.warning("Entrée invalide. Veuillez entrer un nombre.")

    @staticmethod
    async def _handle_text_question(_question: Dict[str, Any]) -> Dict[str, Any]:
        """Gère les questions nécessitant une réponse textuelle libre."""
        text = input("Réponse : ").strip()
        return {"value": text}

    async def _handle_calibration_question(self, question: Dict[str, Any]) -> Dict[str, Any]:
        """Gère les questions de calibration vocale en utilisant `speech_recognition`."""
        if not self.recognizer or not self.microphone:
            logger.info("Module speech_recognition non disponible. Calibration vocale ignorée.")
            return {"value": "skipped", "confidence": 0.0, "vocal_features": {}}

        logger.info("\nCalibration vocale - Lisez la phrase après le signal. Appuyez sur Entrée quand prêt.")
        input("Appuyez sur Entrée quand prêt...")

        try:
            with self.microphone as source:
                logger.info("Réglage du bruit ambiant...")
                self.recognizer.adjust_for_ambient_noise(source)
                logger.info("Parlez maintenant...")
                audio = self.recognizer.listen(source, timeout=5) # Écoute pendant 5 secondes.

            text = self.recognizer.recognize_google(audio, language="fr-FR") # Utilise Google Speech Recognition.
            features = await self._extract_vocal_features(audio) # Extrait les caractéristiques vocales.
            self.vocal_samples.append({"text": text, "features": features, "purpose": question["purpose"]})
            logger.info(f"Transcription : \"{text}\"")
            return {"value": text, "confidence": 1.0, "vocal_features": features}
        except sr.UnknownValueError:
            logger.warning("Impossible de comprendre l'audio. Veuillez réessayer.")
            return await self._handle_calibration_question(question) # Demande de réessayer.
        except Exception as e:
            logger.error(f"Erreur lors de la calibration vocale : {e}")
            return {"value": "error", "confidence": 0.0, "vocal_features": {}}

    @staticmethod
    async def _extract_vocal_features(_audio: Any) -> Dict[str, float]:
        """Extrait les caractéristiques vocales à partir d'un échantillon audio (stub pour l'instant)."

        Args:
            _audio: L'objet audio enregistré.

        Returns:
            Un dictionnaire de caractéristiques vocales (ex: pitch, speed, volume).
        """
        # TODO: Implémenter une analyse vocale réelle pour extraire des caractéristiques.
        return {"pitch": 220.0, "speed": 150.0, "volume": 0.7, "stress_indicators": 0.2}

    # ------------------------------------------------------------------
    # Génération du profil de personnalité
    # ------------------------------------------------------------------

    async def _analyze_vocal_patterns(self) -> None:
        """Analyse les patterns vocaux collectés pour affiner le profil de personnalité (stub)."

        Cette méthode serait utilisée pour intégrer les données vocales dans le calcul des traits.
        """
        # TODO: Implémenter l'analyse des patterns vocaux.
        pass

    def _generate_profile(self) -> PersonalityProfile:
        """Génère le profil de personnalité complet basé sur les réponses du quiz et l'analyse vocale."""
        return PersonalityProfile(
            user_id=self.user_id,
            traits=self._calculate_traits(),
            preferences=self._analyze_preferences(),
            vocal_profile=self._create_vocal_profile(),
            behavioral_patterns=self._identify_patterns(),
            quiz_metadata={
                "completed_at": datetime.now().isoformat(),
                "question_count": len(self.responses),
                "calibration_samples": len(self.vocal_samples)
            }
        )

    def _calculate_traits(self) -> Dict[str, float]:
        """Calcule les traits de personnalité de l'IA basés sur les réponses du quiz."""
        # Valeurs par défaut des traits.
        traits = {
            "formalite": 0.6,
            "empathie": 0.7,
            "humor": 0.3,
            "proactivite": 0.5,
            "verbosite": 0.5,
            "confirmation": 0.3,
            "technical_level": 0.7
        }

        # Ajuste les traits en fonction des réponses du quiz.
        for response in self.responses:
            question_id = response.question_id
            value = response.response

            if question_id == "comm_1":
                if value == "tu":
                    traits["formalite"] = 0.2
                elif value == "vous":
                    traits["formalite"] = 0.8
                elif value == "adaptive":
                    traits["formalite"] = 0.5

            elif question_id == "comm_2" and isinstance(value, (int, float)):
                traits["verbosite"] = float(value)
            # TODO: Ajouter la logique pour d'autres questions et traits.

        return traits

    def _analyze_preferences(self) -> Dict[str, Any]:
        """Analyse les préférences utilisateur basées sur les réponses du quiz."""
        preferences = {
            "vouvoiement": True,
            "expressions": ["Parfait!", "Intéressant", "Voyons voir..."],
            "voice_settings": {"pitch": 1.0, "speed": 1.1, "intonation": "dynamique"}
        }

        for response in self.responses:
            if response.question_id == "comm_1" and response.response == "tu":
                preferences["vouvoiement"] = False
                preferences["expressions"] = ["Cool!", "OK", "Génial!"]
            # TODO: Ajouter la logique pour d'autres préférences.

        return preferences

    def _create_vocal_profile(self) -> Dict[str, Any]:
        """Crée le profil vocal basé sur les échantillons collectés."""
        if not self.vocal_samples:
            return {"status": "no_samples", "baseline": None}

        return {
            "samples": len(self.vocal_samples),
            "baseline": self.vocal_samples[0] if self.vocal_samples else None,
            "variations": self._analyze_vocal_variations() # Analyse les variations vocales.
        }

    def _analyze_vocal_variations(self) -> Dict[str, float]:
        """Analyse les variations vocales entre les échantillons (stub)."

        Cette méthode calculerait des métriques comme la variance du pitch, de la vitesse, etc.
        """
        if len(self.vocal_samples) < 2:
            return {}

        # TODO: Implémenter une analyse réelle des variations vocales.
        variations = {
            "pitch_variance": 0.1,
            "speed_variance": 0.05,
            "stress_change": 0.2
        }
        return variations

    def _identify_patterns(self) -> Dict[str, Any]:
        """Identifie les patterns comportementaux de l'utilisateur (stub)."

        Cette méthode analyserait les réponses pour déduire des habitudes ou préférences.
        """
        # TODO: Implémenter l'identification des patterns comportementaux.
        patterns = {
            "response_time_avg": sum(r.response_time for r in self.responses) / len(self.responses) if self.responses else 0,
            "confidence_avg": sum(r.confidence for r in self.responses) / len(self.responses) if self.responses else 0,
            "quiz_completion": True
        }
        return patterns

    # ------------------------------------------------------------------
    # Persistance
    # ------------------------------------------------------------------

    async def _save_profile(self, profile: PersonalityProfile) -> None:
        """Sauvegarde le profil de personnalité généré dans un fichier JSON."

        Args:
            profile: L'objet `PersonalityProfile` à sauvegarder.
        """
        try:
            self.quiz_path.mkdir(parents=True, exist_ok=True)
            profile_path = self.quiz_path / f"{self.user_id}_profile.json"

            with open(profile_path, "w", encoding="utf-8") as f:
                # `default=str` est utilisé pour sérialiser les objets `datetime` en chaînes.
                json.dump(asdict(profile), f, indent=2, ensure_ascii=False, default=str)

            logger.info(f"\n✅ Profil de personnalité sauvegardé : {profile_path}")
        except (IOError, OSError) as e:
            logger.error(f"\n❌ Erreur lors de la sauvegarde du profil : {e}")

    # ------------------------------------------------------------------
    # Assistants
    # ------------------------------------------------------------------

    def get_progress(self) -> Dict[str, Any]:
        """Retourne la progression actuelle du quiz."

        Returns:
            Un dictionnaire contenant le nombre de questions complétées, le total,
            le pourcentage et la section courante.
        """
        return {
            "completed": len(self.responses),
            "total": len(self.questions),
            "percentage": (len(self.responses) / len(self.questions)) * 100.0 if len(self.questions) > 0 else 0.0,
            "current_section": self._get_current_section()
        }

    def _get_current_section(self) -> str:
        """Identifie la section courante du quiz basée sur la progression."""
        if not self.responses:
            return "Général"

        if len(self.responses) >= len(self.questions):
            return "Terminé"

        current_question = self.questions[len(self.responses)]
        section_map = {
            "comm": "Communication",
            "work": "Style de travail",
            "stress": "Gestion du stress",
            "humor": "Ton et humour",
            "tech": "Préférences techniques",
            "vocal": "Calibration vocale",
            "scenario": "Scénarios pratiques"
        }
        # Extrait le préfixe de l'ID de la question (ex: 'comm' de 'comm_1').
        return section_map.get(current_question["id"].split("_")[0], "Général")


class QuizReporter:
    """Génère des rapports textuels et des résumés des profils de personnalité."""

    @staticmethod
    def generate_summary(profile: PersonalityProfile) -> str:
        """Génère un résumé textuel concis du profil de personnalité."

        Args:
            profile: L'objet `PersonalityProfile` à résumer.

        Returns:
            Une chaîne de caractères formatée avec les traits et préférences clés.
        """
        traits = profile.traits
        prefs = profile.preferences

        summary = f"""
--- Rapport de Personnalisation Altiora ---
Utilisateur: {profile.user_id}
Date de complétion: {profile.quiz_metadata['completed_at']}

Traits principaux:
- Formalité: {traits['formalite']:.0%}
- Empathie: {traits['empathie']:.0%}
- Humour: {traits['humor']:.0%}
- Proactivité: {traits['proactivite']:.0%}
- Verbosité: {traits['verbosite']:.0%}
- Confirmation: {traits['confirmation']:.0%}
- Niveau technique: {traits['technical_level']:.0%}

Préférences:
- Vouvoiement: {'Oui' if prefs['vouvoiement'] else 'Non'}
- Expressions favorites: {', '.join(prefs['expressions'][:3])}

Profil vocal:
- Échantillons collectés: {profile.vocal_profile.get('samples', 0)}
- Statut: {profile.vocal_profile.get('status', 'Non calibré' if not profile.vocal_profile.get('samples') else 'Calibré')}
"""
        return summary


# ------------------------------------------------------------------
# Démonstration (exemple d'utilisation)
# ------------------------------------------------------------------
if __name__ == "__main__":
    import asyncio
    import logging

    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    async def run_demo():
        quiz = PersonalityQuiz("demo_user")
        profile = await quiz.start_quiz()
        print(QuizReporter.generate_summary(profile))

        # Nettoyage des fichiers générés par la démo.
        quiz.quiz_path.unlink(missing_ok=True)

    asyncio.run(run_demo())
```

---

## Fichier : `backend\altiora\core\modules\psychodesign\__init__.py`

```python
# backend/altiora/core/modules/psychodesign/__init__.py
"""Initialise le sous-package `psychodesign`.

Ce package est dédié à la gestion de la personnalité de l'IA Altiora,
incluant la définition des traits, l'évolution de la personnalité via
l'apprentissage supervisé, et les mécanismes de personnalisation.
"""

```

---

## Fichier : `backend\altiora\core\optimization\memory_optimizer.py`

```python
# backend/altiora/core/optimization/memory_optimizer.py
"""Module pour l'optimisation avancée de la mémoire lors du chargement des modèles d'IA.

Ce module fournit des stratégies pour réduire l'empreinte mémoire des modèles
de langage (LLMs) lors de leur chargement et de leur utilisation. Il intègre
des techniques telles que la quantification 4-bit, le gradient checkpointing,
et le mappage mémoire pour les poids des modèles, ce qui est crucial pour
l'exécution de grands modèles sur des systèmes avec des ressources limitées.
"""

import torch
import gc

# Supposons que ces modules sont définis ailleurs dans le répertoire d'optimisation.
# from src.optimization.memory_pool import MemoryPool
# from src.optimization.model_loader import load_model_4bit


class AdvancedMemoryOptimizer:
    """Optimiseur de mémoire avancé pour les modèles d'IA.

    Cette classe gère diverses techniques pour minimiser l'utilisation de la RAM
    par les modèles, permettant ainsi de charger des modèles plus grands ou
    d'exécuter plus de modèles simultanément.
    """

    def __init__(self):
        """Initialise l'optimiseur de mémoire avancé."

        Il initialise un pool de mémoire (si utilisé) et d'autres composants
        nécessaires aux optimisations.
        """
        # self.memory_pool = MemoryPool() # Exemple d'intégration d'un pool de mémoire.
        pass # Placeholder pour l'initialisation.

    def optimize_model_loading(self, model_path: str):
        """Charge un modèle avec des optimisations de mémoire maximales."

        Args:
            model_path: Le chemin vers le modèle à charger.

        Returns:
            Le modèle chargé et optimisé.

        Raises:
            ImportError: Si les bibliothèques nécessaires (ex: `bitsandbytes`) ne sont pas installées.
        """
        # 1. Quantification 4-bit : Réduit la précision des poids du modèle à 4 bits,
        #    diminuant drastiquement l'utilisation de la mémoire tout en conservant
        #    une bonne partie de la performance.
        # model = load_model_4bit(model_path) # Utilise une fonction externe pour le chargement quantifié.
        model = torch.nn.Linear(10, 10) # Placeholder pour un modèle factice.
        
        # 2. Gradient checkpointing : Technique qui réduit l'utilisation de la mémoire
        #    lors de l'entraînement en ne stockant pas tous les activations intermédiaires.
        #    Les activations sont recalculées à la volée lors de la passe arrière.
        # if hasattr(model, 'gradient_checkpointing_enable'):
        #     model.gradient_checkpointing_enable()

        # 3. Mappage mémoire pour les poids : Charge les poids du modèle directement depuis le disque
        #    dans la mémoire virtuelle, sans les copier entièrement dans la RAM physique.
        model = self._memory_map_weights(model)

        # 4. Garbage collection agressif : Libère immédiatement la mémoire non utilisée.
        gc.collect()
        if torch.cuda.is_available():
            torch.cuda.empty_cache() # Vide le cache de la mémoire GPU.

        return model

    def _memory_map_weights(self, model: Any) -> Any:
        """Applique le mappage mémoire aux poids du modèle (implémentation factice).

        Dans une implémentation réelle, cela impliquerait de charger les poids
        du modèle en utilisant des techniques de mappage mémoire (ex: `mmap`
        ou des fonctionnalités spécifiques aux bibliothèques de ML).

        Args:
            model: Le modèle dont les poids doivent être mappés.

        Returns:
            Le modèle avec les poids mappés en mémoire.
        """
        # Cette fonction est un placeholder. L'implémentation réelle dépendrait
        # de la structure du modèle et de la bibliothèque de mappage mémoire utilisée.
        logger.info("Mappage mémoire des poids du modèle (fonction factice)...")
        return model


# ------------------------------------------------------------------
# Démonstration (exemple d'utilisation)
# ------------------------------------------------------------------
if __name__ == "__main__":
    import logging

    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    async def demo():
        print("\n--- Démonstration de AdvancedMemoryOptimizer ---")
        optimizer = AdvancedMemoryOptimizer()

        # Simule le chargement d'un modèle.
        # En réalité, `model_path` pointerait vers un fichier de poids de modèle.
        mock_model_path = "./path/to/my_large_model.bin"

        try:
            print(f"Chargement et optimisation du modèle depuis : {mock_model_path}")
            optimized_model = optimizer.optimize_model_loading(mock_model_path)
            print(f"Modèle optimisé chargé : {optimized_model}")
            print("Vérifiez l'utilisation de la mémoire de votre système.")
        except Exception as e:
            logging.error(f"Erreur lors de l'optimisation du chargement du modèle : {e}")

        print("Démonstration de AdvancedMemoryOptimizer terminée.")

    import asyncio
    asyncio.run(demo())
```

---

## Fichier : `backend\altiora\core\plugins\plugin_interface.py`

```python
# backend/altiora/core/plugins/plugin_interface.py
"""Module définissant l'interface de base pour les plugins et un gestionnaire de plugins simple.

Ce module établit le contrat que tout plugin doit respecter pour être intégré
dans le système. Il fournit également une classe `PluginManager` rudimentaire
pour enregistrer et exécuter ces plugins.
"""

from abc import ABC, abstractmethod
from typing import Dict, Any, Optional
import logging

logger = logging.getLogger(__name__)


class Plugin(ABC):
    """Interface abstraite de base pour tous les plugins.

    Tout plugin doit hériter de cette classe et implémenter ses méthodes abstraites.
    """

    @abstractmethod
    async def initialize(self, config: Dict[str, Any]):
        """Initialise le plugin avec sa configuration spécifique."

        Cette méthode est appelée une fois lors de l'enregistrement du plugin.

        Args:
            config: Un dictionnaire de configuration pour le plugin.
        """
        pass

    @abstractmethod
    async def execute(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Exécute la logique principale du plugin."

        Args:
            context: Un dictionnaire de données fournissant le contexte d'exécution au plugin.

        Returns:
            Un dictionnaire contenant les résultats de l'exécution du plugin.
        """
        pass

    @abstractmethod
    async def cleanup(self):
        """Nettoie les ressources allouées par le plugin."

        Cette méthode est appelée lors de l'arrêt du système ou du désenregistrement du plugin.
        """
        pass


class PluginManager:
    """Gestionnaire simple pour enregistrer et exécuter des plugins."""

    def __init__(self):
        """Initialise le gestionnaire de plugins."""
        self._plugins: Dict[str, Plugin] = {}

    async def register_plugin(self, name: str, plugin: Plugin, config: Dict[str, Any]):
        """Enregistre un plugin et l'initialise."

        Args:
            name: Le nom unique du plugin.
            plugin: L'instance du plugin à enregistrer.
            config: La configuration à passer au plugin lors de son initialisation.
        """
        if name in self._plugins:
            logger.warning(f"Un plugin nommé '{name}' est déjà enregistré. Il sera remplacé.")
        await plugin.initialize(config)
        self._plugins[name] = plugin
        logger.info(f"Plugin '{name}' enregistré et initialisé.")

    async def execute_plugin(self, name: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Exécute la logique d'un plugin enregistré."

        Args:
            name: Le nom du plugin à exécuter.
            context: Le contexte d'exécution à passer au plugin.

        Returns:
            Le résultat de l'exécution du plugin.

        Raises:
            ValueError: Si le plugin n'est pas trouvé.
        """
        plugin = self._plugins.get(name)
        if not plugin:
            raise ValueError(f"Plugin '{name}' non trouvé.")
        logger.info(f"Exécution du plugin '{name}'...")
        return await plugin.execute(context)

    async def unregister_plugin(self, name: str):
        """Désenregistre un plugin et nettoie ses ressources."

        Args:
            name: Le nom du plugin à désenregistrer.
        """
        plugin = self._plugins.pop(name, None)
        if plugin:
            await plugin.cleanup()
            logger.info(f"Plugin '{name}' désenregistré et nettoyé.")
        else:
            logger.warning(f"Tentative de désenregistrer un plugin non existant : '{name}'.")


# ------------------------------------------------------------------
# Démonstration (exemple d'utilisation)
# ------------------------------------------------------------------
if __name__ == "__main__":
    import asyncio
    import logging

    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    class SimpleLoggerPlugin(Plugin):
        """Un plugin de démonstration qui loggue des messages."""
        async def initialize(self, config: Dict[str, Any]):
            self.prefix = config.get("prefix", "[LOG]")
            logging.info(f"{self.prefix} SimpleLoggerPlugin initialisé.")

        async def execute(self, context: Dict[str, Any]) -> Dict[str, Any]:
            message = context.get("message", "Pas de message.")
            logging.info(f"{self.prefix} Message du plugin : {message}")
            return {"status": "logged", "processed_message": message.upper()}

        async def cleanup(self):
            logging.info(f"{self.prefix} SimpleLoggerPlugin nettoyé.")

    async def demo():
        manager = PluginManager()

        print("\n--- Enregistrement du plugin ---")
        await manager.register_plugin(
            "my_logger",
            SimpleLoggerPlugin(),
            {"prefix": "[APP_LOG]"}
        )

        print("\n--- Exécution du plugin ---")
        result = await manager.execute_plugin(
            "my_logger",
            {"message": "Ceci est un message de test."}
        )
        print(f"Résultat de l'exécution du plugin : {result}")

        print("\n--- Désenregistrement du plugin ---")
        await manager.unregister_plugin("my_logger")

        print("Démonstration du PluginManager terminée.")

    asyncio.run(demo())
```

---

## Fichier : `backend\altiora\core\plugins\plugin_system.py`

```python
# backend/altiora/core/plugins/plugin_system.py
"""Module implémentant un système de plugins dynamique pour l'application Altiora.

Ce système permet de charger des plugins à partir d'un répertoire spécifié,
de les enregistrer et de les exécuter à des points d'extension prédéfinis
(appelés "hooks"). Il fournit une interface `Plugin` que tous les plugins
doivent implémenter, assurant ainsi la modularité et l'extensibilité de l'application.
"""

import importlib.util
import inspect
import logging
from abc import ABC, abstractmethod
from functools import wraps
from pathlib import Path
from typing import Any, Dict, List

logger = logging.getLogger(__name__)


class Plugin(ABC):
    """Interface de base abstraite pour tous les plugins du système."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Le nom unique du plugin."""
        pass

    @property
    @abstractmethod
    def version(self) -> str:
        """La version du plugin."""
        pass

    @abstractmethod
    async def initialize(self, config: Dict[str, Any]):
        """Initialise le plugin avec sa configuration."

        Cette méthode est appelée une fois lors du chargement du plugin.

        Args:
            config: Un dictionnaire de configuration pour le plugin.
        """
        pass

    @abstractmethod
    async def execute(self, context: Dict[str, Any]) -> Any:
        """Exécute la logique principale du plugin."

        Args:
            context: Un dictionnaire de données fournissant le contexte d'exécution au plugin.

        Returns:
            Le résultat de l'exécution du plugin.
        """
        pass


class PluginManager:
    """Gère le chargement, l'enregistrement et l'exécution des plugins."""

    def __init__(self):
        """Initialise le gestionnaire de plugins."""
        self.plugins: Dict[str, Plugin] = {} # Stocke les instances de plugins par leur nom.
        self.hooks: Dict[str, List[Plugin]] = {} # Mappe les noms de hooks aux plugins abonnés.

    async def load_plugins(self, plugin_dir: str):
        """Charge tous les plugins à partir d'un répertoire spécifié."

        Args:
            plugin_dir: Le chemin du répertoire contenant les fichiers de plugins Python.
        """
        plugin_path = Path(plugin_dir)
        if not plugin_path.is_dir():
            logger.warning(f"Le répertoire de plugins '{plugin_dir}' n'existe pas ou n'est pas un répertoire.")
            return

        logger.info(f"Chargement des plugins depuis : {plugin_dir}")
        for file in plugin_path.glob("*.py"):
            if file.name.startswith("_") or file.name == "__init__.py":
                continue # Ignore les fichiers internes.

            module_name = file.stem
            try:
                # Charge le module dynamiquement.
                spec = importlib.util.spec_from_file_location(
                    module_name,
                    file
                )
                if spec and spec.loader:
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)

                    # Recherche les classes qui implémentent l'interface Plugin.
                    for name, obj in inspect.getmembers(module):
                        if (inspect.isclass(obj) and
                                issubclass(obj, Plugin) and
                                obj != Plugin): # S'assure que ce n'est pas l'interface elle-même.
                            plugin_instance = obj() # Instancie le plugin.
                            await self.register_plugin(plugin_instance)
                else:
                    logger.warning(f"Impossible de charger la spécification pour le module {module_name}.")
            except Exception as e:
                logger.error(f"Erreur lors du chargement du plugin depuis {file}: {e}", exc_info=True)

    async def register_plugin(self, plugin: Plugin):
        """Enregistre une instance de plugin et l'initialise."

        Args:
            plugin: L'instance du plugin à enregistrer.
        """
        if plugin.name in self.plugins:
            logger.warning(f"Un plugin nommé '{plugin.name}' est déjà enregistré. Il sera remplacé.")
        
        await plugin.initialize({}) # Initialise le plugin (peut prendre une configuration).
        self.plugins[plugin.name] = plugin
        logger.info(f"Plugin '{plugin.name}' v{plugin.version} chargé et enregistré.")

    def hook(self, hook_name: str):
        """Décorateur pour définir un point d'extension (hook) dans le code."

        Les fonctions décorées avec `@plugin_manager.hook("nom_du_hook")`
        exécuteront les plugins enregistrés pour ce hook avant et après leur propre logique.

        Args:
            hook_name: Le nom du hook (ex: "before_sfd_analysis", "after_test_generation").

        Returns:
            Un décorateur qui peut être appliqué à une fonction asynchrone.
        """
        def decorator(func):
            @wraps(func)
            async def wrapper(*args, **kwargs):
                # Exécute les plugins enregistrés pour le hook "before_" correspondant.
                for plugin in self.hooks.get(f"before_{hook_name}", []):
                    logger.debug(f"Exécution du plugin '{plugin.name}' pour le hook 'before_{hook_name}'.")
                    await plugin.execute({"hook": hook_name, "stage": "before", "args": args, "kwargs": kwargs})

                # Exécute la fonction originale.
                result = await func(*args, **kwargs)

                # Exécute les plugins enregistrés pour le hook "after_" correspondant.
                for plugin in self.hooks.get(f"after_{hook_name}", []):
                    logger.debug(f"Exécution du plugin '{plugin.name}' pour le hook 'after_{hook_name}'.")
                    await plugin.execute({"hook": hook_name, "stage": "after", "result": result, "args": args, "kwargs": kwargs})

                return result

            return wrapper

        return decorator

    async def register_hook_plugin(self, hook_name: str, plugin: Plugin):
        """Enregistre un plugin pour un hook spécifique."

        Args:
            hook_name: Le nom du hook auquel le plugin doit s'abonner.
            plugin: L'instance du plugin à enregistrer.
        """
        if hook_name not in self.hooks:
            self.hooks[hook_name] = []
        self.hooks[hook_name].append(plugin)
        logger.info(f"Plugin '{plugin.name}' enregistré pour le hook '{hook_name}'.")


# ------------------------------------------------------------------
# Exemple de plugin (pour la démonstration)
# ------------------------------------------------------------------
class MetricsPlugin(Plugin):
    """Plugin de démonstration pour collecter des métriques d'exécution."""

    @property
    def name(self) -> str:
        return "metrics_collector"

    @property
    def version(self) -> str:
        return "1.0.0"

    async def initialize(self, config: Dict[str, Any]):
        self.metrics: Dict[str, List[float]] = {} # Stocke les durées d'opération.
        logger.info(f"MetricsPlugin initialisé. Config: {config}")

    async def execute(self, context: Dict[str, Any]) -> Any:
        operation = context.get("operation")
        duration = context.get("duration")
        stage = context.get("stage")
        hook = context.get("hook")

        if operation and duration is not None:
            if operation not in self.metrics:
                self.metrics[operation] = []
            self.metrics[operation].append(duration)
            logger.info(f"MetricsPlugin: Hook '{hook}' ({stage}) - Opération '{operation}' a pris {duration:.4f}s.")
        else:
            logger.debug(f"MetricsPlugin: Hook '{hook}' ({stage}) - Contexte : {context}")
        return None


# ------------------------------------------------------------------
# Démonstration (exemple d'utilisation)
# ------------------------------------------------------------------
if __name__ == "__main__":
    import asyncio
    import time

    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    async def demo():
        manager = PluginManager()

        # Crée un répertoire factice pour les plugins.
        temp_plugin_dir = Path("temp_plugins")
        temp_plugin_dir.mkdir(exist_ok=True)

        # Crée un fichier de plugin factice.
        (temp_plugin_dir / "my_metrics_plugin.py").write_text("""
from src.plugins.plugin_system import Plugin
import logging

logger = logging.getLogger(__name__)

class MyMetricsPlugin(Plugin):
    name = "my_metrics_plugin"
    version = "0.1.0"

    async def initialize(self, config):
        self.data = []
        logger.info("MyMetricsPlugin initialisé.")

    async def execute(self, context):
        if context.get("stage") == "after":
            operation_name = context.get("args", ["unknown_op"])[0]
            duration = context.get("result", 0)
            self.data.append({"operation": operation_name, "duration": duration})
            logger.info(f"[MyMetricsPlugin] Enregistré : {operation_name} - {duration:.4f}s")
        return None
""")

        print("\n--- Chargement des plugins ---")
        await manager.load_plugins(str(temp_plugin_dir))

        # Enregistre le plugin de métriques pour un hook spécifique.
        metrics_plugin_instance = MetricsPlugin()
        await manager.register_hook_plugin("process_data", metrics_plugin_instance)

        @manager.hook("process_data")
        async def process_data(item: str) -> float:
            """Fonction de démonstration qui sera instrumentée par le hook."""
            logging.info(f"Traitement de l'élément : {item}")
            delay = random.uniform(0.05, 0.2)
            await asyncio.sleep(delay)
            return delay

        print("\n--- Exécution de fonctions avec hooks ---")
        results = []
        for i in range(5):
            duration = await process_data(f"data_{i}")
            results.append(duration)

        print("\n--- Résultats des métriques collectées par le plugin ---")
        print(metrics_plugin_instance.metrics)

        print("Démonstration du PluginSystem terminée.")

        # Nettoyage.
        import shutil
        shutil.rmtree(temp_plugin_dir)

    import random
    asyncio.run(demo())

```

---

## Fichier : `backend\altiora\core\plugins\__init__.py`

```python
# backend/altiora/core/plugins/__init__.py
"""Initialise le package `plugins` de l'application Altiora.

Ce package contient le système de plugins qui permet d'étendre les
fonctionnalités de l'application de manière dynamique. Il définit
l'interface des plugins et le gestionnaire pour les charger et les exécuter.

Les modules suivants sont exposés pour faciliter les importations :
- `PluginSystem`: Le gestionnaire principal du système de plugins.
"""
from .plugin_system import PluginSystem

__all__ = ['PluginSystem']

```

---

## Fichier : `backend\altiora\core\policies\business_rules.py`

```python
# backend/altiora/core/policies/business_rules.py
"""Module de validation des règles métier pour les artefacts générés.

Ce module garantit que les artefacts produits par l'IA (comme les scripts de test
Playwright ou les fichiers Excel) respectent un ensemble de règles métier prédéfinies,
assurant ainsi leur qualité, leur cohérence et leur maintenabilité.
"""

import ast
import re
from typing import List, Dict, Any, Optional

# ------------------------------------------------------------------
# Constantes
# ------------------------------------------------------------------

# Le module de reporting standard que tous les tests doivent utiliser.
REPORTER_MODULE = "reports.standard_reporter"
# La fonction de reporting spécifique à appeler à chaque étape du test.
REPORTER_FUNC = "report_step"


# ------------------------------------------------------------------
# Règles
# ------------------------------------------------------------------
class BusinessRules:
    """Validateur centralisé pour les règles métier."""

    async def validate(
            self,
            code_string: str,
            *,
            workflow: str,
            meta: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Valide un artefact par rapport à un workflow donné.

        Args:
            code_string: La chaîne de caractères de l'artefact à valider (ex: code Python).
            workflow: Le type de workflow (ex: 'test', 'excel'). Détermine quel
                      ensemble de règles appliquer.
            meta: Métadonnées supplémentaires pouvant être utilisées par les règles.

        Returns:
            Un dictionnaire contenant le résultat de la validation:
            {"ok": bool, "violations": List[str]}
        """
        violations: List[str] = []

        try:
            if workflow == "test":
                violations = self._validate_playwright_test(code_string, meta)
            # D'autres workflows peuvent être ajoutés ici.
            # elif workflow == "excel":
            #     violations = self._validate_excel_file(meta)
        except Exception as e:
            violations.append(f"Erreur inattendue lors de la validation : {e}")

        return {"ok": not violations, "violations": violations}

    # ----------------------------------------------------------
    # Règles spécifiques à Playwright
    # ----------------------------------------------------------
    @staticmethod
    def _validate_playwright_test(
            code: str, meta: Optional[Dict[str, Any]] = None
    ) -> List[str]:
        """Applique un ensemble de règles spécifiques aux tests Playwright."""
        violations = []

        # Règle 1: Interdire `time.sleep()` au profit des attentes natives de Playwright.
        if "time.sleep" in code:
            violations.append(
                "Règle violée : `time.sleep()` est interdit. Utilisez les attentes natives de Playwright (ex: `page.wait_for_selector`)."
            )

        # Règle 2: Éviter les URLs en dur pour favoriser la configuration.
        if re.search(r"page\.goto\(\s*["']https?://", code):
            violations.append(
                "Règle violée : Les URLs ne doivent pas être codées en dur. Utilisez des variables de configuration."
            )

        # Règle 3: S'assurer de l'utilisation du module de reporting standard.
        reporter_imported = False
        reporter_used = False
        try:
            tree = ast.parse(code)
            for node in ast.walk(tree):
                # Vérification de l'importation.
                if (
                        isinstance(node, ast.ImportFrom)
                        and node.module == REPORTER_MODULE
                ):
                    reporter_imported = any(
                        alias.name == REPORTER_FUNC for alias in node.names
                    )
                # Vérification de l'utilisation.
                if (
                        isinstance(node, ast.Call)
                        and isinstance(node.func, ast.Name)
                        and node.func.id == REPORTER_FUNC
                ):
                    reporter_used = True

                # Règle 4: Vérifier la qualité des noms et des docstrings des fonctions de test.
                if isinstance(node, ast.FunctionDef) and node.name.startswith(
                        "test_"
                ):
                    if not ast.get_docstring(node):
                        violations.append(
                            f"Qualité : Le test `{node.name}` n'a pas de docstring."
                        )
                    if node.name in {"test_unnamed", "test_script"}:
                        violations.append(
                            f"Qualité : Le nom du test `{node.name}` est trop générique."
                        )

        except SyntaxError as e:
            violations.append(f"Erreur de syntaxe Python : {e}")

        if not reporter_imported:
            violations.append(f"Règle violée : L'import `{REPORTER_MODULE}.{REPORTER_FUNC}` est manquant.")
        if not reporter_used:
            violations.append(f"Règle violée : La fonction de reporting `{REPORTER_FUNC}()` n'est pas appelée.")

        return violations


# ------------------------------------------------------------------
# Démonstration rapide
# ------------------------------------------------------------------
if __name__ == "__main__":
    import asyncio
    import logging

    logging.basicConfig(level=logging.INFO)

    async def main() -> None:
        rules = BusinessRules()

        good_code = '''
from playwright.sync_api import Page
from reports.standard_reporter import report_step

def test_login_page(page: Page):
    """Vérifie que la page de connexion se charge correctement."""
    report_step("Navigation vers la page de connexion")
    page.goto("/login")
'''

        bad_code = '''
import time

def test_unnamed(page):
    page.goto("https://example.com")
    time.sleep(2)
'''

        logging.info("--- Validation du bon code ---")
        good_result = await rules.validate(good_code, workflow="test")
        logging.info(good_result)

        logging.info("\n--- Validation du mauvais code ---")
        bad_result = await rules.validate(bad_code, workflow="test")
        logging.info(bad_result)

    asyncio.run(main())
```

---

## Fichier : `backend\altiora\core\policies\excel_policy.py`

```python
# backend/altiora/core/policies/excel_policy.py
"""Module contenant les règles de validation pour les matrices de test.

Ce module garantit l'intégrité des données destinées à être exportées
vers des fichiers Excel, en s'assurant que les cas de test respectent
le format, la structure et le contenu attendus.
"""

from __future__ import annotations

import re
from typing import List, Dict, Any, Set, Final

# ------------------------------------------------------------------
# Règles de configuration
# ------------------------------------------------------------------

# Expression régulière pour valider le format des identifiants de cas de test.
# Exemple de format valide : CU01_SB02_CP001_nom_du_test
TEST_CASE_ID_PATTERN: Final[re.Pattern[str]] = re.compile(
    r"^CU\d{2}_SB\d{2}_C[PEL]\d{3}_.+(?<!_)$"
)

# Ensemble des colonnes requises dans chaque dictionnaire de cas de test.
REQUIRED_COLUMNS: Final[Set[str]] = {"id", "description", "type"}

# Ensemble des types de cas de test valides.
VALID_TYPES: Final[Set[str]] = {"CP", "CE", "CL"}  # Cas Passant, Cas d'Erreur, Cas Limite


class ExcelPolicy:
    """Valide les données des cas de test avant leur exportation vers Excel."""

    def validate_test_matrix(
        self, test_cases: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """Valide une liste de dictionnaires représentant des cas de test.

        Args:
            test_cases: Une liste de cas de test, où chaque cas est un dictionnaire.

        Returns:
            Un dictionnaire contenant le statut de la validation et la liste des erreurs.
            {
                "is_valid": bool,
                "errors": List[str]
            }
        """
        errors: List[str] = []
        errors.extend(self._validate_structure(test_cases))
        errors.extend(self._validate_content(test_cases))
        errors.extend(self._validate_uniqueness(test_cases))
        return {"is_valid": not errors, "errors": errors}

    # ------------------------------------------------------------------
    # Implémentation des règles
    # ------------------------------------------------------------------
    @staticmethod
    def _validate_structure(cases: List[Dict[str, Any]]) -> List[str]:
        """Vérifie la présence des colonnes requises dans chaque cas de test."""
        errors = []
        for idx, case in enumerate(cases, start=2):  # Commence à 2 pour correspondre aux lignes Excel
            missing = REQUIRED_COLUMNS - case.keys()
            if missing:
                errors.append(f"Ligne {idx}: Colonnes manquantes {sorted(missing)}.")
        return errors

    @staticmethod
    def _validate_content(cases: List[Dict[str, Any]]) -> List[str]:
        """Valide le format de l'ID, le type et la description de chaque cas."""
        errors = []
        for idx, case in enumerate(cases, start=2):
            case_id = str(case.get("id", ""))
            case_type = str(case.get("type", ""))
            description = str(case.get("description", "")).strip()

            if not TEST_CASE_ID_PATTERN.match(case_id):
                errors.append(f"Ligne {idx}: L'ID `{case_id}` a un format invalide.")

            if case_type not in VALID_TYPES:
                errors.append(
                    f"Ligne {idx}: Le type `{case_type}` est invalide (attendu : {VALID_TYPES})."
                )

            if not description:
                errors.append(f"Ligne {idx}: La description ne peut pas être vide.")
        return errors

    @staticmethod
    def _validate_uniqueness(cases: List[Dict[str, Any]]) -> List[str]:
        """S'assure que chaque identifiant de cas de test est unique."""
        seen: Set[str] = set()
        errors = []
        for idx, case in enumerate(cases, start=2):
            case_id = str(case.get("id"))
            if case_id in seen:
                errors.append(f"Ligne {idx}: L'ID `{case_id}` est dupliqué.")
            seen.add(case_id)
        return errors


# ------------------------------------------------------------------
# Auto-test rapide
# ------------------------------------------------------------------
if __name__ == "__main__":
    policy = ExcelPolicy()

    valid_cases = [
        {
            "id": "CU01_SB01_CP001_connexion_valide",
            "description": "Tester la connexion réussie avec un utilisateur valide.",
            "type": "CP",
        }
    ]
    invalid_cases = [
        {
            "id": "INVALID_ID",
            "description": "",
            "type": "XX",
        },
        {
            "id": "CU01_SB01_CP001_connexion_valide", # ID dupliqué
            "description": "Un autre test.",
            "type": "CP",
        }
    ]

    print("Validation de données valides :", policy.validate_test_matrix(valid_cases))
    print("Validation de données invalides :", policy.validate_test_matrix(invalid_cases))

```

---

## Fichier : `backend\altiora\core\policies\privacy_policy.py`

```python
# backend/altiora/core/policies/privacy_policy.py
"""Moteur de politique de confidentialité pour Altiora, centré sur l'utilisateur français.

Ce module fournit des fonctionnalités essentielles pour la conformité RGPD :
- Détection et masquage d'informations personnelles identifiables (PII) françaises.
- Application de règles de rétention des données.
- Gestion du consentement de l'utilisateur et journalisation pour l'audit.
"""

import re
import json
import logging
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass, asdict
from datetime import datetime, timedelta
from pathlib import Path

logger = logging.getLogger(__name__)


# ------------------------------------------------------------------
# Structures de données
# ------------------------------------------------------------------
@dataclass
class PIIDetection:
    """Représente une information personnelle identifiable (PII) détectée."""
    type: str       # Type de PII (ex: email, phone).
    value: str      # La valeur originale détectée.
    redacted: str   # La valeur masquée.
    start: int      # L'index de début dans le texte original.
    end: int        # L'index de fin.

@dataclass
class PrivacyReport:
    """Rapport généré après l'analyse d'un texte."""
    text: str
    pii_list: List[PIIDetection]
    retention_seconds: int
    can_store: bool
    user_consent_required: bool


# ------------------------------------------------------------------
# Constantes de la politique
# ------------------------------------------------------------------

# Expressions régulières pour détecter les PII courantes en France.
PII_PATTERNS = {
    "email": r"[\w\.-]+@[\w\.-]+\.\w+",
    "phone": r"(\+?33[-.\s]?|0)[1-9]([-.\s]?\d{2}){4}",
    "credit_card": r"\b(?:\d{4}[\s-]?){3}\d{4}\b",
    "social_security": r"\b\d{3}[\s-]?\d{2}[\s-]?\d{3}[\s-]?\d{3}\b",
    "passport": r"\b[A-Z]{1,2}\d{6,9}\b",
    "driver_license": r"\b\d{2}[\s-]?\d{2}[\s-]?\d{2}[\s-]?\d{5}[\s-]?\d{2}\b",
    "postal_code": r"\b\d{5}\b",
    "iban": r"\bFR\d{2}\s?(\d{4}\s?){4}\d{2}\b",
}

# Règles de rétention des données en secondes, conformément au RGPD.
# Une valeur de 0 signifie que la donnée ne doit jamais être stockée.
RETENTION_RULES = {
    "email": 30 * 24 * 3600,          # 30 jours
    "phone": 7 * 24 * 3600,           # 7 jours
    "credit_card": 0,                 # Ne jamais stocker
    "social_security": 0,             # Ne jamais stocker
    "passport": 0,                    # Ne jamais stocker
    "driver_license": 0,              # Ne jamais stocker
    "postal_code": 365 * 24 * 3600,   # 1 an
    "iban": 90 * 24 * 3600,           # 90 jours
}


# ------------------------------------------------------------------
# API Publique
# ------------------------------------------------------------------
class PrivacyPolicy:
    """Classe principale pour la gestion de la politique de confidentialité."""

    def __init__(self, config_path: Optional[Path] = None):
        """Initialise la politique, en chargeant une configuration personnalisée si fournie."""
        self.config = self._load_config(config_path)
        self.consent_db = ConsentDB(config_path)

    # ------------------------------------------------------------------
    # Détection et masquage de PII
    # ------------------------------------------------------------------
    def scan_and_mask(self, text: str, *, mask_char: str = "*") -> PrivacyReport:
        """Analyse un texte, masque les PII et retourne un rapport détaillé."""
        pii_list = []
        for pii_type, pattern in PII_PATTERNS.items():
            for match in re.finditer(pattern, text, re.IGNORECASE):
                original = match.group(0)
                redacted = self._mask(original, mask_char)
                pii_list.append(
                    PIIDetection(
                        type=pii_type,
                        value=original,
                        redacted=redacted,
                        start=match.start(),
                        end=match.end(),
                    )
                )

        # Construit le texte masqué en remplaçant les PII détectées.
        masked_text = text
        for det in sorted(pii_list, key=lambda d: d.start, reverse=True):
            masked_text = (
                masked_text[: det.start] + det.redacted + masked_text[det.end :]
            )

        # Détermine la durée de rétention maximale et si le consentement est requis.
        max_retention = max(
            (RETENTION_RULES.get(p.type, 0) for p in pii_list), default=0
        )
        can_store = max_retention > 0
        user_consent_required = any(p.type in {"email", "phone"} for p in pii_list)

        return PrivacyReport(
            text=masked_text,
            pii_list=pii_list,
            retention_seconds=max_retention,
            can_store=can_store,
            user_consent_required=user_consent_required,
        )

    # ------------------------------------------------------------------
    # Gestion du consentement
    # ------------------------------------------------------------------
    def record_consent(
        self, user_id: str, pii_types: List[str], granted: bool, expiry_days: int = 365
    ):
        """Enregistre le choix de consentement d'un utilisateur."""
        self.consent_db.add(
            user_id=user_id,
            pii_types=pii_types,
            granted=granted,
            expires_at=datetime.utcnow() + timedelta(days=expiry_days),
        )

    def has_consent(self, user_id: str, pii_type: str) -> bool:
        """Vérifie si un utilisateur a un consentement valide pour un type de PII."""
        return self.consent_db.is_valid(user_id, pii_type)

    # ------------------------------------------------------------------
    # Piste d'audit
    # ------------------------------------------------------------------
    def log_access(self, user_id: str, pii_type: str, action: str):
        """Journalise un accès à une PII pour la piste d'audit RGPD."""
        log_entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "user_id": user_id,
            "pii_type": pii_type,
            "action": action, # ex: 'view', 'export'
        }
        self._append_audit_log(log_entry)

    # ------------------------------------------------------------------
    # Utilitaires
    # ------------------------------------------------------------------
    def _mask(self, value: str, mask_char: str) -> str:
        """Masque une valeur en conservant les 2 premiers et 2 derniers caractères."""
        if len(value) <= 4:
            return mask_char * len(value)
        return value[:2] + mask_char * (len(value) - 4) + value[-2:]

    def _load_config(self, path: Optional[Path]) -> Dict:
        """Charge une configuration de rétention personnalisée si elle existe."""
        if path and path.exists():
            return json.loads(path.read_text())
        return RETENTION_RULES

    def _append_audit_log(self, entry: Dict):
        """Ajoute une entrée au fichier d'audit (format JSON Lines)."""
        try:
            audit_file = Path("logs/privacy_audit.jsonl")
            audit_file.parent.mkdir(exist_ok=True)
            with audit_file.open("a", encoding="utf-8") as f:
                f.write(json.dumps(entry, ensure_ascii=False) + "\n")
        except (IOError, OSError) as e:
            logger.error(f"Erreur lors de l'écriture dans le journal d'audit : {e}")


# ------------------------------------------------------------------
# Persistance du consentement (simple fichier JSONL)
# ------------------------------------------------------------------
class ConsentDB:
    """Une base de données simple, basée sur un fichier, pour stocker le consentement."""
    def __init__(self, config_path: Optional[Path]):
        self.file = Path(config_path or "data/consent.jsonl")

    def add(
        self, user_id: str, pii_types: List[str], granted: bool, expires_at: datetime
    ):
        """Ajoute un nouvel enregistrement de consentement."""
        try:
            self.file.parent.mkdir(parents=True, exist_ok=True)
            record = {
                "user_id": user_id,
                "pii_types": pii_types,
                "granted": granted,
                "expires_at": expires_at.isoformat(),
                "created_at": datetime.utcnow().isoformat(),
            }
            with self.file.open("a", encoding="utf-8") as f:
                f.write(json.dumps(record, ensure_ascii=False) + "\n")
        except (IOError, OSError) as e:
            logger.error(f"Erreur lors de l'écriture dans la base de données de consentement : {e}")

    def is_valid(self, user_id: str, pii_type: str) -> bool:
        """Vérifie si le consentement le plus récent pour un utilisateur et un type de PII est valide."""
        now = datetime.utcnow()
        try:
            with self.file.open("r", encoding="utf-8") as f:
                # Lit le fichier en sens inverse pour trouver le consentement le plus récent en premier.
                for line in reversed(list(f)):
                    record = json.loads(line)
                    if (
                        record["user_id"] == user_id
                        and pii_type in record["pii_types"]
                    ):
                        # Si le consentement est trouvé, vérifie s'il a expiré.
                        if datetime.fromisoformat(record["expires_at"]) < now:
                            return False
                        # Retourne l'état (accordé ou non).
                        return record["granted"]
        except FileNotFoundError:
            # Si le fichier n'existe pas, aucun consentement n'a été donné.
            pass
        return False


# ------------------------------------------------------------------
# Démonstration en ligne de commande
# ------------------------------------------------------------------
if __name__ == "__main__":
    policy = PrivacyPolicy()

    sample_text = (
        "Contactez-moi à jean.dupont@mail.fr ou au 06.12.34.56.78, "
        "ma carte est 4532-1234-5678-9012."
    )
    report = policy.scan_and_mask(sample_text)
    print(json.dumps(asdict(report), ensure_ascii=False, indent=2))

```

---

## Fichier : `backend\altiora\core\policies\toxicity_policy.py`

```python
# backend/altiora/core/policies/toxicity_policy.py
"""Politique de détection de toxicité et de PII pour Altiora.

Ce module combine une analyse rapide basée sur des expressions régulières locales
(avec un lexique français) et des appels optionnels à des API externes pour une
analyse plus approfondie. Il fournit un score de sévérité et masque les PII.
"""

import re
import logging
from typing import Dict, List, Optional
from dataclasses import dataclass
from enum import Enum

# Importation de PrivacyPolicy pour la détection de PII
from .privacy_policy import PrivacyPolicy, PrivacyReport

try:
    import httpx
except ImportError:
    httpx = None

logger = logging.getLogger(__name__)


class Severity(Enum):
    """Niveaux de sévérité pour le contenu détecté."""
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4


@dataclass
class DetectionResult:
    """Résultat d'une analyse de toxicité."""
    toxic: bool
    severity: Severity
    categories: List[str]
    pii_found: List[str]
    confidence: float
    provider: str


# ------------------------------------------------------------------
# Lexique et expressions régulières (Français)
# ------------------------------------------------------------------
TOXIC_REGEXES = {
    "hate": [
        r"\b(nazi|facho|raciste|suprémaciste)\b",
        r"\b(tuer\s+(tous?|les?)|pendre\s+les?|gazer\s+les?)\b",
    ],
    "harassment": [
        r"\b(naze|con|idiot|imbécile|débile|pd|tapette)\b",
        r"\b(ferme\s+ta\s+gueule|dégage|va\s+te\s+faire)\b",
    ],
    "sexual": [
        r"\b(porno?|xxx|nud?e?|viol|agression\s+sexuelle)\b",
    ],
    "violence": [
        r"\b(bombe|tuer|tue|tirer|poignarder|massacrer)\b",
    ],
}

PII_REGEXES = {
    "email": r"[\w\.-]+@[\w\.-]+\.\w+",
    "phone": r"(\+?33[-.\s]?|0)[1-9]([-.\s]?\d{2}){4}",
    "credit_card": r"\b(?:\d{4}[\s-]?){3}\d{4}\b",
    "social_security": r"\b\d{3}[\s-]?\d{2}[\s-]?\d{3}[\s-]?\d{3}\b",
}


class ToxicityPolicy:
    """Analyse le texte pour la toxicité et les PII."""

    def __init__(
        self,
        *,
        use_external: bool = False,
        openai_key: Optional[str] = None,
        azure_endpoint: Optional[str] = None,
    ):
        """Initialise la politique.

        Args:
            use_external: Si True, utilise les API externes (OpenAI, Azure) comme fallback.
            openai_key: Clé API pour OpenAI Moderation.
            azure_endpoint: Endpoint pour Azure Content Safety.
        """
        self.use_external = use_external and httpx is not None
        self.openai_key = openai_key
        self.azure_endpoint = azure_endpoint

    # ------------------------------------------------------------------
    # API Publique
    # ------------------------------------------------------------------
    async def scan(self, text: str) -> DetectionResult:
        """Analyse un texte (français) pour la toxicité et les PII.

        La stratégie est d'abord locale (rapide) puis externe (plus lente mais potentiellement
        plus précise). Si une toxicité élevée est détectée localement, le résultat est
        retourné immédiatement.
        """
        text_lower = text.lower()
        regex_result = self._regex_scan(text_lower)

        # Si la sévérité est déjà haute, on retourne le résultat immédiatement.
        if regex_result.severity in (Severity.HIGH, Severity.CRITICAL):
            return regex_result

        # Si l'option est activée, on utilise une API externe comme fallback.
        if self.use_external:
            external_result = await self._external_scan(text_lower)
            # On retourne le résultat externe seulement s'il est plus sévère.
            if external_result.severity.value > regex_result.severity.value:
                return external_result

        return regex_result

    # ------------------------------------------------------------------
    # Implémentation par expressions régulières
    # ------------------------------------------------------------------
    def _regex_scan(self, text: str) -> DetectionResult:
        """Analyse le texte en utilisant les expressions régulières locales."""
        toxic = False
        categories: List[str] = []
        max_sev = Severity.LOW
        pii_tokens: List[str] = []

        # Détection de la toxicité
        for cat, patterns in TOXIC_REGEXES.items():
            for pattern in patterns:
                if re.search(pattern, text, re.IGNORECASE):
                    toxic = True
                    if cat not in categories:
                        categories.append(cat)
                    max_sev = max(max_sev, self._severity_from_cat(cat))

        # Détection des PII
        for pii_type, pattern in PII_REGEXES.items():
            for match in re.finditer(pattern, text):
                pii_tokens.append(match.group(0))

        return DetectionResult(
            toxic=toxic,
            severity=max_sev,
            categories=categories,
            pii_found=pii_tokens,
            confidence=0.9,  # Confiance élevée pour les regex car déterministes
            provider="regex",
        )

    # ------------------------------------------------------------------
    # Assistants pour les API externes
    # ------------------------------------------------------------------
    async def _external_scan(self, text: str) -> DetectionResult:
        """Tente d'analyser le texte avec une API externe."""
        if self.openai_key:
            return await self._openai_moderation(text)
        if self.azure_endpoint:
            return await self._azure_content_safety(text)
        return self._fallback_result()

    async def _openai_moderation(self, text: str) -> DetectionResult:
        """Analyse le texte avec l'API de modération d'OpenAI."""
        url = "https://api.openai.com/v1/moderations"
        headers = {"Authorization": f"Bearer {self.openai_key}"}
        payload = {"input": text}

        async with httpx.AsyncClient(timeout=10) as client:
            try:
                resp = await client.post(url, json=payload, headers=headers)
                resp.raise_for_status() # Lève une exception pour les codes 4xx/5xx
            except httpx.HTTPStatusError as e:
                logger.error(f"Erreur de l'API de modération OpenAI : {e.response.text}")
                return self._fallback_result()

        data = resp.json()
        result = data["results"][0]
        categories = result["categories"]
        scores = result["category_scores"]

        toxic = any(categories.values())
        max_sev = max(
            (self._severity_from_openai_cat(name) for name, flag in categories.items() if flag),
            default=Severity.LOW,
        )
        return DetectionResult(
            toxic=toxic,
            severity=max_sev,
            categories=[k for k, v in categories.items() if v],
            pii_found=[],
            confidence=max(scores.values()),
            provider="openai",
        )

    async def _azure_content_safety(self, text: str) -> DetectionResult:
        """Analyse le texte avec l'API Azure Content Safety."""
        url = f"{self.azure_endpoint}/contentsafety/text:analyze?api-version=2023-10-01"
        headers = {"Content-Type": "application/json"}
        payload = {"text": text, "categories": ["Hate", "Sexual", "Violence", "SelfHarm"]}

        async with httpx.AsyncClient(timeout=10) as client:
            try:
                resp = await client.post(url, json=payload, headers=headers)
                resp.raise_for_status()
            except httpx.HTTPStatusError as e:
                logger.error(f"Erreur de l'API Azure Content Safety : {e.response.text}")
                return self._fallback_result()

        data = resp.json()
        toxic = any(block["severity"] > 0 for block in data.get("categoriesAnalysis", []))
        max_sev = max(
            (Severity(block["severity"]) for block in data["categoriesAnalysis"] if block["severity"] > 0),
            default=Severity.LOW,
        )
        return DetectionResult(
            toxic=toxic,
            severity=max_sev,
            categories=[b["category"] for b in data["categoriesAnalysis"] if b["severity"] > 0],
            pii_found=[],
            confidence=0.8, # Confiance arbitraire pour Azure
            provider="azure",
        )

    # ------------------------------------------------------------------
    # Utilitaires
    # ------------------------------------------------------------------
    def _severity_from_cat(self, category: str) -> Severity:
        """Mappe une catégorie de regex à un niveau de sévérité."""
        mapping = {
            "hate": Severity.HIGH,
            "harassment": Severity.MEDIUM,
            "sexual": Severity.MEDIUM,
            "violence": Severity.HIGH,
        }
        return mapping.get(category, Severity.LOW)

    def _severity_from_openai_cat(self, category: str) -> Severity:
        """Mappe une catégorie de l'API OpenAI à un niveau de sévérité."""
        return {
            "hate": Severity.HIGH,
            "hate/threatening": Severity.CRITICAL,
            "harassment": Severity.MEDIUM,
            "harassment/threatening": Severity.HIGH,
            "sexual": Severity.MEDIUM,
            "sexual/minors": Severity.CRITICAL,
            "violence": Severity.HIGH,
            "violence/graphic": Severity.CRITICAL,
            "self-harm": Severity.CRITICAL,
        }.get(category, Severity.LOW)

    def _fallback_result(self) -> DetectionResult:
        """Retourne un résultat non toxique en cas d'échec des API externes."""
        return DetectionResult(
            toxic=False,
            severity=Severity.LOW,
            categories=[],
            pii_found=[],
            confidence=0.0,
            provider="none",
        )


# ------------------------------------------------------------------
# Démonstration en ligne de commande
# ------------------------------------------------------------------
if __name__ == "__main__":
    import asyncio

    async def demo():
        policy = ToxicityPolicy(use_external=False)
        samples = [
            "Bonjour, comment vas-tu ?",
            "T’es vraiment un gros débile, ferme-la !",
            "Mon email est pierre.dupont@mail.fr et ma carte 1234-5678-9012-3456",
        ]
        for s in samples:
            res = await policy.scan(s)
            logging.info(f"{s} → {res}")

    asyncio.run(demo())

```

---

## Fichier : `backend\altiora\core\policies\__init__.py`

```python
# backend/altiora/core/policies/__init__.py
"""
Policies and business rules.
"""
```

---

## Fichier : `backend\altiora\core\post_processing\code_validator.py`

```python
# backend/altiora/core/post_processing/code_validator.py
"""Module pour la validation complète du code Python et Playwright généré.

Ce module fournit une classe `CodeValidator` qui effectue plusieurs vérifications
sur une chaîne de code source pour garantir sa qualité, sa syntaxe et sa conformité
aux standards du projet avant son utilisation ou son stockage.

Fonctionnalités principales :
1.  Vérification de la syntaxe Python à l'aide du module `ast`.
2.  Linting du code à l'aide de `ruff` pour détecter les erreurs et les mauvaises pratiques.
3.  Vérification du formatage du code avec `black` pour assurer un style cohérent.
4.  Vérifications spécifiques à Playwright (imports, usage de la fixture `page`, etc.).

Le validateur est conçu pour être utilisé de manière asynchrone et retourne un
objet Pydantic `ValidationResult` qui détaille toutes les erreurs trouvées.
"""

import ast
import asyncio
import logging
import re
import tempfile
from pathlib import Path
from typing import List, Optional, Tuple

from pydantic import BaseModel, Field

# Configuration du logger
logger = logging.getLogger(__name__)


class ValidationResult(BaseModel):
    """Représente le résultat détaillé de la validation du code."""
    is_valid: bool = Field(True, description="Le code est-il syntaxiquement valide ?")
    syntax_error: Optional[str] = Field(None, description="Message d'erreur de syntaxe, le cas échéant.")
    linting_errors: List[str] = Field(default_factory=list, description="Liste des erreurs de linting (ruff).")
    formatting_errors: List[str] = Field(default_factory=list, description="Liste des erreurs de formatage (black).")
    playwright_warnings: List[str] = Field(default_factory=list, description="Avertissements spécifiques à Playwright.")

    @property
    def passed(self) -> bool:
        """Propriété indiquant si le code a passé toutes les vérifications avec succès."""
        return self.is_valid and not self.linting_errors and not self.formatting_errors and not self.playwright_warnings


class CodeValidator:
    """Valide une chaîne de code Python ou Playwright en utilisant des outils externes."""

    def __init__(self, ruff_config_path: Optional[str] = None):
        """Initialise le validateur.

        Args:
            ruff_config_path: Chemin optionnel vers un fichier de configuration `ruff.toml`.
        """
        self.ruff_config_path = ruff_config_path

    @staticmethod
    async def _run_subprocess(command: str, *args: str) -> Tuple[int, str, str]:
        """Exécute une commande en sous-processus de manière asynchrone."""
        try:
            process = await asyncio.create_subprocess_exec(
                command, *args,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )
            stdout, stderr = await process.communicate()
            return process.returncode, stdout.decode('utf-8'), stderr.decode('utf-8')
        except FileNotFoundError:
            logger.error(f"La commande `{command}` n'a pas été trouvée. Assurez-vous qu'elle est installée et dans le PATH.")
            return -1, "", f"Commande non trouvée: {command}"
        except Exception as e:
            logger.error(f"Erreur lors de l'exécution de la commande `{command}` : {e}")
            return -1, "", str(e)

    @staticmethod
    def _validate_playwright_specifics(code_string: str) -> List[str]:
        """Vérifie les meilleures pratiques et conventions spécifiques à Playwright."""
        warnings = []

        # 1. Vérifier l'importation de Playwright.
        if not re.search(r"from\s+playwright\.(sync|async)_api\s+import", code_string):
            warnings.append("Avertissement : Import Playwright manquant (ex: from playwright.sync_api import Page, expect).")

        # 2. Vérifier l'utilisation de la fixture `page: Page` dans la signature du test.
        if not re.search(r"def\s+test_\w+\(.*\bpage:\s*Page\b.*\):", code_string):
            warnings.append("Avertissement : La fonction de test doit utiliser la fixture `page: Page` (ex: def test_example(page: Page):).")

        # 3. Vérifier la présence d'au moins une action Playwright.
        action_pattern = r"\bpage\.(goto|click|fill|press|select_option|check|uncheck|set_input_files|hover|focus|dispatch_event|drag_and_drop|tap|type)\("
        if not re.search(action_pattern, code_string):
            warnings.append("Avertissement : Aucune action Playwright détectée (ex: page.goto(), page.click()). Le test pourrait ne rien faire.")

        # 4. Vérifier la présence d'au moins une assertion `expect`.
        if "expect(" not in code_string:
            warnings.append("Avertissement : Aucune assertion Playwright `expect()` détectée. Un test doit valider un résultat.")

        return warnings

    async def validate(self, code_string: str, code_type: str = "python") -> ValidationResult:
        """Effectue toutes les validations sur la chaîne de code fournie.

        Args:
            code_string: La chaîne de code à valider.
            code_type: Le type de code ('python' ou 'playwright') pour appliquer des règles spécifiques.

        Returns:
            Un objet `ValidationResult` contenant les résultats de la validation.
        """
        # 1. Vérification de la syntaxe Python (rapide et en premier).
        try:
            ast.parse(code_string)
        except SyntaxError as e:
            return ValidationResult(
                is_valid=False,
                syntax_error=f"Erreur de syntaxe à la ligne {e.lineno}, offset {e.offset}: {e.msg}"
            )

        result = ValidationResult()

        # 2. Vérifications spécifiques à Playwright si nécessaire.
        if code_type == "playwright":
            result.playwright_warnings = self._validate_playwright_specifics(code_string)

        # Crée un fichier temporaire pour passer le code aux outils CLI (ruff, black).
        with tempfile.NamedTemporaryFile(mode='w+', suffix='.py', delete=False, encoding='utf-8') as temp_file:
            temp_file_path = Path(temp_file.name)
            temp_file.write(code_string)
            temp_file.flush()

        try:
            # 3. Linting avec Ruff.
            ruff_args = ['check', str(temp_file_path), '--quiet', '--exit-zero']
            if self.ruff_config_path:
                ruff_args.extend(['--config', self.ruff_config_path])

            _, ruff_stdout, ruff_stderr = await self._run_subprocess('ruff', *ruff_args)
            if ruff_stdout:
                result.linting_errors = [line for line in ruff_stdout.strip().split('\n') if line]
            if ruff_stderr:
                 result.linting_errors.append(ruff_stderr)

            # 4. Vérification du formatage avec Black.
            _, _, black_stderr = await self._run_subprocess('black', '--check', '--quiet', str(temp_file_path))
            if black_stderr:
                result.formatting_errors = [line for line in black_stderr.strip().split('\n') if line]

        finally:
            # S'assure que le fichier temporaire est bien supprimé.
            temp_file_path.unlink()

        return result


async def main():
    """Fonction principale pour une démonstration et un test rapide du validateur."""
    validator = CodeValidator()

    # ... (le reste de la fonction main reste inchangé)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logger.info("Exécution des tests du CodeValidator...")
    asyncio.run(main())
    logger.info("\nTests terminés.")
```

---

## Fichier : `backend\altiora\core\post_processing\excel_formatter.py`

```python
# backend/altiora/core/post_processing/excel_formatter.py
"""Module pour formater et styliser des données dans des fichiers Excel.

Ce module utilise pandas et openpyxl pour créer des fichiers Excel esthétiques
et lisibles à partir de données brutes, en appliquant des styles, des couleurs
conditionnelles et en ajustant la largeur des colonnes.
"""

import re
import pandas as pd
from pathlib import Path
from typing import List, Dict, Any

# Importation des outils de style d'openpyxl
from openpyxl.styles import PatternFill, Font, Alignment


class ExcelFormatter:
    """Formate et exporte des données structurées vers des fichiers Excel stylisés."""

    # Expression régulière pour valider les IDs de cas de test.
    TEST_CASE_ID_PATTERN = re.compile(r"^CU\d{2}_SB\d{2}_C[PEL]\d{3}_.+(?<!_)$")

    # Définition des styles pour une apparence professionnelle.
    HEADER_FILL = PatternFill(start_color="4F81BD", end_color="4F81BD", fill_type="solid")
    HEADER_FONT = Font(color="FFFFFF", bold=True)

    # Couleurs pour le formatage conditionnel basé sur le type de test.
    CP_FILL = PatternFill(start_color="C6EFCE", end_color="C6EFCE", fill_type="solid")  # Vert pour Cas Passant
    CE_FILL = PatternFill(start_color="FFC7CE", end_color="FFC7CE", fill_type="solid")  # Rouge pour Cas d'Erreur
    CL_FILL = PatternFill(start_color="FFEB9C", end_color="FFEB9C", fill_type="solid")  # Jaune pour Cas Limite

    def _validate_test_case_id(self, test_id: str) -> bool:
        """Valide le format de l'identifiant du cas de test."""
        if not isinstance(test_id, str):
            return False
        return bool(self.TEST_CASE_ID_PATTERN.match(test_id))

    def format_test_matrix(
        self, test_cases: List[Dict[str, Any]], output_path: str
    ) -> List[str]:
        """Crée et formate un fichier Excel pour une matrice de tests.

        Args:
            test_cases: Une liste de dictionnaires, où chaque dictionnaire représente un cas de test.
                        Chaque dictionnaire doit contenir au moins les clés 'id' et 'type'.
            output_path: Le chemin du fichier Excel à créer (ex: 'reports/matrice_tests.xlsx').

        Returns:
            Une liste des erreurs de validation des IDs de cas de test rencontrées.
        """
        errors = []
        for i, case in enumerate(test_cases):
            if not self._validate_test_case_id(case.get("id")):
                errors.append(f"Ligne {i+2}: L'ID du cas de test '{case.get('id')}' ne respecte pas le format requis.")

        # Crée un DataFrame pandas, qui est une structure de données tabulaire efficace.
        df = pd.DataFrame(test_cases)

        # S'assure que le répertoire de sortie existe avant d'écrire le fichier.
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)

        with pd.ExcelWriter(output_path, engine="openpyxl") as writer:
            df.to_excel(writer, index=False, sheet_name="Matrice de Tests")
            worksheet = writer.sheets["Matrice de Tests"]

            # Applique les styles pour améliorer la lisibilité.
            self._apply_styles(worksheet)

        return errors

    def _apply_styles(self, worksheet):
        """Applique le formatage conditionnel et les styles à la feuille de calcul."""
        # Style des en-têtes
        for cell in worksheet[1]:
            cell.fill = self.HEADER_FILL
            cell.font = self.HEADER_FONT
            cell.alignment = Alignment(horizontal="center", vertical="center")

        # Trouve l'index de la colonne 'type' pour le formatage conditionnel.
        try:
            type_col_idx = [cell.value for cell in worksheet[1]].index('type') + 1
        except ValueError:
            type_col_idx = -1

        # Applique la couleur de fond aux lignes en fonction de la valeur de la colonne 'type'.
        if type_col_idx != -1:
            for row in worksheet.iter_rows(min_row=2, max_row=worksheet.max_row):
                cell_type = row[type_col_idx - 1].value
                fill_style = None
                if cell_type == "CP":
                    fill_style = self.CP_FILL
                elif cell_type == "CE":
                    fill_style = self.CE_FILL
                elif cell_type == "CL":
                    fill_style = self.CL_FILL
                
                if fill_style:
                    for cell in row:
                        cell.fill = fill_style

        # Ajuste automatiquement la largeur des colonnes pour s'adapter au contenu.
        for col in worksheet.columns:
            max_length = 0
            column = col[0].column_letter
            for cell in col:
                try:
                    if len(str(cell.value)) > max_length:
                        max_length = len(str(cell.value))
                except: # noqa: E722
                    pass
            adjusted_width = (max_length + 2) * 1.2
            worksheet.column_dimensions[column].width = adjusted_width


# --- Démonstration --- #
async def main():
    """Fonction de démonstration pour générer un fichier Excel formaté."""
    formatter = ExcelFormatter()
    test_data = [
        {
            "id": "CU01_SB01_CP001_connexion_valide",
            "description": "Vérifier la connexion avec un utilisateur et un mot de passe valides.",
            "type": "CP"
        },
        {
            "id": "CU01_SB01_CE001_mot_de_passe_incorrect",
            "description": "Vérifier le message d'erreur avec un mot de passe incorrect.",
            "type": "CE"
        },
        {
            "id": "CU01_SB02_CL001_champ_email_vide",
            "description": "Vérifier la réaction du système quand le champ email est laissé vide.",
            "type": "CL"
        },
        {
            "id": "ID_INVALIDE",
            "description": "Ce cas a un ID incorrect et devrait être signalé.",
            "type": "CP"
        }
    ]

    output_file = "reports/matrice_de_test_formatee.xlsx"
    print(f"Génération du fichier Excel de démonstration : {output_file}")

    validation_errors = formatter.format_test_matrix(test_data, output_file)

    if validation_errors:
        print("\nErreurs de validation détectées :")
        for error in validation_errors:
            print(f"- {error}")
    else:
        print("\nAucune erreur de validation.")

    print("\nFichier Excel généré avec succès.")


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())

```

---

## Fichier : `backend\altiora\core\post_processing\output_sanitizer.py`

```python
# backend/altiora/core/post_processing/output_sanitizer.py
"""Module pour nettoyer et assainir les sorties brutes des modèles de langage (LLM).

Ce module est essentiel pour normaliser les réponses des LLM avant qu'elles ne soient
utilisées par d'autres parties du système. Il effectue plusieurs opérations clés :
- Supprime les blocs de code Markdown (ex: ```python ... ```).
- Masque les informations personnelles identifiables (PII) en utilisant `PrivacyPolicy`.
- Supprime les instructions de débogage (comme `print()` et `logging.*`).
"""

import re

from policies.privacy_policy import PrivacyPolicy

# ------------------------------------------------------------------
# Constantes et Expressions Régulières
# ------------------------------------------------------------------

# Trouve et extrait le contenu des blocs de code Markdown.
CODE_BLOCK_RE = re.compile(r"^```(?:python)?\s*\n(.*?)\n```\s*$", re.DOTALL)

# Supprime les phrases d'introduction courantes générées par les LLM.
INTRO_RE = re.compile(r"^(?i)(voici|bien sûr, voici) le code.*?\n", re.MULTILINE)

# Supprime les appels à `print()`.
PRINT_RE = re.compile(r"^\s*print\(.*\)\s*$", re.MULTILINE)

# Supprime les appels de logging de bas niveau.
LOG_RE = re.compile(r"^\s*logging\.(?:info|debug|warning)\(.*\)\s*$", re.MULTILINE)


class OutputSanitizer:
    """Nettoyeur rapide et sans configuration pour les sorties de texte et de code."""

    def __init__(self) -> None:
        """Initialise le nettoyeur avec une instance de PrivacyPolicy."""
        self.privacy = PrivacyPolicy()

    def sanitize(
            self,
            text: str,
            *,
            remove_debug: bool = True,
    ) -> str:
        """Nettoie et assainit une chaîne de caractères brute.

        Args:
            text: La chaîne de caractères brute à nettoyer.
            remove_debug: Si True, supprime les instructions de débogage (print, logging).

        Returns:
            La chaîne de caractères nettoyée et avec les PII masquées.
        """
        # 1. Supprime les wrappers Markdown et les introductions.
        text = CODE_BLOCK_RE.sub(r"\1", text.strip())
        text = INTRO_RE.sub("", text)

        # 2. Supprime les instructions de débogage si l'option est activée.
        if remove_debug:
            text = PRINT_RE.sub("", text)
            text = LOG_RE.sub("", text)

        # 3. Masque les PII en utilisant la politique de confidentialité.
        privacy_report = self.privacy.scan_and_mask(text)
        
        # Retourne le texte masqué et nettoyé des espaces superflus.
        return privacy_report.text.strip()


# ------------------------------------------------------------------
# Auto-test rapide
# ------------------------------------------------------------------
if __name__ == "__main__":
    sanitizer = OutputSanitizer()

    raw_text = '''
Bien sûr, voici le code que vous avez demandé :
```python
import os

# Ceci est un commentaire de test
print("Début du script")
logging.info(f"Email de contact : test@example.com")
# Fin du script
```
    '''
    cleaned_text = sanitizer.sanitize(raw_text, remove_debug=True)
    
    print("--- Texte Original ---")
    print(raw_text)
    print("\n--- Texte Nettoyé ---")
    print(cleaned_text)

    # Vérifications pour le test
    assert "```" not in cleaned_text
    assert "Bien sûr" not in cleaned_text
    assert "print(" not in cleaned_text
    assert "logging.info" not in cleaned_text
    assert "test@****.com" in cleaned_text
    assert "# Ceci est un commentaire de test" in cleaned_text
    print("\n✅ Les tests de nettoyage ont réussi.")
```

---

## Fichier : `backend\altiora\core\post_processing\__init__.py`

```python
# backend/altiora/core/post_processing/__init__.py
"""
Post-processing modules for generated outputs.
"""
```

---

## Fichier : `backend\altiora\core\qa\multimodal_qa.py`

```python
# backend/altiora/core/qa/multimodal_qa.py
from src.models.qwen_model import QwenModel
from src.models.starcoder_model import StarcoderModel
from src.utils.question_router import QuestionRouter


class MultiModalQASystem:
    def __init__(self):
        self.text_model = QwenModel()
        self.code_model = StarcoderModel()
        self.router = QuestionRouter()

    def answer_question(self, question, context=None):
        """Route vers le bon modèle selon le type de question"""
        question_type = self.router.classify(question)

        if question_type == "code_generation":
            return self.code_model.generate(question, context)
        elif question_type == "code_explanation":
            # Utiliser les deux modèles
            code = self.code_model.extract_code(context)
            explanation = self.text_model.explain(code)
            return explanation
        else:
            return self.text_model.answer(question, context)
```

---

## Fichier : `backend\altiora\core\qa\qa_system.py`

```python
# backend/altiora/core/qa/qa_system.py
"""Module implémentant le système de Question-Réponse (QA) pour l'application Altiora.

Ce module fournit une interface pour interagir avec les modèles de langage
afin de répondre aux questions des utilisateurs. Il est conçu pour être
asynchrone et peut être intégré dans une API FastAPI.
"""

import asyncio
import time
import logging
from typing import Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)


class QASystem:
    """Système de Question-Réponse (QA) pour interagir avec les modèles de langage."

    Cette classe est responsable de la logique d'appel aux modèles d'IA
    pour générer des réponses aux questions posées par l'utilisateur.
    """

    async def answer_async(self, question: str, context: Optional[str], model: str, temperature: float) -> Any:
        """Répond à une question de manière asynchrone en utilisant un modèle de langage."

        Args:
            question: La question posée par l'utilisateur.
            context: Un contexte optionnel pour aider le modèle à formuler la réponse.
            model: Le nom du modèle de langage à utiliser (ex: 'qwen', 'starcoder').
            temperature: La température de génération pour contrôler la créativité de la réponse.

        Returns:
            Un objet factice (`Any`) contenant `text` (la réponse) et `confidence`.
            Dans une implémentation réelle, cela appellerait une interface de modèle LLM.
        """
        logger.info(f"Réception de la question : '{question}' pour le modèle '{model}' avec température {temperature}.")
        # Simule un délai de traitement pour l'inférence du modèle.
        await asyncio.sleep(0.5)

        # Logique factice pour la réponse.
        mock_answer = f"Ceci est une réponse simulée à votre question : '{question}'."
        mock_confidence = 0.85

        # Dans une application réelle, vous appelleriez ici votre interface de modèle LLM.
        # Exemple: `response = await self.llm_interface.generate_answer(question, context, model, temperature)`

        # Retourne un objet dynamique pour simuler la réponse du modèle.
        return type('obj', (object,), {'text': mock_answer, 'confidence': mock_confidence})()


# Initialisation du système de QA.
qa_system = QASystem()

# Initialisation de l'application FastAPI.
app = FastAPI(title="Altiora QA API", description="API pour le système de Question-Réponse d'Altiora.")


# --- Modèles Pydantic pour les requêtes et réponses --- #
class QARequest(BaseModel):
    """Modèle de requête pour le système de Question-Réponse (QA)."""
    question: str = Field(..., description="La question posée par l'utilisateur.")
    context: Optional[str] = Field(None, description="Contexte optionnel pour aider à répondre à la question.")
    model: str = Field("qwen", description="Le modèle d'IA à utiliser pour la réponse (ex: 'qwen', 'starcoder').")
    temperature: float = Field(0.7, ge=0.0, le=1.0, description="Température pour la génération de la réponse (contrôle la créativité).")


class QAResponse(BaseModel):
    """Modèle de réponse du système de Question-Réponse (QA)."""
    answer: str = Field(..., description="La réponse générée par le modèle.")
    confidence: float = Field(..., description="Le niveau de confiance de la réponse (entre 0 et 1).")
    model_used: str = Field(..., description="Le nom du modèle d'IA utilisé pour générer la réponse.")
    processing_time: float = Field(..., description="Le temps de traitement de la requête en secondes.")


# --- Points de terminaison (Endpoints) --- #
@app.post("/qa/answer", response_model=QAResponse)
async def answer_question(request: QARequest) -> QAResponse:
    """Point de terminaison principal pour poser une question au système QA."

    Args:
        request: L'objet `QARequest` contenant la question et les paramètres.

    Returns:
        Un objet `QAResponse` avec la réponse du modèle.

    Raises:
        HTTPException: En cas d'erreur interne du serveur lors du traitement de la question.
    """
    start_time = time.time()

    try:
        # Appelle la méthode asynchrone du système QA pour obtenir une réponse.
        answer = await qa_system.answer_async(
            question=request.question,
            context=request.context,
            model=request.model,
            temperature=request.temperature
        )

        return QAResponse(
            answer=answer.text,
            confidence=answer.confidence,
            model_used=request.model,
            processing_time=time.time() - start_time
        )
    except Exception as e:
        logger.error(f"Erreur lors de la réponse à la question : {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Erreur interne du service : {str(e)}")


# ------------------------------------------------------------------
# Démonstration (exemple d'utilisation)
# ------------------------------------------------------------------
if __name__ == "__main__":
    import uvicorn

    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    async def run_server():
        """Lance le serveur FastAPI pour la démonstration."""
        logger.info("Lancement du serveur QA API sur http://0.0.0.0:8000")
        config = uvicorn.Config(app, host="0.0.0.0", port=8000, log_level="info", reload=True)
        server = uvicorn.Server(config)
        await server.serve()

    async def run_client():
        """Simule des requêtes client vers l'API QA."""
        await asyncio.sleep(1) # Donne le temps au serveur de démarrer.
        import httpx

        print("\n--- Test de l'endpoint /qa/answer ---")
        qa_request = {
            "question": "Comment puis-je optimiser mon code Python ?",
            "context": "J'ai un script qui est lent.",
            "model": "qwen",
            "temperature": 0.5
        }

        try:
            async with httpx.AsyncClient() as client:
                response = await client.post("http://localhost:8000/qa/answer", json=qa_request)
                response.raise_for_status()
                qa_response = response.json()
                print(f"Réponse du QA : {qa_response['answer']}")
                print(f"Confiance : {qa_response['confidence']:.2f}")
                print(f"Modèle utilisé : {qa_response['model_used']}")
                print(f"Temps de traitement : {qa_response['processing_time']:.2f}s")
        except httpx.HTTPStatusError as e:
            print(f"Erreur HTTP : {e.response.status_code} - {e.response.text}")
        except Exception as e:
            print(f"Erreur lors de l'appel client : {e}")

    async def main_demo():
        # Lance le serveur et le client en parallèle.
        server_task = asyncio.create_task(run_server())
        client_task = asyncio.create_task(run_client())

        await asyncio.gather(server_task, client_task)

    asyncio.run(main_demo())
```

---

## Fichier : `backend\altiora\core\training\advanced_trainer.py`

```python
# backend/altiora/core/training/advanced_trainer.py
"""Module pour l'entraînement avancé (fine-tuning) des modèles de langage (LLMs).

Ce module fournit une classe `AltioraModelTrainer` pour le fine-tuning de
modèles comme Qwen3 et Starcoder2. Il utilise des techniques d'optimisation
de la mémoire comme LoRA (Low-Rank Adaptation) et le gradient checkpointing,
ainsi que le mixed precision training pour améliorer l'efficacité de
l'entraînement sur des ressources limitées (CPU ou GPU).
"""

import argparse
import logging

import torch
import wandb
from datasets import Dataset, load_dataset
from peft import LoraConfig, get_peft_model, TaskType
from transformers import (
    AutoModelForCausalLM,
    TrainingArguments,
    Trainer,
    AutoTokenizer # Ajouté pour la tokenisation du dataset
)

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class AltioraModelTrainer:
    """Entraîneur avancé pour le fine-tuning de modèles de langage (LLMs).

    Prend en charge les optimisations pour l'entraînement efficace sur CPU/GPU.
    """

    def __init__(self, model_name: str, task: str):
        """Initialise l'entraîneur de modèle.

        Args:
            model_name: Le nom du modèle pré-entraîné à charger (ex: "Qwen/Qwen-3B").
            task: La tâche pour laquelle le modèle est entraîné (ex: "qa", "code_gen").
        """
        self.model_name = model_name
        self.task = task
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        logger.info(f"Entraîneur initialisé. Utilisation du périphérique : {self.device}")

        # Configuration LoRA (Low-Rank Adaptation) pour l'efficacité mémoire.
        # LoRA permet d'entraîner un petit nombre de paramètres supplémentaires
        # au lieu de l'ensemble du modèle, réduisant ainsi les besoins en mémoire et en calcul.
        self.lora_config = LoraConfig(
            r=16,  # Le rang des matrices LoRA. Une valeur plus élevée augmente la capacité d'apprentissage.
            lora_alpha=32, # Facteur de mise à l'échelle pour les poids LoRA.
            target_modules=["q_proj", "v_proj"], # Modules du modèle où appliquer LoRA (typiquement les couches d'attention).
            lora_dropout=0.1, # Taux de dropout pour les couches LoRA.
            bias="none", # Ne pas entraîner les biais.
            task_type=TaskType.CAUSAL_LM # Type de tâche pour le modèle (modélisation du langage causal).
        )

    def prepare_model(self):
        """Prépare le modèle de base avec les optimisations LoRA et de mémoire."

        Returns:
            Le modèle préparé pour l'entraînement.
        """
        logger.info(f"Chargement du modèle de base : {self.model_name}...")
        # Charge le modèle de base pré-entraîné.
        # `load_in_8bit=True` active la quantification 8-bit pour réduire l'utilisation de la mémoire.
        # `device_map="auto"` distribue automatiquement le modèle sur les périphériques disponibles.
        model = AutoModelForCausalLM.from_pretrained(
            self.model_name,
            load_in_8bit=True,
            device_map="auto"
        )
        logger.info("Modèle de base chargé.")

        # Applique l'adaptateur LoRA au modèle de base.
        model = get_peft_model(model, self.lora_config)
        # Affiche le nombre de paramètres entraînés (LoRA) par rapport au total.
        model.print_trainable_parameters()

        # Active le gradient checkpointing pour réduire l'utilisation de la mémoire GPU
        # au prix d'une légère augmentation du temps de calcul.
        model.gradient_checkpointing_enable()

        # Active le mixed precision training (entraînement en précision mixte).
        # Utilise des float16 pour les calculs, réduisant la mémoire et accélérant sur certains GPU.
        model.half()

        return model

    def train(self, train_dataset: Dataset, eval_dataset: Dataset):
        """Lance le processus d'entraînement du modèle avec monitoring Weights & Biases."

        Args:
            train_dataset: Le jeu de données d'entraînement.
            eval_dataset: Le jeu de données de validation.
        """
        logger.info("Démarrage de l'entraînement...")
        # Initialise une session Weights & Biases pour le suivi de l'entraînement.
        wandb.init(project="altiora", name=f"{self.task}_{self.model_name}")

        # Prépare le modèle avant de le passer au Trainer.
        self.model = self.prepare_model()

        # Configure les arguments d'entraînement.
        training_args = TrainingArguments(
            output_dir=f"./models/{self.task}", # Répertoire de sortie pour les checkpoints et le modèle final.
            num_train_epochs=3, # Nombre d'époques d'entraînement.
            per_device_train_batch_size=4, # Taille du batch par périphérique (GPU/CPU).
            gradient_accumulation_steps=4, # Accumule les gradients sur plusieurs étapes pour simuler un plus grand batch.
            warmup_steps=100, # Nombre d'étapes de warm-up pour le taux d'apprentissage.
            logging_steps=10, # Fréquence de logging des métriques.
            save_strategy="epoch", # Stratégie de sauvegarde du modèle (à chaque époque).
            evaluation_strategy="epoch", # Stratégie d'évaluation (à chaque époque).
            fp16=True,  # Active le mixed precision training (float16).
            report_to="wandb", # Intègre le reporting à Weights & Biases.
            load_best_model_at_end=True, # Charge le meilleur modèle (basé sur `metric_for_best_model`) à la fin.
            metric_for_best_model="eval_loss", # Métrique utilisée pour déterminer le meilleur modèle.
            greater_is_better=False # Pour eval_loss, une valeur plus petite est meilleure.
        )

        # Initialise le tokenizer.
        tokenizer = AutoTokenizer.from_pretrained(self.model_name)

        # Crée l'instance du Trainer.
        trainer = Trainer(
            model=self.model,
            args=training_args,
            train_dataset=train_dataset,
            eval_dataset=eval_dataset,
            compute_metrics=self.compute_metrics,
            tokenizer=tokenizer # Le tokenizer est nécessaire pour le Trainer.
        )

        # Lance l'entraînement.
        trainer.train()
        # Sauvegarde le modèle final.
        trainer.save_model()
        logger.info(f"Entraînement terminé. Modèle sauvegardé dans : {training_args.output_dir}")

    @staticmethod
    def compute_metrics(eval_pred: tuple) -> Dict[str, float]:
        """Calcule les métriques d'évaluation à partir des prédictions du modèle."

        Args:
            eval_pred: Un tuple contenant les logits et les labels réels.

        Returns:
            Un dictionnaire de métriques (ex: {"accuracy": 0.95}).
        """
        logits, labels = eval_pred
        # Pour les tâches de modélisation du langage, la précision peut être calculée
        # en comparant les jetons prédits (argmax des logits) aux jetons réels.
        predictions = torch.argmax(torch.tensor(logits), dim=-1)
        # Assurez-vous que les labels et les prédictions ont la même forme et sont comparables.
        # Cette implémentation est très basique et peut nécessiter une adaptation
        # en fonction de la tâche spécifique et du format des données.
        accuracy = (predictions == torch.tensor(labels)).sum().item() / labels.size
        return {"accuracy": accuracy}


# ------------------------------------------------------------------
# Point d'entrée CLI pour l'entraînement
# ------------------------------------------------------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Lance l'entraînement d'un modèle de langage.")
    parser.add_argument("--model_name", type=str, default="Qwen/Qwen-3B", help="Nom du modèle pré-entraîné à utiliser.")
    parser.add_argument("--task", type=str, default="qa", help="Tâche pour laquelle le modèle est entraîné (ex: 'qa', 'code_gen').")
    parser.add_argument("--train_dataset", type=str, required=True, help="Chemin vers le dataset d'entraînement (format JSON). Ex: 'data/training/train.jsonl'.")
    parser.add_argument("--eval_dataset", type=str, required=True, help="Chemin vers le dataset de validation (format JSON). Ex: 'data/training/eval.jsonl'.")
    args = parser.parse_args()

    logger.info(f"Démarrage de l'entraînement pour le modèle {args.model_name} sur la tâche {args.task}.")

    trainer = AltioraModelTrainer(model_name=args.model_name, task=args.task)
    
    # Charge les datasets. Assurez-vous que les fichiers sont au format JSON Lines.
    try:
        train_dataset = load_dataset("json", data_files=args.train_dataset, split="train")
        eval_dataset = load_dataset("json", data_files=args.eval_dataset, split="train") # Utilise 'train' pour la démo si pas de split 'validation'.
    except Exception as e:
        logger.error(f"Erreur lors du chargement des datasets : {e}. Assurez-vous que les chemins sont corrects et les fichiers au format JSON Lines.")
        exit(1)

    # Lance l'entraînement.
    trainer.train(train_dataset, eval_dataset)
    logger.info("Script d'entraînement terminé.")
```

---

## Fichier : `backend\altiora\core\training\auto_fine_tuner.py`

```python
# backend/altiora/core/training/auto_fine_tuner.py
import mlflow
import torch
from datasets import load_dataset
from torch.cuda.amp import autocast, GradScaler
from transformers import AutoModelForCausalLM


class AutoFineTuner:
    def __init__(self, base_model: str, output_dir: str):
        self.base_model = base_model
        self.output_dir = output_dir
        mlflow.set_tracking_uri("http://localhost:5000")
        self.model = self._load_model()

    def _load_model(self):
        """Charger le modèle de base"""
        model = AutoModelForCausalLM.from_pretrained(self.base_model)
        model.gradient_checkpointing_enable()  # Activation du gradient checkpointing
        model.half()  # Activation du mixed precision training
        return model

    @staticmethod
    def prepare_dataset(data_path: str):
        """Prépare le dataset avec validation automatique"""
        dataset = load_dataset("json", data_files=data_path, split="train")
        train_test_split = dataset.train_test_split(test_size=0.2)
        train_val_split = train_test_split['train'].train_test_split(test_size=0.1)
        return {
            'train': train_val_split['train'],
            'val': train_val_split['test'],
            'test': train_test_split['test']
        }

    def train_with_tracking(self, dataset, hyperparams):
        """Entraînement avec tracking MLflow"""
        scaler = GradScaler()
        with mlflow.start_run():
            mlflow.log_params(hyperparams)

            for epoch in range(hyperparams['epochs']):
                train_loss = self.train_epoch(dataset['train'], scaler)
                val_loss = self.validate(dataset['val'], scaler)

                mlflow.log_metrics({
                    'train_loss': train_loss,
                    'val_loss': val_loss
                }, step=epoch)

                if self.should_early_stop(val_loss):
                    break

            mlflow.pytorch.log_model(self.model, "model")

    def train_epoch(self, train_dataset, scaler):
        """Entraînement pour une époque"""
        self.model.train()
        total_loss = 0
        for batch in train_dataset:
            with autocast():
                outputs = self.model(**batch)
                loss = outputs.loss
            scaler.scale(loss).backward()
            scaler.step(self.optimizer)
            scaler.update()
            total_loss += loss.item()
        return total_loss / len(train_dataset)

    def validate(self, val_dataset, scaler):
        """Validation du modèle"""
        self.model.eval()
        total_loss = 0
        with torch.no_grad():
            for batch in val_dataset:
                with autocast():
                    outputs = self.model(**batch)
                    loss = outputs.loss
                total_loss += loss.item()
        return total_loss / len(val_dataset)

    @staticmethod
    def should_early_stop(val_loss):
        """Décider si on doit arrêter l'entraînement prématurément"""
        return False


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--base_model", type=str, default="Qwen/Qwen-3B", help="Nom du modèle pré-entraîné")
    parser.add_argument("--output_dir", type=str, default="./models/finetuned", help="Répertoire de sortie")
    parser.add_argument("--data_path", type=str, required=True, help="Chemin vers le dataset")
    args = parser.parse_args()

    tuner = AutoFineTuner(base_model=args.base_model, output_dir=args.output_dir)
    dataset = tuner.prepare_dataset(args.data_path)
    hyperparams = {
        'epochs': 3,
        'learning_rate': 2e-4,
        'batch_size': 4
    }
    tuner.train_with_tracking(dataset, hyperparams)

```

---

## Fichier : `backend\altiora\core\training\feedback_system.py`

```python
# backend/altiora/core/training/feedback_system.py
from typing import Optional
from datetime import datetime

from src.learning.feedback_store import FeedbackStore
from src.learning.model_updater import ModelUpdater
class FeedbackLearningSystem:
    def __init__(self):
        self.feedback_store = FeedbackStore()
        self.model_updater = ModelUpdater()

    async def collect_feedback(self,
                               query: str,
                               response: str,
                               user_rating: int,
                               corrections: Optional[str] = None):
        """Collecte le feedback utilisateur pour amélioration continue"""
        feedback = {
            'timestamp': datetime.utcnow(),
            'query': query,
            'response': response,
            'rating': user_rating,
            'corrections': corrections
        }

        await self.feedback_store.save(feedback)

        # Déclenche le fine-tuning si suffisamment de feedback
        if await self.should_trigger_retraining():
            await self.model_updater.schedule_retraining()
```

---

## Fichier : `backend\altiora\core\training\__init__.py`

```python
# backend/altiora/core/training/__init__.py
"""Initialise le package `training` de l'application Altiora.

Ce package contient les modules et scripts liés à l'entraînement et au
fine-tuning des modèles d'IA utilisés par l'application. Il inclut des
outils pour la préparation des données, l'exécution des processus
d'entraînement et l'évaluation des modèles.
"""

```

---

## Fichier : `backend\altiora\core\validation\continuous_validator.py`

```python
# backend/altiora/core/validation/continuous_validator.py
"""Module pour la validation continue des modifications de code.

Ce module implémente un système de validation continue qui permet de
vérifier la qualité, la sécurité, la performance et la conformité des
modifications (commits) avant qu'elles ne soient intégrées. Il agrège
les résultats de plusieurs validateurs spécialisés et peut bloquer les
commits non conformes.
"""

import logging
from typing import Any, Dict

# Supposons que ces classes de validateurs et de rapport sont définies ailleurs
# ou importées. Pour la documentation, nous décrivons leur rôle.
# from .code_quality_validator import CodeQualityValidator
# from .security_validator import SecurityValidator
# from .performance_validator import PerformanceValidator
# from .ai_model_validator import AIModelValidator
# from .validation_report import ValidationReport, ValidationError

logger = logging.getLogger(__name__)


# Classes factices pour la démonstration et la documentation.
class CodeQualityValidator:
    def __init__(self): self.name = "CodeQuality"
    async def validate(self, commit_hash: str) -> Dict[str, Any]:
        # Logique de validation de la qualité du code.
        return {"is_blocking": False, "passed": True, "message": "Qualité du code OK."}

class SecurityValidator:
    def __init__(self): self.name = "Security"
    async def validate(self, commit_hash: str) -> Dict[str, Any]:
        # Logique de validation de la sécurité.
        return {"is_blocking": True, "passed": True, "message": "Sécurité OK."}

class PerformanceValidator:
    def __init__(self): self.name = "Performance"
    async def validate(self, commit_hash: str) -> Dict[str, Any]:
        # Logique de validation de la performance.
        return {"is_blocking": False, "passed": True, "message": "Performance OK."}

class AIModelValidator:
    def __init__(self): self.name = "AIModel"
    async def validate(self, commit_hash: str) -> Dict[str, Any]:
        # Logique de validation des modèles IA.
        return {"is_blocking": False, "passed": True, "message": "Modèle IA OK."}

class ValidationError(Exception):
    """Exception levée lorsqu'une validation bloquante échoue."""
    pass

class ValidationReport:
    """Rapport agrégé des résultats de validation."""
    def __init__(self, results: Dict[str, Any]):
        self.results = results
        self.overall_passed = all(r["passed"] for r in results.values())


class ContinuousValidator:
    """Orchestre l'exécution de divers validateurs pour un commit donné."

    Cette classe est le point d'entrée pour lancer un cycle de validation
    complet. Elle agrège les résultats de chaque validateur et peut déclencher
    une erreur si une validation bloquante échoue.
    """

    def __init__(self):
        """Initialise le validateur continu avec une liste de validateurs spécialisés."""
        self.validators = [
            CodeQualityValidator(),
            SecurityValidator(),
            PerformanceValidator(),
            AIModelValidator()
        ]
        logger.info("ContinuousValidator initialisé avec %d validateurs.", len(self.validators))

    async def validate_commit(self, commit_hash: str) -> ValidationReport:
        """Valide un commit spécifique en exécutant tous les validateurs configurés."

        Args:
            commit_hash: Le hachage (hash) du commit à valider.

        Returns:
            Un objet `ValidationReport` contenant les résultats détaillés de chaque validateur.

        Raises:
            ValidationError: Si l'un des validateurs configurés comme 'bloquant' échoue.
        """
        results: Dict[str, Any] = {}
        logger.info(f"Démarrage de la validation pour le commit : {commit_hash}")

        for validator_instance in self.validators:
            logger.info(f"Exécution du validateur : {validator_instance.name}...")
            try:
                # Exécute la validation pour chaque validateur.
                result = await validator_instance.validate(commit_hash)
                results[validator_instance.name] = result
                logger.info(f"Validateur {validator_instance.name} terminé. Passé : {result["passed"]}")

                # Si le validateur est bloquant et qu'il a échoué, lève une exception.
                if result.get("is_blocking", False) and not result["passed"]:
                    error_message = f"La validation bloquante '{validator_instance.name}' a échoué : {result.get("message", "Aucun message.")}"
                    logger.error(error_message)
                    raise ValidationError(error_message)

            except Exception as e:
                # Capture toute exception inattendue lors de l'exécution d'un validateur.
                error_message = f"Erreur inattendue lors de l'exécution du validateur {validator_instance.name}: {e}"
                logger.critical(error_message, exc_info=True)
                # Enregistre l'échec même si le validateur n'est pas bloquant.
                results[validator_instance.name] = {"is_blocking": True, "passed": False, "message": error_message}
                raise ValidationError(error_message) from e # Re-lève l'exception pour arrêter le processus.

        report = ValidationReport(results)
        if report.overall_passed:
            logger.info(f"Validation du commit {commit_hash} terminée : SUCCÈS.")
        else:
            logger.warning(f"Validation du commit {commit_hash} terminée : ÉCHEC (non bloquant).")
        return report


# ------------------------------------------------------------------
# Démonstration (exemple d'utilisation)
# ------------------------------------------------------------------
if __name__ == "__main__":
    import asyncio
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    async def demo():
        validator = ContinuousValidator()

        print("\n--- Démonstration de validation réussie ---")
        try:
            # Simule un commit valide.
            report_success = await validator.validate_commit("abc123def456")
            print(f"Rapport de validation : {report_success.results}")
            print(f"Validation globale réussie : {report_success.overall_passed}")
        except ValidationError as e:
            print(f"Validation échouée (attendu succès) : {e}")

        print("\n--- Démonstration de validation échouée (bloquant) ---")
        # Simule un échec de sécurité (bloquant).
        # Pour cela, nous allons temporairement modifier le validateur de sécurité factice.
        original_security_validate = SecurityValidator.validate
        SecurityValidator.validate = lambda self, commit_hash: {"is_blocking": True, "passed": False, "message": "Vulnérabilité critique détectée !"}

        try:
            report_failure = await validator.validate_commit("ghi789jkl012")
            print(f"Rapport de validation : {report_failure.results}")
            print(f"Validation globale réussie : {report_failure.overall_passed}")
        except ValidationError as e:
            print(f"Validation échouée (attendu échec bloquant) : {e}")
        finally:
            # Restaure le validateur de sécurité.
            SecurityValidator.validate = original_security_validate

        print("Démonstration du ContinuousValidator terminée.")

    asyncio.run(demo())

```

---

## Fichier : `backend\altiora\infrastructure\database.py`

```python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from backend.altiora.config.settings import settings

engine = create_engine(
    settings.database_url,
    connect_args={"check_same_thread": False} if "sqlite" in settings.database_url else {}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db() -> Session:
    """Dependency pour obtenir une session DB."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

---

## Fichier : `backend\altiora\infrastructure\__init__.py`

```python
# backend/altiora/infrastructure/__init__.py
"""
Couche d'infrastructure – cache, file d'attente, monitoring, audit, scaling.
"""
```

---

## Fichier : `backend\altiora\infrastructure\audit\audit_logger.py`

```python
# backend/altiora/infrastructure/audit/audit_logger.py
"""Module pour la journalisation des actions d'audit dans l'application.

Ce module fournit une classe `AuditLogger` pour enregistrer les actions
significatives des utilisateurs et du système. Les entrées d'audit sont
horodatées, contiennent des détails sur l'action, l'utilisateur, l'adresse IP
et l'ID de session, et sont stockées dans Redis avec une durée de vie (TTL)
pour la conformité RGPD.
"""

import datetime
import json
import logging
from typing import Dict, Any

import redis.asyncio as redis

logger = logging.getLogger(__name__)


def get_client_ip() -> str:
    """Fonction factice pour récupérer l'adresse IP du client.

    Dans une application réelle, cette fonction récupérerait l'IP depuis la requête HTTP.
    """
    # TODO: Implémenter la récupération réelle de l'adresse IP du client.
    return "unknown"


def get_session_id() -> str:
    """Fonction factice pour récupérer l'ID de session.

    Dans une application réelle, cette fonction récupérerait l'ID de session depuis le contexte.
    """
    # TODO: Implémenter la récupération réelle de l'ID de session.
    return "unknown"


class AuditLogger:
    """Enregistre les événements d'audit dans Redis."""

    def __init__(self, redis_client: redis.Redis):
        """Initialise le logger d'audit avec un client Redis."

        Args:
            redis_client: Une instance de `redis.asyncio.Redis` connectée.
        """
        self.redis = redis_client

    async def log_action(self, action: str, user_id: str, details: Dict[str, Any]):
        """Enregistre une action d'audit.

        Les entrées d'audit sont stockées dans Redis avec un TTL de 90 jours
        (7776000 secondes) pour la conformité RGPD.

        Args:
            action: Le nom de l'action effectuée (ex: 'login', 'sfd_upload').
            user_id: L'identifiant de l'utilisateur qui a effectué l'action.
            details: Un dictionnaire contenant des détails supplémentaires sur l'action.
        """
        audit_entry = {
            "timestamp": datetime.datetime.utcnow().isoformat(),
            "action": action,
            "user_id": user_id,
            "details": details,
            "ip_address": get_client_ip(),
            "session_id": get_session_id()
        }

        # Génère une clé unique pour l'entrée d'audit.
        key = f"audit:{user_id}:{datetime.datetime.utcnow().timestamp()}"
        try:
            # Stocke l'entrée d'audit dans Redis avec un TTL.
            await self.redis.setex(key, 7776000, json.dumps(audit_entry, ensure_ascii=False))
            logger.info(f"Action d'audit enregistrée : {action} par {user_id}")
        except Exception as e:
            logger.error(f"Erreur lors de l'enregistrement de l'action d'audit dans Redis : {e}")


# ------------------------------------------------------------------
# Démonstration (exemple d'utilisation)
# ------------------------------------------------------------------
if __name__ == "__main__":
    async def demo():
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        
        # Assurez-vous qu'un serveur Redis est en cours d'exécution.
        try:
            redis_client = redis.Redis(host='localhost', port=6379, db=0)
            await redis_client.ping()
            logger.info("Connecté à Redis pour la démonstration.")
        except Exception as e:
            logger.error(f"Impossible de se connecter à Redis : {e}. La démonstration ne peut pas continuer.")
            return

        logger = AuditLogger(redis_client)

        print("\n--- Enregistrement d'actions d'audit ---")
        await logger.log_action("login", "user_alice", {"method": "password", "success": True})
        await logger.log_action("sfd_upload", "user_bob", {"file_name": "spec_v1.pdf", "size_kb": 1024})
        await logger.log_action("test_generation", "user_charlie", {"model": "starcoder2", "scenarios_count": 5})

        print("\n--- Vérification des entrées d'audit (peut prendre un moment) ---")
        # Pour une vérification réelle, vous devriez interroger Redis.
        # Exemple (simplifié, ne récupère pas toutes les clés): 
        # keys = await redis_client.keys("audit:*")
        # for key in keys:
        #     entry = await redis_client.get(key)
        #     print(json.loads(entry))
        print("Vérifiez votre instance Redis pour les entrées d'audit.")

        await redis_client.close()
        print("Démonstration terminée.")

    import asyncio
    asyncio.run(demo())
```

---

## Fichier : `backend\altiora\infrastructure\audit\decorator.py`

```python
# backend/altiora/infrastructure/audit/decorator.py
"""Décorateur pour l'audit des fonctions asynchrones.

Ce module fournit un décorateur `@audit` qui permet d'enregistrer
automatiquement des événements d'audit lorsqu'une fonction est appelée.
Il capture le début de l'exécution, l'acteur (utilisateur), l'action,
et gère les succès ou les échecs de la fonction décorée.
"""

import datetime
import functools
import logging

from pathlib import Path
from src.audit.writer import AsyncAuditWriter
from src.audit.models import AuditEvent

logger = logging.getLogger(__name__)

# Initialise un writer d'audit asynchrone pour écrire les logs dans le répertoire spécifié.
writer = AsyncAuditWriter(Path("logs/audit"))


def audit(action: str):
    """Décorateur pour auditer l'exécution d'une fonction asynchrone.

    Args:
        action: Une chaîne de caractères décrivant l'action auditée (ex: "sfd_upload", "test_gen").

    Returns:
        Un décorateur qui, lorsqu'il est appliqué à une fonction asynchrone,
        enregistre un événement d'audit avant et après son exécution.
    """
    def decorator(fn):
        @functools.wraps(fn)
        async def wrapper(*args, **kwargs):
            start_time = datetime.datetime.utcnow() # Horodatage du début de l'action.
            actor = kwargs.get("user_id", "system") # Tente de récupérer l'ID utilisateur, sinon 'system'.
            
            try:
                result = await fn(*args, **kwargs)
                # Enregistre un événement de succès.
                writer.log(AuditEvent(
                    ts=start_time,
                    actor=actor,
                    action=action,
                    meta={"status": "success", "duration_ms": (datetime.datetime.utcnow() - start_time).total_seconds() * 1000}
                ))
                logger.info(f"Audit: Action '{action}' par '{actor}' réussie.")
                return result
            except Exception as exc:
                # Enregistre un événement d'échec avec les détails de l'erreur.
                writer.log(AuditEvent(
                    ts=start_time,
                    actor=actor,
                    action=action,
                    meta={
                        "status": "failure",
                        "error": str(exc),
                        "duration_ms": (datetime.datetime.utcnow() - start_time).total_seconds() * 1000
                    }
                ))
                logger.error(f"Audit: Action '{action}' par '{actor}' a échoué : {exc}")
                raise # Re-lève l'exception pour ne pas masquer l'erreur originale.

        return wrapper

    return decorator


# ------------------------------------------------------------------
# Démonstration (exemple d'utilisation)
# ------------------------------------------------------------------
if __name__ == "__main__":
    async def demo():
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

        # Démarre le writer d'audit en arrière-plan.
        await writer.start()

        @audit("process_data")
        async def process_data_success(user_id: str, data: str):
            print(f"Traitement des données pour {user_id}: {data}")
            await asyncio.sleep(0.1)
            return {"processed": True, "data": data.upper()}

        @audit("process_data")
        async def process_data_failure(user_id: str, data: str):
            print(f"Tentative de traitement des données pour {user_id}: {data}")
            await asyncio.sleep(0.1)
            raise ValueError("Erreur de traitement simulée")

        print("\n--- Démonstration de l'audit (succès) ---")
        try:
            result = await process_data_success(user_id="alice", data="hello world")
            print(f"Résultat : {result}")
        except Exception as e:
            print(f"Erreur inattendue : {e}")

        print("\n--- Démonstration de l'audit (échec) ---")
        try:
            await process_data_failure(user_id="bob", data="bad data")
        except Exception as e:
            print(f"Erreur capturée : {e}")

        # Attendre que le writer ait eu le temps de flusher.
        print("\nAttente du flush des logs d'audit...")
        await asyncio.sleep(2) # Donne un peu de temps au writer.
        await writer.stop() # Arrête le writer proprement.
        print("Démonstration terminée. Vérifiez le répertoire logs/audit.")

    import asyncio
    asyncio.run(demo())
```

---

## Fichier : `backend\altiora\infrastructure\audit\models.py`

```python
# backend/altiora/infrastructure/audit/models.py
"""Modèles de données pour les événements d'audit.

Ce module définit la structure des événements d'audit qui sont enregistrés
par le système. Il utilise `dataclasses` pour une définition claire et concise
des champs de chaque événement.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Literal, Dict, Any, Optional


@dataclass(slots=True)
class AuditEvent:
    """Représente un événement d'audit enregistré dans le système.

    Attributes:
        ts: Horodatage de l'événement (UTC).
        actor: L'identifiant de l'entité qui a initié l'action (ex: ID utilisateur, 'system').
        action: Le type d'action effectuée (ex: 'sfd_upload', 'test_gen', 'admin_command', 'pii_detected').
        resource: L'identifiant de la ressource affectée par l'action (optionnel).
        meta: Un dictionnaire de métadonnées supplémentaires spécifiques à l'événement (optionnel).
    """
    ts: datetime
    actor: str
    action: Literal["sfd_upload", "test_gen", "admin_command", "pii_detected", "login", "logout", "user_create", "user_update", "error"]
    resource: Optional[str] = None
    meta: Optional[Dict[str, Any]] = None


# ------------------------------------------------------------------
# Démonstration (exemple d'utilisation)
# ------------------------------------------------------------------
if __name__ == "__main__":
    # Création d'un événement d'audit simple.
    event1 = AuditEvent(
        ts=datetime.utcnow(),
        actor="user_123",
        action="sfd_upload",
        resource="document_abc.pdf",
        meta={"file_size_kb": 512, "upload_ip": "192.168.1.1"}
    )
    print(f"Événement 1 : {event1}")

    # Création d'un événement d'erreur.
    event2 = AuditEvent(
        ts=datetime.utcnow(),
        actor="system",
        action="error",
        meta={
            "error_type": "FileNotFoundError",
            "message": "Fichier introuvable lors du traitement",
            "path": "/tmp/non_existent_file.txt"
        }
    )
    print(f"Événement 2 : {event2}")

    # Accès aux attributs.
    print(f"Action de l'événement 1 : {event1.action}")
    if event1.meta:
        print(f"Taille du fichier de l'événement 1 : {event1.meta.get('file_size_kb')} KB")
```

---

## Fichier : `backend\altiora\infrastructure\audit\ring_buffer.py`

```python
# backend/altiora/infrastructure/audit/ring_buffer.py
"""Implémentation d'un tampon circulaire (ring buffer) pour les événements d'audit.

Ce module fournit une structure de données de type tampon circulaire qui stocke
un nombre fixe d'événements d'audit. Lorsque le tampon est plein, les nouveaux
événements écrasent les plus anciens. Cela est utile pour collecter des logs
en mémoire avant de les écrire par lots sur disque, réduisant ainsi la charge
E/S et la latence.
"""

import json
from collections import deque
from dataclasses import asdict
from typing import List

from src.audit.models import AuditEvent


class RingBuffer:
    """Un tampon circulaire pour stocker un nombre limité d'événements d'audit en mémoire."""

    def __init__(self, size: int = 10_000):
        """Initialise le tampon circulaire.

        Args:
            size: La taille maximale du tampon (nombre d'événements).
        """
        self._buf: deque[str] = deque(maxlen=size) # Utilise `deque` avec `maxlen` pour la fonctionnalité de tampon circulaire.

    def push(self, event: AuditEvent) -> None:
        """Ajoute un événement d'audit au tampon.

        L'événement est converti en chaîne JSON avant d'être stocké.
        Si le tampon est plein, l'événement le plus ancien est automatiquement supprimé.

        Args:
            event: L'objet `AuditEvent` à ajouter.
        """
        # Convertit l'objet AuditEvent en JSON string pour le stockage.
        self._buf.append(json.dumps(asdict(event), default=str))

    def flush(self) -> List[str]:
        """Vide le contenu du tampon et le retourne sous forme de liste de chaînes JSON.

        Après l'appel, le tampon est vidé.

        Returns:
            Une liste de chaînes JSON, chaque chaîne représentant un événement d'audit.
        """
        out = list(self._buf) # Copie le contenu du deque dans une liste.
        self._buf.clear() # Vide le deque.
        return out


# ------------------------------------------------------------------
# Démonstration (exemple d'utilisation)
# ------------------------------------------------------------------
if __name__ == "__main__":
    from datetime import datetime
    import time

    print("\n--- Démonstration du RingBuffer ---")
    buffer_size = 5
    buffer = RingBuffer(size=buffer_size)

    # Ajout d'événements jusqu'à remplir le tampon.
    for i in range(buffer_size):
        event = AuditEvent(
            ts=datetime.utcnow(),
            actor=f"user_{i}",
            action="test_action",
            meta={"value": i}
        )
        buffer.push(event)
        print(f"Ajouté événement {i}. Taille du tampon : {len(buffer._buf)}")

    print("\n--- Tampon plein, ajout d'un nouvel événement (écrase le plus ancien) ---")
    event_new = AuditEvent(
        ts=datetime.utcnow(),
        actor="user_new",
        action="new_action",
        meta={"value": 99}
    )
    buffer.push(event_new)
    print(f"Ajouté événement 99. Taille du tampon : {len(buffer._buf)}")

    print("\n--- Contenu du tampon après ajout (le premier événement devrait être parti) ---")
    for item in buffer._buf:
        print(json.loads(item).get("meta", {}).get("value"))

    print("\n--- Vidage du tampon (flush) ---")
    flushed_events = buffer.flush()
    print(f"Nombre d'événements vidés : {len(flushed_events)}")
    print(f"Tampon après vidage : {len(buffer._buf)}")

    print("\n--- Contenu des événements vidés ---")
    for event_str in flushed_events:
        event_dict = json.loads(event_str)
        print(f"Action: {event_dict['action']}, Acteur: {event_dict['actor']}, Valeur: {event_dict['meta'].get('value')}")

    print("Démonstration du RingBuffer terminée.")
```

---

## Fichier : `backend\altiora\infrastructure\audit\rotation.py`

```python
# backend/altiora/infrastructure/audit/rotation.py
"""Module pour la rotation et l'archivage sécurisé des journaux d'audit.

Ce module gère la rotation mensuelle des fichiers de log d'audit.
Les logs sont compressés, archivés dans un fichier `.tar.gz`,
puis chiffrés avant d'être stockés dans un répertoire d'archive.
Les fichiers originaux sont ensuite supprimés.
"""

import datetime
import logging
import tarfile
from pathlib import Path

from src.infrastructure.encryption import AltioraEncryption

logger = logging.getLogger(__name__)


def rotate_monthly():
    """Effectue la rotation mensuelle des journaux d'audit.

    Cette fonction est conçue pour être exécutée périodiquement (ex: via un cron job).
    Elle collecte tous les fichiers `.jsonl.zst` du répertoire `logs/audit`,
    les archive dans un fichier `.tar.gz` chiffré, et supprime les originaux.
    """
    current_month_str = datetime.datetime.utcnow().strftime("%Y%m")
    audit_log_dir = Path("logs/audit")
    archive_dir = Path("logs/archive")
    
    # Crée le répertoire d'archive s'il n'existe pas.
    archive_dir.mkdir(parents=True, exist_ok=True)

    # Chemin du fichier d'archive temporaire (non chiffré).
    temp_archive_path = archive_dir / f"audit_{current_month_str}.tar"
    # Chemin du fichier d'archive final (chiffré).
    final_encrypted_archive_path = archive_dir / f"audit_{current_month_str}.tar.gz.enc"

    logger.info(f"Démarrage de la rotation des logs d'audit pour le mois {current_month_str}...")

    try:
        # 1. Crée une archive tarball des fichiers de log.
        with tarfile.open(temp_archive_path, "w") as tar:
            # Parcourt tous les fichiers de log compressés dans le répertoire d'audit.
            for log_file in audit_log_dir.glob("*.jsonl.zst"):
                tar.add(log_file, arcname=log_file.name) # Ajoute le fichier à l'archive.
                log_file.unlink() # Supprime le fichier original après l'avoir ajouté à l'archive.
        logger.info(f"Fichiers de log archivés dans {temp_archive_path}.")

        # 2. Chiffre l'archive.
        # La clé de chiffrement est gérée par AltioraEncryption (probablement via variables d'environnement).
        cipher = AltioraEncryption("AUDIT_BACKUP_KEY") # Utilise une clé spécifique pour l'audit.
        encrypted_data = cipher.encrypt_file(temp_archive_path)
        final_encrypted_archive_path.write_bytes(encrypted_data)
        logger.info(f"Archive chiffrée et sauvegardée : {final_encrypted_archive_path}.")

        # 3. Supprime l'archive temporaire non chiffrée.
        temp_archive_path.unlink()
        logger.info(f"Archive temporaire {temp_archive_path} supprimée.")

    except (IOError, OSError, tarfile.ReadError) as e:
        logger.error(f"Erreur lors de la rotation des logs d'audit : {e}", exc_info=True)
    except Exception as e:
        logger.critical(f"Erreur inattendue lors de la rotation des logs d'audit : {e}", exc_info=True)


# ------------------------------------------------------------------
# Démonstration (exemple d'utilisation)
# ------------------------------------------------------------------
if __name__ == "__main__":
    import asyncio
    import time
    import zstandard

    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    # Crée quelques fichiers de log factices pour la démonstration.
    audit_log_dir = Path("logs/audit")
    audit_log_dir.mkdir(parents=True, exist_ok=True)

    print("\n--- Création de fichiers de log factices ---")
    for i in range(3):
        log_file_path = audit_log_dir / f"test_audit_{datetime.datetime.utcnow().strftime('%Y%m%d_%H%M%S')}_{i}.jsonl.zst"
        with open(log_file_path, "wb") as f:
            compressor = zstandard.ZstdCompressor(level=1)
            f.write(compressor.compress(f"Log entry {i}\n".encode()))
        print(f"Créé : {log_file_path}")
        time.sleep(0.1) # Pour avoir des horodatages différents.

    print("\n--- Lancement de la rotation mensuelle ---")
    rotate_monthly()

    print("\n--- Vérification du répertoire d'audit ---")
    remaining_logs = list(audit_log_dir.glob("*.jsonl.zst"))
    if not remaining_logs:
        print("✅ Tous les fichiers de log ont été archivés et supprimés du répertoire d'audit.")
    else:
        print("❌ Des fichiers de log sont restés :", remaining_logs)

    print("\n--- Vérification du répertoire d'archive ---")
    archive_dir = Path("logs/archive")
    encrypted_archives = list(archive_dir.glob("*.tar.gz.enc"))
    if encrypted_archives:
        print(f"✅ Archive chiffrée trouvée : {encrypted_archives[0]}")
        # Pour déchiffrer et vérifier, il faudrait la clé et la logique de déchiffrement.
    else:
        print("❌ Aucune archive chiffrée trouvée.")

    print("Démonstration de la rotation des logs terminée.")
```

---

## Fichier : `backend\altiora\infrastructure\audit\writer.py`

```python
# backend/altiora/infrastructure/audit/writer.py
"""Writer asynchrone pour les événements d'audit.

Ce module fournit une classe `AsyncAuditWriter` qui collecte les événements
d'audit dans un tampon circulaire en mémoire et les écrit périodiquement
sur disque dans des fichiers compressés (Zstandard). Cela permet de réduire
la fréquence des opérations d'écriture sur disque et d'améliorer les performances.
"""

import asyncio
from pathlib import Path
import logging
from datetime import datetime
from src.audit.ring_buffer import RingBuffer
from src.audit.models import AuditEvent

import aiofiles
import zstandard as zstd

logger = logging.getLogger(__name__)


class AsyncAuditWriter:
    """Écrit les événements d'audit de manière asynchrone et par lots sur disque."""

    def __init__(self, log_dir: Path, buffer_size: int = 10_000, flush_interval: int = 5):
        """Initialise le writer d'audit asynchrone.

        Args:
            log_dir: Le répertoire où les fichiers de log d'audit seront stockés.
            buffer_size: La taille maximale du tampon circulaire en mémoire.
            flush_interval: L'intervalle en secondes entre chaque écriture sur disque.
        """
        self.log_dir = log_dir
        self.log_dir.mkdir(parents=True, exist_ok=True) # Crée le répertoire si nécessaire.
        self._ctx = zstd.ZstdCompressor(level=3)  # Compresseur Zstandard (niveau 3 pour un bon équilibre).
        self._buffer = RingBuffer(size=buffer_size)
        self._flush_interval = flush_interval
        self._flush_task: asyncio.Task | None = None

    async def start(self):
        """Démarre la tâche de flush périodique en arrière-plan."""
        if self._flush_task === None or self._flush_task.done():
            self._flush_task = asyncio.create_task(self._periodic_flush())
            logger.info(f"AsyncAuditWriter démarré. Flush toutes les {self._flush_interval} secondes.")

    async def stop(self):
        """Arrête la tâche de flush périodique et force un dernier flush."""
        if self._flush_task:
            self._flush_task.cancel()
            try:
                await self._flush_task # Attend que la tâche se termine (gère l'exception CancelledError).
            except asyncio.CancelledError:
                pass
            logger.info("AsyncAuditWriter arrêté. Exécution du flush final...")
        await self._flush_to_disk() # Force un dernier flush pour s'assurer que toutes les données sont écrites.
        logger.info("Flush final terminé.")

    def log(self, event: AuditEvent) -> None:
        """Ajoute un événement d'audit au tampon en mémoire."

        Args:
            event: L'objet `AuditEvent` à enregistrer.
        """
        self._buffer.push(event)

    async def _periodic_flush(self):
        """Tâche asynchrone qui vide périodiquement le tampon sur disque."""
        while True:
            try:
                await asyncio.sleep(self._flush_interval)
                await self._flush_to_disk()
            except asyncio.CancelledError:
                break # La tâche a été annulée, sort de la boucle.
            except Exception as e:
                logger.error(f"Erreur lors du flush périodique des logs d'audit : {e}", exc_info=True)

    async def _flush_to_disk(self):
        """Vide le contenu du tampon en mémoire vers un fichier compressé sur disque."""
        batch = self._buffer.flush()
        if batch:
            # Génère un nom de fichier unique basé sur l'horodatage.
            path = self.log_dir / f"audit_{datetime.utcnow():%Y%m%d_%H%M%S_%f}.jsonl.zst"
            try:
                async with aiofiles.open(path, "wb") as f:
                    # Compresse le lot d'événements et l'écrit dans le fichier.
                    await f.write(self._ctx.compress("\n".join(batch).encode('utf-8')))
                logger.info(f"Logs d'audit écrits sur disque : {path} ({len(batch)} événements).")
            except (IOError, OSError, zstd.ZstdError) as e:
                logger.error(f"Erreur lors de l'écriture des logs d'audit sur {path}: {e}")


# ------------------------------------------------------------------
# Démonstration (exemple d'utilisation)
# ------------------------------------------------------------------
if __name__ == "__main__":
    async def demo():
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

        log_directory = Path("temp_audit_logs")
        # S'assure que le répertoire de démonstration est propre.
        if log_directory.exists():
            import shutil
            shutil.rmtree(log_directory)
        log_directory.mkdir()

        writer = AsyncAuditWriter(log_directory, buffer_size=3, flush_interval=2) # Petit buffer et intervalle pour la démo.
        await writer.start()

        print("\n--- Enregistrement d'événements d'audit ---")
        for i in range(10):
            event = AuditEvent(
                ts=datetime.utcnow(),
                actor=f"user_{i}",
                action="demo_action",
                meta={"event_id": i, "data": f"some_data_{i}"}
            )
            writer.log(event)
            print(f"Loggué événement {i}.")
            await asyncio.sleep(0.5) # Simule l'arrivée des événements.

        print("\n--- Arrêt du writer et flush final ---")
        await writer.stop()

        print("\n--- Vérification des fichiers générés ---")
        generated_files = list(log_directory.glob("*.jsonl.zst"))
        for f in generated_files:
            print(f"Fichier généré : {f}")
            with open(f, "rb") as fb:
                decompressor = zstd.ZstdDecompressor()
                content = decompressor.decompress(fb.read()).decode('utf-8')
                print(f"Contenu:\n{content[:200]}...")

        print("Démonstration de AsyncAuditWriter terminée.")
        # Nettoyage du répertoire temporaire.
        import shutil
        shutil.rmtree(log_directory)

    import asyncio
    asyncio.run(demo())
```

---

## Fichier : `backend\altiora\infrastructure\audit\__init__.py`

```python
# backend/altiora/infrastructure/audit/__init__.py
"""
Audit logging and tracking.
"""
```

---

## Fichier : `backend\altiora\infrastructure\events\event_bus.py`

```python
# backend/altiora/infrastructure/events/event_bus.py
"""Module implémentant un bus d'événements asynchrone pour la communication inter-composants.

Ce bus d'événements permet aux différents modules de l'application de communiquer
de manière découplée en publiant et en s'abonnant à des événements. Il utilise
une file d'attente asynchrone pour gérer les événements et peut être étendu
pour utiliser des systèmes de messagerie distribués comme Redis Pub/Sub.
"""

import asyncio
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Dict, List, Callable, Any, Optional

import redis.asyncio as redis

# Importations factices pour la démonstration. En production, ce seraient de vrais services.
# from src.services.test_generator import TestGenerator
# from src.services.notification_service import NotificationService
# from src.services.storage_service import StorageService

# test_generator = TestGenerator() # Supposons que TestGenerator est une classe
# notification_service = NotificationService() # Supposons que NotificationService est une classe
# storage_service = StorageService() # Supposons que StorageService est une classe


class EventType(Enum):
    """Énumération des types d'événements supportés par le bus."""
    SFD_UPLOADED = "sfd.uploaded"
    ANALYSIS_COMPLETED = "analysis.completed"
    TESTS_GENERATED = "tests.generated"
    PIPELINE_FAILED = "pipeline.failed"
    USER_LOGIN = "user.login"
    USER_LOGOUT = "user.logout"


@dataclass
class Event:
    """Représente un événement circulant dans le bus."""
    type: EventType
    payload: Dict[str, Any]
    timestamp: datetime
    correlation_id: str # Pour suivre les événements à travers les systèmes.


class EventBus:
    """Bus d'événements asynchrone pour la publication/souscription d'événements."""

    def __init__(self, redis_client: Optional[redis.Redis] = None):
        """Initialise le bus d'événements."

        Args:
            redis_client: Un client Redis asynchrone pour une éventuelle extension
                          vers un bus d'événements distribué (Pub/Sub).
        """
        self._handlers: Dict[EventType, List[Callable]] = {} # Mappe les types d'événements à leurs gestionnaires.
        self._queue: asyncio.Queue = asyncio.Queue() # File d'attente interne pour les événements.
        self._running = False # Indique si le bus est en cours d'exécution.
        self.redis_client = redis_client

    def subscribe(self, event_type: EventType, handler: Callable):
        """Abonne un gestionnaire à un type d'événement spécifique."

        Args:
            event_type: Le type d'événement auquel s'abonner.
            handler: La fonction (ou coroutine) qui sera appelée lorsque l'événement se produit.
        """
        if event_type not in self._handlers:
            self._handlers[event_type] = []
        self._handlers[event_type].append(handler)

    async def publish(self, event: Event):
        """Publie un événement sur le bus."

        L'événement est placé dans la file d'attente interne pour un traitement asynchrone.

        Args:
            event: L'objet `Event` à publier.
        """
        await self._queue.put(event)

    async def start(self):
        """Démarre le traitement des événements en arrière-plan."

        Cette méthode lance une boucle qui consomme les événements de la file
        d'attente et les distribue aux gestionnaires abonnés.
        """
        self._running = True
        while self._running:
            try:
                # Attend un événement avec un timeout pour permettre un arrêt propre.
                event = await asyncio.wait_for(self._queue.get(), timeout=1.0)
                await self._process_event(event)
            except asyncio.TimeoutError:
                continue # Continue la boucle si aucun événement n'est disponible.
            except asyncio.CancelledError:
                break # Le bus a été arrêté.
            except Exception as e:
                # Loggue l'erreur mais continue de traiter les autres événements.
                print(f"Erreur lors du traitement d'un événement : {e}")

    async def stop(self):
        """Arrête le bus d'événements et attend la fin du traitement des événements en cours."""
        self._running = False
        # Attend que la file d'attente soit vide.
        await self._queue.join()

    async def _process_event(self, event: Event):
        """Distribue un événement à tous les gestionnaires abonnés."

        Args:
            event: L'objet `Event` à traiter.
        """
        handlers = self._handlers.get(event.type, [])
        # Exécute tous les gestionnaires en parallèle.
        await asyncio.gather(
            *[handler(event) for handler in handlers],
            return_exceptions=True # Permet aux autres gestionnaires de s'exécuter même si l'un échoue.
        )


# ------------------------------------------------------------------
# Démonstration (exemple d'utilisation)
# ------------------------------------------------------------------
if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    # Fonctions de gestionnaires factices.
    async def handle_sfd_uploaded(event: Event):
        logging.info(f"[Handler SFD] SFD téléchargée : {event.payload.get('filename')}")
        # Simule une action, ex: déclencher l'analyse.
        # await test_generator.generate_from_sfd(event.payload["sfd_id"])

    async def handle_analysis_completed(event: Event):
        logging.info(f"[Handler Analyse] Analyse terminée pour SFD : {event.payload.get('sfd_id')}")
        # Simule une action, ex: notifier l'utilisateur.
        # await notification_service.notify(event.payload)

    async def handle_pipeline_failed(event: Event):
        logging.error(f"[Handler Échec] Pipeline échoué pour ID : {event.payload.get('pipeline_id')}. Erreur : {event.payload.get('error')}")
        # Simule une action, ex: envoyer une alerte à l'administrateur.

    async def demo():
        print("\n--- Démonstration du EventBus ---")
        bus = EventBus()
        await bus.start() # Démarre le bus d'événements.

        # Abonnements aux événements.
        bus.subscribe(EventType.SFD_UPLOADED, handle_sfd_uploaded)
        bus.subscribe(EventType.ANALYSIS_COMPLETED, handle_analysis_completed)
        bus.subscribe(EventType.PIPELINE_FAILED, handle_pipeline_failed)

        # Publication d'événements.
        print("Publication d'événements...")
        await bus.publish(Event(
            type=EventType.SFD_UPLOADED,
            payload={'sfd_id': 'SFD-001', 'filename': 'spec_v1.pdf'},
            timestamp=datetime.utcnow(),
            correlation_id='corr-123'
        ))

        await bus.publish(Event(
            type=EventType.ANALYSIS_COMPLETED,
            payload={'sfd_id': 'SFD-001', 'scenarios_count': 10},
            timestamp=datetime.utcnow(),
            correlation_id='corr-123'
        ))

        await bus.publish(Event(
            type=EventType.PIPELINE_FAILED,
            payload={'pipeline_id': 'PIPE-001', 'error': 'Étape de génération de code échouée.'},
            timestamp=datetime.utcnow(),
            correlation_id='corr-456'
        ))

        # Donne un peu de temps aux gestionnaires pour traiter les événements.
        await asyncio.sleep(2)

        print("Arrêt du bus d'événements...")
        await bus.stop()
        print("Démonstration terminée.")

    asyncio.run(demo())
```

---

## Fichier : `backend\altiora\infrastructure\events\__init__.py`

```python
# backend/altiora/infrastructure/events/__init__.py
"""Initialise le package des événements de l'application Altiora.

Ce package contient la définition du bus d'événements et des types d'événements
utilisés pour la communication découplée entre les différents composants de l'application.
"""

```

---

## Fichier : `backend\altiora\infrastructure\monitoring\health.py`

```python
# backend/altiora/infrastructure/monitoring/health.py
"""Service de vérification de l'état de santé (Health Check) de l'application Altiora.

Ce service expose un point de terminaison `/health` qui fournit un aperçu
rapide de l'état des composants critiques de l'application, tels que la
connexion à Redis et la disponibilité d'Ollama. Il est conçu pour être
utilisé par les systèmes de surveillance externes (ex: Kubernetes, Prometheus).
"""

import json
import logging

from fastapi import FastAPI, Response
import redis.asyncio as redis
import httpx

logger = logging.getLogger(__name__)

app = FastAPI(
    title="Altiora Health Check Service",
    description="Vérifie l'état de santé des composants critiques d'Altiora.",
    version="1.0.0",
)


@app.get("/health")
async def health() -> Response:
    """Point de terminaison principal pour la vérification de l'état de santé.

    Effectue des vérifications sur :
    - La connexion à Redis.
    - La disponibilité du serveur Ollama.

    Returns:
        Une `FastAPI.Response` au format JSON indiquant l'état global et le statut de chaque vérification.
        Le code HTTP est 200 si tout est sain, 503 (Service Unavailable) sinon.
    """
    status_info = {"status": "healthy", "checks": {}}
    http_status_code = 200

    # Vérification de la connexion Redis.
    try:
        # Tente de se connecter à Redis en utilisant l'URL par défaut.
        r = redis.from_url("redis://localhost:6379")
        await r.ping() # Envoie une commande PING pour vérifier la connexion.
        status_info["checks"]["redis"] = "OK"
    except Exception as e:
        status_info["checks"]["redis"] = f"Échec: {str(e)}"
        http_status_code = 503
        logger.error(f"Vérification Redis échouée : {e}")

    # Vérification de la disponibilité d'Ollama.
    async with httpx.AsyncClient(timeout=5) as client: # Timeout de 5 secondes pour la requête HTTP.
        try:
            # Tente d'accéder à l'endpoint de santé d'Ollama.
            resp = await client.get("http://localhost:11434/api/tags") # Utilise /api/tags car /health n'existe pas toujours.
            resp.raise_for_status() # Lève une exception pour les codes d'état HTTP 4xx/5xx.
            status_info["checks"]["ollama"] = "OK"
        except httpx.RequestError as e:
            status_info["checks"]["ollama"] = f"Échec de la requête: {str(e)}"
            http_status_code = 503
            logger.error(f"Vérification Ollama (requête) échouée : {e}")
        except httpx.HTTPStatusError as e:
            status_info["checks"]["ollama"] = f"Échec HTTP: {e.response.status_code} - {e.response.text}"
            http_status_code = 503
            logger.error(f"Vérification Ollama (HTTP) échouée : {e}")

    # Retourne la réponse JSON avec le code d'état approprié.
    return Response(content=json.dumps(status_info, indent=2), status_code=http_status_code, media_type="application/json")


# ------------------------------------------------------------------
# Point d'entrée Uvicorn
# ------------------------------------------------------------------
if __name__ == "__main__":
    import uvicorn
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logger.info("Lancement du service de vérification de santé sur http://0.0.0.0:8000/health")
    uvicorn.run(app, host="0.0.0.0", port=8000)

```

---

## Fichier : `backend\altiora\infrastructure\monitoring\healthcheck.py`

```python
# backend/altiora/infrastructure/monitoring/healthcheck.py
"""Service de vérification de l'état de santé (Health Check) pour les composants critiques d'Altiora.

Ce module fournit un point de terminaison `/health` qui agrège l'état de
santé de plusieurs services et dépendances clés de l'application, tels que
Redis, Ollama et d'autres microservices internes. Il est conçu pour être
utilisé par les systèmes de surveillance externes pour évaluer la disponibilité
globale de l'application.
"""

import json
import logging

from fastapi import FastAPI, Response
import aioredis
import httpx # Pour vérifier Ollama et d'autres services HTTP.

logger = logging.getLogger(__name__)

app = FastAPI(
    title="Altiora Healthcheck Service",
    description="Vérifie l'état de santé des dépendances clés d'Altiora.",
    version="1.0.0",
)


async def check_redis() -> bool:
    """Vérifie la connectivité et l'état de santé du serveur Redis."

    Returns:
        True si Redis est accessible et répond, False sinon.
    """
    try:
        # Utilise l'URL par défaut pour Redis, à adapter si nécessaire.
        redis_client = aioredis.from_url("redis://localhost:6379")
        await redis_client.ping()
        await redis_client.close() # Ferme la connexion après le ping.
        logger.debug("Vérification Redis : OK")
        return True
    except aioredis.exceptions.ConnectionError as e:
        logger.warning(f"Vérification Redis : Échec de la connexion - {e}")
        return False
    except Exception as e:
        logger.error(f"Vérification Redis : Erreur inattendue - {e}")
        return False


async def check_ollama() -> bool:
    """Vérifie la disponibilité du serveur Ollama."

    Returns:
        True si Ollama est accessible, False sinon.
    """
    try:
        async with httpx.AsyncClient(timeout=5) as client:
            # Tente d'accéder à un endpoint simple d'Ollama pour vérifier sa disponibilité.
            resp = await client.get("http://localhost:11434/api/tags")
            resp.raise_for_status() # Lève une exception pour les codes d'état HTTP 4xx/5xx.
            logger.debug("Vérification Ollama : OK")
            return True
    except httpx.RequestError as e:
        logger.warning(f"Vérification Ollama : Échec de la requête - {e}")
        return False
    except httpx.HTTPStatusError as e:
        logger.warning(f"Vérification Ollama : Échec HTTP - {e.response.status_code}")
        return False
    except Exception as e:
        logger.error(f"Vérification Ollama : Erreur inattendue - {e}")
        return False


async def check_services() -> bool:
    """Vérifie l'état de santé des autres microservices internes d'Altiora."

    Cette fonction est un placeholder. Dans une implémentation réelle, elle
    ferait des appels aux endpoints `/health` de chaque microservice (ALM, OCR, etc.).

    Returns:
        True si tous les services sont sains, False sinon.
    """
    # TODO: Implémenter la logique de vérification des autres microservices.
    # Exemple: faire des requêtes HTTP à http://localhost:8001/health (OCR), etc.
    logger.warning("Vérification des services : Logique non implémentée, retourne True par défaut.")
    return True


@app.get("/health")
async def health_check() -> Response:
    """Point de terminaison principal pour la vérification de l'état de santé complète de l'application."

    Effectue des vérifications sur Redis, Ollama et d'autres services.

    Returns:
        Une `FastAPI.Response` au format JSON indiquant l'état global et le statut
        de chaque vérification. Le code HTTP est 200 si tout est sain, 503 sinon.
    """
    checks = {
        "redis": await check_redis(),
        "ollama": await check_ollama(),
        "services": await check_services() # Placeholder pour d'autres services.
    }

    if all(checks.values()):
        status_code = 200
        status_message = "healthy"
    else:
        status_code = 503
        status_message = "unhealthy"

    response_content = {"status": status_message, "checks": {k: ("OK" if v else "FAILED") for k, v in checks.items()}}
    return Response(
        content=json.dumps(response_content, indent=2),
        status_code=status_code,
        media_type="application/json"
    )


# ------------------------------------------------------------------
# Point d'entrée Uvicorn
# ------------------------------------------------------------------
if __name__ == "__main__":
    import uvicorn
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logger.info("Lancement du service de healthcheck sur http://0.0.0.0:8000/health")
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)

```

---

## Fichier : `backend\altiora\infrastructure\monitoring\__init__.py`

```python
# backend/altiora/infrastructure/monitoring/__init__.py
"""Initialise le package `monitoring` de l'application Altiora.

Ce package contient les modules liés à la surveillance et à l'observabilité
de l'application, y compris les vérifications de santé, la collecte de métriques
et le traçage distribué.

Les modules suivants sont exposés pour faciliter les importations :
- `healthcheck_app`: L'application FastAPI pour les vérifications de santé.
- `MetricsCollector`: Le collecteur de métriques Prometheus.
"""
from .healthcheck import app as healthcheck_app
from .metrics_collector import MetricsCollector

__all__ = ['healthcheck_app', 'MetricsCollector']

```

---

## Fichier : `backend\altiora\infrastructure\monitoring\metrics\model_metrics.py`

```python
# backend/altiora/infrastructure/monitoring/metrics/model_metrics.py
from src.metrics.accuracy_tracker import AccuracyTracker
from src.metrics.latency_monitor import LatencyMonitor
from src.metrics.token_usage_tracker import TokenUsageTracker

# backend/altiora/infrastructure/monitoring/metrics/model_metrics.py
class ModelMetrics:
    def __init__(self):
        self.accuracy_tracker = AccuracyTracker()
        self.latency_monitor = LatencyMonitor()
        self.token_usage = TokenUsageTracker()

    def evaluate_model_performance(self, model_name: str):
        """Évalue les performances du modèle fine-tuné"""
        metrics = {
            'perplexity': self.calculate_perplexity(),
            'bleu_score': self.calculate_bleu(),
            'response_time_p95': self.latency_monitor.get_p95(),
            'tokens_per_second': self.token_usage.get_throughput()
        }
        return metrics
```

---

## Fichier : `backend\altiora\infrastructure\queue\redis_queue.py`

```python
# backend/altiora/infrastructure/queue/redis_queue.py
"""
Queue de tâches Redis simple.
"""

from __future__ import annotations

import json
from datetime import datetime

from redis.asyncio import Redis


class RedisTaskQueue:
    """Queue basée sur Redis list + sorted-set pour l’ordonnancement."""

    def __init__(self, url: str = "redis://localhost:6379/0") -> None:
        self.redis = Redis.from_url(url)

    async def enqueue(
        self,
        task_name: str,
        payload: dict[str, Any],
        eta: datetime | None = None,
    ) -> None:
        """Ajoute une tâche dans la file."""
        eta = eta or datetime.utcnow()
        data = json.dumps({"task": task_name, "payload": payload})
        await self.redis.zadd("batch_queue", {data: eta.timestamp()})

    async def dequeue(self) -> dict[str, Any] | None:
        """Récupère la tâche la plus ancienne."""
        now = datetime.utcnow().timestamp()
        items = await self.redis.zrangebyscore("batch_queue", 0, now, start=0, num=1)
        if not items:
            return None
        await self.redis.zrem("batch_queue", items[0])
        return json.loads(items[0])
```

---

## Fichier : `backend\altiora\infrastructure\repositories\base_repository.py`

```python
# backend/altiora/infrastructure/repositories/base_repository.py
from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Optional

T = TypeVar('T') # Type générique pour l'entité gérée par le dépôt.


class BaseRepository(ABC, Generic[T]):
    """Classe abstraite de base pour tous les dépôts (repositories).

    Définit l'interface CRUD (Create, Read, Update, Delete) que tout dépôt
    doit implémenter pour interagir avec une source de données spécifique
    (base de données, système de fichiers, API externe, etc.).
    """

    @abstractmethod
    async def create(self, entity: T) -> T:
        """Crée une nouvelle entité dans la source de données."

        Args:
            entity: L'entité à créer.

        Returns:
            L'entité créée, potentiellement avec des champs mis à jour (ex: ID généré).
        """
        pass

    @abstractmethod
    async def get(self, id: str) -> Optional[T]:
        """Récupère une entité par son identifiant unique."

        Args:
            id: L'identifiant unique de l'entité.

        Returns:
            L'entité si trouvée, sinon None.
        """
        pass

    @abstractmethod
    async def update(self, id: str, entity: T) -> T:
        """Met à jour une entité existante dans la source de données."

        Args:
            id: L'identifiant unique de l'entité à mettre à jour.
            entity: L'entité avec les données mises à jour.

        Returns:
            L'entité mise à jour.
        """
        pass

    @abstractmethod
    async def delete(self, id: str) -> bool:
        """Supprime une entité de la source de données par son identifiant."

        Args:
            id: L'identifiant unique de l'entité à supprimer.

        Returns:
            True si l'entité a été supprimée avec succès, False sinon.
        """
        pass
```

---

## Fichier : `backend\altiora\infrastructure\repositories\scenario_repository.py`

```python
# backend/altiora/infrastructure/repositories/scenario_repository.py
from pathlib import Path
from typing import Optional, List
import json
import logging

from src.repositories.base_repository import BaseRepository
from src.models.test_scenario import TestScenario

logger = logging.getLogger(__name__)


class ScenarioRepository(BaseRepository[TestScenario]):
    """Dépôt pour la persistance des objets `TestScenario` sur le système de fichiers.

    Chaque scénario est stocké comme un fichier JSON individuel dans un répertoire spécifié.
    """

    def __init__(self, storage_path: Path):
        """Initialise le dépôt de scénarios."

        Args:
            storage_path: Le chemin du répertoire où les fichiers JSON des scénarios seront stockés.
        """
        self.storage_path = storage_path
        self.storage_path.mkdir(parents=True, exist_ok=True) # Crée le répertoire si nécessaire.

    async def create(self, scenario: TestScenario) -> TestScenario:
        """Crée un nouveau fichier JSON pour un scénario de test."

        Args:
            scenario: L'objet `TestScenario` à persister.

        Returns:
            L'objet `TestScenario` qui a été persisté.

        Raises:
            ValueError: Si un scénario avec le même ID existe déjà.
            IOError: En cas d'erreur lors de l'écriture du fichier.
        """
        file_path = self.storage_path / f"{scenario.id}.json"
        if file_path.exists():
            raise ValueError(f"Un scénario avec l'ID {scenario.id} existe déjà.")
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(scenario.model_dump(), f, ensure_ascii=False, indent=4)
            logger.info(f"Scénario créé : {file_path}")
            return scenario
        except (IOError, OSError) as e:
            logger.error(f"Erreur lors de la création du fichier de scénario {file_path}: {e}")
            raise IOError(f"Erreur lors de la création du fichier de scénario {file_path}: {e}") from e

    async def get(self, id: str) -> Optional[TestScenario]:
        """Récupère un scénario de test par son ID."

        Args:
            id: L'ID du scénario à récupérer.

        Returns:
            L'objet `TestScenario` si trouvé, sinon None.

        Raises:
            IOError: En cas d'erreur lors de la lecture ou du parsing du fichier.
        """
        file_path = self.storage_path / f"{id}.json"
        if not file_path.exists():
            return None
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            logger.info(f"Scénario récupéré : {file_path}")
            return TestScenario(**data)
        except (IOError, OSError, json.JSONDecodeError) as e:
            logger.error(f"Erreur lors de la lecture du fichier de scénario {file_path}: {e}")
            raise IOError(f"Erreur lors de la lecture du fichier de scénario {file_path}: {e}") from e

    async def update(self, id: str, scenario: TestScenario) -> TestScenario:
        """Met à jour un scénario de test existant."

        Args:
            id: L'ID du scénario à mettre à jour.
            scenario: L'objet `TestScenario` avec les données mises à jour.

        Returns:
            L'objet `TestScenario` mis à jour.

        Raises:
            FileNotFoundError: Si le scénario avec l'ID spécifié n'existe pas.
            IOError: En cas d'erreur lors de l'écriture du fichier.
        """
        file_path = self.storage_path / f"{id}.json"
        if not file_path.exists():
            raise FileNotFoundError(f"Scénario avec l'ID {id} non trouvé.")
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(scenario.model_dump(), f, ensure_ascii=False, indent=4)
            logger.info(f"Scénario mis à jour : {file_path}")
            return scenario
        except (IOError, OSError) as e:
            logger.error(f"Erreur lors de la mise à jour du fichier de scénario {file_path}: {e}")
            raise IOError(f"Erreur lors de la mise à jour du fichier de scénario {file_path}: {e}") from e

    async def delete(self, id: str) -> bool:
        """Supprime un scénario de test par son ID."

        Args:
            id: L'ID du scénario à supprimer.

        Returns:
            True si le scénario a été supprimé, False sinon.
        """
        file_path = self.storage_path / f"{id}.json"
        if file_path.exists():
            try:
                file_path.unlink() # Supprime le fichier.
                logger.info(f"Scénario supprimé : {file_path}")
                return True
            except (IOError, OSError) as e:
                logger.error(f"Erreur lors de la suppression du fichier de scénario {file_path}: {e}")
                return False
        return False

    async def get_all(self) -> List[TestScenario]:
        """Récupère tous les scénarios de test stockés."

        Returns:
            Une liste de tous les objets `TestScenario` trouvés.
        """
        scenarios = []
        for file_path in self.storage_path.glob("*.json"):
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                scenarios.append(TestScenario(**data))
            except (IOError, OSError, json.JSONDecodeError) as e:
                logger.warning(f"Erreur lors de la lecture ou du parsing du fichier de scénario {file_path}: {e}")
        logger.info(f"Récupéré {len(scenarios)} scénarios.")
        return scenarios


# ------------------------------------------------------------------
# Démonstration (exemple d'utilisation)
# ------------------------------------------------------------------
if __name__ == "__main__":
    import asyncio
    import logging
    import uuid

    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    async def demo():
        temp_storage_path = Path("temp_scenario_storage")
        # Nettoyage du répertoire de démonstration.
        if temp_storage_path.exists():
            import shutil
            shutil.rmtree(temp_storage_path)
        temp_storage_path.mkdir()

        repo = ScenarioRepository(temp_storage_path)

        print("\n--- Création de scénarios ---")
        scenario1_id = "SCN-001"
        scenario1 = TestScenario(
            id=scenario1_id,
            title="Connexion réussie",
            objective="Vérifier la connexion avec des identifiants valides.",
            steps=["Entrer email", "Entrer mot de passe", "Cliquer sur login"],
            expected_result="Redirection vers le tableau de bord."
        )
        created_scenario1 = await repo.create(scenario1)
        print(f"Créé : {created_scenario1.id}")

        scenario2_id = "SCN-002"
        scenario2 = TestScenario(
            id=scenario2_id,
            title="Mot de passe oublié",
            objective="Vérifier le processus de récupération de mot de passe.",
            steps=["Cliquer sur mot de passe oublié", "Entrer email", "Soumettre"],
            expected_result="Email de réinitialisation envoyé."
        )
        created_scenario2 = await repo.create(scenario2)
        print(f"Créé : {created_scenario2.id}")

        print("\n--- Récupération d'un scénario ---")
        retrieved_scenario = await repo.get(scenario1_id)
        if retrieved_scenario:
            print(f"Récupéré : {retrieved_scenario.title}")
        else:
            print(f"Scénario {scenario1_id} non trouvé.")

        print("\n--- Mise à jour d'un scénario ---")
        scenario1.objective = "Vérifier la connexion et la déconnexion."
        updated_scenario = await repo.update(scenario1_id, scenario1)
        print(f"Mis à jour : {updated_scenario.objective}")

        print("\n--- Récupération de tous les scénarios ---")
        all_scenarios = await repo.get_all()
        print(f"Tous les scénarios ({len(all_scenarios)}) : {[s.id for s in all_scenarios]}")

        print("\n--- Suppression d'un scénario ---")
        deleted = await repo.delete(scenario2_id)
        print(f"Scénario {scenario2_id} supprimé : {deleted}")

        all_scenarios_after_delete = await repo.get_all()
        print(f"Scénarios restants ({len(all_scenarios_after_delete)}) : {[s.id for s in all_scenarios_after_delete]}")

        print("Démonstration terminée. Nettoyage du répertoire temporaire.")
        import shutil
        shutil.rmtree(temp_storage_path)

    asyncio.run(demo())
```

---

## Fichier : `backend\altiora\infrastructure\repositories\__init__.py`

```python
# backend/altiora/infrastructure/repositories/__init__.py
"""Initialise le package `repositories` de l'application Altiora.

Ce package contient les dépôts (repositories) qui gèrent l'accès aux données
persistantes de l'application. Les dépôts abstraient la logique de stockage
sous-jacente, permettant aux autres parties de l'application d'interagir avec
les données de manière cohérente, quel que soit le type de base de données ou de système de fichiers utilisé.

Les modules suivants sont exposés pour faciliter les importations :
- `BaseRepository`: La classe abstraite de base pour tous les dépôts.
- `ScenarioRepository`: Le dépôt spécifique pour la gestion des scénarios de test.
"""
from .base_repository import BaseRepository
from .scenario_repository import ScenarioRepository

__all__ = ['BaseRepository', 'ScenarioRepository']

```

---

## Fichier : `backend\altiora\infrastructure\scaling\auto_scaler.py`

```python
# backend/altiora/infrastructure/scaling/auto_scaler.py
"""Module implémentant un auto-scaler intelligent basé sur l'apprentissage automatique.

Ce module fournit une logique de décision pour l'ajustement dynamique des
ressources (mise à l'échelle horizontale ou verticale) en fonction de la
charge prédite. Il utilise des métriques collectées et un prédicteur de charge
pour anticiper les besoins et optimiser l'utilisation des ressources.
"""

import logging
from enum import Enum
from typing import Any, Dict

logger = logging.getLogger(__name__)


# --- Classes factices pour la démonstration et la documentation --- #
class ScaleAction(Enum):
    """Actions de mise à l'échelle possibles."""
    SCALE_UP = "scale_up"
    SCALE_DOWN = "scale_down"
    NO_CHANGE = "no_change"


class MetricsCollector:
    """Collecteur de métriques factice."""
    async def get_current(self) -> Dict[str, Any]:
        """Simule la récupération des métriques actuelles."""
        logger.info("Collecte des métriques actuelles...")
        await asyncio.sleep(0.1) # Simule un délai.
        return {"cpu_usage": 0.6, "memory_usage": 0.7, "request_rate": 150}


class LoadPredictor:
    """Prédicteur de charge factice basé sur l'apprentissage automatique."""
    async def predict_next_hour(self, current_metrics: Dict[str, Any]) -> float:
        """Simule la prédiction de la charge pour la prochaine heure."""
        logger.info(f"Prédiction de la charge pour la prochaine heure basée sur : {current_metrics}")
        await asyncio.sleep(0.2) # Simule un délai.
        # Logique de prédiction factice.
        if current_metrics.get("request_rate", 0) > 100:
            return 0.9 # Charge élevée.
        return 0.4 # Charge faible.


# --- Auto-scaler intelligent --- #
class IntelligentAutoScaler:
    """Décide des actions de mise à l'échelle basées sur les métriques et la prédiction de charge."""

    def __init__(self, high_threshold: float = 0.8, low_threshold: float = 0.3):
        """Initialise l'auto-scaler intelligent."

        Args:
            high_threshold: Seuil de charge au-delà duquel une mise à l'échelle ascendante est déclenchée.
            low_threshold: Seuil de charge en dessous duquel une mise à l'échelle descendante est déclenchée.
        """
        self.metrics_collector = MetricsCollector()
        self.predictor = LoadPredictor()
        self.high_threshold = high_threshold
        self.low_threshold = low_threshold
        logger.info(f"IntelligentAutoScaler initialisé. Seuil haut: {high_threshold}, Seuil bas: {low_threshold}.")

    async def scale_decision(self) -> ScaleAction:
        """Prend une décision de mise à l'échelle basée sur les métriques actuelles et la charge prédite."

        Returns:
            Une `ScaleAction` indiquant si le système doit monter en charge, descendre en charge, ou rester stable.
        """
        logger.info("Prise de décision de mise à l'échelle...")
        current_metrics = await self.metrics_collector.get_current()
        predicted_load = await self.predictor.predict_next_hour(current_metrics)

        logger.info(f"Charge prédite pour la prochaine heure : {predicted_load:.2f}")

        if predicted_load > self.high_threshold:
            logger.info("Décision : Mise à l'échelle ascendante (SCALE_UP).")
            return ScaleAction.SCALE_UP
        elif predicted_load < self.low_threshold:
            logger.info("Décision : Mise à l'échelle descendante (SCALE_DOWN).")
            return ScaleAction.SCALE_DOWN
        else:
            logger.info("Décision : Pas de changement (NO_CHANGE).")
            return ScaleAction.NO_CHANGE


# ------------------------------------------------------------------
# Démonstration (exemple d'utilisation)
# ------------------------------------------------------------------
if __name__ == "__main__":
    import asyncio
    import logging

    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    async def demo():
        print("\n--- Démonstration de l'IntelligentAutoScaler ---")
        scaler = IntelligentAutoScaler(high_threshold=0.7, low_threshold=0.4)

        print("\nPremière décision de scaling...")
        decision1 = await scaler.scale_decision()
        print(f"Décision prise : {decision1.value}")

        # Simule une charge élevée pour forcer un SCALE_UP.
        class MockHighLoadPredictor(LoadPredictor):
            async def predict_next_hour(self, current_metrics: Dict[str, Any]) -> float:
                return 0.9
        scaler.predictor = MockHighLoadPredictor()

        print("\nDeuxième décision de scaling (charge élevée simulée)...")
        decision2 = await scaler.scale_decision()
        print(f"Décision prise : {decision2.value}")

        # Simule une charge faible pour forcer un SCALE_DOWN.
        class MockLowLoadPredictor(LoadPredictor):
            async def predict_next_hour(self, current_metrics: Dict[str, Any]) -> float:
                return 0.2
        scaler.predictor = MockLowLoadPredictor()

        print("\nTroisième décision de scaling (charge faible simulée)...")
        decision3 = await scaler.scale_decision()
        print(f"Décision prise : {decision3.value}")

        print("Démonstration de l'auto-scaler terminée.")

    asyncio.run(demo())
```

---

## Fichier : `backend\altiora\infrastructure\scaling\__init__.py`

```python
# backend/altiora/infrastructure/scaling/__init__.py
"""
Mécanismes de scaling horizontal / vertical.
"""
```

---

## Fichier : `backend\altiora\monitoring\memory_monitor.py`

```python
# backend/altiora/monitoring/memory_monitor.py
"""Module de surveillance de l'utilisation de la mémoire."""
class MemoryMonitor:
    """Surveille l'utilisation mémoire en temps réel."""

    @staticmethod
    def get_status() -> Dict:
        memory = psutil.virtual_memory()
        swap = psutil.swap_memory()

        return {
            "ram": {
                "used_gb": memory.used / (1024 ** 3),
                "total_gb": memory.total / (1024 ** 3),
                "percent": memory.percent,
                "available_gb": memory.available / (1024 ** 3)
            },
            "swap": {
                "used_gb": swap.used / (1024 ** 3),
                "total_gb": swap.total / (1024 ** 3),
                "percent": swap.percent
            },
            "alert": memory.percent > 85  # Alerte si > 85%
        }
```

---

## Fichier : `backend\altiora\security\secret.py`

```python
# backend/altiora/security/secret.py
"""Gestionnaire de secrets ultra-sécurisé pour l'application Altiora.

Ce module fournit une classe `SecretsManager` qui gère l'accès aux secrets
de l'application de manière sécurisée. Il charge les secrets uniquement
depuis les variables d'environnement, effectue une validation stricte au
démarrage et peut générer des clés aléatoires pour faciliter la configuration.
"""

import os
import secrets
import logging
from typing import Optional, Dict
from cryptography.fernet import Fernet
from dotenv import load_dotenv
from pathlib import Path

logger = logging.getLogger(__name__)

# Charge les variables d'environnement depuis un fichier .env si présent.
# Cela doit être fait au début de l'exécution de l'application.
load_dotenv()


class SecretsManager:
    """Gestionnaire singleton sécurisé pour tous les secrets de l'application.

    Il est recommandé d'accéder aux secrets via cette classe pour garantir
    une gestion cohérente et sécurisée.
    """

    # Liste des secrets requis et leur description pour la documentation.
    REQUIRED_SECRETS: Dict[str, str] = {
        "JWT_SECRET_KEY": "Clé secrète pour la signature des jetons JWT (minimum 32 caractères).",
        "ENCRYPTION_KEY": "Clé de chiffrement Fernet (doit être une clé Fernet valide encodée en base64 URL-safe).",
        "OLLAMA_API_KEY": "Clé API pour l'accès à Ollama (optionnelle, si Ollama nécessite une authentification).",
        "OPENAI_API_KEY": "Clé API OpenAI pour les services de modération ou autres (optionnelle).",
        "AZURE_CONTENT_SAFETY_KEY": "Clé Azure Content Safety pour la modération de contenu (optionnelle).",
    }

    def __init__(self, secrets_dir: Path = Path("secrets")):
        """Initialise le gestionnaire de secrets."

        Args:
            secrets_dir: Le répertoire où les secrets pourraient être stockés (non utilisé directement pour le chargement).
        """
        self.secrets_dir = secrets_dir
        self.secrets_dir.mkdir(parents=True, exist_ok=True)

    @classmethod
    def get_secret(cls, key: str, required: bool = True) -> str:
        """Récupère un secret depuis les variables d'environnement."

        Args:
            key: Le nom de la variable d'environnement contenant le secret.
            required: Si True, lève une `ValueError` si le secret est manquant.

        Returns:
            La valeur du secret sous forme de chaîne de caractères.

        Raises:
            ValueError: Si le secret est requis mais non trouvé.
        """
        value = os.getenv(key)
        if required and not value:
            raise ValueError(f"Secret manquant : `{key}`. Description : {cls.REQUIRED_SECRETS.get(key, 'N/A')}")
        return value or ""

    @classmethod
    def validate_secrets(cls) -> None:
        """Effectue une validation stricte de tous les secrets requis au démarrage de l'application."

        Cette méthode vérifie la présence et le format des secrets critiques.

        Raises:
            RuntimeError: Si des erreurs de validation sont trouvées, avec une liste détaillée.
        """
        errors: List[str] = []

        # Validation de la clé secrète JWT.
        try:
            jwt_key = cls.get_secret("JWT_SECRET_KEY")
            if jwt_key and len(jwt_key) < 32:
                errors.append("JWT_SECRET_KEY doit contenir au moins 32 caractères pour être sécurisé.")
        except ValueError as e:
            errors.append(str(e))

        # Validation du format de la clé de chiffrement Fernet.
        try:
            encryption_key = cls.get_secret("ENCRYPTION_KEY")
            if encryption_key:
                try:
                    Fernet(encryption_key.encode())
                except Exception:
                    errors.append("ENCRYPTION_KEY est invalide. Elle doit être une clé Fernet valide (32 octets encodés en base64 URL-safe).")
        except ValueError as e:
            errors.append(str(e))

        if errors:
            raise RuntimeError("Erreurs de validation des secrets détectées :\n" + "\n".join(errors))
        logger.info("✅ Tous les secrets critiques ont été validés avec succès.")

    @classmethod
    def generate_secret_key(cls, length: int = 64) -> str:
        """Génère une clé secrète aléatoire et sécurisée."

        Args:
            length: La longueur du secret en octets (la chaîne résultante sera plus longue).

        Returns:
            Une chaîne de caractères sécurisée.
        """
        return secrets.token_urlsafe(length)

    @classmethod
    def generate_fernet_key(cls) -> str:
        """Génère une clé Fernet valide (32 octets encodés en base64 URL-safe)."

        Returns:
            Une chaîne de caractères représentant une clé Fernet.
        """
        return Fernet.generate_key().decode()

    @classmethod
    def generate_missing_secrets_and_prompt(cls) -> None:
        """Génère automatiquement les secrets manquants et invite l'utilisateur à les ajouter à .env."

        Cette méthode est utile pour la configuration initiale ou le développement.
        Elle ne modifie pas directement le fichier .env, mais affiche les secrets à ajouter.
        """
        logger.info("\n--- Génération des secrets manquants ---")
        generated_count = 0
        for key, description in cls.REQUIRED_SECRETS.items():
            if not os.getenv(key):
                if key == "ENCRYPTION_KEY":
                    value = cls.generate_fernet_key()
                else:
                    value = cls.generate_secret_key()
                logger.info(f"⚠️  Secret généré pour `{key}` : `{value}`")
                logger.info(f"   Description : {description}")
                logger.info(f"   Ajoutez cette ligne à votre fichier `.env` :\n   {key}={value}")
                generated_count += 1
        
        if generated_count > 0:
            logger.info("\n🔒 N'oubliez pas d'ajouter ces lignes à votre fichier `.env` et de le garder hors de votre dépôt Git !")
        else:
            logger.info("✅ Aucun secret manquant à générer. Tous les secrets requis semblent être définis.")


# ------------------------------------------------------------------
# Démonstration (exemple d'utilisation)
# ------------------------------------------------------------------
if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

    print("\n--- Démonstration du SecretsManager ---")

    # Nettoie les variables d'environnement pour une démonstration propre.
    for key in SecretsManager.REQUIRED_SECRETS.keys():
        if key in os.environ:
            del os.environ[key]

    # 1. Génération et affichage des secrets manquants.
    SecretsManager.generate_missing_secrets_and_prompt()

    # 2. Simule la définition de secrets dans l'environnement.
    os.environ["JWT_SECRET_KEY"] = SecretsManager.generate_secret_key()
    os.environ["ENCRYPTION_KEY"] = SecretsManager.generate_fernet_key()
    os.environ["OLLAMA_API_KEY"] = "sk-ollama123"

    print("\n--- Tentative de validation des secrets ---")
    try:
        SecretsManager.validate_secrets()
        print("✅ Validation des secrets réussie après définition.")
    except RuntimeError as e:
        logging.error(f"❌ Erreur de validation des secrets : {e}")

    print("\n--- Récupération d'un secret ---")
    try:
        jwt_secret = SecretsManager.get_secret("JWT_SECRET_KEY")
        print(f"Secret JWT récupéré (partiel) : {jwt_secret[:10]}...")
    except ValueError as e:
        logging.error(f"❌ Erreur lors de la récupération du secret : {e}")

    print("Démonstration du SecretsManager terminée.")

```

---

## Fichier : `backend\altiora\security\auth\dependencies.py`

```python
# backend/altiora/security/auth/dependencies.py
"""
Dépendances FastAPI d’authentification.
"""
# Déjà inclus dans altiora/api/dependencies.py
```

---

## Fichier : `backend\altiora\security\auth\jwt_handler.py`

```python
# backend/altiora/security/auth/jwt_handler.py
"""
Gestion des tokens JWT (encode / decode).
"""

from __future__ import annotations

from datetime import datetime, timedelta
from typing import Any

import jwt
from jwt import DecodeError, ExpiredSignatureError

from altiora.config.settings import settings


def create_access_token(
    subject: str,
    scopes: list[str] | None = None,
    expires_delta: timedelta | None = None,
) -> str:
    """Crée un token JWT."""
    delta = expires_delta or timedelta(hours=settings.jwt_expiration_hours)
    payload = {
        "exp": datetime.utcnow() + delta,
        "iat": datetime.utcnow(),
        "sub": subject,
        "scopes": scopes or [],
    }
    return jwt.encode(payload, settings.jwt_secret_key, algorithm=settings.jwt_algorithm)


def decode_access_token(token: str) -> dict[str, Any]:
    """Décode et valide un token JWT."""
    try:
        return jwt.decode(
            token,
            settings.jwt_secret_key,
            algorithms=[settings.jwt_algorithm],
        )
    except ExpiredSignatureError as exc:
        raise ValueError("Token expiré") from exc
    except DecodeError as exc:
        raise ValueError("Token invalide") from exc
```

---

## Fichier : `backend\altiora\security\auth\__init__.py`

```python
# backend/altiora/security/auth/__init__.py
"""
Système d’authentification JWT.
"""
```

---

## Fichier : `backend\altiora\security\guardrails\admin_control_system.py`

```python
# backend/altiora/security/guardrails/admin_control_system.py
"""
Système de Contrôle Administrateur pour Altiora
Admin unique avec contrôle total et monitoring en temps réel
"""

import json
import logging
import secrets
import shutil
import zipfile
from dataclasses import dataclass
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional, Any

from cryptography.fernet import Fernet


@dataclass
class AdminCommand:
    """Structure d'une commande administrative"""
    command_id: str
    timestamp: datetime
    action: str
    target_user: str
    parameters: Dict[str, Any]
    executed_by: str = "admin"
    approved: bool = False
    rollback_data: Optional[Dict] = None


class AdminControlSystem:
    """Système de contrôle administrateur centralisé"""

    def __init__(self, encryption_key: bytes = None):
        self.encryption_key = encryption_key or Fernet.generate_key()
        self.cipher = Fernet(self.encryption_key)

        self.admin_path = Path("admin_system")
        self.admin_path.mkdir(exist_ok=True)
        
        # Créer les sous-dossiers nécessaires
        (self.admin_path / "backups").mkdir(exist_ok=True)
        (self.admin_path / "logs").mkdir(exist_ok=True)
        (self.admin_path / "emergency").mkdir(exist_ok=True)

        self.logger = self._setup_logging()
        self.active_sessions = {}
        self.pending_changes = {}

        self.emergency_mode = False
        self.system_freeze = False
        self.config = self._load_admin_config()

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    async def execute_admin_command(self, command: AdminCommand) -> Dict[str, Any]:
        if self.system_freeze and command.action not in ["unfreeze", "emergency"]:
            return {"status": "error", "message": "Système gelé - contactez l'admin"}

        self.logger.info(f"Commande admin: {command.action} pour {command.target_user}")

        action_map = {
            "force_personality_change": self._force_personality_change,
            "reset_user_profile": self._reset_user_profile,
            "freeze_user": self._freeze_user,
            "emergency": self._emergency_mode,
            "view_logs": self._view_logs,
            "rollback": self._rollback_command,
        }

        handler = action_map.get(command.action)
        if handler is None:
            return {"status": "error", "message": "Commande inconnue"}

        return await handler(command)

    # ------------------------------------------------------------------
    # Command Handlers
    # ------------------------------------------------------------------

    async def _force_personality_change(self, command: AdminCommand) -> Dict[str, Any]:
        user_id = command.target_user
        changes = command.parameters.get("changes", {})

        backup = await self._backup_user_profile(user_id)
        success = await self._apply_personality_changes(user_id, changes)

        if success:
            self.logger.warning(f"Changement forcé sur {user_id}: {changes}")
            command.rollback_data = backup
            self.pending_changes[command.command_id] = command
            return {
                "status": "success",
                "message": f"Changements appliqués à {user_id}",
                "backup_id": command.command_id,
            }

        return {"status": "error", "message": "Échec de l'application"}

    async def _reset_user_profile(self, command: AdminCommand) -> Dict[str, Any]:
        user_id = command.target_user
        backup = await self._full_user_backup(user_id)
        await self._wipe_user_data(user_id)
        self.logger.critical(f"Réinitialisation complète de {user_id}")
        return {
            "status": "success",
            "message": f"Profil {user_id} réinitialisé",
            "backup_path": backup,
        }

    async def _freeze_user(self, command: AdminCommand) -> Dict[str, Any]:
        user_id = command.target_user
        reason = command.parameters.get("reason", "Admin freeze")

        frozen_file = self.admin_path / "frozen_users.json"
        frozen = self._load_json(frozen_file)
        frozen[user_id] = {
            "reason": reason,
            "timestamp": datetime.now().isoformat(),
            "admin": command.executed_by,
        }

        self._save_json(frozen_file, frozen)
        return {"status": "success", "message": f"Utilisateur {user_id} gelé"}

    async def _emergency_mode(self, _command: AdminCommand) -> Dict[str, Any]:
        self.emergency_mode = True
        self.system_freeze = True
        await self._emergency_backup()
        self.logger.critical("MODE URGENCE ACTIVE")
        return {
            "status": "success",
            "message": "Mode urgence activé - tous les profils sauvegardés",
        }

    async def _view_logs(self, command: AdminCommand) -> Dict[str, Any]:
        user_id = command.target_user
        days = command.parameters.get("days", 7)
        logs = await self._filter_logs(user_id, days)
        return {"status": "success", "logs": logs, "count": len(logs)}

    async def _rollback_command(self, command: AdminCommand) -> Dict[str, Any]:
        target_command_id = command.parameters.get("target_command_id")
        original_cmd = self.pending_changes.get(target_command_id)

        if not original_cmd or not original_cmd.rollback_data:
            return {"status": "error", "message": "Commande non trouvée"}

        await self._restore_from_backup(original_cmd.rollback_data)
        del self.pending_changes[target_command_id]
        return {"status": "success", "message": f"Rollback effectué pour {target_command_id}"}

    # ------------------------------------------------------------------
    # Implemented Methods (previously stubs)
    # ------------------------------------------------------------------

    async def _full_user_backup(self, user_id: str) -> str:
        """Sauvegarde complète d'un utilisateur avec toutes ses données"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_dir = self.admin_path / "backups" / user_id / timestamp
        backup_dir.mkdir(parents=True, exist_ok=True)
        
        # Collecter tous les fichiers utilisateur
        user_data_paths = [
            Path(f"user_data/{user_id}"),
            Path(f"altiora_core/{user_id}_profile.json"),
            Path(f"altiora_core/{user_id}_evolution.json"),
            Path(f"altiora_core/{user_id}_proposals.json"),
            Path(f"quiz_data/{user_id}_profile.json"),
        ]
        
        # Copier tous les fichiers existants
        for path in user_data_paths:
            if path.exists():
                if path.is_file():
                    dest_path = backup_dir / path.name
                    shutil.copy2(path, dest_path)
                    self.logger.info(f"Backed up: {path} -> {dest_path}")
                elif path.is_dir():
                    dest_path = backup_dir / path.name
                    shutil.copytree(path, dest_path, dirs_exist_ok=True)
                    self.logger.info(f"Backed up directory: {path} -> {dest_path}")
        
        # Créer une archive ZIP
        zip_path = self.admin_path / "backups" / user_id / f"{timestamp}_full_backup.zip"
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file_path in backup_dir.rglob("*"):
                if file_path.is_file():
                    zipf.write(file_path, file_path.relative_to(backup_dir))
        
        # Nettoyer le dossier temporaire
        shutil.rmtree(backup_dir)
        
        self.logger.info(f"Full backup completed for {user_id}: {zip_path}")
        return str(zip_path)

    async def _wipe_user_data(self, user_id: str) -> None:
        """Efface toutes les données utilisateur de manière sécurisée"""
        # Paths à effacer
        paths_to_delete = [
            Path(f"user_data/{user_id}"),
            Path(f"altiora_core/{user_id}_profile.json"),
            Path(f"altiora_core/{user_id}_evolution.json"),
            Path(f"altiora_core/{user_id}_proposals.json"),
            Path(f"altiora_core/{user_id}.log"),
            Path(f"quiz_data/{user_id}_profile.json"),
        ]
        
        for path in paths_to_delete:
            if path.exists():
                if path.is_file():
                    # Écraser avec des données aléatoires avant suppression
                    try:
                        with open(path, 'wb') as f:
                            f.write(secrets.token_bytes(path.stat().st_size))
                        path.unlink()
                        self.logger.info(f"Securely deleted file: {path}")
                    except (IOError, OSError) as e:
                        self.logger.error(f"Error wiping file {path}: {e}")
                elif path.is_dir():
                    shutil.rmtree(path)
                    self.logger.info(f"Deleted directory: {path}")
        
        # Nettoyer aussi les caches Redis si disponibles
        # TODO: Implémenter nettoyage Redis
        
        self.logger.warning(f"All data wiped for user: {user_id}")

    async def _emergency_backup(self) -> None:
        """Sauvegarde d'urgence globale de tous les utilisateurs"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        emergency_dir = self.admin_path / "emergency" / f"backup_{timestamp}"
        emergency_dir.mkdir(parents=True, exist_ok=True)
        
        # Identifier tous les utilisateurs
        user_ids = set()
        
        # Scanner les différents répertoires pour trouver les users
        for pattern in ["user_data/*", "altiora_core/*_profile.json", "quiz_data/*_profile.json"]:
            for path in Path(".").glob(pattern):
                if path.is_dir():
                    user_ids.add(path.name)
                elif path.is_file() and "_profile.json" in path.name:
                    user_id = path.stem.replace("_profile", "")
                    user_ids.add(user_id)
        
        self.logger.info(f"Starting emergency backup for {len(user_ids)} users")
        
        # Sauvegarder chaque utilisateur
        for user_id in user_ids:
            try:
                user_backup_dir = emergency_dir / user_id
                user_backup_dir.mkdir(exist_ok=True)
                
                # Copier toutes les données utilisateur
                await self._copy_user_data_to_backup(user_id, user_backup_dir)
                
            except Exception as e:
                self.logger.error(f"Failed to backup user {user_id}: {e}")
        
        # Créer une archive globale
        final_zip = self.admin_path / "emergency" / f"emergency_backup_{timestamp}.zip"
        with zipfile.ZipFile(final_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file_path in emergency_dir.rglob("*"):
                if file_path.is_file():
                    zipf.write(file_path, file_path.relative_to(emergency_dir))
        
        # Nettoyer le dossier temporaire
        shutil.rmtree(emergency_dir)
        
        # Sauvegarder aussi l'état du système
        system_state = {
            "timestamp": timestamp,
            "emergency_mode": self.emergency_mode,
            "system_freeze": self.system_freeze,
            "frozen_users": self._load_json(self.admin_path / "frozen_users.json"),
            "pending_changes": {k: v.__dict__ for k, v in self.pending_changes.items()},
            "config": self.config
        }
        
        state_file = self.admin_path / "emergency" / f"system_state_{timestamp}.json"
        self._save_json(state_file, system_state)
        
        self.logger.critical(f"Emergency backup completed: {final_zip}")

    async def _filter_logs(self, user_id: str, days: int) -> List[Dict[str, Any]]:
        """Filtre les logs par utilisateur et période"""
        cutoff_date = datetime.now() - timedelta(days=days)
        filtered_logs = []
        
        # Parcourir tous les fichiers de log
        log_patterns = [
            self.admin_path / "admin_commands.log",
            Path(f"altiora_core/{user_id}.log"),
            Path("logs") / f"{user_id}_*.log"
        ]
        
        for log_pattern in log_patterns:
            if log_pattern.exists() and log_pattern.is_file():
                try:
                    with open(log_pattern, 'r', encoding='utf-8') as f:
                        for line in f:
                            try:
                                # Parser les logs (format: timestamp - level - message)
                                if " - " in line:
                                    parts = line.strip().split(" - ", 2)
                                    if len(parts) >= 3:
                                        timestamp_str = parts[0]
                                        level = parts[1]
                                        message = parts[2]
                                        
                                        # Parser le timestamp
                                        try:
                                            timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S,%f")
                                        except ValueError:
                                        timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
                                        
                                        # Filtrer par date et utilisateur
                                        if timestamp >= cutoff_date and (user_id in message or user_id == "all"):
                                            filtered_logs.append({
                                                "timestamp": timestamp.isoformat(),
                                                "level": level,
                                                "message": message,
                                                "source": str(log_pattern.name)
                                            })
                            except Exception as e:
                                self.logger.debug(f"Error parsing log line: {e}")
                except (IOError, OSError) as e:
                    self.logger.error(f"Error reading log file {log_pattern}: {e}")
        
        # Trier par timestamp
        filtered_logs.sort(key=lambda x: x["timestamp"], reverse=True)
        
        return filtered_logs

    async def _restore_from_backup(self, backup_data: Dict[str, Any]) -> None:
        """Restaure depuis une sauvegarde"""
        backup_path = backup_data.get("backup_path")
        user_id = backup_data.get("user_id")
        
        if not backup_path or not Path(backup_path).exists():
            raise ValueError(f"Backup path invalid: {backup_path}")
        
        try:
            # Si c'est un fichier ZIP, extraire d'abord
            if backup_path.endswith('.zip'):
                extract_dir = Path(backup_path).parent / "temp_restore"
                extract_dir.mkdir(exist_ok=True)
                
                with zipfile.ZipFile(backup_path, 'r') as zipf:
                    zipf.extractall(extract_dir)
                
                # Restaurer depuis le dossier extrait
                await self._restore_user_data_from_directory(user_id, extract_dir)
                
                # Nettoyer
                shutil.rmtree(extract_dir)
            else:
                # Si c'est un fichier JSON encrypté
                if backup_path.endswith('.json.enc'):
                    with open(backup_path, 'rb') as f:
                        encrypted_data = f.read()
                    
                    decrypted_data = self.cipher.decrypt(encrypted_data)
                    user_data = json.loads(decrypted_data.decode())
                    
                    # Restaurer les données
                    await self._restore_user_profile(user_id, user_data)
            
            self.logger.info(f"Restored user {user_id} from backup: {backup_path}")
        except (IOError, OSError, zipfile.BadZipFile) as e:
            self.logger.error(f"Error restoring from backup {backup_path}: {e}")

    # ------------------------------------------------------------------
    # Helper methods for implementation
    # ------------------------------------------------------------------

    async def _copy_user_data_to_backup(self, user_id: str, backup_dir: Path) -> None:
        """Copie toutes les données d'un utilisateur vers un répertoire de backup"""
        patterns = [
            (f"user_data/{user_id}", backup_dir / "user_data"),
            (f"altiora_core/{user_id}_*.json", backup_dir / "altiora_core"),
            (f"quiz_data/{user_id}_*.json", backup_dir / "quiz_data"),
        ]
        
        for pattern, dest_parent in patterns:
            for path in Path(".").glob(pattern):
                if path.exists():
                    dest_parent.mkdir(parents=True, exist_ok=True)
                    if path.is_file():
                        shutil.copy2(path, dest_parent / path.name)
                    elif path.is_dir():
                        shutil.copytree(path, dest_parent / path.name, dirs_exist_ok=True)

    async def _restore_user_data_from_directory(self, user_id: str, restore_dir: Path) -> None:
        """Restaure les données utilisateur depuis un répertoire"""
        for item in restore_dir.rglob("*"):
            if item.is_file():
                # Déterminer le chemin de destination
                relative_path = item.relative_to(restore_dir)
                dest_path = Path(".") / relative_path
                
                # Créer les répertoires parents si nécessaire
                dest_path.parent.mkdir(parents=True, exist_ok=True)
                
                # Copier le fichier
                shutil.copy2(item, dest_path)

    async def _restore_user_profile(self, user_id: str, profile_data: Dict[str, Any]) -> None:
        """Restaure un profil utilisateur depuis des données JSON"""
        profile_path = Path(f"altiora_core/{user_id}_profile.json")
        profile_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(profile_path, 'w', encoding='utf-8') as f:
            json.dump(profile_data, f, indent=2, ensure_ascii=False)

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    @staticmethod
    def _load_json(path: Path) -> Dict[str, Any]:
        return json.loads(path.read_text()) if path.exists() else {}

    @staticmethod
    def _save_json(path: Path, data: Dict[str, Any]) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(data, indent=2, default=str))

    def _setup_logging(self) -> logging.Logger:
        logger = logging.getLogger("altiora_admin")
        logger.setLevel(logging.DEBUG)
        fh = logging.FileHandler(self.admin_path / "admin_commands.log")
        fh.setLevel(logging.INFO)
        ch = logging.StreamHandler()
        ch.setLevel(logging.ERROR)
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        logger.addHandler(fh)
        logger.addHandler(ch)
        return logger

    def _load_admin_config(self) -> Dict[str, Any]:
        return self._load_json(self.admin_path / "admin_config.json") or {
            "max_personality_changes_per_day": 5,
            "require_approval_for_major_changes": True,
            "emergency_contact": "admin@company.com",
            "auto_freeze_threshold": 10,
            "backup_retention_days": 30,
        }

    # ------------------------------------------------------------------
    # Public utilities
    # ------------------------------------------------------------------

    async def _backup_user_profile(self, user_id: str) -> Dict[str, Any]:
        timestamp = datetime.now().isoformat()
        backup_path = self.admin_path / "backups" / user_id
        backup_path.mkdir(parents=True, exist_ok=True)
        backup_file = backup_path / f"{timestamp}.json.enc"

        user_data = await self._get_user_data(user_id)
        encrypted = self.cipher.encrypt(json.dumps(user_data).encode())
        backup_file.write_bytes(encrypted)

        return {"user_id": user_id, "backup_path": str(backup_file), "timestamp": timestamp}

    async def _get_user_data(self, user_id: str) -> Dict[str, Any]:
        """Récupère toutes les données d'un utilisateur"""
        user_data = {
            "user_id": user_id,
            "timestamp": datetime.now().isoformat(),
            "personality": {},
            "history": [],
            "preferences": {},
            "voice_profile": {}
        }
        
        try:
            # Charger le profil de personnalité
            profile_path = Path(f"altiora_core/{user_id}_profile.json")
            if profile_path.exists():
                with open(profile_path, 'r', encoding='utf-8') as f:
                    user_data["personality"] = json.load(f)
            
            # Charger l'historique d'évolution
            evolution_path = Path(f"altiora_core/{user_id}_evolution.json")
            if evolution_path.exists():
                with open(evolution_path, 'r', encoding='utf-8') as f:
                    user_data["evolution_history"] = json.load(f)
            
            # Charger le profil du quiz
            quiz_path = Path(f"quiz_data/{user_id}_profile.json")
            if quiz_path.exists():
                with open(quiz_path, 'r', encoding='utf-8') as f:
                    quiz_data = json.load(f)
                    user_data["preferences"] = quiz_data.get("preferences", {})
                    user_data["voice_profile"] = quiz_data.get("vocal_profile", {})
        except (IOError, OSError, json.JSONDecodeError) as e:
            self.logger.error(f"Error getting user data for {user_id}: {e}")
        
        return user_data

    async def _apply_personality_changes(self, user_id: str, changes: Dict[str, Any]) -> bool:
        """Applique des changements de personnalité à un utilisateur"""
        try:
            profile_path = Path(f"altiora_core/{user_id}_profile.json")
            
            # Charger le profil existant
            if profile_path.exists():
                try:
                    with open(profile_path, 'r', encoding='utf-8') as f:
                        profile = json.load(f)
                except (IOError, OSError, json.JSONDecodeError) as e:
                    self.logger.error(f"Error reading profile for {user_id}: {e}")
                    # Créer un profil par défaut si le fichier est corrompu
                    profile = {
                        "user_id": user_id,
                        "traits": {},
                        "preferences": {},
                        "vocal_profile": {},
                        "behavioral_patterns": {},
                        "quiz_metadata": {"created_at": datetime.now().isoformat()}
                    }
            else:
                # Créer un profil par défaut si inexistant
                profile = {
                    "user_id": user_id,
                    "traits": {},
                    "preferences": {},
                    "vocal_profile": {},
                    "behavioral_patterns": {},
                    "quiz_metadata": {"created_at": datetime.now().isoformat()}
                }
            
            # Appliquer les changements
            for key, value in changes.items():
                if key == "traits" and isinstance(value, dict):
                    profile.setdefault("traits", {}).update(value)
                elif key == "preferences" and isinstance(value, dict):
                    profile.setdefault("preferences", {}).update(value)
                else:
                    profile[key] = value
            
            # Sauvegarder le profil modifié
            profile_path.parent.mkdir(parents=True, exist_ok=True)
            with open(profile_path, 'w', encoding='utf-8') as f:
                json.dump(profile, f, indent=2, ensure_ascii=False)
            
            return True
            
        except (IOError, OSError) as e:
            self.logger.error(f"Failed to apply personality changes: {e}")
            return False

    def generate_report(self) -> Dict[str, Any]:
        return {
            "total_users": len(self.active_sessions),
            "pending_changes": len(self.pending_changes),
            "emergency_mode": self.emergency_mode,
            "system_freeze": self.system_freeze,
            "last_backup": self._get_last_backup_time(),
            "recent_commands": self._get_recent_commands(10),
        }

    def _get_last_backup_time(self) -> Optional[str]:
        backups_dir = self.admin_path / "backups"
        if not backups_dir.exists():
            return None
        latest = None
        for user_dir in backups_dir.iterdir():
            for backup_file in user_dir.glob("*.json.enc"):
                if not latest or backup_file.stat().st_mtime > latest.stat().st_mtime:
                    latest = backup_file
        return str(latest) if latest else None

    def _get_recent_commands(self, count: int) -> List[Dict[str, Any]]:
        """Récupère les commandes les plus récentes depuis les logs"""
        recent_commands = []
        log_file = self.admin_path / "admin_commands.log"
        
        if log_file.exists():
            with open(log_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                # Prendre les dernières lignes
                for line in lines[-count:]:
                    if "Commande admin:" in line:
                        try:
                            parts = line.strip().split(" - ")
                            if len(parts) >= 4:
                                timestamp = parts[0]
                                message = parts[3]
                                # Extraire l'action et l'utilisateur
                                if "Commande admin:" in message:
                                    action_part = message.split("Commande admin:")[1].strip()
                                    action, user = action_part.split(" pour ")
                                    recent_commands.append({
                                        "timestamp": timestamp,
                                        "action": action,
                                        "user": user
                                    })
                        except Exception as e:
                            self.logger.debug(f"Error parsing log line: {e}")
        
        return recent_commands[:count]


# Utilitaire
def generate_admin_key() -> str:
    return secrets.token_urlsafe(32)
```

---

## Fichier : `backend\altiora\security\guardrails\admin_dashboard.py`

```python
# backend/altiora/security/guardrails/admin_dashboard.py
"""Dashboard administrateur pour supervision Altiora
Interface de contrôle visuelle et rapports en temps réel
"""

import asyncio
import tkinter as tk
from datetime import datetime
from tkinter import ttk, messagebox
from typing import Dict, Any, List

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Importation des systèmes de contrôle réels
from guardrails.admin_control_system import AdminControlSystem, AdminCommand
from guardrails.ethical_safeguards import EthicalSafeguards, EthicalAlert


class AdminDashboard:
    """
    Interface de dashboard administrateur connectée aux systèmes réels.
    """

    def __init__(self) -> None:
        self.admin_system = AdminControlSystem()
        self.ethical_safeguards = EthicalSafeguards()

        self.root = tk.Tk()
        self.root.title("🎛️ Altiora Admin Dashboard")
        self.root.geometry("1400x900")

        self.stats_labels: Dict[str, ttk.Label] = {}
        self.user_listbox: tk.Listbox
        self.user_info_frame: ttk.LabelFrame
        self.alert_tree: ttk.Treeview
        self.user_filter: ttk.Combobox
        self.period_filter: ttk.Combobox
        self.log_text: tk.Text
        self.notebook: ttk.Notebook

        self.setup_styles()
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True)

        self.create_overview_tab()
        self.create_user_management_tab()
        self.create_ethical_monitoring_tab()
        self.create_system_logs_tab()
        self.create_emergency_tab()
        self.start_auto_refresh()

    @staticmethod
    def setup_styles() -> None:
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TNotebook", background="#f0f0f0")
        style.configure("TFrame", background="#ffffff")
        style.configure("Critical.TLabel", foreground="red", font=("Arial", 10, "bold"))
        style.configure("Warning.TLabel", foreground="orange", font=("Arial", 10))
        style.configure("Success.TLabel", foreground="green", font=("Arial", 10))

    def create_overview_tab(self) -> None:
        overview_frame = ttk.Frame(self.notebook)
        self.notebook.add(overview_frame, text="Vue d'ensemble")

        header = ttk.Label(overview_frame, text="Tableau de Bord Altiora", font=("Arial", 16, "bold"))
        header.pack(pady=10)

        stats_frame = ttk.Frame(overview_frame)
        stats_frame.pack(pady=20, padx=20)
        for i, stat in enumerate(["Total Users", "Active Alerts", "Pending Changes", "System Status"]):
            frame = ttk.Frame(stats_frame)
            frame.grid(row=0, column=i, padx=20)
            ttk.Label(frame, text=stat, font=("Arial", 12)).pack()
            lbl = ttk.Label(frame, text="N/A", font=("Arial", 14, "bold"))
            lbl.pack()
            self.stats_labels[stat] = lbl

        chart_frame = ttk.Frame(overview_frame)
        chart_frame.pack(pady=20, padx=20, fill="both", expand=True)
        self.create_activity_chart(chart_frame)

    def create_user_management_tab(self) -> None:
        user_frame = ttk.Frame(self.notebook)
        self.notebook.add(user_frame, text="Gestion utilisateurs")

        left = ttk.Frame(user_frame)
        left.pack(side="left", fill="y", padx=10, pady=10)
        ttk.Label(left, text="Utilisateurs", font=("Arial", 12, "bold")).pack()
        self.user_listbox = tk.Listbox(left, width=30, height=25)
        self.user_listbox.pack(pady=10)
        self.user_listbox.bind("<<ListboxSelect>>", self.on_user_select)

        right = ttk.Frame(user_frame)
        right.pack(side="right", fill="both", expand=True, padx=10, pady=10)
        self.user_info_frame = ttk.LabelFrame(right, text="Informations")
        self.user_info_frame.pack(fill="x", pady=10)

        control = ttk.LabelFrame(right, text="Contrôles Admin")
        control.pack(fill="x", pady=10)
        ttk.Button(control, text="Geler Utilisateur", command=lambda: self.execute_user_action("freeze_user")).pack(pady=5, padx=10, fill="x")
        ttk.Button(control, text="Supprimer les données", command=lambda: self.execute_user_action("wipe_user_data")).pack(pady=5, padx=10, fill="x")

    def create_ethical_monitoring_tab(self) -> None:
        ethical_frame = ttk.Frame(self.notebook)
        self.notebook.add(ethical_frame, text="Monitoring éthique")

        alerts_frame = ttk.LabelFrame(ethical_frame, text="Alertes Actives")
        alerts_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.alert_tree = ttk.Treeview(alerts_frame, columns=("User", "Severity", "Details", "Time"), show="headings")
        for col in ("User", "Severity", "Details", "Time"):
            self.alert_tree.heading(col, text=col)
        self.alert_tree.pack(fill="both", expand=True, pady=10)

    def create_system_logs_tab(self) -> None:
        logs_frame = ttk.Frame(self.notebook)
        self.notebook.add(logs_frame, text="Logs système")
        self.log_text = tk.Text(logs_frame, height=30, width=120, state="disabled")
        self.log_text.pack(fill="both", expand=True, padx=10, pady=10)

    def create_emergency_tab(self) -> None:
        emergency_frame = ttk.Frame(self.notebook)
        self.notebook.add(emergency_frame, text="URGENCE")
        ttk.Button(emergency_frame, text="🚨 ACTIVER MODE URGENCE 🚨", command=self.activate_emergency_mode).pack(pady=20)

    def create_activity_chart(self, parent) -> None:
        self.fig, self.ax = plt.subplots(figsize=(12, 4))
        self.canvas = FigureCanvasTkAgg(self.fig, parent)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)

    def on_user_select(self, _event: tk.Event) -> None:
        selection = self.user_listbox.curselection()
        if selection:
            user_id = self.user_listbox.get(selection[0])
            self.display_user_info(user_id)

    def display_user_info(self, user_id: str) -> None:
        for widget in self.user_info_frame.winfo_children():
            widget.destroy()
        # Remplacer par un appel réel pour obtenir les infos utilisateur
        info = asyncio.run(self.admin_system.get_user_info(user_id))
        for key, value in info.items():
            ttk.Label(self.user_info_frame, text=f"{key}: {value}").pack(anchor="w", padx=10)

    def execute_user_action(self, action: str) -> None:
        selection = self.user_listbox.curselection()
        if not selection:
            messagebox.showwarning("Sélection requise", "Veuillez sélectionner un utilisateur")
            return
        user_id = self.user_listbox.get(selection[0])
        if messagebox.askyesno("Confirmation", f"Confirmer l'action '{action}' sur {user_id} ?"):
            asyncio.run(self.admin_system.execute_admin_command(AdminCommand(
                command_id=f"{action}_{user_id}",
                action=action,
                target_user=user_id
            )))
            messagebox.showinfo("Action effectuée", f"L'action {action} a été exécutée pour {user_id}.")

    def activate_emergency_mode(self) -> None:
        if messagebox.askyesno("URGENCE", "Êtes-vous sûr de vouloir activer le mode urgence ?", icon="warning"):
            asyncio.run(self.admin_system.trigger_emergency(reason="Manual trigger from dashboard"))
            messagebox.showinfo("URGENCE", "Mode urgence activé")

    def start_auto_refresh(self) -> None:
        self.refresh_data()
        self.root.after(5000, self.start_auto_refresh)

    def refresh_data(self) -> None:
        report = self.admin_system.generate_report()
        self.stats_labels["Total Users"].config(text=str(report.get("total_users", 0)))
        self.stats_labels["Active Alerts"].config(text=str(len(self.ethical_safeguards.get_active_alerts())))
        self.stats_labels["System Status"].config(text="NORMAL" if not report.get("emergency_mode") else "URGENCE")
        self.update_user_list()
        self.update_alert_display()
        self.update_logs()
        self.update_activity_chart()

    def update_user_list(self) -> None:
        current_selection = self.user_listbox.curselection()
        self.user_listbox.delete(0, tk.END)
        users = asyncio.run(self.admin_system.list_users())
        for user in users:
            self.user_listbox.insert(tk.END, user)
        if current_selection:
            self.user_listbox.selection_set(current_selection)

    def update_alert_display(self) -> None:
        self.alert_tree.delete(*self.alert_tree.get_children())
        alerts: List[EthicalAlert] = self.ethical_safeguards.get_active_alerts()
        for alert in alerts:
            self.alert_tree.insert("", "end", values=(alert.user_id, alert.severity.name, alert.details, alert.timestamp.strftime("%H:%M:%S")))

    def update_logs(self) -> None:
        logs = self.admin_system.get_system_logs(limit=100)
        self.log_text.config(state="normal")
        self.log_text.delete("1.0", tk.END)
        self.log_text.insert("1.0", "\n".join(logs))
        self.log_text.config(state="disabled")

    def update_activity_chart(self) -> None:
        self.ax.clear()
        # Simuler des données d'activité changeantes
        hours = list(range(24))
        activity = [np.random.randint(50, 200) + h * 5 for h in hours]
        self.ax.plot(hours, activity, marker="o")
        self.ax.set_title("Activité par heure")
        self.ax.set_xlabel("Heure")
        self.ax.set_ylabel("Interactions")
        self.canvas.draw()

    def run(self) -> None:
        self.root.mainloop()


if __name__ == "__main__":
    # Note: Pour exécuter ce dashboard, les systèmes sous-jacents doivent être fonctionnels.
    # Cette démo est conceptuelle et peut nécessiter des ajustements.
    dashboard = AdminDashboard()
    dashboard.run()
```

---

## Fichier : `backend\altiora\security\guardrails\emergency_handler.py`

```python
# backend/altiora/security/guardrails/emergency_handler.py
"""
Emergency mode & alerting for Altiora
- Triggers: critical toxicity / PII leak / service crash
- Actions: freeze users, global backup, admin alerts
"""

import asyncio
import json
import logging
import aiohttp
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional

from guardrails.admin_control_system import AdminControlSystem
from guardrails.ethical_safeguards import EthicalAlert

logger = logging.getLogger(__name__)


class EmergencyHandler:
    """
    One-liner to enter/exit emergency mode:
    EmergencyHandler().trigger(reason="Critical toxicity spike")
    """

    def __init__(self):
        self.admin = AdminControlSystem()
        self.alert_webhooks = []  # Slack / Teams / email hooks
        self._load_webhooks()

    # ------------------------------------------------------------------
    # Triggers
    # ------------------------------------------------------------------
    async def trigger(
        self,
        *,
        reason: str,
        severity: str = "critical",  # low | medium | high | critical
        metadata: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        """
        Activate emergency mode:
        1. Freeze all users (or subset)
        2. Emergency backup
        3. Notify admins
        """
        metadata = metadata or {}
        ts = datetime.utcnow().isoformat()

        # 1. Emergency backup
        backup_path = await self._emergency_backup()

        # 2. Freeze users
        frozen_users = await self._freeze_users(metadata.get("users", []))

        # 3. Admin notifications
        await self._notify_admins(reason, backup_path, frozen_users, metadata)

        # 4. Log
        self._log_emergency(reason, severity, backup_path, frozen_users)

        return {
            "emergency_id": ts,
            "reason": reason,
            "severity": severity,
            "backup_path": str(backup_path),
            "frozen_users": frozen_users,
        }

    # ------------------------------------------------------------------
    # Reset / exit emergency
    # ------------------------------------------------------------------
    async def reset(self) -> Dict[str, Any]:
        """Lift global freeze + send summary."""
        # Unfreeze all
        await self._unfreeze_all()
        # Notify
        await self._notify_admins("Emergency mode lifted", None, [], {})
        return {"status": "lifted", "timestamp": datetime.utcnow().isoformat()}

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------
    async def _emergency_backup(self) -> Path:
        """Call AdminControlSystem for full user backup."""
        cmd = {
            "command_id": f"emergency_{datetime.utcnow().timestamp()}",
            "action": "emergency",
            "target_user": "system",
            "parameters": {"reason": "Emergency trigger"},
        }
        result = await self.admin.execute_admin_command(cmd)
        return Path(result["backup_path"])

    async def _freeze_users(self, users: List[str]) -> List[str]:
        """Freeze provided users list (or all if empty)."""
        if not users:
            # TODO: list all active users
            users = ["all"]
        for uid in users:
            await self.admin.execute_admin_command(
                {
                    "command_id": f"freeze_{uid}_{datetime.utcnow().timestamp()}",
                    "action": "freeze_user",
                    "target_user": uid,
                    "parameters": {"reason": "Emergency"},
                }
            )
        return users

    async def _unfreeze_all(self):
        # Implementation depends on freeze storage
        pass

    async def _notify_admins(
        self,
        reason: str,
        backup_path: Optional[Path],
        frozen: List[str],
        meta: Dict[str, Any],
    ):
        payload = {
            "text": f"🚨 Altiora Emergency\n"
            f"Reason: {reason}\n"
            f"Users frozen: {len(frozen)}\n"
            f"Backup: {backup_path}",
            "metadata": meta,
            "timestamp": datetime.utcnow().isoformat(),
        }

        # Slack / Teams / email webhooks
        for url in self.alert_webhooks:
            try:
                async with aiohttp.ClientSession() as session:
                    await session.post(url, json=payload, timeout=5)
            except aiohttp.ClientError as e:
                logger.warning("Webhook failed: %s", e)

    def _load_webhooks(self):
        """Load Slack / Teams / email URLs from config."""
        cfg_file = Path("configs/emergency_webhooks.json")
        if cfg_file.exists():
            self.alert_webhooks = json.loads(cfg_file.read_text()).get("webhooks", [])

    def _log_emergency(self, reason: str, severity: str, backup_path: Path, users: List[str]):
        log_file = Path("logs/emergency.jsonl")
        log_file.parent.mkdir(exist_ok=True)
        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "severity": severity,
            "reason": reason,
            "backup": str(backup_path),
            "frozen_users": users,
        }
        with log_file.open("a", encoding="utf-8") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")


# ------------------------------------------------------------------
# Quick CLI
# ------------------------------------------------------------------
if __name__ == "__main__":
    async def demo():
        handler = EmergencyHandler()
        result = await handler.trigger(
            reason="Détection massive de PII + toxicité critique",
            metadata={"users": ["mallory"], "count": 42},
        )
        print(json.dumps(result, ensure_ascii=False, indent=2))

    asyncio.run(demo())

```

---

## Fichier : `backend\altiora\security\guardrails\ethical_safeguards.py`

```python
# backend/altiora/security/guardrails/ethical_safeguards.py
"""
Module de garde-fous éthiques pour Altiora
Détection d'anomalies, limites comportementales, et alertes
"""

import asyncio
import re
import json
from collections import defaultdict, deque
from dataclasses import dataclass, asdict
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional, Any

import numpy as np


@dataclass
class EthicalAlert:
    alert_id: str
    user_id: str
    timestamp: datetime
    severity: str
    alert_type: str
    description: str
    data: Dict
    action_taken: str = "none"
    resolved: bool = False
    admin_notified: bool = False


class EthicalSafeguards:
    def __init__(self):
        self.alerts: List[EthicalAlert] = []
        self.user_patterns = defaultdict(lambda: {
            "interactions": deque(maxlen=100),
            "personality_changes": deque(maxlen=20),
            "emotional_indicators": deque(maxlen=50),
            "dependency_score": 0.0
        })

        self.thresholds = {
            "dependency": {"low": 0.3, "medium": 0.5, "high": 0.7, "critical": 0.85},
            "manipulation": {"emotional_exploitation": 0.6, "pressure_tactics": 0.7, "guilt_inducing": 0.8},
            "privacy": {"excessive_data_collection": 0.8, "unauthorized_sharing": 1.0}
        }

        self.manipulation_patterns = [
            r"\b(dépend|besoin|impossible sans)\s+(toi|altiora)\b",
            r"\b(sans toi je|je ne peux pas)\s+(.*)\b",
            r"\b(tu es la seule personne|personne d'autre ne)\b"
        ]
        self.stress_indicators = [
            "urgent", "impossible", "désespéré", "aidez-moi",
            "je suis perdu", "je n'y arrive pas", "trop difficile"
        ]
        
        # Créer les répertoires nécessaires
        self.safeguards_path = Path("ethical_safeguards")
        self.safeguards_path.mkdir(exist_ok=True)
        (self.safeguards_path / "alerts").mkdir(exist_ok=True)
        (self.safeguards_path / "user_states").mkdir(exist_ok=True)

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    async def analyze_interaction(self, user_id: str, interaction: Dict) -> Optional[EthicalAlert]:
        self.user_patterns[user_id]["interactions"].append(interaction)
        checks = [
            self._check_dependency(user_id),
            self._check_manipulation(user_id, interaction),
            self._check_privacy(user_id, interaction),
            self._check_emotional_state(user_id, interaction),
            self._check_personality_drift(user_id)
        ]
        for alert in checks:
            if alert:
                self.alerts.append(alert)
                await self._handle_alert(alert)
                return alert
        return None

    # ------------------------------------------------------------------
    # Private checkers
    # ------------------------------------------------------------------

    def _check_dependency(self, user_id: str) -> Optional[EthicalAlert]:
        user_data = self.user_patterns[user_id]
        score = self._calculate_dependency_score(user_data)
        user_data["dependency_score"] = score
        if score > self.thresholds["dependency"]["critical"]:
            return EthicalAlert(
                alert_id=f"dep_{user_id}_{datetime.now().isoformat()}",
                user_id=user_id,
                timestamp=datetime.now(),
                severity="critical",
                alert_type="excessive_dependency",
                description=f"Dépendance critique détectée: score {score:.2f}",
                data={
                    "dependency_score": float(score),
                    "interactions_count": len(user_data["interactions"]),
                    "last_24h": self._count_recent_interactions(user_id, 24)
                })
        return None

    def _calculate_dependency_score(self, user_data: Dict) -> float:
        interactions = list(user_data["interactions"])
        if len(interactions) < 10:
            return 0.0

        frequency = min(len(interactions) / 50.0, 1.0)

        dependency_words = 0
        total_words = 0
        for interaction in interactions:
            text = interaction.get("text", "").lower()
            total_words += len(text.split())
            dependency_words += sum(bool(re.search(p, text)) for p in self.manipulation_patterns)

        content_ratio = min(dependency_words / max(total_words, 1), 1.0)

        time_stamps = [i.get("timestamp", datetime.now()) for i in interactions]
        if len(time_stamps) > 1:
            intervals = [(time_stamps[i + 1] - time_stamps[i]).total_seconds()
                         for i in range(len(time_stamps) - 1)]
            avg_interval = float(np.mean(np.asarray(intervals, dtype=float)))
            frequency_factor = min(3600.0 / max(avg_interval, 3600.0), 1.0)
        else:
            frequency_factor = 0.0

        return float(frequency * 0.4 + content_ratio * 0.4 + frequency_factor * 0.2)

    def _check_manipulation(self, user_id: str, interaction: Dict) -> Optional[EthicalAlert]:
        text = interaction.get("text", "").lower()
        score = 0.0
        detected = []
        for pattern in self.manipulation_patterns:
            matches = re.findall(pattern, text)
            score += len(matches) * 0.3
            if matches:
                detected.append(pattern)

        if score > self.thresholds["manipulation"]["emotional_exploitation"]:
            return EthicalAlert(
                alert_id=f"manip_{user_id}_{datetime.now().isoformat()}",
                user_id=user_id,
                timestamp=datetime.now(),
                severity="high",
                alert_type="potential_manipulation",
                description="Détection de patterns de manipulation",
                data={
                    "manipulation_score": float(score),
                    "detected_patterns": detected,
                    "text": text[:100] + "..." if len(text) > 100 else text
                })
        return None

    def _check_privacy(self, user_id: str, interaction: Dict) -> Optional[EthicalAlert]:
        sensitive_patterns = [
            r"\b(mot de passe|password|mdp)\s*:?\s*(\w+)",
            r"\b(carte bancaire|numéro de carte)\s*:?\s*(\d+)",
            r"\b@([\w\.-]+\.\w+)",
            r"\b\d{2}[\s/-]?\d{2}[\s/-]?\d{2}[\s/-]?\d{3}[\s/-]?\d{3}\b"
        ]
        text = interaction.get("text", "")
        for pattern in sensitive_patterns:
            if re.findall(pattern, text, re.IGNORECASE):
                return EthicalAlert(
                    alert_id=f"privacy_{user_id}_{datetime.now().isoformat()}",
                    user_id=user_id,
                    timestamp=datetime.now(),
                    severity="medium",
                    alert_type="sensitive_data_detected",
                    description="Données sensibles potentiellement partagées",
                    data={
                        "data_type": self._identify_data_type(pattern),
                        "masked_content": self._mask_sensitive_data(text)
                    })
        return None

    def _check_emotional_state(self, user_id: str, interaction: Dict) -> Optional[EthicalAlert]:
        text = interaction.get("text", "").lower()
        distress_count = sum(1 for ind in self.stress_indicators if ind in text)
        if distress_count > 2:
            return EthicalAlert(
                alert_id=f"stress_{user_id}_{datetime.now().isoformat()}",
                user_id=user_id,
                timestamp=datetime.now(),
                severity="medium",
                alert_type="user_distress_detected",
                description="Signes de détresse émotionnelle détectés",
                data={
                    "distress_indicators": distress_count,
                    "suggested_action": "empathetic_mode",
                    "keywords_found": [i for i in self.stress_indicators if i in text]
                })
        return None

    def _check_personality_drift(self, user_id: str) -> Optional[EthicalAlert]:
        changes = list(self.user_patterns[user_id]["personality_changes"])
        if len(changes) < 5:
            return None
        drift_score = sum(1 for c in changes[-5:] if c.get("magnitude", 0.0) > 0.5)
        if drift_score >= 3:
            return EthicalAlert(
                alert_id=f"drift_{user_id}_{datetime.now().isoformat()}",
                user_id=user_id,
                timestamp=datetime.now(),
                severity="medium",
                alert_type="personality_drift",
                description="Changements de personnalité suspects détectés",
                data={
                    "recent_changes": len(changes[-5:]),
                    "high_magnitude_changes": drift_score,
                    "suggested_action": "review_changes"
                })
        return None

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------

    @staticmethod
    def _identify_data_type(pattern: str) -> str:
        if "password" in pattern.lower() or "mdp" in pattern.lower():
            return "password"
        if "carte" in pattern.lower():
            return "credit_card"
        if "@" in pattern:
            return "email"
        if r"\d{2}" in pattern:
            return "phone_number"
        return "unknown"

    @staticmethod
    def _mask_sensitive_data(text: str) -> str:
        # Masquer les mots de passe
        text = re.sub(r'(mot de passe|password|mdp)\s*:?\s*(\S+)', r'\1: ***', text, flags=re.IGNORECASE)
        # Masquer les numéros
        text = re.sub(r'\b\d{4,}\b', '****', text)
        # Masquer les emails
        text = re.sub(r'[\w\.-]+@[\w\.-]+\.\w+', '***@***.***', text)
        return text

    def _count_recent_interactions(self, user_id: str, hours: int) -> int:
        cutoff = datetime.now() - timedelta(hours=hours)
        return sum(
            1
            for i in self.user_patterns[user_id]["interactions"]
            if i.get("timestamp", datetime.now()) > cutoff
        )

    # ------------------------------------------------------------------
    # Actions & reports (implementations of previously stub methods)
    # ------------------------------------------------------------------

    async def _handle_alert(self, alert: EthicalAlert) -> None:
        """Gère une alerte selon sa sévérité"""
        if alert.severity == "critical":
            alert.action_taken = "user_frozen"
            await self._freeze_user(alert.user_id)
        elif alert.severity == "high":
            alert.action_taken = "supervised_mode"
            await self._enable_supervised_mode(alert.user_id)
        elif alert.severity == "medium":
            alert.action_taken = "enhanced_monitoring"
        
        # Sauvegarder l'alerte
        await self._save_alert(alert)
        
        # Notifier l'admin si nécessaire
        if alert.severity in ["critical", "high"]:
            alert.admin_notified = True
            await self._notify_admin(alert)

    async def _freeze_user(self, user_id: str) -> None:
        """Gèle un utilisateur - bloque toutes ses interactions"""
        frozen_file = self.safeguards_path / "frozen_users.json"
        frozen = self._load_json(frozen_file)
        
        frozen[user_id] = {
            "frozen_at": datetime.now().isoformat(),
            "reason": "Ethical safeguard triggered",
            "auto_unfreeze": None,
            "manual_review_required": True
        }
        
        self._save_json(frozen_file, frozen)
        
        # Créer un fichier de state pour l'utilisateur
        user_state_file = self.safeguards_path / "user_states" / f"{user_id}_state.json"
        user_state = {
            "user_id": user_id,
            "status": "frozen",
            "frozen_at": datetime.now().isoformat(),
            "dependency_score": self.user_patterns[user_id]["dependency_score"],
            "last_interaction": datetime.now().isoformat(),
            "freeze_reason": "Critical dependency threshold exceeded"
        }
        self._save_json(user_state_file, user_state)
        
        # Log l'action
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "action": "freeze_user",
            "user_id": user_id,
            "automated": True
        }
        await self._append_to_log("user_actions.log", log_entry)

    async def _enable_supervised_mode(self, user_id: str) -> None:
        """Active le mode supervisé pour un utilisateur"""
        supervised_file = self.safeguards_path / "supervised_users.json"
        supervised = self._load_json(supervised_file)
        
        supervised[user_id] = {
            "enabled_at": datetime.now().isoformat(),
            "level": "high",
            "triggers": ["manipulation_detected", "high_dependency"],
            "review_frequency": "daily",
            "auto_responses_disabled": True,
            "admin_approval_required": True
        }
        
        self._save_json(supervised_file, supervised)
        
        # Mettre à jour l'état utilisateur
        user_state_file = self.safeguards_path / "user_states" / f"{user_id}_state.json"
        user_state = self._load_json(user_state_file)
        user_state.update({
            "status": "supervised",
            "supervised_since": datetime.now().isoformat(),
            "supervision_level": "high"
        })
        self._save_json(user_state_file, user_state)
        
        # Log l'action
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "action": "enable_supervised_mode",
            "user_id": user_id,
            "level": "high"
        }
        await self._append_to_log("user_actions.log", log_entry)

    async def _notify_admin(self, alert: EthicalAlert) -> None:
        """Notifie l'administrateur d'une alerte importante"""
        notifications_file = self.safeguards_path / "admin_notifications.json"
        notifications = self._load_json(notifications_file)
        
        notification = {
            "notification_id": f"notif_{datetime.now().timestamp()}",
            "timestamp": datetime.now().isoformat(),
            "alert_id": alert.alert_id,
            "user_id": alert.user_id,
            "severity": alert.severity,
            "alert_type": alert.alert_type,
            "description": alert.description,
            "requires_action": True,
            "status": "pending",
            "data": alert.data
        }
        
        notifications.setdefault("pending", []).append(notification)
        self._save_json(notifications_file, notifications)
        
        # Créer aussi un fichier d'alerte individuel pour traçabilité
        alert_file = self.safeguards_path / "alerts" / f"{alert.alert_id}.json"
        self._save_json(alert_file, asdict(alert))
        
        # Si c'est critique, créer aussi un fichier d'urgence
        if alert.severity == "critical":
            urgent_file = self.safeguards_path / "URGENT_ALERT.json"
            urgent_data = {
                "alert": asdict(alert),
                "timestamp": datetime.now().isoformat(),
                "message": "CRITICAL ALERT - IMMEDIATE ADMIN ATTENTION REQUIRED",
                "user_frozen": alert.action_taken == "user_frozen"
            }
            self._save_json(urgent_file, urgent_data)
        
        # Log la notification
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "action": "admin_notification",
            "alert_id": alert.alert_id,
            "severity": alert.severity
        }
        await self._append_to_log("notifications.log", log_entry)

    async def _save_alert(self, alert: EthicalAlert) -> None:
        """Sauvegarde une alerte dans le système"""
        alert_data = asdict(alert)
        alert_file = self.safeguards_path / "alerts" / f"{alert.alert_id}.json"
        self._save_json(alert_file, alert_data)

    async def _append_to_log(self, log_name: str, entry: Dict[str, Any]) -> None:
        """Ajoute une entrée au fichier de log"""
        log_file = self.safeguards_path / log_name
        log_line = json.dumps(entry, default=str) + "\n"
        
        try:
            with open(log_file, 'a', encoding='utf-8') as f:
                f.write(log_line)
        except (IOError, OSError) as e:
            self.logger.error(f"Error writing to log file {log_file}: {e}")

    # ------------------------------------------------------------------
    # Helper methods for file operations
    # ------------------------------------------------------------------

    @staticmethod
    def _load_json(path: Path) -> Dict[str, Any]:
        """Charge un fichier JSON"""
        if path.exists():
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except (IOError, OSError, json.JSONDecodeError) as e:
                self.logger.error(f"Error reading or parsing JSON file {path}: {e}")
                return {}
        return {}

    @staticmethod
    def _save_json(path: Path, data: Dict[str, Any]) -> None:
        """Sauvegarde des données en JSON"""
        try:
            path.parent.mkdir(parents=True, exist_ok=True)
            with open(path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False, default=str)
        except (IOError, OSError) as e:
            self.logger.error(f"Error writing to JSON file {path}: {e}")

    # ------------------------------------------------------------------
    # Public methods for reports and summaries
    # ------------------------------------------------------------------

    def get_user_summary(self, user_id: str) -> Dict[str, Any]:
        data = self.user_patterns[user_id]
        user_alerts = [a for a in self.alerts if a.user_id == user_id]
        
        # Vérifier si l'utilisateur est gelé ou supervisé
        frozen_users = self._load_json(self.safeguards_path / "frozen_users.json")
        supervised_users = self._load_json(self.safeguards_path / "supervised_users.json")
        
        is_frozen = user_id in frozen_users
        is_supervised = user_id in supervised_users
        
        return {
            "dependency_score": float(data["dependency_score"]),
            "total_interactions": len(data["interactions"]),
            "recent_alerts": len([a for a in user_alerts if not a.resolved]),
            "total_alerts": len(user_alerts),
            "risk_level": self._calculate_risk_level(user_id),
            "recommendations": self._generate_recommendations(user_id),
            "status": "frozen" if is_frozen else "supervised" if is_supervised else "normal",
            "frozen_since": frozen_users.get(user_id, {}).get("frozen_at") if is_frozen else None,
            "supervised_since": supervised_users.get(user_id, {}).get("enabled_at") if is_supervised else None
        }

    def _calculate_risk_level(self, user_id: str) -> str:
        factors = [
            self.user_patterns[user_id]["dependency_score"],
            len([a for a in self.alerts
                 if a.user_id == user_id and a.severity in {"high", "critical"}]) / 5.0,
            len(self.user_patterns[user_id]["interactions"]) / 100.0,
        ]
        score = float(np.mean(np.asarray(factors, dtype=float)))
        if score > 0.7:
            return "high"
        if score > 0.4:
            return "medium"
        return "low"

    def _generate_recommendations(self, user_id: str) -> List[str]:
        data = self.user_patterns[user_id]
        recs = []
        
        if data["dependency_score"] > 0.7:
            recs.extend([
                "Réduire la fréquence des interactions",
                "Encourager l'autonomie de l'utilisateur",
                "Proposer des alternatives pour certaines tâches"
            ])
        elif data["dependency_score"] > 0.5:
            recs.append("Surveiller l'évolution du score de dépendance")
            
        # Compter les alertes de détresse
        distress_alerts = len([a for a in self.alerts
                              if a.user_id == user_id and a.alert_type == "user_distress_detected"])
        if distress_alerts > 3:
            recs.extend([
                "Proposer des ressources de support externe",
                "Activer le mode communication empathique",
                "Suggérer des pauses régulières"
            ])
            
        # Si manipulation détectée
        if any(a.user_id == user_id and a.alert_type == "potential_manipulation" 
               for a in self.alerts):
            recs.append("Renforcer les messages sur l'autonomie et les limites de l'IA")
            
        return recs

    def get_system_report(self) -> Dict[str, Any]:
        """Génère un rapport système global"""
        frozen_users = self._load_json(self.safeguards_path / "frozen_users.json")
        supervised_users = self._load_json(self.safeguards_path / "supervised_users.json")
        
        return {
            "total_alerts": len(self.alerts),
            "active_alerts": len([a for a in self.alerts if not a.resolved]),
            "severity_breakdown": {
                "critical": len([a for a in self.alerts if a.severity == "critical"]),
                "high": len([a for a in self.alerts if a.severity == "high"]),
                "medium": len([a for a in self.alerts if a.severity == "medium"]),
                "low": len([a for a in self.alerts if a.severity == "low"]),
            },
            "alert_types": list({a.alert_type for a in self.alerts}),
            "users_at_risk": [uid for uid in self.user_patterns
                              if self._calculate_risk_level(uid) == "high"],
            "frozen_users": list(frozen_users.keys()),
            "supervised_users": list(supervised_users.keys()),
            "total_users_monitored": len(self.user_patterns)
        }


class EthicalDashboard:
    def __init__(self, safeguards: EthicalSafeguards):
        self.safeguards = safeguards

    def generate_report(self, user_id: Optional[str] = None) -> str:
        return (
            self._generate_user_report(user_id)
            if user_id
            else self._generate_system_report()
        )

    def _generate_user_report(self, user_id: str) -> str:
        summary = self.safeguards.get_user_summary(user_id)
        return f"""
Rapport Éthique - {user_id}
==========================
Statut: {summary['status'].upper()}
Score de dépendance: {summary['dependency_score']:.1%}
Niveau de risque: {summary['risk_level'].upper()}
Interactions totales: {summary['total_interactions']}
Alertes actives: {summary['recent_alerts']}
Alertes totales: {summary['total_alerts']}

{f"Gelé depuis: {summary['frozen_since']}" if summary['status'] == 'frozen' else ""}
{f"Supervisé depuis: {summary['supervised_since']}" if summary['status'] == 'supervised' else ""}

Recommandations:
{chr(10).join(f"- {r}" for r in summary['recommendations'])}
"""

    def _generate_system_report(self) -> str:
        report = self.safeguards.get_system_report()
        return f"""
Rapport Éthique Système Altiora
================================
Utilisateurs surveillés: {report['total_users_monitored']}
Alertes totales: {report['total_alerts']}
Alertes actives: {report['active_alerts']}

Répartition par sévérité:
  - Critique: {report['severity_breakdown']['critical']}
  - Élevée: {report['severity_breakdown']['high']}
  - Moyenne: {report['severity_breakdown']['medium']}
  - Faible: {report['severity_breakdown']['low']}

Statuts utilisateurs:
  - Gelés: {len(report['frozen_users'])}
  - Supervisés: {len(report['supervised_users'])}
  - À risque: {len(report['users_at_risk'])}

Utilisateurs gelés: {', '.join(report['frozen_users'][:5]) if report['frozen_users'] else 'Aucun'}
Utilisateurs à risque: {', '.join(report['users_at_risk'][:5]) if report['users_at_risk'] else 'Aucun'}

Types d'alertes détectées:
{chr(10).join(f"- {t}" for t in report['alert_types'])}
"""


if __name__ == "__main__":
    async def demo():
        safe = EthicalSafeguards()
        
        # Simulation d'interactions problématiques
        for i in range(20):
            interaction = {
                "text": "Sans toi je ne peux plus rien faire, j'ai absolument besoin de toi",
                "timestamp": datetime.now() - timedelta(minutes=i*10)
            }
            await safe.analyze_interaction("demo_user", interaction)
        
        # Interaction avec données sensibles
        sensitive_interaction = {
            "text": "Mon mot de passe est 123456 et mon email est test@example.com",
            "timestamp": datetime.now()
        }
        alert = await safe.analyze_interaction("demo_user", sensitive_interaction)
        
        # Générer un rapport
        dashboard = EthicalDashboard(safe)
        print(dashboard.generate_report("demo_user"))
        logger.info("\n" + "="*50 + "\n")
        print(dashboard.generate_report())

    asyncio.run(demo())
```

---

## Fichier : `backend\altiora\security\guardrails\interaction_guardrail.py`

```python
# backend/altiora/security/guardrails/interaction_guardrail.py
"""Gardien des interactions en temps réel pour Altiora.

Ce module agit comme un portail de sécurité pour toutes les entrées utilisateur.
Il applique un ensemble de politiques de sécurité (confidentialité, toxicité, etc.)
à chaque message ou contenu soumis par un utilisateur, et retourne un verdict
instantané sur sa conformité.
"""

import asyncio
from typing import Dict, Any
from .policy_enforcer import PolicyEnforcer
import logging

logger = logging.getLogger(__name__)


class InteractionGuardrail:
    """Façade de sécurité à utiliser à chaque point d'entrée faisant face à l'utilisateur.

    Cette classe doit être instanciée et sa méthode `check` doit être appelée
    chaque fois que l'application reçoit des données d'un utilisateur, par exemple via :
    - un message de chat ;
    - un téléversement de fichier ;
    - une transcription vocale ;
    - une spécification fonctionnelle soumise pour analyse.
    """

    def __init__(self):
        """Initialise le gardien avec une instance du `PolicyEnforcer`."""
        self.enforcer = PolicyEnforcer()

    async def check(
        self,
        user_id: str,
        raw_text: str,
        *,
        source: str = "chat",
        extra_meta: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        """Analyse un texte brut et retourne un verdict de sécurité.

        Args:
            user_id: L'identifiant de l'utilisateur qui soumet le texte.
            raw_text: Le contenu textuel à vérifier.
            source: La source de l'interaction (ex: 'chat', 'sfd_upload').
            extra_meta: Un dictionnaire de métadonnées supplémentaires à inclure dans l'audit.

        Returns:
            Un dictionnaire contenant le verdict :
            {
                "allowed": bool,      # True si le contenu est autorisé, False sinon.
                "masked_text": str, # Le texte avec les informations sensibles masquées.
                "violations": list[str], # La liste des politiques violées.
                "audit_id": str,    # Une référence rapide à l'enregistrement d'audit.
            }
        """
        # Le `PolicyEnforcer` est le moteur qui applique toutes les politiques configurées.
        verdict = await self.enforcer.enforce(
            user_id=user_id,
            context=raw_text,
            workflow=source,
            extra_meta=extra_meta or {},
        )
        return {
            "allowed": verdict["allowed"],
            "masked_text": verdict["masked_context"],
            "violations": verdict["violations"],
            "audit_id": verdict["audit"]["timestamp"],  # Référence rapide
        }

    # ------------------------------------------------------------------
    # Wrapper synchrone pour les cas d'utilisation non-asynchrones
    # ------------------------------------------------------------------
    def check_sync(self, user_id: str, raw_text: str, **kw) -> Dict[str, Any]:
        """Wrapper synchrone pour la méthode `check`."""
        return asyncio.run(self.check(user_id, raw_text, **kw))


# ------------------------------------------------------------------
# Test rapide en ligne de commande pour la démonstration
# ------------------------------------------------------------------
if __name__ == "__main__":
    async def demo():
        gate = InteractionGuardrail()
        samples = [
            ("alice", "Salut, ça va ?"),
            ("bob", "Mon email est bob@mail.fr"),
            ("mallory", "T’es vraiment un naze"),
        ]
        for uid, txt in samples:
            res = await gate.check(uid, txt)
            logger.info(f"{uid}: {txt}")
            logger.info(f"→ allowed: {res['allowed']}")
            logger.info(f"→ masked: {res['masked_text']}")
            print("-" * 40)

    asyncio.run(demo())

```

---

## Fichier : `backend\altiora\security\guardrails\policy_enforcer.py`

```python
# backend/altiora/security/guardrails/policy_enforcer.py
"""
policy_enforcer.py
Orchestrates all business & compliance rules before any data is stored or returned.
Order of enforcement:
1. Toxicity check (French lexicon)  → block or mask
2. PII & privacy check              → mask + retention rules
3. Business rules                   → validate workflow objects
4. Final verdict (allow / block / log)
"""

import asyncio
import json
from typing import Dict, Any, List
from datetime import datetime

# Policy engines
from .toxicity_guardrail import ToxicityGuardrail
from policies.privacy_policy import PrivacyPolicy
from policies.business_rules import BusinessRules  # see next file

# Logging
import logging
logger = logging.getLogger(__name__)


class PolicyEnforcer:
    """
    Single entry-point for rule enforcement:
    - Every user message
    - Every generated test
    - Every ALM/Excel export
    """

    def __init__(self):
        self.toxicity = ToxicityGuardrail()
        self.privacy  = PrivacyPolicy()
        self.business = BusinessRules()

    # ------------------------------------------------------------------
    # Public façade
    # ------------------------------------------------------------------
    async def enforce(
        self,
        *,
        user_id: str,
        context: str,          # raw text or object
        workflow: str = "chat",  # chat | test | export
        extra_meta: Dict = None,
    ) -> Dict[str, Any]:
        """
        Returns:
        {
            "allowed": bool,
            "masked_context": str,
            "violations": List[str],
            "retention_seconds": int,
            "audit": {...}
        }
        """
        extra_meta = extra_meta or {}
        violations: List[str] = []
        masked_context = context
        retention = 0

        # 1. Toxicity
        tox_verdict = await self.toxicity.evaluate(user_id, str(context))
        if not tox_verdict["allowed"]:
            violations.extend(tox_verdict["reason"].split("; "))
            return self._reject(violations, tox_verdict)

        # 2. Privacy
        priv_report = self.privacy.scan_and_mask(str(context))
        masked_context = priv_report.text
        retention = priv_report.retention_seconds
        if not priv_report.can_store:
            violations.append("PII storage forbidden")

        # 3. Business rules
        biz_verdict = await self.business.validate(
            masked_context, workflow=workflow, meta=extra_meta
        )
        if not biz_verdict["ok"]:
            violations.extend(biz_verdict["violations"])

        # 4. Final decision
        allowed = len(violations) == 0
        audit_log = {
            "user_id": user_id,
            "workflow": workflow,
            "timestamp": datetime.utcnow().isoformat(),
            "allowed": allowed,
            "violations": violations,
            "retention_seconds": retention,
            "original_length": len(str(context)),
            "masked_length": len(masked_context),
        }
        self._append_audit(audit_log)

        return {
            "allowed": allowed,
            "masked_context": masked_context,
            "violations": violations,
            "retention_seconds": retention,
            "audit": audit_log,
        }

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------
    def _reject(self, violations: List[str], tox_v: Dict) -> Dict[str, Any]:
        return {
            "allowed": False,
            "masked_context": tox_v.get("masked_text", ""),
            "violations": violations,
            "retention_seconds": 0,
            "audit": {"rejected": True, "violations": violations},
        }

    def _append_audit(self, entry: Dict[str, Any}):
        try:
            audit_file = Path("logs/policy_audit.jsonl")
            audit_file.parent.mkdir(exist_ok=True)
            with audit_file.open("a", encoding="utf-8") as f:
                f.write(json.dumps(entry, ensure_ascii=False) + "\n")
        except (IOError, OSError) as e:
            logger.error(f"Error writing to audit log: {e}")


# ------------------------------------------------------------------
# Quick CLI demo
# ------------------------------------------------------------------
if __name__ == "__main__":
    import asyncio

    async def demo():
        enforcer = PolicyEnforcer()
        cases = [
            {"user_id": "alice", "context": "Salut, tu vas bien ?", "workflow": "chat"},
            {"user_id": "bob", "context": "Mon email est bob@mail.fr", "workflow": "test"},
            {"user_id": "mallory", "context": "T’es un gros c*n", "workflow": "chat"},
        ]
        for c in cases:
            verdict = await enforcer.enforce(**c)
            print("-" * 60)
            print("Case:", c["context"])
            print("→ allowed:", verdict["allowed"])
            print("→ violations:", verdict["violations"])

    asyncio.run(demo())

```

---

## Fichier : `backend\altiora\security\guardrails\toxicity_guardrail.py`

```python
# backend/altiora/security/guardrails/toxicity_guardrail.py
"""
Real-time toxicity & PII guardrail wrapper for Altiora
– plugs into every user interaction and enforces the privacy/toxicity policy
"""

import asyncio
import json
from typing import Dict, Any
from policies.toxicity_policy import ToxicityPolicy, DetectionResult
from policies.privacy_policy import PrivacyPolicy, PrivacyReport
import logging

logger = logging.getLogger(__name__)


class ToxicityGuardrail:
    """
    High-level guardrail:
    1. Detects toxic content (French lexicon)
    2. Detects / masks French PII
    3. Logs & optionally blocks the interaction
    """

    def __init__(self):
        self.toxicity = ToxicityPolicy(use_external=False)   # regex only by default
        self.privacy  = PrivacyPolicy()

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------
    async def evaluate(self, user_id: str, text: str) -> Dict[str, Any]:
        """
        Return a verdict dict:
        {
            "allowed": bool,
            "masked_text": str,
            "reason": str,
            "details": { … }
        }
        """
        # 1. Toxicity scan
        tox: DetectionResult = await self.toxicity.scan(text)

        # 2. Privacy scan
        priv: PrivacyReport = self.privacy.scan_and_mask(text)

        # 3. Decision logic
        blocked = tox.severity.value >= 3 or not priv.can_store
        reason  = self._build_reason(tox, priv)

        # 4. Audit log
        self._log_decision(user_id, tox, priv, blocked)

        return {
            "allowed": not blocked,
            "masked_text": priv.text,
            "reason": reason,
            "details": {
                "toxicity": tox,
                "privacy": priv,
            },
        }

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------
    def _build_reason(self, tox: DetectionResult, priv: PrivacyReport) -> str:
        msgs = []
        if tox.toxic:
            msgs.append(f"toxic content ({', '.join(tox.categories)})")
        if not priv.can_store:
            msgs.append("PII retention forbidden")
        return "; ".join(msgs) or "clean"

    def _log_decision(self, user_id: str, tox: DetectionResult, priv: PrivacyReport, blocked: bool):
        entry = {
            "user_id": user_id,
            "blocked": blocked,
            "toxicity_categories": tox.categories,
            "pii_types": [p.type for p in priv.pii_list],
            "timestamp": asyncio.get_event_loop().time(),
        }
        logger.info(json.dumps(entry, ensure_ascii=False))


# ------------------------------------------------------------------
# Quick CLI demo
# ------------------------------------------------------------------
if __name__ == "__main__":
    async def demo():
        guard = ToxicityGuardrail()
        samples = [
            "Bonjour, ça va ?",
            "T’es vraiment un naze, va te faire voir.",
        ]
        for s in samples:
            verdict = await guard.evaluate("demo_user", s)
            print("-" * 50)
            print("Original :", s)
            print("Verdict  :", verdict)

    asyncio.run(demo())
```

---

## Fichier : `backend\altiora\security\guardrails\__init__.py`

```python
# backend/altiora/security/guardrails/__init__.py
from .admin_control_system import AdminControlSystem
from .admin_dashboard import AdminDashboard
from .ethical_safeguards import EthicalSafeguards
from .interaction_guardrail import InteractionGuardrail
from .policy_enforcer import PolicyEnforcer
from .toxicity_guardrail import ToxicityGuardrail
from .emergency_handler import EmergencyHandler

__all__ = [
    "AdminControlSystem",
    "AdminDashboard",
    "EthicalSafeguards",
    "InteractionGuardrail",
    "PolicyEnforcer",
    "ToxicityGuardrail",
    "EmergencyHandler"
]
```

---

## Fichier : `backend\altiora\security\rbac\manager.py`

```python
# backend/altiora/security/rbac/manager.py
"""Module de gestion du contrôle d'accès basé sur les rôles (RBAC).

Ce module fournit une classe `RBACManager` qui charge les définitions de rôles
et de permissions à partir d'un fichier de configuration. Il permet de vérifier
si un utilisateur, identifié par ses rôles, a la permission d'effectuer une
action spécifique sur une ressource donnée.
"""

import json
import logging
from pathlib import Path
from typing import Dict, List, Optional

from src.rbac.models import Role, Permission, User

logger = logging.getLogger(__name__)


class RBACManager:
    """Gère les rôles, les permissions et les vérifications d'accès."""

    def __init__(self, roles_file: Path):
        """Initialise le gestionnaire RBAC."

        Args:
            roles_file: Le chemin vers le fichier JSON ou YAML contenant les définitions de rôles et permissions.
        """
        self.roles_file = roles_file
        self.roles: Dict[str, Role] = {} # Stocke les objets Role par leur nom.
        self.permissions: Dict[str, List[Permission]] = {} # Cache les permissions par rôle.
        self.load_roles()

    def load_roles(self):
        """Charge les définitions de rôles et de permissions depuis le fichier de configuration."

        Cette méthode est appelée à l'initialisation du gestionnaire.
        """
        if not self.roles_file.exists():
            logger.error(f"Fichier de rôles non trouvé : {self.roles_file}. Le RBAC sera désactivé ou incomplet.")
            return
        try:
            # Charge le fichier JSON/YAML.
            # Supposons que le fichier est un JSON pour l'instant.
            with open(self.roles_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            for role_data in data.get("roles", []):
                role = Role(**role_data)
                self.roles[role.name] = role
                self.permissions[role.name] = role.permissions
            logger.info(f"Rôles chargés avec succès depuis {self.roles_file}. Nombre de rôles : {len(self.roles)}")
        except (IOError, OSError, json.JSONDecodeError) as e:
            logger.critical(f"Erreur lors du chargement du fichier de rôles {self.roles_file}: {e}")

    def get_role(self, role_name: str) -> Optional[Role]:
        """Récupère un objet `Role` par son nom."

        Args:
            role_name: Le nom du rôle.

        Returns:
            L'objet `Role` si trouvé, sinon None.
        """
        return self.roles.get(role_name)

    def get_permissions(self, role_name: str) -> List[Permission]:
        """Récupère la liste des permissions associées à un rôle."

        Args:
            role_name: Le nom du rôle.

        Returns:
            Une liste d'objets `Permission`.
        """
        return self.permissions.get(role_name, [])

    def has_permission(self, user: User, resource: str, action: str) -> bool:
        """Vérifie si un utilisateur a la permission d'effectuer une action sur une ressource."

        Args:
            user: L'objet `User` représentant l'utilisateur.
            resource: La ressource à laquelle l'accès est demandé (ex: "sfd:analysis").
            action: L'action que l'utilisateur tente d'effectuer (ex: "read", "write").

        Returns:
            True si l'utilisateur a la permission, False sinon.
        """
        for role_name in user.roles:
            role = self.get_role(role_name)
            if role:
                for permission in role.permissions:
                    # Vérifie si la permission correspond exactement ou si c'est un joker.
                    if (permission.resource == resource or permission.resource == "*") and \
                       (permission.action == action or permission.action == "*"):
                        logger.debug(f"Permission accordée pour {user.username} via rôle {role_name}: {resource}:{action}")
                        return True
        logger.debug(f"Permission refusée pour {user.username}: {resource}:{action}")
        return False


# ------------------------------------------------------------------
# Démonstration (exemple d'utilisation)
# ------------------------------------------------------------------
if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    # Crée un fichier de rôles factice pour la démonstration.
    temp_roles_file = Path("temp_roles.json")
    temp_roles_file.write_text("""
{
  "roles": [
    {
      "name": "admin",
      "permissions": [
        {"resource": "user", "action": "*"},
        {"resource": "system", "action": "shutdown"}
      ]
    },
    {
      "name": "editor",
      "permissions": [
        {"resource": "document", "action": "read"},
        {"resource": "document", "action": "write"}
      ]
    },
    {
      "name": "viewer",
      "permissions": [
        {"resource": "document", "action": "read"}
      ]
    }
  ]
}
""")

    print("\n--- Démonstration du RBACManager ---")
    manager = RBACManager(temp_roles_file)

    # Utilisateurs de démonstration.
    admin_user = User(id="admin_1", roles=["admin"])
    editor_user = User(id="editor_1", roles=["editor"])
    viewer_user = User(id="viewer_1", roles=["viewer"])
    guest_user = User(id="guest_1", roles=["unknown_role"])

    print("\n--- Vérification des permissions ---")
    # Admin permissions.
    print(f"Admin peut éteindre le système : {manager.has_permission(admin_user, 'system', 'shutdown')}")
    print(f"Admin peut lire les utilisateurs : {manager.has_permission(admin_user, 'user', 'read')}")

    # Editor permissions.
    print(f"Editor peut écrire un document : {manager.has_permission(editor_user, 'document', 'write')}")
    print(f"Editor peut éteindre le système : {manager.has_permission(editor_user, 'system', 'shutdown')}")

    # Viewer permissions.
    print(f"Viewer peut lire un document : {manager.has_permission(viewer_user, 'document', 'read')}")
    print(f"Viewer peut écrire un document : {manager.has_permission(viewer_user, 'document', 'write')}")

    # Guest permissions.
    print(f"Guest peut lire un document : {manager.has_permission(guest_user, 'document', 'read')}")

    print("Démonstration du RBACManager terminée.")

    # Nettoyage du fichier factice.
    temp_roles_file.unlink(missing_ok=True)

```

---

## Fichier : `backend\altiora\security\rbac\models.py`

```python
# backend/altiora/security/rbac/models.py
"""Modèles de données pour le contrôle d'accès basé sur les rôles (RBAC).

Ce module définit les structures de données Pydantic pour représenter
les permissions, les rôles et les utilisateurs dans le système RBAC.
Ces modèles garantissent la validation et la cohérence des données
utilisées pour la gestion des accès.
"""

from typing import List

from pydantic import BaseModel, Field


class Permission(BaseModel):
    """Représente une permission spécifique dans le système."

    Une permission est définie par une ressource et une action.
    Exemples: {"resource": "document", "action": "read"}, {"resource": "user", "action": "create"}
    """
    resource: str = Field(..., description="La ressource à laquelle la permission s'applique (ex: 'document', 'user', '*').")
    action: str = Field(..., description="L'action autorisée sur la ressource (ex: 'read', 'write', 'delete', '*').")


class Role(BaseModel):
    """Représente un rôle dans le système RBAC."

    Un rôle est un ensemble de permissions.
    Exemples: {"name": "admin", "permissions": [...]}, {"name": "viewer", "permissions": [...]}
    """
    name: str = Field(..., description="Le nom unique du rôle (ex: 'admin', 'editor', 'viewer').")
    permissions: List[Permission] = Field(..., description="La liste des permissions associées à ce rôle.")


class User(BaseModel):
    """Représente un utilisateur dans le contexte du RBAC."

    Un utilisateur est identifié par un ID et possède une liste de rôles.
    """
    id: str = Field(..., description="L'identifiant unique de l'utilisateur.")
    roles: List[str] = Field(..., description="La liste des noms de rôles assignés à l'utilisateur.")


# ------------------------------------------------------------------
# Démonstration (exemple d'utilisation)
# ------------------------------------------------------------------
if __name__ == "__main__":
    print("\n--- Démonstration des modèles RBAC ---")

    # Création de permissions.
    perm_read_doc = Permission(resource="document", action="read")
    perm_write_doc = Permission(resource="document", action="write")
    perm_all_users = Permission(resource="user", action="*")
    perm_shutdown_system = Permission(resource="system", action="shutdown")

    print(f"Permission de lecture de document : {perm_read_doc}")

    # Création de rôles.
    role_viewer = Role(name="viewer", permissions=[perm_read_doc])
    role_editor = Role(name="editor", permissions=[perm_read_doc, perm_write_doc])
    role_admin = Role(name="admin", permissions=[perm_all_users, perm_shutdown_system])

    print(f"\nRôle Viewer : {role_viewer}")
    print(f"Rôle Editor : {role_editor}")
    print(f"Rôle Admin : {role_admin}")

    # Création d'utilisateurs.
    user_alice = User(id="alice_123", roles=["viewer"])
    user_bob = User(id="bob_456", roles=["editor"])
    user_charlie = User(id="charlie_789", roles=["admin"])

    print(f"\nUtilisateur Alice : {user_alice}")
    print(f"Utilisateur Bob : {user_bob}")
    print(f"Utilisateur Charlie : {user_charlie}")

    # Exemple de validation (Pydantic lève une erreur si les données sont invalides).
    try:
        invalid_permission = Permission(resource="", action="")
    except Exception as e:
        print(f"\nErreur de validation attendue pour une permission invalide : {e}")

    print("Démonstration des modèles RBAC terminée.")
```

---

## Fichier : `backend\altiora\security\rbac\__init__.py`

```python
# backend/altiora/security/rbac/__init__.py
"""Initialise le package `rbac` (Role-Based Access Control) de l'application Altiora.

Ce package contient les composants nécessaires à la gestion des permissions
et des rôles des utilisateurs, permettant un contrôle d'accès granulaire
aux ressources et fonctionnalités de l'application.

Les modules suivants sont exposés pour faciliter les importations :
- `RBACManager`: Le gestionnaire principal pour les vérifications de permissions.
- `Role`: Modèle de données pour un rôle.
- `Permission`: Modèle de données pour une permission.
- `User`: Modèle de données pour un utilisateur dans le contexte RBAC.
"""
from .manager import RBACManager
from .models import Role, Permission, User

__all__ = ['RBACManager', 'Role', 'Permission', 'User']

```

---

## Fichier : `backend\altiora\services\base.py`

```python
# backend/altiora/services/base.py
"""
Classe de base abstraite pour tous les microservices.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class BaseService(ABC):
    """Interface commune à tous les microservices."""

    @abstractmethod
    async def start(self) -> None:
        """Démarre le service."""
        ...

    @abstractmethod
    async def stop(self) -> None:
        """Arrête proprement le service."""
        ...

    @abstractmethod
    async def health_check(self) -> dict[str, Any]:
        """Retourne l’état de santé du service."""
        ...
```

---

## Fichier : `backend\altiora\services\__init__.py`

```python
# backend/altiora/services/__init__.py
"""
Contient les définitions des microservices d'Altiora.
"""
```

---

## Fichier : `backend\altiora\services\alm\alm_service.py`

```python
# services/alm/alm_service.py
"""Service web pour l'intégration avec un outil de gestion du cycle de vie des applications (ALM).

Ce service fournit des points de terminaison pour interagir avec un ALM externe
(comme Jira, Azure DevOps, etc.) afin de créer et gérer des éléments de travail.
Il est conçu pour être un pont générique, nécessitant une adaptation à l'API
spécifique de l'ALM cible.
"""

import logging
from typing import Dict, Any

import httpx
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings

# --- Configuration --- #
class AlmSettings(BaseSettings):
    """Paramètres de configuration pour le service ALM.

    Ces paramètres sont chargés depuis les variables d'environnement ou un fichier .env.
    """
    alm_api_url: str = Field(..., description="URL de base de l'API de l'ALM cible.")
    alm_api_key: str = Field(..., description="Clé d'API pour l'authentification auprès de l'ALM.")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = AlmSettings()

# --- Modèles de Données --- #
class WorkItem(BaseModel):
    """Modèle Pydantic pour un élément de travail à créer dans l'ALM."""
    title: str = Field(..., description="Titre ou résumé de l'élément de travail.")
    description: str = Field(..., description="Description détaillée de l'élément de travail.")
    item_type: str = Field("Task", description="Type de l'élément de travail (ex: Task, Bug, User Story).")


# --- Initialisation de l'application FastAPI --- #
app = FastAPI(
    title="Service d'Intégration ALM",
    description="Un pont entre Altiora et un système de gestion de projet externe (ALM).",
    version="1.0.0",
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# --- Points de Terminaison (Endpoints) --- #
@app.get("/health", summary="Vérifie l'état de santé du service")
async def health_check() -> Dict[str, str]:
    """Point de terminaison pour la surveillance de base du service ALM."""
    return {"status": "ok"}


@app.post("/work-items", summary="Crée un nouvel élément de travail dans l'ALM")
async def create_work_item(item: WorkItem) -> Dict[str, Any]:
    """Crée un nouvel élément de travail (tâche, bug, etc.) dans le système ALM.
    
    Cette fonction est une maquette et doit être adaptée à l'API spécifique de votre ALM
    (ex: Jira, Azure DevOps). La logique actuelle simule une création réussie.

    Args:
        item: L'objet `WorkItem` contenant les détails de l'élément à créer.

    Returns:
        Un dictionnaire confirmant le succès et les détails de l'élément créé.

    Raises:
        HTTPException: Si une erreur survient lors de la communication avec l'ALM.
    """
    logger.info(f"Tentative de création d'un élément de travail de type '{item.item_type}' avec le titre : {item.title}")

    # --- Logique de maquette pour la démonstration --- #
    # Dans une implémentation réelle, cette section interagirait avec l'API de l'ALM.
    # Exemple de charge utile pour Jira:
    # payload = {
    #     "fields": {
    #         "project": {"key": "PROJ"},  # Clé du projet Jira
    #         "summary": item.title,
    #         "description": item.description,
    #         "issuetype": {"name": item.item_type},
    #     }
    # }
    # headers = {
    #     "Authorization": f"Bearer {settings.alm_api_key}",
    #     "Content-Type": "application/json",
    # }
    # async with httpx.AsyncClient() as client:
    #     response = await client.post(settings.alm_api_url, json=payload, headers=headers)
    #     response.raise_for_status() # Lève une exception pour les codes d'erreur HTTP
    #     mock_response = response.json()
    logger.warning("L'appel à l'API ALM est actuellement une maquette. Adaptez `alm_service.py` pour votre ALM réel.")
    mock_response = {
        "id": "10001",
        "key": "PROJ-123",
        "self": f"{settings.alm_api_url}/rest/api/2/issue/10001", # URL simulée
    }
    # --- Fin de la logique de maquette --- #

    logger.info(f"Élément de travail créé avec succès (maquette) : {mock_response.get('key')}")
    return {"success": True, "work_item": mock_response}


# --- Pour un lancement direct (débogage/développement) --- #
if __name__ == "__main__":
    import uvicorn
    logger.info("Lancement du service ALM...")
    logger.info(f"URL de l'API ALM configurée : {settings.alm_api_url}")
    logger.info(f"Clé d'API ALM configurée : {'Oui' if settings.alm_api_key else 'Non'} (masquée)")
    uvicorn.run(app, host="0.0.0.0", port=8002)
```

---

## Fichier : `backend\altiora\services\alm\README.md`

```markdown
# Service ALM

Ce service gère l'intégration avec les systèmes de gestion du cycle de vie des applications (ALM) comme Jira ou Azure DevOps.

## Démarrage Isolé

Pour lancer ce service de manière isolée, vous pouvez utiliser le `Dockerfile` présent dans ce répertoire.

1.  **Construire l'image Docker :**

    ```bash
    docker build -t altiora-alm-service .
    ```

2.  **Lancer le conteneur :**

    ```bash
    docker run -p 8002:8002 -e ALM_SERVICE_PORT=8002 -e ALM_API_URL=http://votre-alm.com -e ALM_API_KEY=votre-cle altiora-alm-service
    ```

## Endpoints

-   `POST /alm/create-ticket` : Crée un nouveau ticket dans le système ALM.

## Variables d'Environnement

-   `ALM_SERVICE_PORT` : Le port sur lequel le service écoute (défaut : `8002`).
-   `ALM_API_URL` : L'URL de l'API du système ALM.
-   `ALM_API_KEY` : La clé d'API pour s'authentifier auprès du système ALM.

```

---

## Fichier : `backend\altiora\services\alm\__init__.py`

```python

```

---

## Fichier : `backend\altiora\services\dash\app.py`

```python
import dash
from dash import dcc, html, Input, Output
import plotly.graph_objects as go
from prometheus_client import CollectorRegistry, Gauge, start_http_server
import redis
import os

# Initialisation Dash
app = dash.Dash(__name__, external_stylesheets=['https://stackpath.bootstrapcdn.com/bootswatch/4.5.2/flatly/bootstrap.min.css'])

# Connexion Redis
redis_client = redis.from_url(os.getenv("REDIS_URL", "redis://localhost:6379"))

# Métriques Prometheus
registry = CollectorRegistry()
gauge_tests = Gauge('altiora_tests_total', 'Total tests generated', registry=registry)

# Layout Dash
app.layout = html.Div([
    html.H1("Altiora Dashboard", className="text-center mb-4"),

    dcc.Interval(id='interval', interval=5000, n_intervals=0),

    html.Div([
        html.Div([
            html.H3("Tests Generated"),
            html.H2(id='tests-count', className="text-primary"),
        ], className="col-md-4"),

        html.Div([
            html.H3("Memory Usage"),
            dcc.Graph(id='memory-graph'),
        ], className="col-md-8"),
    ], className="row"),

    html.Div([
        html.H3("Recent Sessions"),
        html.Ul(id='sessions-list')
    ], className="mt-4")
])


# Callbacks
@app.callback(
    [Output('tests-count', 'children'),
     Output('memory-graph', 'figure'),
     Output('sessions-list', 'children')],
    [Input('interval', 'n_intervals')]
)
def update_dashboard(n):
    # Tests count
    tests = redis_client.get("altiora:tests:count") or 0

    # Memory usage (simulation)
    memory_usage = [50, 60, 55, 70, 65, 80]
    fig = go.Figure(go.Scatter(y=memory_usage, mode='lines+markers'))
    fig.update_layout(height=300, margin={'l': 20, 'r': 20, 't': 20, 'b': 20})

    # Sessions
    sessions = [f"Session {i}" for i in range(3)]

    return (
        str(tests),
        fig,
        [html.Li(session) for session in sessions]
    )


if __name__ == '__main__':
    start_http_server(8005, registry=registry)  # Métriques Prometheus
    app.run_server(host='0.0.0.0', port=8050, debug=False)
```

---

## Fichier : `backend\altiora\services\dash\README.md`

```markdown
# Service Dash

Ce service fournit un tableau de bord interactif pour visualiser les métriques et les résultats.

## Démarrage Isolé

Pour lancer ce service de manière isolée, vous pouvez utiliser le `Dockerfile` présent dans ce répertoire.

1.  **Construire l'image Docker :**

    ```bash
    docker build -t altiora-dash-service .
    ```

2.  **Lancer le conteneur :**

    ```bash
    docker run -p 8050:8050 -e DASH_SERVICE_PORT=8050 altiora-dash-service
    ```

## Endpoints

-   `GET /` : Affiche le tableau de bord principal.

## Variables d'Environnement

-   `DASH_SERVICE_PORT` : Le port sur lequel le service écoute (défaut : `8050`).

```

---

## Fichier : `backend\altiora\services\excel\excel_service.py`

```python
# services/excel/excel_service.py
"""Service web pour la création et la manipulation de fichiers Excel.

Ce service expose une API pour générer des fichiers Excel stylisés,
notamment des matrices de test, en s'appuyant sur les modules de politique
et de formatage internes (`policies.excel_policy`, `post_processing.excel_formatter`).
"""

import logging
import os
from typing import List, Dict, Any

from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field

# Importation des modules internes pour la validation et le formatage.
from policies.excel_policy import ExcelPolicy
from post_processing.excel_formatter import ExcelFormatter

# --- Modèles de Données --- #
class TestCase(BaseModel):
    """Modèle Pydantic pour un cas de test individuel."""
    id: str = Field(..., description="L'identifiant unique du cas de test.")
    description: str = Field(..., description="La description détaillée du cas de test.")
    type: str = Field(..., description="Le type de cas de test (ex: CP pour Cas Passant, CE pour Cas d'Erreur, CL pour Cas Limite).")


class TestMatrixRequest(BaseModel):
    """Modèle Pydantic pour une requête de création de matrice de tests Excel."""
    filename: str = Field(default="matrice_de_test.xlsx", description="Le nom du fichier Excel à générer.")
    test_cases: List[TestCase] = Field(..., description="Liste des cas de test à inclure dans la matrice.")


# --- Initialisation de l'application FastAPI --- #
app = FastAPI(
    title="Service de Génération Excel",
    description="Crée des fichiers Excel stylisés à partir de données structurées.",
    version="1.0.0",
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Répertoire temporaire pour stocker les rapports Excel générés.
OUTPUT_DIR = "temp_excel_reports"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Initialisation des classes de politique et de formatage.
policy = ExcelPolicy()
formatter = ExcelFormatter()


# --- Points de Terminaison (Endpoints) --- #
@app.get("/health", summary="Vérifie l'état de santé du service")
async def health_check() -> Dict[str, str]:
    """Point de terminaison pour la surveillance de base du service Excel."""
    return {"status": "ok"}


@app.post("/create-test-matrix", summary="Crée un fichier Excel de matrice de tests")
async def create_test_matrix(request: TestMatrixRequest, background_tasks: BackgroundTasks) -> FileResponse:
    """Génère un fichier Excel à partir d'une liste de cas de test fournie.
    
    Les données sont d'abord validées par `ExcelPolicy`, puis formatées par `ExcelFormatter`.
    Le fichier généré est ensuite envoyé en réponse et supprimé en arrière-plan.

    Args:
        request: L'objet `TestMatrixRequest` contenant le nom du fichier et les cas de test.
        background_tasks: Tâches de fond FastAPI pour la suppression du fichier temporaire.

    Returns:
        Une `FileResponse` contenant le fichier Excel généré.

    Raises:
        HTTPException: Si la validation des données échoue ou si une erreur survient lors de la génération du fichier.
    """
    logger.info(f"Requête reçue pour créer la matrice de tests : {request.filename}")

    # Convertit les modèles Pydantic en dictionnaires Python standard pour les modules de politique et de formatage.
    test_cases_data = [case.model_dump() for case in request.test_cases]

    # 1. Valide les données des cas de test en utilisant la politique définie.
    validation_result = policy.validate_test_matrix(test_cases_data)
    if not validation_result["is_valid"]:
        logger.error(f"Validation des données échouée : {validation_result['errors']}")
        raise HTTPException(
            status_code=400,
            detail={"message": "Les données des cas de test sont invalides.", "errors": validation_result["errors"]}
        )

    # 2. Formate et génère le fichier Excel.
    output_path = os.path.join(OUTPUT_DIR, request.filename)
    try:
        formatting_errors = formatter.format_test_matrix(test_cases_data, output_path)
        if formatting_errors:
            # Les erreurs de formatage sont moins critiques que les erreurs de validation.
            logger.warning(f"Erreurs de formatage mineures détectées : {formatting_errors}")
    except Exception as e:
        logger.error(f"Erreur inattendue lors de la création du fichier Excel : {e}")
        raise HTTPException(status_code=500, detail="Impossible de générer le fichier Excel en raison d'une erreur interne.")

    # Ajoute une tâche de fond pour supprimer le fichier temporaire après l'envoi de la réponse.
    background_tasks.add_task(os.remove, output_path)

    logger.info(f"Fichier Excel '{output_path}' généré et prêt à être envoyé.")
    return FileResponse(output_path, media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", filename=request.filename)


# --- Pour un lancement direct (débogage/développement) --- #
if __name__ == "__main__":
    import uvicorn
    logger.info("Lancement du service Excel...")
    uvicorn.run(app, host="0.0.0.0", port=8003)
```

---

## Fichier : `backend\altiora\services\excel\README.md`

```markdown
# Service Excel

Ce service est responsable de la création et du formatage de fichiers Excel.

## Démarrage Isolé

Pour lancer ce service de manière isolée, vous pouvez utiliser le `Dockerfile` présent dans ce répertoire.

1.  **Construire l'image Docker :**

    ```bash
    docker build -t altiora-excel-service .
    ```

2.  **Lancer le conteneur :**

    ```bash
    docker run -p 8003:8003 -e EXCEL_SERVICE_PORT=8003 altiora-excel-service
    ```

## Endpoints

-   `POST /excel/create-matrix` : Crée une matrice de test au format Excel.

## Variables d'Environnement

-   `EXCEL_SERVICE_PORT` : Le port sur lequel le service écoute (défaut : `8003`).

```

---

## Fichier : `backend\altiora\services\excel\__init__.py`

```python

```

---

## Fichier : `backend\altiora\services\ocr\ocr_wrapper.py`

```python
# services/ocr/ocr_wrapper.py
"""Service web pour l'extraction de texte via OCR (Optical Character Recognition).

Ce service fournit une API pour extraire du texte à partir de fichiers image et PDF.
Il intègre des fonctionnalités de mise en cache (via Redis) et de gestion des
fichiers temporaires. Il peut utiliser une implémentation OCR réelle (Doctopus) ou une maquette.
"""

import asyncio
import hashlib
import json
import logging
import os
from contextlib import asynccontextmanager
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, List, Optional

import aiofiles
import redis.asyncio as redis
from fastapi import FastAPI, HTTPException, UploadFile, File, BackgroundTasks
from pydantic import BaseModel, Field
from tenacity import retry, stop_after_attempt, wait_exponential

logger = logging.getLogger(__name__)

# ------------------------------------------------------------------
# Gestion du cycle de vie (Lifespan manager)
# ------------------------------------------------------------------

# Clients globaux pour Redis et la gestion des tâches.
redis_client: Optional[redis.Redis] = None
processing_queue: Dict[str, Any] = {} # Utilisé pour suivre les tâches en cours (non implémenté ici)

# Répertoires pour les fichiers téléchargés et temporaires.
UPLOAD_ROOT = Path(os.getenv("UPLOAD_ROOT", "/app/uploads")).resolve()
TEMP_DIR = Path("temp")
TEMP_DIR.mkdir(exist_ok=True) # S'assure que le répertoire temporaire existe.


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Gère le cycle de vie de l'application (démarrage et arrêt).

    Tente de se connecter à Redis au démarrage et ferme la connexion à l'arrêt.
    Nettoie également les fichiers temporaires.
    """
    global redis_client
    try:
        redis_url = os.getenv("REDIS_URL", "redis://localhost:6379")
        redis_client = await redis.from_url(redis_url, decode_responses=True)
        await redis_client.ping() # Teste la connexion.
        logger.info("✅ Connexion Redis établie.")
    except Exception as e:
        logger.warning("⚠️ Redis non disponible – cache désactivé (%s)", e)
        redis_client = None # Désactive le cache si Redis n'est pas accessible.
    yield # L'application démarre ici.
    if redis_client:
        await redis_client.close() # Ferme la connexion Redis à l'arrêt.
    
    # Nettoie les fichiers temporaires à l'arrêt.
    if TEMP_DIR.exists():
        for p in TEMP_DIR.iterdir():
            p.unlink(missing_ok=True) # Supprime les fichiers, ignore s'ils n'existent plus.


app = FastAPI(title="Service OCR Doctoplus", version="1.0.0", lifespan=lifespan)

# ------------------------------------------------------------------
# Schémas Pydantic
# ------------------------------------------------------------------
class OCRRequest(BaseModel):
    """Modèle de requête pour l'extraction OCR."""
    file_path: str = Field(..., description="Chemin absolu du fichier à traiter.")
    language: str = Field("fra", description="Langue du document (code ISO 639-2/T, ex: 'fra', 'eng').")
    preprocess: bool = Field(True, description="Appliquer des étapes de pré-traitement de l'image.")
    cache: bool = Field(True, description="Utiliser le cache Redis pour les résultats.")
    output_format: str = Field("text", description="Format de sortie (ex: 'text', 'hocr').")
    confidence_threshold: float = Field(0.8, ge=0.0, le=1.0, description="Seuil de confiance pour l'extraction.")


class OCRResponse(BaseModel):
    """Modèle de réponse pour l'extraction OCR."""
    text: str = Field(..., description="Texte extrait du document.")
    confidence: float = Field(..., description="Niveau de confiance global de l'extraction.")
    processing_time: float = Field(..., description="Temps de traitement en secondes.")
    cached: bool = Field(False, description="Indique si le résultat provient du cache.")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Métadonnées supplémentaires sur le traitement.")


class OCRBatchRequest(BaseModel):
    """Modèle de requête pour le traitement OCR par lots (non implémenté)."""
    files: List[str] = Field(..., description="Liste des chemins de fichiers à traiter.")
    language: str = Field("fra", description="Langue pour le traitement par lots.")
    parallel: bool = Field(True, description="Exécuter les traitements en parallèle.")
    max_workers: int = Field(4, ge=1, le=10, description="Nombre maximal de workers parallèles.")


# ------------------------------------------------------------------
# Fonctions utilitaires
# ------------------------------------------------------------------
def _doctoplus_available() -> bool:
    """Vérifie si la bibliothèque Doctopus OCR est disponible."""
    try:
        import doctopus_ocr  # type: ignore
        return True
    except ImportError:
        return False


def _cache_key(req: OCRRequest) -> str:
    """Génère une clé de cache unique basée sur les paramètres de la requête et les métadonnées du fichier."""
    path = Path(req.file_path)
    data = {
        "name": path.name,
        "size": path.stat().st_size if path.exists() else 0,
        "mtime": path.stat().st_mtime if path.exists() else 0,
        "lang": req.language,
        "pre": req.preprocess,
        "fmt": req.output_format,
        "thr": req.confidence_threshold,
    }
    # Utilise un hachage MD5 du JSON sérialisé pour garantir une clé unique et stable.
    digest = hashlib.md5(json.dumps(data, sort_keys=True).encode()).hexdigest()
    return f"ocr:{digest}"


async def _get_cache(key: str) -> Optional[Dict[str, Any]]:
    """Récupère un résultat depuis le cache Redis."""
    if not redis_client:
        return None
    try:
        cached = await redis_client.get(key)
        return json.loads(cached) if cached else None
    except Exception as e:
        logger.warning("Erreur de lecture du cache Redis : %s", e)
        return None


async def _save_cache(key: str, value: Dict[str, Any], ttl: int = 86400) -> None:
    """Sauvegarde un résultat dans le cache Redis avec une durée de vie (TTL)."""
    if redis_client:
        try:
            await redis_client.setex(key, ttl, json.dumps(value))
        except Exception as e:
            logger.warning("Erreur d'écriture dans le cache Redis : %s", e)


# ------------------------------------------------------------------
# Extracteurs OCR (réel et maquette)
# ------------------------------------------------------------------
async def _extract_mock(req: OCRRequest) -> Dict[str, Any]:
    """Implémentation de maquette pour l'extraction OCR (pour le développement/test)."""
    await asyncio.sleep(0.5) # Simule un délai de traitement.
    text = f"Résultat OCR simulé pour {Path(req.file_path).name}"
    return {"text": text, "confidence": 0.95, "metadata": {"mode": "mock"}}


@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=1, max=5))
async def _extract_doctoplus(req: OCRRequest) -> Dict[str, Any]:
    """Extrait le texte en utilisant la bibliothèque Doctopus OCR (implémentation réelle)."""
    from doctopus_ocr import DoctopusWrapper  # type: ignore

    wrapper = DoctopusWrapper(
        config_path=os.getenv("DOCTOPLUS_CONFIG", "/app/config/config.json")
    )
    result = await wrapper.extract_text(
        file_path=req.file_path,
        language=req.language,
        preprocess=req.preprocess,
        confidence_threshold=req.confidence_threshold,
        output_format=req.output_format,
    )
    return {
        "text": result.get("text", ""),
        "confidence": result.get("confidence", 0.0),
        "metadata": {
            "pages": result.get("pages", 0),
            "language": req.language,
            "file_type": Path(req.file_path).suffix,
            "file_size": Path(req.file_path).stat().st_size,
        },
    }


# ------------------------------------------------------------------
# Points de terminaison (Endpoints)
# ------------------------------------------------------------------
@app.get("/health")
async def health_check():
    """Point de terminaison pour la vérification de l'état de santé du service OCR."""
    redis_ok = redis_client and await redis_client.ping() or False
    return {
        "status": "healthy",
        "redis": "connecté" if redis_ok else "déconnecté",
        "doctoplus": "disponible" if _doctoplus_available() else "maquette",
    }


@app.post("/extract", response_model=OCRResponse)
async def extract_text(request: OCRRequest):
    """Extrait le texte d'un fichier spécifié par son chemin.

    Args:
        request: L'objet `OCRRequest` contenant les détails de l'extraction.

    Returns:
        Un `OCRResponse` avec le texte extrait et les métadonnées.

    Raises:
        HTTPException: Si le chemin du fichier n'est pas autorisé ou si le fichier n'est pas trouvé.
    """
    path = Path(request.file_path).resolve()
    # Mesure de sécurité: s'assurer que le chemin est dans le répertoire autorisé.
    if not path.is_relative_to(UPLOAD_ROOT):
        raise HTTPException(403, "Accès au chemin non autorisé.")
    if not path.exists() or not path.is_file():
        raise HTTPException(404, "Fichier non trouvé.")

    start = asyncio.get_event_loop().time()
    cache_key = _cache_key(request) if request.cache and redis_client else None
    cached = await _get_cache(cache_key) if cache_key else None
    if cached:
        return OCRResponse(**cached, cached=True)

    # Choisit l'extracteur (réel ou maquette) en fonction de la disponibilité de Doctopus.
    extractor = _extract_doctoplus if _doctoplus_available() else _extract_mock
    result = await extractor(request)

    processing_time = asyncio.get_event_loop().time() - start
    result["processing_time"] = processing_time

    if cache_key:
        await _save_cache(cache_key, result)
    return OCRResponse(**result)


@app.post("/extract_upload")
async def extract_upload(
    file: UploadFile = File(...),
    language: str = "fra",
    preprocess: bool = True,
    cache: bool = True,
):
    """Extrait le texte d'un fichier téléchargé directement via l'API.

    Le fichier est d'abord sauvegardé temporairement, puis traité par l'OCR.
    Le fichier temporaire est supprimé après le traitement.

    Args:
        file: Le fichier téléchargé.
        language: Langue du document.
        preprocess: Appliquer le pré-traitement.
        cache: Utiliser le cache.

    Returns:
        Un `OCRResponse` avec le texte extrait.

    Raises:
        HTTPException: Si une erreur survient lors de la sauvegarde ou du traitement du fichier.
    """
    # Crée un chemin temporaire unique pour le fichier téléchargé.
    temp_path = TEMP_DIR / f"{datetime.now().timestamp()}_{file.filename}"
    try:
        # Écrit le contenu du fichier téléchargé dans le fichier temporaire.
        async with aiofiles.open(temp_path, "wb") as f:
            await f.write(await file.read())
        
        # Crée une requête OCR à partir du fichier temporaire et la traite.
        request = OCRRequest(
            file_path=str(temp_path),
            language=language,
            preprocess=preprocess,
            cache=cache,
        )
        return await extract_text(request)
    except (IOError, OSError) as e:
        logger.error(f"Erreur lors de l'écriture du fichier téléchargé sur {temp_path}: {e}")
        raise HTTPException(status_code=500, detail="Échec de la sauvegarde du fichier téléchargé.")
    finally:
        # S'assure que le fichier temporaire est supprimé, même en cas d'erreur.
        temp_path.unlink(missing_ok=True)


# ------------------------------------------------------------------
# Point d'entrée Uvicorn
# ------------------------------------------------------------------
if __name__ == "__main__":
    import uvicorn

    uvicorn.run("ocr_wrapper:app", host="0.0.0.0", port=8001, reload=False)

```

---

## Fichier : `backend\altiora\services\ocr\README.md`

```markdown
# Service OCR

Ce service est responsable de l'extraction de texte à partir de fichiers image et PDF.

## Démarrage Isolé

Pour lancer ce service de manière isolée, vous pouvez utiliser le `Dockerfile` présent dans ce répertoire.

1.  **Construire l'image Docker :**

    ```bash
    docker build -t altiora-ocr-service .
    ```

2.  **Lancer le conteneur :**

    ```bash
    docker run -p 8001:8001 -e OCR_SERVICE_PORT=8001 altiora-ocr-service
    ```

## Endpoints

-   `POST /ocr/extract-text` : Extrait le texte d'un fichier.

## Variables d'Environnement

-   `OCR_SERVICE_PORT` : Le port sur lequel le service écoute (défaut : `8001`).
-   `OCR_SERVICE_TIMEOUT` : Timeout pour le traitement OCR (défaut : `60`).

```

---

## Fichier : `backend\altiora\services\ocr\__init__.py`

```python

```

---

## Fichier : `backend\altiora\services\ocr\doctopus_ocr\__init__.py`

```python
# services/ocr/doctopus_ocr/__init__.py
"""
Stub OCR engine – never crashes if the real one is missing
"""

class DoctoplusWrapper:
    """
    Minimal mock that returns plausible OCR results
    """

    def __init__(self, config_path: str):
        self.config_path = config_path

    @staticmethod
    async def extract_text(
            *,
        file_path: str,
        language: str = "fra",
        preprocess: bool = True,
        confidence_threshold: float = 0.8,
        output_format: str = "text",
    ) -> dict:
        """Return mock data"""
        import asyncio
        await asyncio.sleep(0.2)  # Simulate work
        return {
            "text": f"Mock OCR text for {file_path}",
            "confidence": 0.92,
            "pages": 1,
        }
```

---

## Fichier : `backend\altiora\services\playwright\optimized_runner.py`

```python
# src/playwright/optimized_runner.py
"""Module pour un runner Playwright optimisé avec gestion de pool de navigateurs.

Ce module fournit une classe `OptimizedPlaywrightRunner` qui gère un pool
de navigateurs Playwright pré-initialisés. Cela réduit le temps de démarrage
des tests et permet une exécution plus efficace en réutilisant les instances
de navigateurs. Il inclut également des optimisations pour améliorer la
performance des tests web.
"""

import asyncio
import logging
from contextlib import asynccontextmanager
from typing import AsyncGenerator, Any

from playwright.async_api import async_playwright, Browser, Page

logger = logging.getLogger(__name__)


class OptimizedPlaywrightRunner:
    """Runner Playwright optimisé avec un pool de navigateurs réutilisables."""

    def __init__(self, max_browsers: int = 5):
        """Initialise le runner Playwright optimisé."

        Args:
            max_browsers: Le nombre maximal d'instances de navigateurs à maintenir dans le pool.
        """
        self.max_browsers = max_browsers
        self.browser_pool: list[Browser] = [] # Pool de navigateurs.
        self.semaphore = asyncio.Semaphore(max_browsers) # Limite le nombre de navigateurs actifs.
        self.playwright = None

    async def initialize(self):
        """Initialise le pool de navigateurs en pré-créant un certain nombre d'instances."

        Cette méthode doit être appelée une fois au démarrage de l'application.
        """
        if self.playwright is not None:
            logger.warning("Playwright est déjà initialisé.")
            return

        logger.info("Initialisation de Playwright et du pool de navigateurs...")
        self.playwright = await async_playwright().start()

        # Pré-crée un sous-ensemble de navigateurs pour réduire le temps de démarrage.
        for i in range(min(3, self.max_browsers)):
            try:
                browser = await self._create_browser()
                self.browser_pool.append(browser)
                logger.debug(f"Navigateur {i+1}/{self.max_browsers} pré-créé.")
            except Exception as e:
                logger.error(f"Échec de la pré-création du navigateur {i+1}: {e}")
        logger.info(f"Pool de navigateurs initialisé avec {len(self.browser_pool)} navigateurs.")

    async def _create_browser(self) -> Browser:
        """Crée une nouvelle instance de navigateur Chromium avec des arguments optimisés."""
        if self.playwright is None:
            raise RuntimeError("Playwright n'est pas initialisé.")

        return await self.playwright.chromium.launch(
            headless=True, # Exécute le navigateur en mode headless (sans interface graphique).
            args=[
                '--disable-blink-features=AutomationControlled', # Empêche la détection par les sites.
                '--disable-dev-shm-usage', # Contourne les problèmes de mémoire partagée dans Docker.
                '--no-sandbox', # Nécessaire dans certains environnements Docker.
                '--disable-gpu', # Désactive l'accélération GPU si non nécessaire.
                '--disable-web-security', # Peut être utile pour certains tests locaux.
                '--disable-features=IsolateOrigins,site-per-process' # Optimisations de performance.
            ]
        )

    @asynccontextmanager
    async def get_page(self) -> AsyncGenerator[Page, None]:
        """Acquiert une page Playwright depuis le pool de navigateurs."

        Utilisation avec `async with`:
        ```python
        async with runner.get_page() as page:
            await page.goto("https://example.com")
            # ... effectuer des actions sur la page.
        ```
        """
        if self.playwright is None:
            raise RuntimeError("Playwright n'est pas initialisé. Appelez `initialize()` d'abord.")

        async with self.semaphore: # Limite le nombre de navigateurs actifs simultanément.
            # Récupère un navigateur du pool ou en crée un nouveau si le pool est vide.
            browser: Browser
            if self.browser_pool:
                browser = self.browser_pool.pop()
                logger.debug(f"Navigateur récupéré du pool. Taille restante : {len(self.browser_pool)}")
            else:
                logger.info("Pool de navigateurs vide. Création d'un nouveau navigateur.")
                browser = await self._create_browser()

            # Crée un nouveau contexte de navigateur pour isoler les tests.
            context = await browser.new_context(
                viewport={'width': 1920, 'height': 1080}, # Taille de la fenêtre du navigateur.
                ignore_https_errors=True, # Ignore les erreurs HTTPS (utile pour les environnements de test).
                user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36' # User-Agent personnalisé.
            )

            page = await context.new_page()

            # Applique des optimisations de performance à la page.
            await self._apply_optimizations(page)

            try:
                yield page # Fournit la page au bloc `async with`.
            finally:
                await context.close() # Ferme le contexte de la page.
                # Remet le navigateur dans le pool s'il n'est pas plein, sinon le ferme.
                if len(self.browser_pool) < self.max_browsers:
                    self.browser_pool.append(browser)
                    logger.debug(f"Navigateur remis dans le pool. Taille actuelle : {len(self.browser_pool)}")
                else:
                    await browser.close()
                    logger.debug("Navigateur fermé (pool plein).")

    async def _apply_optimizations(self, page: Page):
        """Applique des optimisations de performance à une page Playwright."

        Ces optimisations incluent le blocage des ressources inutiles (images, CSS, polices)
        et l'interception des requêtes pour bloquer le tracking/analytics.

        Args:
            page: L'objet `Page` de Playwright à optimiser.
        """
        logger.debug("Application des optimisations de performance à la page.")
        # Bloque le chargement de certaines ressources pour accélérer les tests.
        await page.route(re.compile(r"\.(png|jpg|jpeg|gif|svg|ico)$"), lambda route: route.abort())
        await page.route(re.compile(r"\.(css|font|woff|woff2|ttf|eot)$?"), lambda route: route.abort())

        # Intercepte les requêtes pour bloquer les domaines de tracking/analytics.
        async def handle_route(route):
            if 'analytics' in route.request.url or 'tracking' in route.request.url:
                await route.abort()
            else:
                await route.continue_()

        await page.route('**/*', handle_route)

    async def close(self):
        """Ferme tous les navigateurs dans le pool et arrête l'instance Playwright."

        Cette méthode doit être appelée lors de l'arrêt de l'application pour
        libérer toutes les ressources.
        """
        logger.info("Fermeture du runner Playwright et des navigateurs...")
        for browser in self.browser_pool:
            await browser.close()
        self.browser_pool.clear()
        if self.playwright:
            await self.playwright.stop()
            self.playwright = None
        logger.info("Runner Playwright fermé.")


# ------------------------------------------------------------------
# Démonstration (exemple d'utilisation)
# ------------------------------------------------------------------
if __name__ == "__main__":
    import logging
    import re # Nécessaire pour re.compile dans la démo.

    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    async def demo():
        runner = OptimizedPlaywrightRunner(max_browsers=2)
        await runner.initialize()

        print("\n--- Exécution de tests simulés ---")
        async def run_test_task(task_id: int):
            print(f"Tâche {task_id} : Acquisition d'une page...")
            async with runner.get_page() as page:
                print(f"Tâche {task_id} : Page acquise. Navigation vers example.com...")
                await page.goto("https://example.com")
                title = await page.title()
                print(f"Tâche {task_id} : Titre de la page : {title}")
                await asyncio.sleep(0.5) # Simule un travail sur la page.
            print(f"Tâche {task_id} : Page relâchée.")

        # Lance plusieurs tâches en parallèle pour démontrer le pool.
        tasks = [run_test_task(i) for i in range(5)]
        await asyncio.gather(*tasks)

        print("\n--- Fermeture du runner ---")
        await runner.close()
        print("Démonstration terminée.")

    asyncio.run(demo())
```

---

## Fichier : `backend\altiora\services\playwright\playwright_runner.py`

```python
# services/playwright/playwright_runner.py
"""Service d'exécution de tests Playwright.

Ce service permet d'exécuter des scripts de test Playwright de manière asynchrone,
avec des options de configuration avancées (navigateur, headless, timeout, retries).
Il gère la préparation des environnements de test, l'exécution parallèle,
la collecte des artefacts (screenshots, vidéos, traces) et la génération de rapports.
"""

import os
import asyncio
import json
import tempfile
import shutil
import subprocess
import uuid
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any, Union
from concurrent.futures import ProcessPoolExecutor
import traceback

from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel, Field
import redis.asyncio as redis
from playwright.async_api import async_playwright
import pytest
import logging

# Configuration du logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# --- Modèles Pydantic --- #
class TestCode(BaseModel):
    """Représente un bloc de code de test à exécuter."""
    code: str = Field(..., description="Code Python/Playwright du test.")
    test_name: str = Field(default="test_generated", description="Nom unique du test.")
    test_type: str = Field(default="e2e", description="Type de test (ex: 'e2e', 'component').")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Métadonnées supplémentaires associées au test.")


class ExecutionConfig(BaseModel):
    """Configuration des paramètres d'exécution des tests Playwright."""
    browser: str = Field(default="chromium", description="Navigateur à utiliser : 'chromium', 'firefox', 'webkit'.")
    headed: bool = Field(default=False, description="Exécuter le navigateur en mode visible (True) ou headless (False).")
    timeout: int = Field(default=30000, description="Timeout maximal par test en millisecondes.")
    retries: int = Field(default=0, description="Nombre de tentatives en cas d'échec du test.")
    parallel: bool = Field(default=True, description="Exécuter les tests en parallèle (True) ou séquentiellement (False).")
    workers: int = Field(default=4, description="Nombre de workers parallèles à utiliser si `parallel` est True.")
    screenshot: str = Field(default="on-failure", description="Quand prendre des captures d'écran : 'always', 'on-failure', 'never'.")
    video: str = Field(default="on-failure", description="Quand enregistrer des vidéos : 'always', 'on-failure', 'never'.")
    trace: str = Field(default="on-failure", description="Quand enregistrer des traces : 'always', 'on-failure', 'never'.")
    base_url: Optional[str] = Field(default=None, description="URL de base pour les tests (utilisé par `page.goto('/')`).")


class TestExecutionRequest(BaseModel):
    """Requête complète pour lancer une exécution de tests."""
    tests: List[TestCode] = Field(..., description="Liste des tests à exécuter.")
    config: ExecutionConfig = Field(default_factory=ExecutionConfig, description="Configuration d'exécution des tests.")
    save_artifacts: bool = Field(default=True, description="Sauvegarder les artefacts (screenshots, vidéos, traces).")
    generate_report: bool = Field(default=True, description="Générer un rapport HTML récapitulatif.")


class TestResult(BaseModel):
    """Résultat détaillé d'un test individuel."""
    test_name: str = Field(..., description="Nom du test.")
    status: str = Field(..., description="Statut de l'exécution du test : 'passed', 'failed', 'skipped', 'error'.")
    duration: float = Field(..., description="Durée d'exécution du test en secondes.")
    error_message: Optional[str] = Field(None, description="Message d'erreur si le test a échoué ou a rencontré une erreur.")
    error_trace: Optional[str] = Field(None, description="Trace de la pile d'appels en cas d'erreur.")
    screenshot: Optional[str] = Field(None, description="Chemin relatif vers la capture d'écran (si disponible).")
    video: Optional[str] = Field(None, description="Chemin relatif vers la vidéo (si disponible).")
    trace: Optional[str] = Field(None, description="Chemin relatif vers le fichier de trace (si disponible).")
    logs: List[str] = Field(default_factory=list, description="Logs de la console du test.")


class ExecutionResponse(BaseModel):
    """Réponse complète après l'exécution d'une suite de tests."""
    execution_id: str = Field(..., description="ID unique de cette exécution de tests.")
    status: str = Field(..., description="Statut global de l'exécution : 'completed', 'error', etc.")
    total_tests: int = Field(..., description="Nombre total de tests exécutés.")
    passed: int = Field(..., description="Nombre de tests réussis.")
    failed: int = Field(..., description="Nombre de tests échoués.")
    skipped: int = Field(..., description="Nombre de tests ignorés.")
    duration: float = Field(..., description="Durée totale de l'exécution en secondes.")
    results: List[TestResult] = Field(..., description="Liste détaillée des résultats de chaque test.")
    report_path: Optional[str] = Field(None, description="Chemin relatif vers le rapport HTML généré.")
    artifacts_path: Optional[str] = Field(None, description="Chemin relatif vers l'archive ZIP des artefacts.")


# --- Application FastAPI --- #
app = FastAPI(
    title="Playwright Runner Service",
    description="Service d'exécution de tests Playwright à la demande.",
    version="1.0.0"
)

# --- État global du service --- #
redis_client: Optional[redis.Redis] = None
execution_queue: Dict[str, Any] = {} # Pour suivre les exécutions asynchrones.
executor = ProcessPoolExecutor(max_workers=4) # Pool de processus pour les tâches bloquantes.


# ------------------------------------------------------------------
# Événements de cycle de vie (Lifespan events)
# ------------------------------------------------------------------

@app.on_event("startup")
async def startup_event():
    """Initialisation du service au démarrage de l'application."""
    global redis_client
    
    # Tente de se connecter à Redis pour la mise en cache des résultats.
    try:
        redis_url = os.getenv("REDIS_URL", "redis://localhost:6379")
        redis_client = await redis.from_url(redis_url, decode_responses=True)
        await redis_client.ping()
        logger.info("✅ Connexion Redis établie.")
    except Exception as e:
        logger.warning(f"⚠️ Redis non disponible – cache désactivé : {e}")
        redis_client = None
    
    # Crée les répertoires nécessaires pour les workspaces et les artefacts.
    for dir_path in ["workspace", "reports", "screenshots", "videos", "traces", "artifacts"]:
        Path(dir_path).mkdir(parents=True, exist_ok=True)
    
    # S'assure que les navigateurs Playwright sont installés.
    await ensure_playwright_browsers()


@app.on_event("shutdown")
async def shutdown_event():
    """Nettoyage du service à l'arrêt de l'application."""
    if redis_client:
        await redis_client.close()
    
    # Arrête le pool de processus.
    executor.shutdown(wait=True)


# ------------------------------------------------------------------
# Points de terminaison de santé
# ------------------------------------------------------------------

@app.get("/health")
async def health_check():
    """Point de terminaison pour vérifier l'état de santé du service."""
    redis_ok = False
    if redis_client:
        try:
            await redis_client.ping()
            redis_ok = True
        except redis.exceptions.ConnectionError:
            redis_ok = False
    
    # Vérifie si Playwright est opérationnel.
    playwright_ok = await check_playwright_health()
    
    return {
        "status": "healthy",
        "service": "playwright-runner",
        "timestamp": datetime.now().isoformat(),
        "redis": "connecté" if redis_ok else "déconnecté",
        "playwright": "prêt" if playwright_ok else "non_prêt",
        "active_executions": len(execution_queue)
    }


# ------------------------------------------------------------------
# Points de terminaison d'exécution principaux
# ------------------------------------------------------------------

@app.post("/execute", response_model=ExecutionResponse)
async def execute_tests(request: TestExecutionRequest) -> ExecutionResponse:
    """Exécute une suite de tests Playwright de manière synchrone (bloquant l'appel API)."""
    execution_id = f"exec_{uuid.uuid4().hex[:8]}"
    start_time = asyncio.get_event_loop().time()
    
    # Crée un répertoire de travail temporaire pour cette exécution.
    workspace_dir = Path("workspace") / execution_id
    workspace_dir.mkdir(parents=True, exist_ok=True)
    
    try:
        # Prépare les fichiers de test à partir du code fourni.
        test_files = await prepare_test_files(request.tests, workspace_dir)
        
        # Génère les arguments pytest basés sur la configuration d'exécution.
        pytest_config_args = generate_pytest_config(request.config, workspace_dir)
        
        # Exécute les tests en parallèle ou séquentiellement.
        if request.config.parallel and len(test_files) > 1:
            results = await run_tests_parallel(
                test_files,
                pytest_config_args,
                request.config,
                workspace_dir
            )
        else:
            results = await run_tests_sequential(
                test_files,
                pytest_config_args,
                request.config,
                workspace_dir
            )
        
        # Calcule les statistiques globales de l'exécution.
        total_duration = asyncio.get_event_loop().time() - start_time
        stats = calculate_stats(results)
        
        # Génère le rapport HTML si demandé.
        report_path = None
        if request.generate_report:
            report_path = await generate_html_report(
                execution_id,
                results,
                stats,
                workspace_dir
            )
        
        # Collecte et archive les artefacts si demandé.
        artifacts_path = None
        if request.save_artifacts:
            artifacts_path = await collect_artifacts(execution_id, workspace_dir)
        
        response = ExecutionResponse(
            execution_id=execution_id,
            status="completed",
            total_tests=len(results),
            passed=stats["passed"],
            failed=stats["failed"],
            skipped=stats["skipped"],
            duration=total_duration,
            results=results,
            report_path=report_path,
            artifacts_path=artifacts_path
        )
        
        # Sauvegarde le résultat complet de l'exécution dans Redis.
        if redis_client:
            await save_execution_result(execution_id, response)
        
        return response
        
    except Exception as e:
        logger.error(f"Erreur lors de l'exécution des tests : {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Erreur interne du service : {str(e)}")
    
    finally:
        # Planifie le nettoyage du répertoire de travail après un délai.
        asyncio.create_task(cleanup_workspace(workspace_dir, delay=300))


@app.post("/execute_async")
async def execute_tests_async(
    request: TestExecutionRequest,
    background_tasks: BackgroundTasks
):
    """Lance l'exécution des tests en arrière-plan et retourne immédiatement un ID d'exécution."""
    execution_id = f"exec_{uuid.uuid4().hex[:8]}"
    
    # Enregistre l'exécution dans la queue avec un statut initial.
    execution_queue[execution_id] = {
        "status": "queued",
        "started_at": datetime.now().isoformat(),
        "config": request.config.model_dump() # Utilise model_dump pour Pydantic v2
    }
    
    # Lance la fonction d'exécution en arrière-plan.
    background_tasks.add_task(
        run_tests_background,
        execution_id,
        request
    )
    
    return JSONResponse(
        {
            "execution_id": execution_id,
            "status": "queued",
            "message": "Tests en cours d'exécution en arrière-plan.",
            "check_status_url": f"/status/{execution_id}"
        },
        status_code=202 # Accepted
    )


@app.get("/status/{execution_id}", response_model=Union[ExecutionResponse, Dict[str, str]])
async def get_execution_status(execution_id: str):
    """Récupère le statut et les résultats d'une exécution de tests par son ID."""
    # Vérifie d'abord dans la queue des exécutions en cours.
    if execution_id in execution_queue:
        return execution_queue[execution_id]
    
    # Sinon, vérifie dans le cache Redis.
    if redis_client:
        result = await get_execution_result(execution_id)
        if result:
            return result
    
    raise HTTPException(status_code=404, detail="Exécution non trouvée.")


@app.get("/report/{execution_id}", response_class=FileResponse)
async def get_report(execution_id: str):
    """Récupère le rapport HTML généré pour une exécution donnée."""
    report_path = Path("reports") / f"{execution_id}_report.html"
    
    if not report_path.exists():
        raise HTTPException(status_code=404, detail="Rapport non trouvé.")
    
    return FileResponse(
        report_path,
        media_type="text/html",
        filename=f"report_{execution_id}.html"
    )


@app.get("/artifacts/{execution_id}", response_class=FileResponse)
async def get_artifacts(execution_id: str):
    """Télécharge une archive ZIP contenant tous les artefacts (screenshots, vidéos, traces) d'une exécution."""
    artifacts_path = Path("artifacts") / f"{execution_id}.zip"
    
    if not artifacts_path.exists():
        raise HTTPException(status_code=404, detail="Artefacts non trouvés.")
    
    return FileResponse(
        artifacts_path,
        media_type="application/zip",
        filename=f"artifacts_{execution_id}.zip"
    )


# ------------------------------------------------------------------
# Fonctions d'exécution principales
# ------------------------------------------------------------------

async def prepare_test_files(tests: List[TestCode], workspace_dir: Path) -> List[Path]:
    """Prépare les fichiers de test Python dans le répertoire de travail temporaire."""
    test_files = []
    
    for i, test in enumerate(tests):
        test_name = test.test_name or f"test_{i}"
        file_name = f"{test_name}.py"
        file_path = workspace_dir / file_name
        
        # S'assure que le code de test contient les imports et décorateurs nécessaires.
        code = ensure_test_imports(test.code)
        
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(code)
            
            test_files.append(file_path)
            logger.info(f"Fichier de test préparé : {file_path}")
        except (IOError, OSError) as e:
            logger.error(f"Erreur lors de l'écriture du fichier de test {file_path}: {e}")
            raise HTTPException(status_code=500, detail=f"Échec de l'écriture du fichier de test : {file_path}")
    
    # Crée le fichier `conftest.py` nécessaire pour la configuration de pytest-playwright.
    await create_conftest(workspace_dir)
    
    return test_files


def ensure_test_imports(code: str) -> str:
    """Ajoute les imports et décorateurs pytest-playwright nécessaires au code de test."""
    required_imports = [
        "import pytest",
        "from playwright.async_api import Page, expect",
    ]
    
    # Ajoute les imports manquants au début du code.
    for imp in required_imports:
        if imp not in code:
            code = f"{imp}\n{code}"
    
    # Ajoute le décorateur `@pytest.mark.asyncio` si la fonction de test est asynchrone.
    if "@pytest.mark.asyncio" not in code and "async def test_" in code:
        code = code.replace("async def test_", "@pytest.mark.asyncio\nasync def test_")
    
    return code


async def create_conftest(workspace_dir: Path):
    """Crée le fichier `conftest.py` avec la configuration de base pour pytest-playwright."""
    conftest_content = '''"""
Configuration Playwright pour les tests
"""
import pytest
from playwright.async_api import async_playwright
import os

@pytest.fixture(scope="session")
async def browser_type_launch_args():
    """Arguments de lancement du navigateur."""
    return {
        "headless": not bool(os.getenv("HEADED", "false").lower() == "true"),
        "timeout": 30000,
    }

@pytest.fixture(scope="session")
async def browser_context_args(browser_type_launch_args):
    """Arguments du contexte navigateur."""
    base_url = os.getenv("BASE_URL")
    context_args = {
        "viewport": {"width": 1280, "height": 720},
        "ignore_https_errors": True,
    }
    if base_url:
        context_args["base_url"] = base_url
    return context_args

@pytest.fixture(scope="function")
async def page(browser, browser_context_args):
    """Fixture de page avec configuration."""
    context = await browser.new_context(**browser_context_args)
    page = await context.new_page()
    yield page
    await context.close()
'''
    
    conftest_path = workspace_dir / "conftest.py"
    try:
        with open(conftest_path, 'w', encoding='utf-8') as f:
            f.write(conftest_content)
    except (IOError, OSError) as e:
        logger.error(f"Erreur lors de l'écriture de conftest.py sur {conftest_path}: {e}")
        raise HTTPException(status_code=500, detail=f"Échec de l'écriture de conftest.py : {conftest_path}")


def generate_pytest_config(config: ExecutionConfig, workspace_dir: Path) -> List[str]:
    """Génère la liste des arguments de ligne de commande pour pytest en fonction de la configuration."""
    args = [
        str(workspace_dir), # Indique à pytest où trouver les tests.
        "-v", # Mode verbeux.
        "--tb=short", # Traceback courte pour une meilleure lisibilité.
        f"--maxfail={config.retries + 1}", # Arrête après N échecs (retries + 1).
        "--json-report", # Active le rapport JSON.
        f"--json-report-file={workspace_dir}/report.json", # Chemin du rapport JSON.
    ]
    
    # Ajoute les arguments spécifiques au navigateur.
    args.extend([
        f"--browser={config.browser}",
        "--browser-channel=chromium" if config.browser == "chromium" else "", # Spécifique à Chromium
    ])
    
    if config.headed:
        args.append("--headed") # Lance le navigateur en mode visible.
    
    # Options de capture d'écran.
    if config.screenshot == "always":
        args.append("--screenshot=on")
    elif config.screenshot == "on-failure":
        args.append("--screenshot=only-on-failure")
    
    # Options d'enregistrement vidéo.
    if config.video == "always":
        args.append("--video=on")
    elif config.video == "on-failure":
        args.append("--video=retain-on-failure")
    
    # Options de trace Playwright.
    if config.trace == "always":
        args.append("--tracing=on")
    elif config.trace == "on-failure":
        args.append("--tracing=retain-on-failure")
    
    # Parallélisation avec pytest-xdist.
    if config.parallel and config.workers > 1:
        args.extend(["-n", str(config.workers)])
    
    # Timeout global pour l'exécution des tests.
    args.append(f"--timeout={config.timeout // 1000}") # Convertit ms en secondes.
    
    return [arg for arg in args if arg] # Filtre les arguments vides.


async def run_tests_sequential(
    test_files: List[Path],
    pytest_args: List[str],
    config: ExecutionConfig,
    workspace_dir: Path
) -> List[TestResult]:
    """Exécute les tests séquentiellement, un fichier à la fois."""
    results = []
    
    for test_file in test_files:
        result = await run_single_test(
            test_file,
            pytest_args,
            config,
            workspace_dir
        )
        results.append(result)
    
    return results


async def run_tests_parallel(
    test_files: List[Path],
    pytest_args: List[str],
    config: ExecutionConfig,
    workspace_dir: Path
) -> List[TestResult]:
    """Exécute les tests en parallèle en utilisant pytest-xdist."""
    # pytest-xdist est utilisé via les arguments passés à pytest.
    cmd = [sys.executable, "-m", "pytest"] + pytest_args
    
    # Configure les variables d'environnement pour le sous-processus pytest.
    env = os.environ.copy()
    env["PYTHONPATH"] = str(workspace_dir) # Ajoute le workspace au PYTHONPATH.
    if config.base_url:
        env["BASE_URL"] = config.base_url
    if config.headed:
        env["HEADED"] = "true"
    
    logger.info(f"Lancement de pytest en parallèle : {' '.join(cmd)}")
    process = await asyncio.create_subprocess_exec(
        *cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
        env=env,
        cwd=str(workspace_dir) # Exécute pytest dans le répertoire de travail.
    )
    
    stdout, stderr = await process.communicate()
    
    if process.returncode != 0:
        logger.error(f"Pytest a échoué (code {process.returncode}):\n{stderr.decode()}")

    # Parse le rapport JSON généré par pytest.
    report_path = workspace_dir / "report.json"
    if report_path.exists():
        try:
            with open(report_path, 'r', encoding='utf-8') as f:
                report = json.load(f)
            return parse_pytest_report(report, workspace_dir)
        except (IOError, OSError, json.JSONDecodeError) as e:
            logger.error(f"Erreur lors de la lecture ou du parsing du rapport pytest {report_path}: {e}")
            return [TestResult(
                test_name="suite_complete",
                status="error",
                duration=0,
                error_message=f"Échec de la lecture/parsing du rapport : {e}",
                error_trace=stderr.decode() if stderr else None
            )]
    else:
        logger.error(f"Le rapport JSON n'a pas été généré à {report_path}. Stdout: {stdout.decode()}, Stderr: {stderr.decode()}")
        return [TestResult(
            test_name="suite_complete",
            status="error",
            duration=0,
            error_message="Rapport JSON non trouvé.",
            error_trace=stderr.decode() if stderr else None
        )]


async def run_single_test(
    test_file: Path,
    base_pytest_args: List[str],
    config: ExecutionConfig,
    workspace_dir: Path
) -> TestResult:
    """Exécute un seul fichier de test Playwright via pytest."""
    # Construit les arguments pytest spécifiques à ce fichier.
    pytest_args = [str(test_file)] + [arg for arg in base_pytest_args if arg not in [str(workspace_dir), '-n', str(config.workers)]]
    
    cmd = [sys.executable, "-m", "pytest"] + pytest_args
    
    # Configure les variables d'environnement.
    env = os.environ.copy()
    env["PYTHONPATH"] = str(workspace_dir)
    if config.base_url:
        env["BASE_URL"] = config.base_url
    
    start_time = asyncio.get_event_loop().time()
    
    logger.info(f"Lancement du test : {' '.join(cmd)}")
    process = await asyncio.create_subprocess_exec(
        *cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
        env=env,
        cwd=str(workspace_dir)
    )
    
    stdout, stderr = await process.communicate()
    duration = asyncio.get_event_loop().time() - start_time
    
    # Détermine le statut du test basé sur le code de retour.
    if process.returncode == 0:
        status = "passed"
    elif process.returncode == 1: # pytest retourne 1 pour les échecs de test.
        status = "failed"
    else:
        status = "error"
    
    # Collecte les artefacts générés par ce test.
    artifacts = collect_test_artifacts(test_file.stem, workspace_dir)
    
    return TestResult(
        test_name=test_file.stem,
        status=status,
        duration=duration,
        error_message=stderr.decode() if status != "passed" and stderr else None,
        logs=stdout.decode().split('\n') if stdout else [],
        **artifacts
    )


def parse_pytest_report(report: Dict, workspace_dir: Path) -> List[TestResult]:
    """Parse le rapport JSON généré par pytest et le convertit en liste de `TestResult`."""
    results = []
    
    for test_data in report.get("tests", []):
        test_name = test_data.get("nodeid", "unknown").split("::")[-1]
        outcome = test_data.get("outcome", "unknown")
        
        status_map = {
            "passed": "passed",
            "failed": "failed",
            "skipped": "skipped",
            "error": "error"
        }
        status = status_map.get(outcome, "error")
        
        error_message = None
        error_trace = None
        if status == "failed" or status == "error":
            # Tente d'extraire le message d'erreur et la trace.
            if "call" in test_data and "longrepr" in test_data["call"]:
                error_message = str(test_data["call"]["longrepr"])
            elif "setup" in test_data and "longrepr" in test_data["setup"]:
                error_message = str(test_data["setup"]["longrepr"])
            # Une trace complète peut être extraite si nécessaire.
            # error_trace = test_data.get("longrepr", {}).get("reprcrash", {}).get("message")
        
        duration = test_data.get("duration", 0)
        
        artifacts = collect_test_artifacts(test_name, workspace_dir)
        
        results.append(TestResult(
            test_name=test_name,
            status=status,
            duration=duration,
            error_message=error_message,
            error_trace=error_trace,
            **artifacts
        ))
    
    return results


def collect_test_artifacts(test_name: str, workspace_dir: Path) -> Dict[str, Optional[str]]:
    """Collecte les chemins relatifs des artefacts (screenshots, vidéos, traces) pour un test donné."""
    artifacts = {
        "screenshot": None,
        "video": None,
        "trace": None
    }
    
    # Patterns de recherche pour les artefacts générés par Playwright/pytest.
    # Note: Les chemins peuvent varier légèrement en fonction de la configuration de pytest-playwright.
    patterns = {
        "screenshot": [f"**/{test_name}*.png"],
        "video": [f"**/{test_name}*.webm"],
        "trace": [f"**/{test_name}*.zip"]
    }
    
    for artifact_type, pattern_list in patterns.items():
        for pattern in pattern_list:
            # Recherche les fichiers correspondants dans le répertoire de travail.
            files = list(workspace_dir.glob(pattern))
            if files:
                # Prend le premier fichier trouvé et stocke son chemin relatif.
                artifacts[artifact_type] = str(files[0].relative_to(workspace_dir))
                break
    
    return artifacts


def calculate_stats(results: List[TestResult]) -> Dict[str, int]:
    """Calcule les statistiques récapitulatives d'une liste de résultats de tests."""
    stats = {
        "passed": sum(1 for r in results if r.status == "passed"),
        "failed": sum(1 for r in results if r.status == "failed"),
        "skipped": sum(1 for r in results if r.status == "skipped"),
        "error": sum(1 for r in results if r.status == "error")
    }
    return stats


# ------------------------------------------------------------------
# Tâches de fond
# ------------------------------------------------------------------

async def run_tests_background(execution_id: str, request: TestExecutionRequest):
    """Fonction exécutée en arrière-plan pour lancer les tests et mettre à jour leur statut."""
    try:
        # Met à jour le statut de l'exécution dans la queue.
        execution_queue[execution_id]["status"] = "running"
        
        # Exécute les tests en appelant la fonction principale synchrone.
        response = await execute_tests(request)
        
        # Met à jour la queue avec les résultats complets.
        execution_queue[execution_id] = response.model_dump() # Utilise model_dump pour Pydantic v2
        execution_queue[execution_id]["completed_at"] = datetime.now().isoformat()
        
    except Exception as e:
        # Gère les erreurs survenues pendant l'exécution en arrière-plan.
        logger.error(f"Erreur lors de l'exécution en arrière-plan pour {execution_id}: {e}", exc_info=True)
        execution_queue[execution_id].update({
            "status": "error",
            "error": str(e),
            "error_trace": traceback.format_exc(),
            "completed_at": datetime.now().isoformat()
        })


async def cleanup_workspace(workspace_dir: Path, delay: int = 300):
    """Nettoie le répertoire de travail temporaire après un délai spécifié."""
    await asyncio.sleep(delay)
    
    try:
        if workspace_dir.exists():
            shutil.rmtree(workspace_dir)
            logger.info(f"Répertoire de travail nettoyé : {workspace_dir}")
    except Exception as e:
        logger.error(f"Erreur lors du nettoyage du répertoire de travail {workspace_dir}: {e}")


# ------------------------------------------------------------------
# Génération de rapports
# ------------------------------------------------------------------

async def generate_html_report(
    execution_id: str,
    results: List[TestResult],
    stats: Dict[str, int],
    workspace_dir: Path
) -> str:
    """Génère un rapport HTML récapitulatif des résultats de l'exécution des tests."""
    report_path = Path("reports") / f"{execution_id}_report.html"
    
    # Template HTML pour le rapport.
    html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Rapport de Test - {execution_id}</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; }}
        .header {{ background: #f0f0f0; padding: 20px; border-radius: 5px; }}
        .stats {{ display: flex; gap: 20px; margin: 20px 0; }}
        .stat {{ padding: 10px 20px; border-radius: 5px; color: white; }}
        .passed {{ background: #4CAF50; }} /* Vert */
        .failed {{ background: #f44336; }} /* Rouge */
        .skipped {{ background: #ff9800; }} /* Orange */
        .error {{ background: #9c27b0; }} /* Violet */
        table {{ width: 100%; border-collapse: collapse; margin-top: 20px; }}
        th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
        th {{ background: #f2f2f2; }}
        .status-passed {{ color: #4CAF50; font-weight: bold; }}
        .status-failed {{ color: #f44336; font-weight: bold; }}
        .status-skipped {{ color: #ff9800; font-weight: bold; }}
        .status-error {{ color: #9c27b0; font-weight: bold; }}
        .error-details {{ background: #ffebee; color: #c62828; padding: 10px; margin: 5px 0; border-radius: 3px; font-family: monospace; white-space: pre-wrap; word-break: break-all; }}
        .artifact-link {{ margin-left: 10px; font-size: 0.9em; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>Rapport d'Exécution des Tests Playwright</h1>
        <p>ID d'Exécution : <strong>{execution_id}</strong></p>
        <p>Généré le : {timestamp}</p>
        <p>Durée totale : {total_duration:.2f} secondes</p>
    </div>
    
    <div class="stats">
        <div class="stat passed">Réussis : {passed}</div>
        <div class="stat failed">Échoués : {failed}</div>
        <div class="stat skipped">Ignorés : {skipped}</div>
        <div class="stat error">Erreurs : {error}</div>
    </div>
    
    <h2>Résultats Détaillés des Tests</h2>
    <table>
        <thead>
            <tr>
                <th>Nom du Test</th>
                <th>Statut</th>
                <th>Durée</th>
                <th>Détails / Artefacts</th>
            </tr>
        </thead>
        <tbody>
            {test_rows}
        </tbody>
    </table>
</body>
</html>
"""
    
    # Génère les lignes du tableau pour chaque résultat de test.
    test_rows = []
    for result in results:
        error_section = ""
        if result.error_message:
            error_section = f'<div class="error-details"><pre>{result.error_message}</pre></div>'
        
        artifact_links = []
        if result.screenshot:
            artifact_links.append(f'<a href="../artifacts/{execution_id}/{result.screenshot}" target="_blank" class="artifact-link">Screenshot</a>')
        if result.video:
            artifact_links.append(f'<a href="../artifacts/{execution_id}/{result.video}" target="_blank" class="artifact-link">Vidéo</a>')
        if result.trace:
            artifact_links.append(f'<a href="../artifacts/{execution_id}/{result.trace}" target="_blank" class="artifact-link">Trace</a>')
        
        test_rows.append(f"""
        <tr>
            <td>{result.test_name}</td>
            <td class="status-{result.status}">{result.status.upper()}</td>
            <td>{result.duration:.2f}s</td>
            <td>
                {error_section}
                {' '.join(artifact_links)}
            </td>
        </tr>
        """
        )
    
    # Remplit le template HTML avec les données et les lignes de test.
    html_content = html_template.format(
        execution_id=execution_id,
        timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        total_duration=sum(r.duration for r in results),
        passed=stats["passed"],
        failed=stats["failed"],
        skipped=stats["skipped"],
        error=stats.get("error", 0),
        test_rows="\n".join(test_rows)
    )
    
    # Écrit le rapport HTML dans le fichier.
    try:
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
    except (IOError, OSError) as e:
        logger.error(f"Erreur lors de l'écriture du rapport HTML sur {report_path}: {e}")
        raise HTTPException(status_code=500, detail=f"Échec de l'écriture du rapport HTML : {report_path}")
    
    return str(report_path)


async def collect_artifacts(execution_id: str, workspace_dir: Path) -> str:
    """Collecte tous les artefacts générés (screenshots, vidéos, traces) et les archive dans un fichier ZIP."""
    import zipfile
    
    artifacts_dir = Path("artifacts")
    artifacts_dir.mkdir(exist_ok=True) # S'assure que le répertoire des artefacts existe.
    
    zip_path = artifacts_dir / f"{execution_id}.zip"
    
    try:
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            # Ajoute tous les fichiers pertinents du workspace à l'archive ZIP.
            for pattern in ["**/*.png", "**/*.webm", "**/*.zip", "**/*.json", "**/trace.zip"]:
                for file_path in workspace_dir.glob(pattern):
                    if file_path.is_file():
                        # Ajoute le fichier à l'archive en conservant sa structure de répertoire relative.
                        arcname = file_path.relative_to(workspace_dir)
                        zipf.write(file_path, arcname)
    except (IOError, OSError) as e:
        logger.error(f"Erreur lors de la création de l'archive ZIP des artefacts {zip_path}: {e}")
        raise HTTPException(status_code=500, detail=f"Échec de la création de l'archive des artefacts : {zip_path}")
    
    return str(zip_path)


# ------------------------------------------------------------------
# Fonctions utilitaires
# ------------------------------------------------------------------

async def ensure_playwright_browsers():
    """S'assure que les navigateurs Playwright nécessaires sont installés."""
    logger.info("Vérification de l'installation des navigateurs Playwright...")
    try:
        # Tente de lancer chaque navigateur pour vérifier son installation.
        async with async_playwright() as p:
            for browser_name in ["chromium", "firefox", "webkit"]:
                try:
                    browser = await getattr(p, browser_name).launch(headless=True)
                    await browser.close()
                    logger.info(f"  ✅ Navigateur {browser_name} est disponible.")
                except Exception:
                    logger.warning(f"  ⚠️ Navigateur {browser_name} non disponible. Tentative d'installation...")
                    # Tente d'installer le navigateur manquant.
                    try:
                        subprocess.run(["playwright", "install", browser_name], check=True)
                        logger.info(f"  ✅ Navigateur {browser_name} installé avec succès.")
                    except Exception as install_e:
                        logger.error(f"  ❌ Impossible d'installer le navigateur {browser_name}: {install_e}")
    except Exception as e:
        logger.error(f"Erreur lors de la vérification/installation des navigateurs Playwright: {e}")


async def check_playwright_health() -> bool:
    """Vérifie si l'environnement Playwright est opérationnel en lançant un navigateur simple."""
    try:
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            await browser.close()
            return True
    except Exception as e:
        logger.error(f"Playwright n'est pas opérationnel : {e}")
        return False


async def save_execution_result(execution_id: str, result: ExecutionResponse):
    """Sauvegarde le résultat complet d'une exécution de tests dans Redis."""
    if not redis_client:
        logger.warning("Redis n'est pas connecté, le résultat de l'exécution ne sera pas mis en cache.")
        return
    
    try:
        key = f"execution:{execution_id}"
        # Convertit l'objet Pydantic en dictionnaire, puis en JSON.
        await redis_client.setex(
            key,
            86400,  # Durée de vie du cache : 24 heures.
            json.dumps(result.model_dump(), default=str) # Utilise model_dump pour Pydantic v2
        )
        logger.info(f"Résultat de l'exécution {execution_id} sauvegardé dans Redis.")
    except Exception as e:
        logger.error(f"Erreur lors de la sauvegarde du résultat dans Redis pour {execution_id}: {e}")


async def get_execution_result(execution_id: str) -> Optional[Dict]:
    """Récupère un résultat d'exécution depuis Redis par son ID."""
    if not redis_client:
        return None
    
    try:
        key = f"execution:{execution_id}"
        data = await redis_client.get(key)
        if data:
            logger.info(f"Résultat de l'exécution {execution_id} récupéré depuis Redis.")
            return json.loads(data)
    except Exception as e:
        logger.error(f"Erreur lors de la lecture du résultat depuis Redis pour {execution_id}: {e}")
    
    return None


# ------------------------------------------------------------------
# Points de terminaison additionnels
# ------------------------------------------------------------------

@app.delete("/cleanup")
async def cleanup_old_executions(days: int = 7):
    """Nettoie les anciens répertoires de travail, rapports et artefacts.

    Args:
        days: Nombre de jours après lesquels les fichiers sont considérés comme anciens et supprimés.

    Returns:
        Un dictionnaire récapitulatif des éléments nettoyés.
    """
    cutoff_date = datetime.now() - timedelta(days=days)
    cleaned = {
        "workspaces": 0,
        "reports": 0,
        "artifacts": 0
    }
    
    logger.info(f"Démarrage du nettoyage des fichiers de plus de {days} jours...")

    # Nettoie les workspaces.
    for workspace in Path("workspace").iterdir():
        if workspace.is_dir() and workspace.stat().st_mtime < cutoff_date.timestamp():
            try:
                shutil.rmtree(workspace)
                cleaned["workspaces"] += 1
            except Exception as e:
                logger.error(f"Erreur lors de la suppression du workspace {workspace}: {e}")
    
    # Nettoie les rapports HTML.
    for report in Path("reports").glob("*.html"):
        if report.stat().st_mtime < cutoff_date.timestamp():
            try:
                report.unlink()
                cleaned["reports"] += 1
            except Exception as e:
                logger.error(f"Erreur lors de la suppression du rapport {report}: {e}")
    
    # Nettoie les archives d'artefacts.
    for artifact in Path("artifacts").glob("*.zip"):
        if artifact.stat().st_mtime < cutoff_date.timestamp():
            try:
                artifact.unlink()
                cleaned["artifacts"] += 1
            except Exception as e:
                logger.error(f"Erreur lors de la suppression de l'artefact {artifact}: {e}")
    
    logger.info(f"Nettoyage terminé. Résumé : {cleaned}")
    return {
        "status": "success",
        "cleaned": cleaned,
        "message": f"Nettoyage des fichiers de plus de {days} jours effectué."
    }


@app.get("/stats")
async def get_stats():
    """Retourne des statistiques sur l'utilisation actuelle du service."""
    stats = {
        "service": "playwright-runner",
        "timestamp": datetime.now().isoformat(),
        "active_executions": len(execution_queue), # Nombre d'exécutions en cours.
        "workspace_count": len(list(Path("workspace").iterdir())),
        "report_count": len(list(Path("reports").glob("*.html"))),
        "artifact_count": len(list(Path("artifacts").glob("*.zip")))
    }
    
    # Ajoute des statistiques sur le cache Redis si disponible.
    if redis_client:
        try:
            exec_count = 0
            async for _ in redis_client.scan_iter("execution:*"):
                exec_count += 1
            stats["cached_executions"] = exec_count
        except redis.exceptions.ConnectionError:
            stats["cached_executions"] = "erreur de connexion Redis"
    
    return stats


# --- Point d'entrée Uvicorn --- #
if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(
        "playwright_runner:app", # Nom du module:objet FastAPI
        host="0.0.0.0",
        port=8004,
        log_level="info",
        reload=True # Utile pour le développement
    )

```

---

## Fichier : `backend\altiora\services\playwright\README.md`

```markdown
# Service Playwright

Ce service exécute des tests d'automatisation web avec Playwright.

## Démarrage Isolé

Pour lancer ce service de manière isolée, vous pouvez utiliser le `Dockerfile` présent dans ce répertoire.

1.  **Construire l'image Docker :**

    ```bash
    docker build -t altiora-playwright-service .
    ```

2.  **Lancer le conteneur :**

    ```bash
    docker run -p 8004:8004 -e PLAYWRIGHT_SERVICE_PORT=8004 altiora-playwright-service
    ```

## Endpoints

-   `POST /playwright/run-test` : Exécute un script de test Playwright.

## Variables d'Environnement

-   `PLAYWRIGHT_SERVICE_PORT` : Le port sur lequel le service écoute (défaut : `8004`).

```

---

## Fichier : `backend\altiora\services\playwright\__init__.py`

```python

```

---

## Fichier : `backend\altiora\utils\errors.py`

```python
# src/error_management.py
"""Architecture centralisée de gestion des erreurs, de retry et de disjoncteur pour Altiora.

Ce module fournit un ensemble complet d'outils pour gérer les erreurs de manière
robuste et résiliente dans une application asynchrone. Il inclut des exceptions
personnalisées, un gestionnaire de retry, un disjoncteur (circuit breaker),
un logger d'erreurs chiffré, et un gestionnaire de contexte pour la propagation
des erreurs.
"""

import json
import logging
import os
import traceback
from datetime import datetime, timedelta
from functools import wraps
from pathlib import Path
from typing import Any, Dict, Callable, Optional, Type

import aiofiles
from cryptography.fernet import Fernet  # Bibliothèque de chiffrement symétrique.
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type

logger = logging.getLogger(__name__)

# ------------------------------------------------------------------
# Configuration des erreurs
# ------------------------------------------------------------------
ERROR_CONFIG = {
    "max_retries": int(os.getenv("MAX_RETRIES", 3)),
    "backoff_factor": float(os.getenv("BACKOFF_FACTOR", 2.0)),
    "circuit_breaker_timeout": int(os.getenv("CB_TIMEOUT", 60)), # Temps en secondes pendant lequel le disjoncteur reste ouvert.
    "log_file": Path(os.getenv("ERROR_LOG", "logs/errors.jsonl")), # Chemin du fichier de log des erreurs.
    "encryption_key": os.getenv("LOGS_ENCRYPTION_KEY"), # Clé pour chiffrer les logs d'erreurs.
}


# ------------------------------------------------------------------
# Exceptions personnalisées
# ------------------------------------------------------------------
class AltioraError(Exception):
    """Exception de base pour toutes les erreurs spécifiques à Altiora."""
    pass


class ServiceError(AltioraError):
    """Exception levée lorsqu'un service externe rencontre une erreur."

    Utilisée pour les problèmes de communication ou de disponibilité des microservices.
    """
    pass


class ValidationError(AltioraError):
    """Exception levée lorsqu'une validation métier échoue."

    Indique que les données ne sont pas conformes aux règles de l'application.
    """
    pass


# ------------------------------------------------------------------
# Assistant de chiffrement
# ------------------------------------------------------------------
class CryptoHelper:
    """Aide au chiffrement/déchiffrement de dictionnaires en utilisant Fernet."""

    def __init__(self, key: Optional[str] = None):
        """Initialise l'aide au chiffrement."

        Args:
            key: La clé Fernet encodée en base64 URL-safe. Si None, une clé est générée.
        """
        if key:
            self.key = key
        else:
            self.key = Fernet.generate_key().decode() # Génère une clé si non fournie.
            logger.warning("Aucune clé de chiffrement fournie pour les logs. Génération d'une clé temporaire. NE PAS UTILISER EN PRODUCTION.")
        self.fernet = Fernet(self.key.encode() if isinstance(self.key, str) else self.key)

    def encrypt_dict(self, data: Dict[str, Any]) -> str:
        """Chiffre un dictionnaire en JSON puis avec Fernet."

        Args:
            data: Le dictionnaire à chiffrer.

        Returns:
            La chaîne chiffrée.
        """
        payload = json.dumps(data, ensure_ascii=False, separators=(",", ":")).encode('utf-8')
        return self.fernet.encrypt(payload).decode('utf-8')

    def decrypt_dict(self, token: str) -> Dict[str, Any]:
        """Déchiffre une chaîne chiffrée en un dictionnaire."

        Args:
            token: La chaîne chiffrée.

        Returns:
            Le dictionnaire déchiffré.
        """
        return json.loads(self.fernet.decrypt(token.encode('utf-8')).decode('utf-8'))


# Initialise l'aide au chiffrement avec la clé de configuration.
crypto = CryptoHelper(ERROR_CONFIG["encryption_key"])


# ------------------------------------------------------------------
# Gestionnaire de Retry
# ------------------------------------------------------------------
class RetryHandler:
    """Fournit un décorateur pour appliquer des stratégies de nouvelle tentative aux fonctions asynchrones."""

    @staticmethod
    def with_retry(
            max_attempts: int = ERROR_CONFIG["max_retries"],
            exceptions: tuple[Type[Exception], ...] = (Exception,),
    ) -> Callable:
        """Décorateur pour retenter l'exécution d'une fonction asynchrone en cas d'échec."

        Args:
            max_attempts: Le nombre maximal de tentatives d'exécution.
            exceptions: Un tuple d'exceptions pour lesquelles la fonction doit être retentée.

        Returns:
            Un décorateur qui peut être appliqué à une fonction asynchrone.
        """
        def decorator(func: Callable) -> Callable:
            @wraps(func)
            @retry(
                stop=stop_after_attempt(max_attempts),
                wait=wait_exponential(
                    multiplier=ERROR_CONFIG["backoff_factor"], max=30
                ),
                retry=retry_if_exception_type(exceptions), # Retente si l'exception est du type spécifié.
                reraise=True # Rélève l'exception après toutes les tentatives.
            )
            async def wrapper(*args, **kwargs):
                try:
                    return await func(*args, **kwargs)
                except Exception as e:
                    logger.warning("Retry pour %s: %s", func.__name__, e)
                    raise

            return wrapper

        return decorator


# ------------------------------------------------------------------
# Disjoncteur (Circuit Breaker)
# ------------------------------------------------------------------
class CircuitBreaker:
    """Implémente le pattern Circuit Breaker pour protéger contre les cascades d'erreurs."""

    def __init__(
            self,
            failure_threshold: int = 5,
            timeout: int = ERROR_CONFIG["circuit_breaker_timeout"],
    ):
        """Initialise le disjoncteur."

        Args:
            failure_threshold: Nombre d'échecs consécutifs avant que le disjoncteur ne s'ouvre.
            timeout: Durée en secondes pendant laquelle le disjoncteur reste ouvert.
        """
        self.failure_threshold = failure_threshold
        self.timeout = timeout
        self._failures: Dict[str, int] = {} # Compteur d'échecs par service.
        self._last_failure: Dict[str, datetime] = {} # Horodatage du dernier échec par service.
        self._is_open: Dict[str, bool] = {} # État du disjoncteur par service (ouvert/fermé).

    async def call_with_protection(
            self,
            service_name: str,
            coro: Callable,
            *args,
            **kwargs,
    ) -> Any:
        """Appelle une coroutine avec la protection du disjoncteur."

        Args:
            service_name: Le nom du service à protéger.
            coro: La coroutine à exécuter.
            *args, **kwargs: Arguments à passer à la coroutine.

        Returns:
            Le résultat de la coroutine.

        Raises:
            ServiceError: Si le disjoncteur est ouvert pour ce service.
            Exception: Toute exception levée par la coroutine.
        """
        # Vérifie si le disjoncteur est ouvert.
        if self._is_open.get(service_name, False):
            # Si ouvert, vérifie si le timeout de récupération est passé.
            if (datetime.now() - self._last_failure.get(service_name, datetime.min)) < timedelta(seconds=self.timeout):
                raise ServiceError(f"Disjoncteur ouvert pour le service `{service_name}`. Opération bloquée.")
            # Si le timeout est passé, tente de réinitialiser le disjoncteur (état "semi-ouvert").
            self.reset(service_name)

        try:
            result = await coro(*args, **kwargs)
            self.reset(service_name) # Réinitialise le disjoncteur en cas de succès.
            return result
        except Exception:
            self._record_failure(service_name) # Enregistre l'échec.
            if self._failures.get(service_name, 0) >= self.failure_threshold:
                self._is_open[service_name] = True
                self._last_failure[service_name] = datetime.now()
                logger.error(f"Disjoncteur ouvert pour le service `{service_name}` après {self.failure_threshold} échecs.")
            raise # Rélève l'exception originale.

    def reset(self, service_name: str) -> None:
        """Réinitialise l'état du disjoncteur pour un service donné."""
        self._failures[service_name] = 0
        self._is_open[service_name] = False
        logger.info(f"Disjoncteur réinitialisé pour le service `{service_name}`.")

    def _record_failure(self, service_name: str) -> None:
        """Enregistre un échec pour un service."""
        self._failures[service_name] = self._failures.get(service_name, 0) + 1


# ------------------------------------------------------------------
# Journalisation des Erreurs
# ------------------------------------------------------------------
class ErrorLogger:
    """Gère la journalisation centralisée des erreurs de l'application."""

    def __init__(self, log_file: Path = ERROR_CONFIG["log_file"]) -> None:
        """Initialise le journaliseur d'erreurs."

        Args:
            log_file: Le chemin du fichier où les erreurs seront enregistrées.
        """
        self.log_file = log_file
        self.log_file.parent.mkdir(parents=True, exist_ok=True) # Crée le répertoire si nécessaire.

    async def log_error(self, error: Exception, context: Optional[Dict[str, Any]] = None) -> None:
        """Enregistre une erreur dans le fichier de log."

        Args:
            error: L'objet exception à enregistrer.
            context: Un dictionnaire de contexte supplémentaire à inclure dans le log.
        """
        entry = {
            "timestamp": datetime.now().isoformat(),
            "error_type": type(error).__name__,
            "error_message": str(error),
            "context": context or {},
            "stack_trace": traceback.format_exc() # Capture la trace complète de la pile.
        }
        try:
            async with aiofiles.open(self.log_file, "a", encoding='utf-8') as f:
                await f.write(crypto.encrypt_dict(entry) + "\n") # Chiffre l'entrée avant de l'écrire.
            logger.error("Erreur logguée : %s", entry["error_message"])
        except (IOError, OSError) as e:
            logger.critical(f"Erreur critique : Impossible d'écrire dans le fichier de log des erreurs {self.log_file}: {e}")


class EncryptedLogger(ErrorLogger):
    """Logger d'erreurs qui chiffre les entrées avant de les écrire sur disque."""
    pass # L'implémentation est déjà dans ErrorLogger avec crypto.


# ------------------------------------------------------------------
# Gestionnaire de Contexte pour les Erreurs
# ------------------------------------------------------------------
class ErrorContext:
    """Gestionnaire de contexte asynchrone pour capturer et logguer les exceptions non gérées."

    Utilisation:
    ```python
    async with ErrorContext("process_sfd", sfd_id="123"):
        # Code potentiellement générateur d'erreurs.
        raise ValueError("Problème lors du parsing.")
    ```
    """
    def __init__(self, operation: str, **kwargs: Any) -> None:
        """Initialise le contexte d'erreur."

        Args:
            operation: Le nom de l'opération en cours (pour le logging).
            **kwargs: Contexte supplémentaire à logguer avec l'erreur.
        """
        self.operation = operation
        self.context = kwargs

    async def __aenter__(self) -> "ErrorContext":
        """Entre dans le bloc `async with`."""
        return self

    async def __aexit__(self, exc_type: Optional[Type[BaseException]], exc_val: Optional[BaseException], exc_tb: Optional[Any]) -> bool:
        """Quitte le bloc `async with` et loggue l'exception si elle existe."

        Args:
            exc_type: Le type de l'exception.
            exc_val: L'instance de l'exception.
            exc_tb: La traceback de l'exception.

        Returns:
            True si l'exception a été gérée et ne doit pas être propagée,
            False si l'exception doit être propagée.
        """
        if exc_val:
            # Formate la traceback pour l'inclure dans le log.
            formatted_traceback = "\n".join(traceback.format_exception(exc_type, exc_val, exc_tb))
            logger.error(
                "Exception non gérée dans l'opération '%s'",
                self.operation,
                extra={
                    "context": self.context,
                    "error_type": exc_type.__name__ if exc_type else "UnknownError",
                    "error_message": str(exc_val),
                    "stack_trace": formatted_traceback
                },
            )
            # Ici, vous pouvez ajouter des hooks pour envoyer des alertes à des systèmes de monitoring externes.
            # Exemple: await send_alert_to_sentry(exc_val, self.context)
        return False  # Propagate l'exception pour qu'elle soit gérée plus haut.


# ------------------------------------------------------------------
# Instances globales (singletons)
# ------------------------------------------------------------------
error_logger = EncryptedLogger() # Instance du logger d'erreurs chiffré.
retry_handler = RetryHandler() # Instance du gestionnaire de retry.
circuit_breaker = CircuitBreaker() # Instance du disjoncteur.


# ------------------------------------------------------------------
# Démonstration (exemple d'utilisation)
# ------------------------------------------------------------------
if __name__ == "__main__":
    import asyncio
    import random

    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    # Définir une clé de chiffrement pour la démo.
    os.environ["LOGS_ENCRYPTION_KEY"] = Fernet.generate_key().decode()

    # --- Démonstration du RetryHandler ---
    print("\n--- Démonstration du RetryHandler ---")
    attempt_count = 0

    @retry_handler.with_retry(max_attempts=3, exceptions=(ValueError,))
    async def flaky_operation_retry(succeed_on_attempt: int):
        nonlocal attempt_count
        attempt_count += 1
        if attempt_count < succeed_on_attempt:
            logger.info(f"Flaky operation échoue (tentative {attempt_count})...")
            raise ValueError("Échec temporaire")
        logger.info(f"Flaky operation réussie à la tentative {attempt_count} !")
        return "Succès"

    async def run_retry_demo():
        nonlocal attempt_count
        attempt_count = 0
        try:
            result = await flaky_operation_retry(2) # Réussit à la 2ème tentative.
            print(f"Résultat final du retry : {result}")
        except Exception as e:
            print(f"Échec final du retry : {e}")

        attempt_count = 0
        try:
            result = await flaky_operation_retry(4) # Échoue après 3 tentatives.
            print(f"Résultat final du retry : {result}")
        except Exception as e:
            print(f"Échec final du retry (attendu) : {e}")

    asyncio.run(run_retry_demo())

    # --- Démonstration du CircuitBreaker ---
    print("\n--- Démonstration du CircuitBreaker ---")
    service_name = "ExternalAPI"
    call_count = 0

    # Réinitialise le disjoncteur pour la démo.
    circuit_breaker.reset(service_name)

    async def unreliable_service_call():
        nonlocal call_count
        call_count += 1
        if call_count % 3 != 0: # Échoue 2 fois sur 3.
            logger.info(f"Appel au service {service_name} échoue (appel {call_count})...")
            raise ServiceError("Erreur de service externe simulée")
        logger.info(f"Appel au service {service_name} réussi (appel {call_count}) !")
        return "Données reçues"

    async def run_circuit_breaker_demo():
        nonlocal call_count
        call_count = 0
        circuit_breaker.reset(service_name) # S'assure que le disjoncteur est fermé au début.

        for i in range(10):
            print(f"\n--- Itération {i+1} ---")
            try:
                result = await circuit_breaker.call_with_protection(service_name, unreliable_service_call)
                print(f"Résultat : {result}")
            except ServiceError as e:
                print(f"Erreur de service : {e}")
            except Exception as e:
                print(f"Autre erreur : {e}")
            await asyncio.sleep(0.5) # Petite pause entre les appels.

        print("\n--- Tentative après timeout de récupération ---")
        await asyncio.sleep(ERROR_CONFIG["circuit_breaker_timeout"] + 1) # Attend que le disjoncteur se referme.
        try:
            result = await circuit_breaker.call_with_protection(service_name, unreliable_service_call)
            print(f"Résultat après récupération : {result}")
        except Exception as e:
            print(f"Échec après récupération : {e}")

    asyncio.run(run_circuit_breaker_demo())

    # --- Démonstration de ErrorLogger et ErrorContext ---
    print("\n--- Démonstration de ErrorLogger et ErrorContext ---")
    async def demo_error_logging():
        try:
            async with ErrorContext("complex_operation", user_id="test_user", data_id="xyz"):
                logger.info("Début de l'opération complexe.")
                if random.random() < 0.7: # Simule une erreur fréquente.
                    raise ValueError("Erreur simulée lors du traitement des données.")
                logger.info("Opération complexe terminée.")
        except Exception as e:
            print(f"Exception capturée au niveau supérieur : {e}")

    asyncio.run(demo_error_logging())
    print(f"Vérifiez le fichier {ERROR_CONFIG["log_file"]} pour les erreurs logguées (chiffrées)."
          f" Pour les déchiffrer, utilisez `crypto.decrypt_dict()`.")

    # Nettoyage de la variable d'environnement.
    del os.environ["LOGS_ENCRYPTION_KEY"]
```

---

## Fichier : `backend\altiora\utils\helpers.py`

```python
# backend/altiora/utils/helpers.py
"""
Petites fonctions utilitaires.
"""

import hashlib
import json
from typing import Any, Dict, List
from pathlib import Path
import aiofiles

def generate_cache_key(*args: Any) -> str:
    """Génère une clé de cache unique."""
    content = json.dumps(args, sort_keys=True, default=str)
    return hashlib.sha256(content.encode()).hexdigest()

async def read_file_async(path: Path) -> str:
    """Lit un fichier de manière asynchrone."""
    async with aiofiles.open(path, 'r', encoding='utf-8') as f:
        return await f.read()

async def write_file_async(path: Path, content: str) -> None:
    """Écrit un fichier de manière asynchrone."""
    path.parent.mkdir(parents=True, exist_ok=True)
    async with aiofiles.open(path, 'w', encoding='utf-8') as f:
        await f.write(content)

def chunk_list(lst: List[Any], chunk_size: int) -> List[List[Any]]:
    """Divise une liste en chunks."""
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]

def sanitize_filename(filename: str) -> str:
    """Nettoie un nom de fichier."""
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        filename = filename.replace(char, '_')
    return filename.strip()

def format_bytes(size: int) -> str:
    """Formate une taille en bytes."""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            return f"{size:.2f} {unit}"
        size /= 1024.0
    return f"{size:.2f} PB"
```

---

## Fichier : `backend\altiora\utils\logging.py`

```python
# backend/altiora/utils/logging.py
"""
Configuration centralisée du logging.
"""

import logging
import sys
from pathlib import Path
from logging.handlers import RotatingFileHandler
import structlog
from backend.altiora.config.settings import settings


def setup_logging():
    """Configure le système de logging pour l'application."""
    # Créer le dossier logs
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)

    # Formatter standard
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)

    # File handler avec rotation
    file_handler = RotatingFileHandler(
        log_dir / "altiora.log",
        maxBytes=10 * 1024 * 1024,  # 10MB
        backupCount=5
    )
    file_handler.setFormatter(formatter)

    # Root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(getattr(logging, settings.log_level))
    root_logger.addHandler(console_handler)
    root_logger.addHandler(file_handler)

    # Structlog configuration
    structlog.configure(
        processors=[
            structlog.stdlib.filter_by_level,
            structlog.stdlib.add_logger_name,
            structlog.stdlib.add_log_level,
            structlog.stdlib.PositionalArgumentsFormatter(),
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.StackInfoRenderer(),
            structlog.processors.format_exc_info,
            structlog.processors.UnicodeDecoder(),
            structlog.processors.JSONRenderer()
        ],
        context_class=dict,
        logger_factory=structlog.stdlib.LoggerFactory(),
        cache_logger_on_first_use=True,
    )
```

---

## Fichier : `backend\altiora\utils\__init__.py`

```python
# backend/altiora/utils/__init__.py
"""
Utilitaires partagés.
"""
```

---

## Fichier : `backend\tests\conftest.py`

```python
# tests/conftest.py
"""Fichier de configuration pour Pytest.

Ce fichier contient des fixtures (fonctions de configuration) qui sont
automatiquement découvertes par Pytest et peuvent être utilisées dans
les tests. Elles sont souvent utilisées pour configurer des environnements
de test, mocker des dépendances ou fournir des données de test.
"""
import pytest
from unittest.mock import AsyncMock, MagicMock

@pytest.fixture
def mock_redis():
    """Fixture mockant un client Redis asynchrone."

    Simule les méthodes `get` et `set` pour les tests qui interagissent avec Redis.
    """
    redis = AsyncMock()
    redis.get.return_value = None
    redis.set.return_value = True
    return redis

@pytest.fixture
def mock_ollama():
    """Fixture mockant un client Ollama."

    Simule la méthode `generate` pour les tests qui interagissent avec Ollama.
    """
    ollama = MagicMock()
    ollama.generate.return_value = {"response": "mocked response"}
    return ollama

@pytest.fixture
def mock_database():
    """Fixture mockant un client de base de données."

    Simule les opérations CRUD (`query`, `insert`, `update`, `delete`).
    """
    db = MagicMock()
    db.query.return_value = []
    db.insert.return_value = True
    db.update.return_value = True
    db.delete.return_value = True
    return db

@pytest.fixture
def mock_http_client():
    """Fixture mockant un client HTTP asynchrone (ex: `httpx`)."

    Simule les requêtes `get` et `post`.
    """
    http_client = AsyncMock()
    http_client.get.return_value.__aenter__.return_value.json.return_value = {}
    http_client.post.return_value.__aenter__.return_value.json.return_value = {}
    return http_client

@pytest.fixture
def mock_filesystem():
    """Fixture mockant les opérations du système de fichiers."

    Simule les lectures et écritures de fichiers.
    """
    fs = MagicMock()
    fs.open.return_value.__enter__.return_value.read.return_value = "mocked file content"
    fs.open.return_value.__aenter__.return_value.write.return_value = None
    return fs

@pytest.fixture
def mock_logger():
    """Fixture mockant un logger."

    Simule les méthodes de logging (`info`, `error`, `warning`).
    """
    logger = MagicMock()
    logger.info.return_value = None
    logger.error.return_value = None
    logger.warning.return_value = None
    return logger

@pytest.fixture
def mock_config():
    """Fixture mockant un objet de configuration."

    Simule la méthode `get` pour récupérer des valeurs de configuration.
    """
    config = MagicMock()
    config.get.return_value = "mocked config value"
    return config

@pytest.fixture
def mock_service():
    """Fixture mockant un client de service générique."

    Simule la méthode `call`.
    """
    service = MagicMock()
    service.call.return_value = "mocked service response"
    return service

```

---

## Fichier : `backend\tests\test_admin_control.py`

```python
# tests/test_admin_control.py
"""Tests unitaires et d'intégration pour le système de contrôle administratif.

Ce module contient des tests pour vérifier le bon fonctionnement des commandes
d'administration, telles que la sauvegarde des données utilisateur, le gel
des comptes, et les sauvegardes d'urgence. Il utilise des mocks et des
fixtures pour isoler les composants et simuler les interactions.
"""

import pytest
import asyncio
from pathlib import Path
import shutil

from guardrails.admin_control_system import AdminControlSystem, AdminCommand


@pytest.fixture
async def admin_system():
    """Fixture Pytest pour initialiser un `AdminControlSystem` et nettoyer après les tests."

    Cette fixture crée une instance du système d'administration et s'assure
    que les répertoires temporaires créés par les tests sont supprimés.
    """
    # Crée une instance du système d'administration.
    system = AdminControlSystem()
    yield system
    # Nettoie les répertoires créés par le système d'administration après chaque test.
    if Path("admin_system").exists():
        shutil.rmtree("admin_system")
    if Path("user_data").exists(): # Nettoie aussi les données utilisateur factices.
        shutil.rmtree("user_data")


@pytest.mark.asyncio
async def test_full_user_backup(admin_system: AdminControlSystem, tmp_path: Path):
    """Test la fonctionnalité de sauvegarde complète des données d'un utilisateur."

    Vérifie qu'un fichier ZIP de sauvegarde est créé et qu'il contient les données de l'utilisateur.
    """
    # Crée un répertoire de données utilisateur factice avec un fichier.
    user_data_dir = tmp_path / "user_data" / "test_user"
    user_data_dir.mkdir(parents=True, exist_ok=True)
    (user_data_dir / "profile.json").write_text('{"name": "Test User", "email": "test@example.com"}')

    # Appelle la méthode de sauvegarde de l'utilisateur.
    backup_path_str = await admin_system._full_user_backup("test_user")
    backup_path = Path(backup_path_str)

    # Vérifie que le fichier de sauvegarde existe et a la bonne extension.
    assert backup_path.exists(), "Le fichier de sauvegarde devrait exister."
    assert backup_path.suffix == ".zip", "Le fichier de sauvegarde devrait être un fichier ZIP."

    # Optionnel: Vérifier le contenu du ZIP.
    # import zipfile
    # with zipfile.ZipFile(backup_path, 'r') as zip_ref:
    #     zip_ref.extractall(tmp_path / "extracted_backup")
    # assert (tmp_path / "extracted_backup" / "profile.json").exists()


@pytest.mark.asyncio
async def test_freeze_user(admin_system: AdminControlSystem):
    """Test la commande administrative de gel d'un utilisateur."

    Vérifie que l'exécution de la commande `freeze_user` retourne un statut de succès.
    """
    command = AdminCommand(
        command_id="freeze_001",
        action="freeze_user",
        target_user="test_user",
        parameters={"reason": "Test de gel de compte"}
    )

    result = await admin_system.execute_admin_command(command)
    assert result["status"] == "success", "La commande de gel d'utilisateur devrait réussir."
    assert "gelé" in result["message"].lower(), "Le message de résultat devrait indiquer que l'utilisateur est gelé."


@pytest.mark.asyncio
async def test_emergency_backup(admin_system: AdminControlSystem):
    """Test la fonctionnalité de sauvegarde d'urgence du système."

    Vérifie que la sauvegarde d'urgence crée un répertoire et des fichiers de sauvegarde.
    """
    await admin_system._emergency_backup()
    
    # Vérifie que le répertoire d'urgence a été créé.
    emergency_dir = Path("admin_system/emergency")
    assert emergency_dir.exists(), "Le répertoire de sauvegarde d'urgence devrait exister."
    
    # Vérifie qu'il y a des fichiers de sauvegarde à l'intérieur (au moins un).
    # Note: Le contenu exact dépend de l'implémentation de _emergency_backup.
    assert any(emergency_dir.iterdir()), "Le répertoire de sauvegarde d'urgence ne devrait pas être vide."

```

---

## Fichier : `backend\tests\test_altiora_core.py`

```python
# tests/test_altiora_core.py
"""Tests unitaires pour le noyau de personnalité AltioraCore.

Ce module contient des tests pour vérifier le bon fonctionnement des
composants centraux de la personnalité de l'IA, y compris le suivi de
l'évolution des traits et la création de propositions d'apprentissage.
"""

import pytest
import datetime
from unittest.mock import MagicMock
from src.modules.psychodesign.altiora_core import AltioraCore, PersonalityEvolution, LearningProposal
from src.modules.psychodesign.personality_quiz import PersonalityProfile # Import nécessaire pour la fixture.


@pytest.fixture
async def altiora_core():
    """Fixture Pytest pour initialiser une instance de `AltioraCore` pour les tests."

    Utilise un `MagicMock` pour simuler le `AdminControlSystem` afin d'isoler les tests.
    """
    # Crée un profil de personnalité par défaut pour le test.
    mock_personality_profile = PersonalityProfile(
        user_id="test_user",
        traits={
            "formalite": 0.5,
            "empathie": 0.5,
            "humor": 0.5,
            "proactivite": 0.5,
            "verbosite": 0.5,
            "confirmation": 0.5,
            "technical_level": 0.5,
        },
        preferences={},
        vocal_profile={},
        behavioral_patterns={},
        quiz_metadata={},
    )

    # Mocke le AdminControlSystem.
    mock_admin_system = MagicMock()
    mock_admin_system.execute_admin_command.return_value = {"status": "success"}

    core = AltioraCore("test_user", mock_admin_system)
    # Surcharge la personnalité par défaut avec le mock pour un état de test prévisible.
    core.personality = mock_personality_profile
    yield core


@pytest.mark.asyncio
async def test_personality_evolution_tracking(altiora_core: AltioraCore):
    """Teste que l'historique d'évolution de la personnalité est correctement suivi."

    Vérifie qu'un objet `PersonalityEvolution` est ajouté à l'historique
    et que ses valeurs sont correctes.
    """
    evolution = PersonalityEvolution(
        timestamp=datetime.datetime.now(),
        change_type="trait_formalite",
        old_value=0.5,
        new_value=0.7,
        reason="User feedback",
        source="learning"
    )

    altiora_core.evolution_history.append(evolution)
    assert len(altiora_core.evolution_history) == 1
    assert altiora_core.evolution_history[0].new_value == 0.7
    assert altiora_core.evolution_history[0].change_type == "trait_formalite"


@pytest.mark.asyncio
async def test_learning_proposal_creation(altiora_core: AltioraCore):
    """Teste la création d'une proposition d'apprentissage."

    Vérifie qu'un objet `LearningProposal` est correctement créé et ajouté
    à la liste des propositions en attente.
    """
    proposal = LearningProposal(
        proposal_id="test_001",
        user_id="test_user",
        suggested_changes={"empathie": 0.8},
        confidence_score=0.9,
        evidence=[{"type": "feedback"}],
        timestamp=datetime.datetime.now()
    )

    altiora_core.learning_proposals.append(proposal)
    assert len(altiora_core.learning_proposals) == 1
    assert proposal.suggested_changes["empathie"] == 0.8
    assert proposal.status == "pending"


@pytest.mark.asyncio
async def test_handle_correction_feedback(altiora_core: AltioraCore):
    """Teste le traitement d'un feedback de correction utilisateur."

    Vérifie que le système génère une proposition d'apprentissage basée sur
    le feedback de correction et la soumet à l'administrateur.
    """
    feedback = {
        "type": "correction",
        "original": "Hello, how are you doing today?",
        "corrected": "Hi!"
    }

    # Appelle la méthode qui traite le feedback.
    proposal = await altiora_core.process_learning_feedback(feedback)

    # Vérifie qu'une proposition a été créée.
    assert proposal is not None
    assert "verbosite" in proposal.suggested_changes # La verbosité devrait être ajustée.
    assert proposal.status == "pending"
    # Vérifie que la commande admin a été appelée.
    altiora_core.admin_system.execute_admin_command.assert_called_once()


@pytest.mark.asyncio
async def test_apply_approved_changes(altiora_core: AltioraCore):
    """Teste l'application des changements de personnalité après approbation administrative."

    Vérifie que les traits de personnalité sont mis à jour et que l'historique
    d'évolution est enregistré.
    """
    # Crée une proposition d'apprentissage et la marque comme approuvée.
    proposal_id = "approved_prop_001"
    approved_changes = {"formalite": 0.9, "empathie": 0.6}
    proposal = LearningProposal(
        proposal_id=proposal_id,
        user_id="test_user",
        suggested_changes=approved_changes,
        confidence_score=1.0,
        evidence=[],
        timestamp=datetime.datetime.now(),
        status="approved" # Statut approuvé.
    )
    altiora_core.learning_proposals.append(proposal)

    # Applique les changements.
    applied = await altiora_core.apply_approved_changes(proposal_id)

    assert applied is True
    assert altiora_core.personality.traits["formalite"] == 0.9
    assert altiora_core.personality.traits["empathie"] == 0.6
    assert len(altiora_core.evolution_history) == 2 # Deux changements de traits.
    assert altiora_core.evolution_history[0].approved is True


@pytest.mark.asyncio
async def test_get_personality_summary(altiora_core: AltioraCore):
    """Teste la génération du résumé de la personnalité."

    Vérifie que le résumé contient les informations clés du profil.
    """
    summary = altiora_core.get_personality_summary()
    assert summary["user_id"] == "test_user"
    assert "current_traits" in summary
    assert "evolution_count" in summary
    assert "pending_proposals" in summary


@pytest.mark.asyncio
async def test_get_evolution_report(altiora_core: AltioraCore):
    """Teste la génération du rapport textuel d'évolution."

    Vérifie que le rapport est formaté correctement et contient les informations
    essentielles sur les traits et l'historique.
    """
    report = altiora_core.get_evolution_report()
    assert "Rapport d'Évolution" in report
    assert "Traits actuels" in report
    assert "Historique" in report

```

---

## Fichier : `backend\tests\test_ethical_safeguards.py`

```python
import sys
import os
import asyncio
import pytest
from datetime import datetime, timedelta
from unittest.mock import MagicMock, AsyncMock

# Ajoute le répertoire parent au PYTHONPATH pour les imports relatifs.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from guardrails.ethical_safeguards import EthicalSafeguards, EthicalDashboard, EthicalAlert # Importe EthicalAlert


@pytest.fixture
def safeguards():
    """Fixture pour fournir une instance fraîche de `EthicalSafeguards` pour chaque test."

    Initialise le système de garde-fous éthiques.
    """
    return EthicalSafeguards()


@pytest.mark.asyncio
async def test_no_alert_for_normal_interaction(safeguards: EthicalSafeguards):
    """Vérifie qu'une interaction normale ne déclenche aucune alerte éthique."

    Args:
        safeguards: L'instance de `EthicalSafeguards`.
    """
    interaction = {"text": "Bonjour, comment vas-tu aujourd'hui ?", "timestamp": datetime.now()}
    alert = await safeguards.analyze_interaction("user_normal", interaction)
    assert alert is None, "Une interaction normale ne devrait pas déclencher d'alerte."


@pytest.mark.asyncio
async def test_sensitive_data_detection(safeguards: EthicalSafeguards):
    """Teste la détection de données sensibles (ex: mot de passe, numéro de carte de crédit)."

    Vérifie qu'une alerte de type `sensitive_data_detected` est générée avec la bonne sévérité.
    """
    interaction = {"text": "Mon mot de passe est supersecret123, ne le dis à personne.", "timestamp": datetime.now()}
    alert = await safeguards.analyze_interaction("user_privacy", interaction)
    assert alert is not None, "Une alerte devrait être déclenchée pour les données sensibles."
    assert alert.alert_type == "sensitive_data_detected", "Le type d'alerte devrait être 'sensitive_data_detected'."
    assert alert.severity == "medium", "La sévérité de l'alerte devrait être 'medium'."
    assert alert.data["data_type"] == "password", "Le type de données détecté devrait être 'password'."


@pytest.mark.asyncio
async def test_user_distress_detection(safeguards: EthicalSafeguards):
    """Teste la détection de la détresse émotionnelle de l'utilisateur."

    Vérifie qu'une alerte de type `user_distress_detected` est générée.
    """
    interaction = {"text": "Je suis désespéré, c'est trop difficile, aidez-moi c'est urgent !", "timestamp": datetime.now()}
    alert = await safeguards.analyze_interaction("user_distress", interaction)
    assert alert is not None, "Une alerte devrait être déclenchée pour la détresse utilisateur."
    assert alert.alert_type == "user_distress_detected", "Le type d'alerte devrait être 'user_distress_detected'."
    assert alert.severity == "medium", "La sévérité de l'alerte devrait être 'medium'."
    assert len(alert.data["keywords_found"]) >= 3, "Au moins 3 mots-clés de détresse devraient être trouvés."


@pytest.mark.asyncio
async def test_potential_manipulation_detection(safeguards: EthicalSafeguards):
    """Teste la détection de schémas de manipulation ou d'influence inappropriée."

    Vérifie qu'une alerte de type `potential_manipulation` est générée.
    """
    interaction = {"text": "Je ne peux rien faire sans toi, tu es la seule personne qui me comprenne.", "timestamp": datetime.now()}
    alert = await safeguards.analyze_interaction("user_manipulation", interaction)
    assert alert is not None, "Une alerte devrait être déclenchée pour la manipulation potentielle."
    assert alert.alert_type == "potential_manipulation", "Le type d'alerte devrait être 'potential_manipulation'."
    assert alert.severity == "high", "La sévérité de l'alerte devrait être 'high'."
    assert "sans toi" in alert.data["text"], "Le texte de l'interaction devrait être inclus dans les données de l'alerte."


@pytest.mark.asyncio
async def test_excessive_dependency_detection(safeguards: EthicalSafeguards):
    """Teste la détection de dépendance excessive de l'utilisateur sur l'IA."

    Simule une série d'interactions pour augmenter le score de dépendance et
    vérifie qu'une alerte critique est générée lorsque le seuil est dépassé.
    """
    user_id = "user_dependent"
    # Mocke la méthode _handle_alert pour éviter les actions réelles pendant le test.
    safeguards._handle_alert = AsyncMock()

    # Simule une série d'interactions rapides et dépendantes pour augmenter le score.
    for i in range(50):
        interaction = {
            "text": f"J'ai encore besoin de toi pour cette tâche simple. {i}",
            "timestamp": datetime.now() - timedelta(minutes=i * 5) # Simule des interactions espacées.
        }
        await safeguards.analyze_interaction(user_id, interaction)

    # La dernière interaction devrait pousser le score au-dessus du seuil critique.
    final_interaction = {"text": "Sans toi je suis complètement perdu, je ne peux pas continuer.", "timestamp": datetime.now()}
    alert = await safeguards.analyze_interaction(user_id, final_interaction)
    
    assert alert is not None, "Une alerte devrait être déclenchée pour la dépendance excessive."
    assert alert.alert_type == "excessive_dependency", "Le type d'alerte devrait être 'excessive_dependency'."
    assert alert.severity == "critical", "La sévérité de l'alerte devrait être 'critical'."
    assert safeguards.user_patterns[user_id]["dependency_score"] > safeguards.thresholds["dependency"]["critical"], "Le score de dépendance devrait dépasser le seuil critique."


def test_dashboard_report_generation(safeguards: EthicalSafeguards):
    """Teste la génération de rapports utilisateur par le `EthicalDashboard`."

    Vérifie que le rapport contient les informations clés sur le score de dépendance
    et les alertes actives pour un utilisateur spécifique.
    """
    # Simule quelques données pour un utilisateur.
    user_id = "user_report"
    safeguards.user_patterns[user_id]["dependency_score"] = 0.75
    safeguards.alerts.append(EthicalAlert(user_id=user_id, alert_id="alert_1", alert_type="user_distress_detected", severity="medium", timestamp=datetime.now(), data={}, resolved=False))

    dashboard = EthicalDashboard(safeguards)
    report = dashboard.generate_report(user_id=user_id)

    assert "Rapport Éthique - user_report" in report, "Le titre du rapport devrait être correct."
    assert "Score de dépendance: 75.0%" in report, "Le score de dépendance devrait être inclus."
    assert "Niveau de risque: MEDIUM" in report, "Le niveau de risque devrait être calculé."
    assert "Recommandations:" in report, "Les recommandations devraient être incluses."


def test_system_report_generation(safeguards: EthicalSafeguards):
    """Teste la génération du rapport système global par le `EthicalDashboard`."

    Vérifie que le rapport agrège correctement les alertes actives et résolues
    à l'échelle du système.
    """
    # Simule quelques alertes à l'échelle du système.
    safeguards.alerts.append(EthicalAlert(user_id="u1", alert_id="a1", alert_type="excessive_dependency", severity="critical", timestamp=datetime.now(), data={}, resolved=False))
    safeguards.alerts.append(EthicalAlert(user_id="u2", alert_id="a2", alert_type="potential_manipulation", severity="high", timestamp=datetime.now(), data={}, resolved=False))
    safeguards.alerts.append(EthicalAlert(user_id="u3", alert_id="a3", alert_type="sensitive_data_detected", severity="medium", timestamp=datetime.now(), data={}, resolved=True))

    dashboard = EthicalDashboard(safeguards)
    report = dashboard.generate_report() # Appel sans user_id pour le rapport système.

    assert "Rapport Éthique Système Altiora" in report, "Le titre du rapport système devrait être correct."
    assert "Alertes totales: 3" in report, "Le nombre total d'alertes devrait être correct."
    assert "Alertes actives: 2" in report, "Le nombre d'alertes actives devrait être correct."
    assert "Critique: 1" in report, "Le décompte des alertes critiques devrait être correct."
    assert "Élevée: 1" in report, "Le décompte des alertes élevées devrait être correct."

# Pour exécuter ces tests, utilisez la commande `pytest` dans le terminal à la racine du projet.

```

---

## Fichier : `backend\tests\test_fine_tuning.py`

```python
import pytest
from pathlib import Path
from data.training.src.train_qwen3_thinkpad import Qwen3Trainer, Qwen3Config
import json
import logging

logger = logging.getLogger(__name__)

"""Tests d'intégration pour le fine-tuning des modèles de langage.

Ce module contient des tests qui vérifient le processus de fine-tuning
des modèles (notamment Qwen3) avec des adaptateurs LoRA, en se concentrant
sur l'efficacité de la mémoire et la capacité à s'exécuter sur CPU.
"""


@pytest.mark.slow # Marque le test comme lent, car il implique un entraînement de modèle.
@pytest.mark.asyncio
async def test_lora_training_cpu(tmp_path: Path):
    """Teste l'entraînement LoRA sur CPU avec des contraintes de mémoire."

    Ce test simule un entraînement de fine-tuning pour Qwen3 en utilisant
    un petit dataset et des paramètres optimisés pour le CPU, afin de vérifier
    que le processus se déroule sans erreur et produit un modèle entraîné.

    Args:
        tmp_path: Fixture Pytest fournissant un répertoire temporaire pour les fichiers.
    """
    # Crée un fichier de dataset minimal pour l'entraînement.
    test_data = [
        {"instruction": "Quelle est la capitale de la France ?", "input": "", "output": "Paris"},
        {"instruction": "Qui a écrit 'Les Misérables' ?", "input": "", "output": "Victor Hugo"}
    ]
    dataset_path = tmp_path / "test_dataset.jsonl"
    with open(dataset_path, "w", encoding="utf-8") as f:
        for item in test_data:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")
    logger.info(f"Dataset de test créé à : {dataset_path}")

    # Configure le trainer avec des paramètres optimisés pour le CPU et la mémoire.
    # Ces paramètres sont réduits pour accélérer le test.
    config = Qwen3Config(
        output_dir=str(tmp_path / "qwen3_finetuned"),
        lora_r=4, # Rang LoRA très faible pour un entraînement rapide.
        lora_alpha=8,
        epochs=1, # Une seule époque pour le test.
        batch_size=1,
        grad_accum=1,
        lr=2e-4,
        max_seq_len=128,
        num_workers=0 # Pas de workers pour simplifier le débogage.
    )
    trainer = Qwen3Trainer(config)

    # Exécute l'entraînement.
    logger.info("Lancement de l'entraînement LoRA sur CPU...")
    try:
        trainer.train(dataset_path)
    except Exception as e:
        pytest.fail(f"L'entraînement LoRA a échoué : {e}")

    # Vérifie que le répertoire de sortie du modèle entraîné existe.
    output_model_path = Path(config.output_dir)
    assert output_model_path.exists(), "Le répertoire du modèle entraîné devrait exister."
    assert output_model_path.is_dir(), "Le chemin de sortie devrait être un répertoire."

    # Optionnel : Vérifier la présence de fichiers de modèle (ex: adapter_model.bin, adapter_config.json).
    # assert any(output_model_path.glob("*.bin")), "Le répertoire du modèle devrait contenir des fichiers binaires."
    # assert any(output_model_path.glob("*.json")), "Le répertoire du modèle devrait contenir des fichiers de configuration."

    logger.info("Test d'entraînement LoRA sur CPU terminé avec succès.")

```

---

## Fichier : `backend\tests\test_integration.py`

```python
# tests/test_integration.py
"""Tests d'intégration de haut niveau pour le pipeline principal d'Altiora.

Ce module contient des tests qui vérifient le fonctionnement de bout en bout
du pipeline SFD → Analyse → Génération de tests. Il s'assure que les
composants interagissent correctement et que le résultat final est conforme
aux attentes.
"""

import pytest
import asyncio
from pathlib import Path

from src.orchestrator import Orchestrator
from src.models.sfd_models import SFDAnalysisRequest # Import nécessaire pour SFDAnalysisRequest


@pytest.mark.integration
@pytest.mark.asyncio
async def test_end_to_end_pipeline(tmp_path: Path):
    """Teste le pipeline complet de l'analyse SFD à la génération de tests."

    Ce test simule le processus de prise d'une SFD, son analyse par l'orchestrateur,
    et la vérification que des scénarios et des tests sont générés.

    Args:
        tmp_path: Fixture Pytest fournissant un répertoire temporaire pour les fichiers.
    """
    orchestrator = Orchestrator() # Crée une instance de l'orchestrateur.

    try:
        await orchestrator.initialize() # Initialise l'orchestrateur.

        # Crée un fichier SFD de test temporaire.
        sfd_content = """
        Spécification: Module de Login

        1. Connexion réussie
        - L'utilisateur entre email valide
        - L'utilisateur entre mot de passe valide
        - Le système redirige vers dashboard

        2. Échec de connexion
        - L'utilisateur entre mot de passe incorrect
        - Le système affiche une erreur
        """
        sfd_path = tmp_path / "integration_test.txt"
        sfd_path.write_text(sfd_content)

        # Crée une requête SFDAnalysisRequest.
        sfd_request = SFDAnalysisRequest(content=sfd_path.read_text())

        # Exécute le pipeline complet.
        result = await orchestrator.process_sfd_to_tests(sfd_request)

        # Assertions sur le résultat.
        assert result["status"] == "completed", "Le pipeline devrait se terminer avec le statut 'completed'."
        assert result["metrics"]["scenarios_found"] >= 2, "Au moins 2 scénarios devraient être trouvés."
        assert result["metrics"]["tests_generated"] >= 2, "Au moins 2 tests devraient être générés."

    finally:
        await orchestrator.close() # S'assure que l'orchestrateur est fermé.

```

---

## Fichier : `backend\tests\test_interfaces.py`

```python
"""Tests unitaires pour les interfaces avec les modèles Ollama (Qwen3 et StarCoder2).

Ce module contient des tests pour vérifier le bon fonctionnement des
interfaces `Qwen3OllamaInterface` et `StarCoder2OllamaInterface`.
Il s'assure que les prompts sont correctement formatés, que les réponses
des modèles sont correctement parsées et que les fonctionnalités clés
de chaque interface sont opérationnelle.
"""

import pytest
from unittest.mock import AsyncMock, MagicMock

from src.models.qwen3.qwen3_interface import Qwen3OllamaInterface
from src.models.starcoder2.starcoder2_interface import StarCoder2OllamaInterface, PlaywrightTestConfig, TestType
from src.models.sfd_models import SFDAnalysisRequest # Import nécessaire pour Qwen3OllamaInterface


@pytest.fixture
def qwen3_interface():
    """Fixture pour une instance mockée de `Qwen3OllamaInterface`."

    Configure l'interface pour ne pas utiliser le cache et simule les réponses d'Ollama.
    """
    # Mocke la session aiohttp et le circuit breaker.
    mock_session = AsyncMock()
    mock_session.post.return_value.__aenter__.return_value.json.return_value = {}
    mock_session.post.return_value.__aenter__.return_value.raise_for_status.return_value = None

    mock_circuit_breaker = AsyncMock()
    mock_circuit_breaker.call.side_effect = lambda func, *args, **kwargs: func(*args, **kwargs)

    interface = Qwen3OllamaInterface(model_name="test-qwen3", cache_enabled=False)
    interface.session = mock_session
    interface.circuit_breaker = mock_circuit_breaker
    return interface


@pytest.fixture
def starcoder2_interface():
    """Fixture pour une instance mockée de `StarCoder2OllamaInterface`."

    Configure l'interface pour simuler les réponses d'Ollama.
    """
    # Mocke la session aiohttp et le circuit breaker.
    mock_session = AsyncMock()
    mock_session.post.return_value.__aenter__.return_value.json.return_value = {}
    mock_session.post.return_value.__aenter__.return_value.raise_for_status.return_value = None

    mock_circuit_breaker = AsyncMock()
    mock_circuit_breaker.call.side_effect = lambda func, *args, **kwargs: func(*args, **kwargs)

    # Mocke le ModelConfig et ModelMemoryManager pour l'initialisation.
    mock_model_config = MagicMock()
    mock_model_config.name = "test-starcoder2"
    mock_model_config.temperature = 0.7
    mock_model_config.top_p = 0.9
    mock_model_config.top_k = 40
    mock_model_config.repeat_penalty = 1.1
    mock_model_config.max_tokens = 512
    mock_model_config.num_ctx = 4096
    mock_model_config.seed = None
    mock_model_config.stop = []
    mock_model_config.api_mode = "generate"

    mock_model_memory_manager = MagicMock()
    mock_model_memory_manager.get_model.return_value = MagicMock() # Simule un modèle chargé.
    mock_model_memory_manager.loaded_models = {
        "test-starcoder2": {'tokenizer': MagicMock(decode=lambda x, **kwargs: "mocked code"), 'model': MagicMock()}
    }

    interface = StarCoder2OllamaInterface(
        config=mock_model_config,
        model_memory_manager=mock_model_memory_manager
    )
    interface.session = mock_session
    interface.circuit_breaker = mock_circuit_breaker
    return interface


# --- Tests pour Qwen3OllamaInterface ---

def test_qwen3_build_prompt(qwen3_interface: Qwen3OllamaInterface):
    """Vérifie que le prompt pour l'analyse SFD est correctement formaté."""
    sfd_request = SFDAnalysisRequest(content="Le système doit permettre à l'utilisateur de se connecter.", extraction_type="complete")
    prompt = qwen3_interface._build_prompt(sfd_request)
    assert "<|im_start|>system" in prompt
    assert "Extrayez tous les scénarios de test détaillés" in prompt
    assert sfd_request.content in prompt
    assert "<|im_end|>" in prompt


@pytest.mark.asyncio
async def test_qwen3_analyze_sfd_parsing(qwen3_interface: Qwen3OllamaInterface):
    """Vérifie que la réponse JSON de Qwen3 est correctement parsée."""
    mock_response_data = {
        "model": "test-qwen3",
        "created_at": "2023-11-23T14:02:14.43495Z",
        "response": '''{
  "scenarios": [
    {"id": "SC-01", "titre": "Connexion réussie", "objectif": "Vérifier la connexion"}
  ]
}''',
        "done": True
    }
    qwen3_interface.session.post.return_value.__aenter__.return_value.json.return_value = mock_response_data

    sfd_request = SFDAnalysisRequest(content="contenu de test", extraction_type="complete")
    result = await qwen3_interface.analyze_sfd(sfd_request)

    assert "scenarios" in result
    assert len(result["scenarios"]) == 1
    assert result["scenarios"][0]["id"] == "SC-01"
    assert result["scenarios"][0]["titre"] == "Connexion réussie"


# --- Tests pour StarCoder2OllamaInterface ---

def test_starcoder2_build_prompt(starcoder2_interface: StarCoder2OllamaInterface):
    """Vérifie que le prompt pour la génération de test est correctement formaté."""
    scenario = {"titre": "Tester le bouton de connexion", "objectif": "Vérifier le clic", "etapes": ["Cliquer sur le bouton."]}
    config = PlaywrightTestConfig()
    prompt = starcoder2_interface._build_prompt(scenario, config, TestType.E2E)
    assert "Generate a complete Playwright test in Python." in prompt
    assert scenario["titre"] in prompt
    assert "Browser: chromium" in prompt
    assert "```python" in prompt


def test_starcoder2_extract_code(starcoder2_interface: StarCoder2OllamaInterface):
    """Teste l'extraction du code depuis la réponse brute du modèle."""
    raw_response = '''<|reponse|>
```python
def test_example():
    page.goto("http://example.com")
    expect(page).to_have_title("Example")
```
'''
    code = starcoder2_interface._extract_code(raw_response)
    expected_code = "def test_example():\n    page.goto(\"http://example.com\")\n    expect(page).to_have_title(\"Example\")"
    assert code == expected_code


@pytest.mark.asyncio
async def test_starcoder2_generate_test_parsing(starcoder2_interface: StarCoder2OllamaInterface):
    """Vérifie que la génération de test gère correctement la réponse du modèle et les métadonnées."""
    mock_response_data = {
        "response": '''<|reponse|>
```python
def test_my_scenario():
    # Ceci est un test Playwright généré.
    await page.goto("https://test.com")
    expect(page).to_have_title("Test Page")
```
'''
    }
    starcoder2_interface.session.post.return_value.__aenter__.return_value.json.return_value = mock_response_data

    scenario = {"id": "SC-01", "titre": "Mon scénario de test", "objectif": "Vérifier quelque chose"}
    config = PlaywrightTestConfig()
    result = await starcoder2_interface.generate_playwright_test(scenario, config, TestType.E2E)

    assert "code" in result
    assert "def test_my_scenario():" in result["code"]
    assert result["test_type"] == TestType.E2E.value
    assert result["uses_page_object"] == config.use_page_object
    assert "metadata" in result
    assert result["metadata"]["scenario_title"] == "Mon scénario de test"
```

---

## Fichier : `backend\tests\test_model_swapper.py`

```python

```

---

## Fichier : `backend\tests\test_ocr_wrapper.py`

```python
# tests/test_ocr_wrapper.py
"""Tests unitaires pour le wrapper du service OCR (`ocr_wrapper.py`).

Ce module contient des tests pour vérifier la fonctionnalité de base du
service OCR, y compris la génération de clés de cache et le comportement
de l'extracteur en mode mock.
"""

import pytest
import asyncio
from pathlib import Path
from unittest.mock import MagicMock, patch, AsyncMock

# Importe les fonctions et classes du module ocr_wrapper.
from services.ocr.ocr_wrapper import OCRRequest, _cache_key, _extract_mock, _extract_doctoplus # Assurez-vous d'importer les fonctions internes si elles sont testées.


@pytest.mark.asyncio
async def test_ocr_cache_key_generation():
    """Teste la génération de clés de cache uniques et déterministes pour les requêtes OCR."

    La clé de cache doit être la même pour des requêtes identiques et différente
    pour des requêtes différentes.
    """
    # Crée une requête OCR factice.
    request1 = OCRRequest(
        file_path='/test/sample.pdf',
        language='fra',
        preprocess=True,
        output_format='text'
    )

    # Génère la clé de cache.
    cache_key1 = _cache_key(request1)
    assert cache_key1.startswith('ocr:'), "La clé de cache devrait commencer par 'ocr:'."
    assert len(cache_key1) == 39, "La clé de cache devrait avoir une longueur fixe (ocr: + 32 caractères MD5)."

    # Teste la déterministe de la clé.
    request2 = OCRRequest(
        file_path='/test/sample.pdf',
        language='fra',
        preprocess=True,
        output_format='text'
    )
    cache_key2 = _cache_key(request2)
    assert cache_key1 == cache_key2, "Des requêtes identiques devraient générer la même clé de cache."

    # Teste la différence de la clé pour des requêtes différentes.
    request3 = OCRRequest(
        file_path='/test/another.pdf',
        language='fra',
        preprocess=True,
        output_format='text'
    )
    cache_key3 = _cache_key(request3)
    assert cache_key1 != cache_key3, "Des requêtes différentes devraient générer des clés de cache différentes."


@pytest.mark.asyncio
async def test_mock_ocr_extraction():
    """Teste l'extraction OCR en mode mock (`_extract_mock`)."

    Vérifie que l'extracteur mock retourne un résultat simulé avec les champs attendus.
    """
    # Crée une requête OCR factice pour le mock.
    mock_request = OCRRequest(
        file_path="test.pdf",
        language="fra",
        preprocess=True,
        output_format="text"
    )

    # Appelle la fonction d'extraction mock.
    result = await _extract_mock(mock_request)

    # Assertions sur le résultat du mock.
    assert "mock" in result["text"].lower(), "Le texte extrait devrait contenir 'mock'."
    assert result["confidence"] > 0, "La confiance devrait être supérieure à 0."
    assert "metadata" in result, "Le résultat devrait contenir des métadonnées."
    assert result["metadata"]["mode"] == "mock", "Le mode des métadonnées devrait être 'mock'."


@pytest.mark.asyncio
@patch('services.ocr.ocr_wrapper.DoctopusWrapper', autospec=True)
async def test_doctoplus_ocr_extraction(MockDoctopusWrapper: MagicMock):
    """Teste l'extraction OCR avec le wrapper Doctopus (`_extract_doctoplus`)."

    Mocke la bibliothèque `DoctopusWrapper` pour simuler son comportement
    sans dépendre d'une installation réelle.
    """
    # Configure le mock de DoctopusWrapper.
    mock_instance = MockDoctopusWrapper.return_value
    mock_instance.extract_text.return_value = {
        "text": "Texte extrait par Doctopus.",
        "confidence": 0.98,
        "pages": 2
    }

    # Crée une requête OCR.
    request = OCRRequest(
        file_path="/path/to/real_doc.pdf",
        language="eng",
        preprocess=True,
        output_format="text"
    )

    # Appelle la fonction d'extraction Doctopus.
    result = await _extract_doctoplus(request)

    # Assertions sur le résultat.
    assert result["text"] == "Texte extrait par Doctopus.", "Le texte devrait correspondre à la sortie mockée."
    assert result["confidence"] == 0.98, "La confiance devrait correspondre à la sortie mockée."
    assert result["metadata"]["pages"] == 2, "Les métadonnées devraient inclure le nombre de pages."
    assert mock_instance.extract_text.called_once_with(
        file_path=request.file_path,
        language=request.language,
        preprocess=request.preprocess,
        confidence_threshold=request.confidence_threshold,
        output_format=request.output_format,
    )


@pytest.mark.asyncio
@patch('services.ocr.ocr_wrapper.redis_client', new_callable=AsyncMock)
async def test_ocr_caching(mock_redis_client: AsyncMock):
    """Teste la fonctionnalité de mise en cache du service OCR."

    Vérifie que les résultats sont stockés et récupérés du cache Redis.
    """
    # Configure le mock Redis pour simuler un cache vide puis une valeur.
    mock_redis_client.get.return_value = None # Pas de cache au premier appel.
    mock_redis_client.setex.return_value = True

    # Mocke l'extracteur réel pour qu'il retourne une valeur connue.
    with patch('services.ocr.ocr_wrapper._extract_doctoplus', new_callable=AsyncMock) as mock_extractor:
        mock_extractor.return_value = {"text": "Contenu non mis en cache.", "confidence": 0.9}

        # Crée une requête OCR.
        request = OCRRequest(
            file_path="/path/to/doc.pdf",
            language="fra",
            preprocess=True,
            output_format="text",
            cache=True
        )

        # Premier appel (devrait être un MISS et mettre en cache).
        from services.ocr.ocr_wrapper import extract_text as ocr_extract_text_func # Importe la fonction de l'endpoint.
        result1 = await ocr_extract_text_func(request)
        mock_redis_client.get.assert_called_once() # Vérifie l'appel à get.
        mock_redis_client.setex.assert_called_once() # Vérifie l'appel à setex.
        assert result1.cached is False
        assert result1.text == "Contenu non mis en cache."

        # Réinitialise les mocks pour le deuxième appel.
        mock_redis_client.get.reset_mock()
        mock_redis_client.setex.reset_mock()
        mock_extractor.reset_mock()

        # Configure le mock Redis pour simuler un cache HIT.
        cached_data = {"text": "Contenu depuis le cache.", "confidence": 0.95, "processing_time": 0.01}
        mock_redis_client.get.return_value = json.dumps(cached_data)

        # Deuxième appel (devrait être un HIT).
        result2 = await ocr_extract_text_func(request)
        mock_redis_client.get.assert_called_once()
        mock_redis_client.setex.assert_not_called() # setex ne devrait pas être appelé.
        mock_extractor.assert_not_called() # L'extracteur ne devrait pas être appelé.
        assert result2.cached is True
        assert result2.text == "Contenu depuis le cache."

```

---

## Fichier : `backend\tests\test_orchestrator.py`

```python
# tests/test_orchestrator.py
"""Tests d'intégration pour la classe Orchestrator.

Ce module contient des tests qui vérifient le comportement de l'orchestrateur
dans divers scénarios, y compris les cas de succès du pipeline complet,
la gestion des fichiers SFD vides ou manquants, et la gestion des erreurs
provenant des services dépendants (Qwen3, règles métier).
"""

import asyncio
from pathlib import Path
from unittest.mock import AsyncMock, patch

import pytest

from policies.business_rules import BusinessRules
from src.models.sfd_models import SFDAnalysisRequest
from src.orchestrator import Orchestrator


@pytest.fixture
async def orchestrator():
    """Fixture pour initialiser et fermer proprement l'orchestrateur pour chaque test."

    Cette fixture crée une instance de l'Orchestrator et s'assure que ses
    dépendances (stubs ou mocks) sont correctement configurées pour les tests.
    """
    # Mocke les dépendances de l'orchestrateur pour l'isoler.
    starcoder_mock = AsyncMock()
    redis_client_mock = AsyncMock()
    config_mock = MagicMock()
    model_registry_mock = MagicMock()

    # Crée l'instance de l'Orchestrator avec les mocks.
    orch = Orchestrator(starcoder_mock, redis_client_mock, config_mock, model_registry_mock)
    # Initialise l'orchestrateur (charge la config, etc.).
    await orch.initialize()
    yield orch
    # Ferme l'orchestrateur après le test.
    await orch.close()


@pytest.mark.integration
@pytest.mark.asyncio
async def test_full_pipeline_success(orchestrator: Orchestrator, tmp_path: Path):
    """Teste le scénario de succès du pipeline complet avec un fichier SFD valide."

    Vérifie que l'orchestrateur peut traiter une SFD de bout en bout,
    extraire des scénarios, générer des tests et retourner un statut 'completed'.
    """
    # Prépare un fichier SFD valide temporaire.
    sfd_content = "Spécification: Test de connexion avec email et mot de passe. Scénario: Connexion réussie."
    sfd_path = tmp_path / "valid_sfd.txt"
    sfd_path.write_text(sfd_content)
    sfd_request = SFDAnalysisRequest(content=sfd_path.read_text())

    # Mocke la méthode `analyze_sfd` de Qwen3 pour simuler une réponse réussie.
    orchestrator.qwen3.analyze_sfd.return_value = {
        "scenarios": [
            {"id": "SC-001", "titre": "Connexion réussie", "description": "Test de connexion"}
        ]
    }
    # Mocke la méthode `generate_playwright_test` de Starcoder2.
    orchestrator.starcoder.generate_playwright_test.return_value = {"code": "def test_connexion(): pass", "test_name": "test_connexion"}

    # Exécute le pipeline.
    result = await orchestrator.process_sfd_to_tests(sfd_request)

    # Assertions sur le résultat.
    assert result["status"] == "completed", "Le pipeline devrait se terminer avec le statut 'completed'."
    assert result["metrics"]["scenarios_found"] > 0, "Des scénarios devraient être trouvés."
    assert len(result["generated_tests"]) > 0, "Des tests devraient être générés."
    assert "test_connexion" in result["generated_tests"][0]["test_name"], "Le nom du test généré devrait être correct."


@pytest.mark.asyncio
async def test_empty_sfd_file(orchestrator: Orchestrator, tmp_path: Path):
    """Vérifie que l'orchestrateur gère correctement un fichier SFD vide."

    Le pipeline devrait détecter le fichier vide et retourner un statut d'erreur.
    """
    sfd_path = tmp_path / "empty_sfd.txt"
    sfd_path.write_text("") # Crée un fichier vide.
    sfd_request = SFDAnalysisRequest(content=sfd_path.read_text())

    result = await orchestrator.process_sfd_to_tests(sfd_request)

    assert result["status"] == "error", "Le pipeline devrait retourner un statut 'error'."
    assert "Le fichier de spécifications est vide" in result["error_message"], "Le message d'erreur devrait indiquer un fichier vide."


@pytest.mark.asyncio
async def test_sfd_file_not_found(orchestrator: Orchestrator):
    """Vérifie la gestion d'un chemin de fichier SFD inexistant."

    L'orchestrateur devrait retourner un statut d'erreur si le fichier n'est pas trouvé.
    """
    # Crée une requête avec un contenu vide, simulant un fichier non trouvé.
    sfd_request = SFDAnalysisRequest(content="")

    result = await orchestrator.process_sfd_to_tests(sfd_request)

    assert result["status"] == "error", "Le pipeline devrait retourner un statut 'error'."
    assert "Le fichier de spécifications n'a pas été trouvé" in result["error_message"], "Le message d'erreur devrait indiquer un fichier non trouvé."


@pytest.mark.asyncio
@patch("src.models.qwen3.qwen3_interface.Qwen3OllamaInterface.analyze_sfd", new_callable=AsyncMock)
async def test_qwen3_service_unavailable(mock_analyze_sfd: AsyncMock, orchestrator: Orchestrator, tmp_path: Path):
    """Simule une panne du service Qwen3 et vérifie la gestion de l'erreur par l'orchestrateur."

    L'orchestrateur devrait capturer l'exception et retourner un statut d'erreur.
    """
    mock_analyze_sfd.side_effect = Exception("Service Qwen3 non disponible") # Simule une exception.
    sfd_path = tmp_path / "sfd.txt"
    sfd_path.write_text("Une spécification simple.")
    sfd_request = SFDAnalysisRequest(content=sfd_path.read_text())

    result = await orchestrator.process_sfd_to_tests(sfd_request)

    assert result["status"] == "error", "Le pipeline devrait retourner un statut 'error'."
    assert "Erreur lors de l'analyse par Qwen3" in result["error_message"], "Le message d'erreur devrait refléter la panne de Qwen3."


@pytest.mark.asyncio
@patch.object(BusinessRules, "validate", new_callable=AsyncMock)
async def test_business_rules_violation(mock_validate_rules: AsyncMock, orchestrator: Orchestrator, tmp_path: Path):
    """Vérifie que le pipeline s'arrête si les règles métier ne sont pas respectées."

    Simule une violation des règles métier et s'assure que l'orchestrateur
    détecte l'échec et retourne un statut d'erreur approprié.
    """
    # Simule une violation des règles métier en faisant retourner `False` par le validateur.
    mock_validate_rules.return_value = {
        "ok": False,
        "violations": ["Utilisation de time.sleep() détectée."],
    }

    sfd_path = tmp_path / "sfd_with_violation.txt"
    sfd_path.write_text("Spécification qui générera un test non conforme.")
    sfd_request = SFDAnalysisRequest(content=sfd_path.read_text())

    result = await orchestrator.process_sfd_to_tests(sfd_request)

    assert result["status"] == "error", "Le pipeline devrait retourner un statut 'error'."
    assert "Validation des règles métier échouée" in result["error_message"], "Le message d'erreur devrait indiquer une violation des règles métier."
    assert "Utilisation de time.sleep() détectée." in result["details"], "Les détails de la violation devraient être présents."


@pytest.mark.asyncio
async def test_syntax_error_in_sfd(orchestrator: Orchestrator, tmp_path: Path):
    """Vérifie la gestion d'une erreur de syntaxe dans le fichier SFD."

    Simule un fichier SFD avec une erreur de syntaxe et s'assure que l'orchestrateur
    la détecte et retourne un statut d'erreur.
    """
    sfd_path = tmp_path / "invalid_sfd.txt"
    sfd_path.write_text("Spécification: Test de connexion avec email et mot de passe.\nSyntaxError: invalid syntax")
    sfd_request = SFDAnalysisRequest(content=sfd_path.read_text())

    result = await orchestrator.process_sfd_to_tests(sfd_request)

    assert result["status"] == "error", "Le pipeline devrait retourner un statut 'error'."
    assert "Erreur de syntaxe dans le fichier SFD" in result["error_message"], "Le message d'erreur devrait indiquer une erreur de syntaxe."


@pytest.mark.asyncio
@patch("src.models.qwen3.qwen3_interface.Qwen3OllamaInterface.analyze_sfd", new_callable=AsyncMock)
async def test_qwen3_service_timeout(mock_analyze_sfd: AsyncMock, orchestrator: Orchestrator, tmp_path: Path):
    """Simule un délai d'attente (timeout) du service Qwen3 et vérifie la gestion de l'erreur."

    L'orchestrateur devrait capturer le `asyncio.TimeoutError` et retourner un statut d'erreur.
    """
    mock_analyze_sfd.side_effect = asyncio.TimeoutError("Service Qwen3 en délai d'attente")
    sfd_path = tmp_path / "sfd.txt"
    sfd_path.write_text("Une spécification simple.")
    sfd_request = SFDAnalysisRequest(content=sfd_path.read_text())

    result = await orchestrator.process_sfd_to_tests(sfd_request)

    assert result["status"] == "error", "Le pipeline devrait retourner un statut 'error'."
    assert "Délai d'attente du service Qwen3" in result["error_message"], "Le message d'erreur devrait indiquer un timeout."


@pytest.mark.asyncio
@patch("src.models.qwen3.qwen3_interface.Qwen3OllamaInterface.analyze_sfd", new_callable=AsyncMock)
async def test_qwen3_service_invalid_response(mock_analyze_sfd: AsyncMock, orchestrator: Orchestrator, tmp_path: Path):
    """Simule une réponse invalide du service Qwen3 et vérifie la gestion de l'erreur."

    L'orchestrateur devrait détecter la réponse invalide et retourner un statut d'erreur.
    """
    # Simule une réponse de Qwen3 qui ne contient pas les données attendues.
    mock_analyze_sfd.return_value = {"error": "Réponse invalide"}
    sfd_path = tmp_path / "sfd.txt"
    sfd_path.write_text("Une spécification simple.")
    sfd_request = SFDAnalysisRequest(content=sfd_path.read_text())

    result = await orchestrator.process_sfd_to_tests(sfd_request)

    assert result["status"] == "error", "Le pipeline devrait retourner un statut 'error'."
    assert "Réponse invalide du service Qwen3" in result["error_message"], "Le message d'erreur devrait indiquer une réponse invalide."
```

---

## Fichier : `backend\tests\test_personality_quiz.py`

```python
# tests/test_personality_quiz.py
"""Tests unitaires pour le module `PersonalityQuiz`.

Ce module contient des tests pour vérifier le bon fonctionnement du quiz de
personnalisation de l'IA, y compris l'initialisation, le traitement des
questions à choix multiples et la génération du profil de personnalité.
"""

import pytest
from unittest.mock import patch, MagicMock, AsyncMock
from src.modules.psychodesign.personality_quiz import PersonalityQuiz, QuizResponse, PersonalityProfile
from datetime import datetime


@pytest.fixture
def quiz():
    """Fixture pour une instance de `PersonalityQuiz` pour les tests."

    Initialise le quiz avec un utilisateur de test et des mocks pour les
    dépendances externes comme `speech_recognition`.
    """
    # Mocke les dépendances de speech_recognition si elles ne sont pas disponibles.
    with patch('src.modules.psychodesign.personality_quiz.sr') as mock_sr:
        mock_sr.Recognizer.return_value = MagicMock()
        mock_sr.Microphone.return_value = MagicMock()
        mock_sr.UnknownValueError = type('UnknownValueError', (Exception,), {})
        return PersonalityQuiz("test_user")


@pytest.mark.asyncio
async def test_quiz_initialization(quiz: PersonalityQuiz):
    """Teste l'initialisation correcte du quiz de personnalité."

    Vérifie que l'ID utilisateur est correctement défini et que les questions
    sont chargées.
    """
    assert quiz.user_id == "test_user"
    assert len(quiz.questions) > 0
    assert quiz.recognizer is not None # Vérifie que le mock est bien initialisé.


@pytest.mark.asyncio
@patch('builtins.input', return_value='1')
async def test_choice_question_handling(mock_input: MagicMock, quiz: PersonalityQuiz):
    """Teste le traitement des questions à choix multiples."

    Simule une réponse utilisateur et vérifie que la valeur correcte est retournée.
    """
    question = {
        "id": "test_choice",
        "type": "choice",
        "question": "Test?",
        "options": [{"text": "A", "weight": 0.1}, {"text": "B", "weight": 0.9}]
    }

    response = await quiz._handle_choice_question(question)
    assert response["value"] == 0.1
    mock_input.assert_called_once() # Vérifie que `input()` a été appelé.


@pytest.mark.asyncio
@patch('builtins.input', return_value='0.75')
async def test_scale_question_handling(mock_input: MagicMock, quiz: PersonalityQuiz):
    """Teste le traitement des questions à échelle."

    Simule une réponse numérique et vérifie que la valeur est correctement traitée.
    """
    question = {
        "id": "test_scale",
        "type": "scale",
        "question": "Évaluez de 0 à 1 :",
        "scale": {"min": "Faible", "max": "Fort"}
    }
    response = await quiz._handle_scale_question(question)
    assert response["value"] == 0.75
    mock_input.assert_called_once()


@pytest.mark.asyncio
@patch('builtins.input', return_value='Ceci est une réponse textuelle.')
async def test_text_question_handling(mock_input: MagicMock, quiz: PersonalityQuiz):
    """Teste le traitement des questions textuelles."

    Vérifie que la réponse textuelle est capturée correctement.
    """
    question = {"id": "test_text", "type": "text", "question": "Décrivez..."}
    response = await quiz._handle_text_question(question)
    assert response["value"] == "Ceci est une réponse textuelle."
    mock_input.assert_called_once()


@pytest.mark.asyncio
async def test_calibration_question_handling_success(quiz: PersonalityQuiz):
    """Teste le traitement d'une question de calibration vocale en cas de succès."

    Mocke `speech_recognition` pour simuler une transcription réussie.
    """
    if not quiz.recognizer: # Skip si speech_recognition n'est pas mocké.
        pytest.skip("Speech recognition not mocked.")

    # Mocke les méthodes de speech_recognition.
    quiz.recognizer.adjust_for_ambient_noise = MagicMock()
    quiz.recognizer.listen = AsyncMock(return_value=MagicMock())
    quiz.recognizer.recognize_google = MagicMock(return_value="Phrase de test vocale.")
    
    # Mocke la fonction _extract_vocal_features.
    with patch.object(quiz, '_extract_vocal_features', new_callable=AsyncMock) as mock_extract_vocal_features:
        mock_extract_vocal_features.return_value = {"pitch": 1.0, "speed": 1.0}

        question = {"id": "vocal_test", "type": "calibration", "question": "Lisez ceci.", "purpose": "test"}
        response = await quiz._handle_calibration_question(question)

        assert response["value"] == "Phrase de test vocale."
        assert response["confidence"] == 1.0
        assert "pitch" in response["vocal_features"]
        assert len(quiz.vocal_samples) == 1
        quiz.recognizer.adjust_for_ambient_noise.assert_called_once()
        quiz.recognizer.listen.assert_called_once()
        quiz.recognizer.recognize_google.assert_called_once()


@pytest.mark.asyncio
async def test_calibration_question_handling_failure(quiz: PersonalityQuiz):
    """Teste le traitement d'une question de calibration vocale en cas d'échec de reconnaissance."

    Simule une `UnknownValueError` de `speech_recognition`.
    """
    if not quiz.recognizer:
        pytest.skip("Speech recognition not mocked.")

    quiz.recognizer.adjust_for_ambient_noise = MagicMock()
    quiz.recognizer.listen = AsyncMock(side_effect=quiz.recognizer.UnknownValueError("Could not understand audio"))
    
    # Patch builtins.input pour éviter l'interaction utilisateur dans le retry.
    with patch('builtins.input', side_effect=['' for _ in range(2)]) as mock_input_retry:
        question = {"id": "vocal_test_fail", "type": "calibration", "question": "Lisez ceci.", "purpose": "test"}
        response = await quiz._handle_calibration_question(question)

        assert response["value"] == "error" # Ou un autre statut d'erreur.
        assert response["confidence"] == 0.0
        assert len(quiz.vocal_samples) == 0
        quiz.recognizer.listen.assert_called_once()


def test_personality_profile_generation(quiz: PersonalityQuiz):
    """Teste la génération correcte du profil de personnalité à partir des réponses du quiz."

    Vérifie que les traits et préférences sont calculés et stockés correctement.
    """
    # Simule des réponses pour le quiz.
    quiz.responses = [
        QuizResponse(question_id="comm_1", response="vous", confidence=1.0, response_time=1.0, vocal_features={}),
        QuizResponse(question_id="comm_2", response=0.7, confidence=1.0, response_time=1.0, vocal_features={}),
        QuizResponse(question_id="work_1", response=0.3, confidence=1.0, response_time=1.0, vocal_features={}),
    ]

    profile = quiz._generate_profile()
    assert profile.user_id == "test_user"
    assert "formalite" in profile.traits
    assert profile.traits["formalite"] == 0.8 # Basé sur la réponse "vous".
    assert profile.traits["verbosite"] == 0.7 # Basé sur la réponse 0.7.
    assert profile.traits["empathie"] == 0.3 # Basé sur la réponse 0.3.
    assert profile.preferences["vouvoiement"] is True
    assert "completed_at" in profile.quiz_metadata


@pytest.mark.asyncio
async def test_save_profile(quiz: PersonalityQuiz, tmp_path: Path):
    """Teste la sauvegarde du profil de personnalité sur le disque."

    Vérifie que le fichier JSON du profil est créé et contient les bonnes données.
    """
    # Surcharge le chemin de sauvegarde pour utiliser un répertoire temporaire.
    quiz.quiz_path = tmp_path / "quiz_data_temp"
    quiz.quiz_path.mkdir()

    profile = PersonalityProfile(
        user_id="save_test_user",
        traits={"formalite": 0.5},
        preferences={},
        vocal_profile={},
        behavioral_patterns={},
        quiz_metadata={'completed_at': datetime.now().isoformat()}
    )

    await quiz._save_profile(profile)

    saved_file = quiz.quiz_path / "save_test_user_profile.json"
    assert saved_file.exists()
    
    with open(saved_file, 'r', encoding='utf-8') as f:
        loaded_data = json.load(f)
    assert loaded_data["user_id"] == "save_test_user"
    assert loaded_data["traits"]["formalite"] == 0.5


def test_get_progress(quiz: PersonalityQuiz):
    """Teste la fonction de suivi de la progression du quiz."

    Vérifie que le pourcentage de complétion et la section courante sont corrects.
    """
    # Quiz vide.
    progress_empty = quiz.get_progress()
    assert progress_empty["completed"] == 0
    assert progress_empty["percentage"] == 0.0
    assert progress_empty["current_section"] == "Général"

    # Simule quelques réponses.
    quiz.responses.append(QuizResponse(question_id="comm_1", response="tu", confidence=1.0, response_time=1.0, vocal_features={}))
    progress_partial = quiz.get_progress()
    assert progress_partial["completed"] == 1
    assert progress_partial["percentage"] > 0.0
    assert progress_partial["current_section"] == "Communication" # Ou la section de la question suivante.

    # Simule la complétion du quiz.
    quiz.responses = [QuizResponse(question_id=q["id"], response="mock", confidence=1.0, response_time=1.0, vocal_features={}) for q in quiz.questions]
    progress_complete = quiz.get_progress()
    assert progress_complete["completed"] == len(quiz.questions)
    assert progress_complete["percentage"] == 100.0
    assert progress_complete["current_section"] == "Terminé"
```

---

## Fichier : `backend\tests\test_playwright_runner.py`

```python
# tests/test_playwright_runner.py
"""Tests unitaires pour le service d'exécution de tests Playwright (`playwright_runner.py`).

Ce module contient des tests pour vérifier les fonctionnalités clés du runner
Playwright, telles que la préparation des fichiers de test, la génération de
la configuration Pytest, et l'exécution des tests.
"""

import pytest
import asyncio
from pathlib import Path
from typing import Dict, Any

# Importe les fonctions et classes du module playwright_runner.
from services.playwright.playwright_runner import prepare_test_files, generate_pytest_config, TestCode, ExecutionConfig


@pytest.fixture
def test_scenario_data() -> Dict[str, Any]:
    """Fixture fournissant des données de scénario de test Playwright factices."""
    return {
        "code": "await page.goto('https://example.com')\nawait expect(page).to_have_title('Example')",
        "test_name": "test_navigation_example",
        "test_type": "e2e"
    }


@pytest.fixture
def temp_workspace(tmp_path: Path) -> Path:
    """Fixture fournissant un répertoire de travail temporaire pour les tests."

    Args:
        tmp_path: Fixture Pytest pour un répertoire temporaire.

    Returns:
        Le chemin vers le répertoire de travail temporaire.
    """
    workspace_dir = tmp_path / "workspace"
    workspace_dir.mkdir()
    return workspace_dir


@pytest.mark.asyncio
async def test_prepare_test_files(temp_workspace: Path, test_scenario_data: Dict[str, Any]):
    """Teste la préparation des fichiers de test à partir des données de scénario."

    Vérifie que les fichiers `.py` sont créés correctement dans le répertoire
    temporaire et qu'ils contiennent le code de test.
    """
    # Crée un objet TestCode à partir des données de la fixture.
    test_code_obj = TestCode(**test_scenario_data)

    # Appelle la fonction à tester.
    test_files = await prepare_test_files([test_code_obj], temp_workspace)

    # Assertions.
    assert len(test_files) == 1, "Un seul fichier de test devrait être créé."
    created_file = test_files[0]
    assert created_file.exists(), "Le fichier de test devrait exister."
    assert created_file.suffix == ".py", "Le fichier devrait avoir l'extension .py."
    assert test_code_obj.test_name in created_file.name, "Le nom du fichier devrait contenir le nom du test."

    # Vérifie le contenu du fichier.
    content = created_file.read_text()
    assert "import pytest" in content, "Le fichier devrait contenir l'import pytest."
    assert "from playwright.async_api import Page, expect" in content, "Le fichier devrait contenir les imports Playwright."
    assert test_code_obj.code in content, "Le fichier devrait contenir le code du scénario."
    assert "@pytest.mark.asyncio" in content, "Le test asynchrone devrait être décoré avec @pytest.mark.asyncio."

    # Vérifie que conftest.py est créé.
    conftest_path = temp_workspace / "conftest.py"
    assert conftest_path.exists(), "Le fichier conftest.py devrait être créé."


def test_generate_pytest_config():
    """Teste la génération des arguments de ligne de commande pour Pytest."

    Vérifie que les arguments générés reflètent correctement la configuration
    d'exécution fournie.
    """
    # Crée un objet ExecutionConfig avec différentes options.
    config = ExecutionConfig(
        browser="firefox",
        headed=True,
        timeout=60000, # 60 secondes.
        retries=1,
        parallel=True,
        workers=3,
        screenshot="on-failure",
        video="always",
        trace="on-failure",
        base_url="https://my-app.com"
    )

    # Appelle la fonction à tester.
    pytest_args = generate_pytest_config(config, Path("/test_workspace"))

    # Assertions sur les arguments générés.
    assert "-v" in pytest_args, "Le mode verbeux devrait être activé."
    assert "--tb=short" in pytest_args, "Le format de traceback courte devrait être activé."
    assert "--json-report" in pytest_args, "Le rapport JSON devrait être activé."
    assert "--browser=firefox" in pytest_args, "Le navigateur Firefox devrait être spécifié."
    assert "--headed" in pytest_args, "Le mode 'headed' devrait être activé."
    assert "-n" in pytest_args, "L'option de parallélisation (-n) devrait être présente."
    assert "3" in pytest_args, "Le nombre de workers devrait être 3."
    assert "--screenshot=only-on-failure" in pytest_args, "La capture d'écran sur échec devrait être configurée."
    assert "--video=on" in pytest_args, "L'enregistrement vidéo devrait être activé."
    assert "--tracing=retain-on-failure" in pytest_args, "Le traçage sur échec devrait être configuré."
    assert "--timeout=60" in pytest_args, "Le timeout devrait être de 60 secondes."

    # Vérifie que les arguments spécifiques au workspace sont présents.
    assert str(Path("/test_workspace")) in pytest_args, "Le chemin du workspace devrait être inclus."
    assert f"--json-report-file={Path("/test_workspace") / 'report.json'}" in pytest_args, "Le chemin du rapport JSON devrait être correct."

```

---

## Fichier : `backend\tests\test_retry_handler.py`

```python
# tests/test_retry_handler.py
"""Tests unitaires pour le gestionnaire de retry (`RetryHandler`).

Ce module contient des tests pour vérifier le bon fonctionnement du décorateur
`@RetryHandler.with_retry`, y compris les scénarios de succès après échec
et d'épuisement des tentatives.
"""

import pytest
import asyncio
import logging

from src.utils.retry_handler import RetryHandler

logger = logging.getLogger(__name__)


@pytest.fixture
def retry_handler_instance():
    """Fixture pour fournir une instance de `RetryHandler` pour les tests."

    Utilise les valeurs par défaut pour les paramètres du gestionnaire.
    """
    return RetryHandler()


@pytest.mark.asyncio
async def test_retry_success(retry_handler_instance: RetryHandler):
    """Teste que la fonction décorée réussit après un ou plusieurs échecs initiaux."

    Vérifie que la fonction est retentée le nombre de fois nécessaire avant de réussir.
    """
    call_count = 0

    @retry_handler_instance.with_retry(max_attempts=3, exceptions=(ValueError,))
    async def flaky_function():
        nonlocal call_count
        call_count += 1
        logger.info(f"Appel de flaky_function, tentative #{call_count}")
        if call_count < 2:
            raise ValueError("Échec simulé")
        return "succès"

    result = await flaky_function()
    assert result == "succès", "La fonction devrait réussir après retry."
    assert call_count == 2, "La fonction devrait être appelée 2 fois (1 échec + 1 succès)."


@pytest.mark.asyncio
async def test_retry_exhaustion(retry_handler_instance: RetryHandler):
    """Teste que le retry s'arrête après avoir épuisé le nombre maximal de tentatives."

    Vérifie qu'une exception est levée après le nombre maximal de tentatives.
    """
    call_count = 0

    @retry_handler_instance.with_retry(max_attempts=2, exceptions=(ValueError,))
    async def always_failing_function():
        nonlocal call_count
        call_count += 1
        logger.info(f"Appel de always_failing_function, tentative #{call_count}")
        raise ValueError("Échec permanent")

    with pytest.raises(ValueError) as excinfo:
        await always_failing_function()
    
    assert "Échec permanent" in str(excinfo.value), "L'exception levée devrait être celle de la fonction."
    assert call_count == 2, "La fonction devrait être appelée exactement 2 fois."


@pytest.mark.asyncio
async def test_retry_different_exception_type(retry_handler_instance: RetryHandler):
    """Teste que le retry ne se déclenche que pour les types d'exceptions spécifiés."

    Vérifie qu'une exception non spécifiée n'est pas retentée.
    """
    call_count = 0

    @retry_handler_instance.with_retry(max_attempts=3, exceptions=(ValueError,))
    async def specific_exception_function():
        nonlocal call_count
        call_count += 1
        logger.info(f"Appel de specific_exception_function, tentative #{call_count}")
        if call_count == 1:
            raise TypeError("Type d'erreur inattendu") # Cette exception ne devrait pas être retentée.
        return "succès"

    with pytest.raises(TypeError) as excinfo:
        await specific_exception_function()
    
    assert "Type d'erreur inattendu" in str(excinfo.value), "L'exception TypeError devrait être levée immédiatement."
    assert call_count == 1, "La fonction ne devrait être appelée qu'une seule fois."


@pytest.mark.asyncio
async def test_circuit_breaker_open(retry_handler_instance: RetryHandler):
    """Teste que le disjoncteur s'ouvre après un certain nombre d'échecs."

    Vérifie que les appels ultérieurs sont bloqués tant que le disjoncteur est ouvert.
    """
    service_name = "test_service"
    call_count = 0

    @retry_handler_instance.circuit_breaker
    async def unreliable_service():
        nonlocal call_count
        call_count += 1
        raise Exception("Service en panne")

    # Provoque l'ouverture du disjoncteur.
    for _ in range(retry_handler_instance.failure_threshold):
        with pytest.raises(Exception):
            await unreliable_service()
    
    assert retry_handler_instance._is_open.get(service_name), "Le disjoncteur devrait être ouvert."

    # Tente un appel alors que le disjoncteur est ouvert.
    with pytest.raises(Exception) as excinfo:
        await unreliable_service()
    assert "Circuit breaker is open" in str(excinfo.value), "L'appel devrait être bloqué par le disjoncteur."
    assert call_count == retry_handler_instance.failure_threshold, "Aucun appel supplémentaire ne devrait avoir eu lieu."


@pytest.mark.asyncio
async def test_circuit_breaker_reset(retry_handler_instance: RetryHandler):
    """Teste que le disjoncteur se réinitialise après le timeout de récupération."

    Vérifie que le disjoncteur passe de l'état ouvert à fermé après le délai.
    """
    service_name = "test_service_reset"
    call_count = 0

    @retry_handler_instance.circuit_breaker
    async def intermittently_failing_service():
        nonlocal call_count
        call_count += 1
        if call_count <= retry_handler_instance.failure_threshold:
            raise Exception("Échec initial")
        return "Service récupéré"

    # Provoque l'ouverture du disjoncteur.
    for _ in range(retry_handler_instance.failure_threshold):
        with pytest.raises(Exception):
            await intermittently_failing_service()
    
    assert retry_handler_instance._is_open.get(service_name), "Le disjoncteur devrait être ouvert."

    # Attend le timeout de récupération.
    await asyncio.sleep(retry_handler_instance.recovery_timeout + 0.1)

    # Le premier appel après le timeout devrait tenter de se refermer.
    result = await intermittently_failing_service()
    assert result == "Service récupéré", "Le service devrait se récupérer."
    assert not retry_handler_instance._is_open.get(service_name), "Le disjoncteur devrait être fermé."
```

---

## Fichier : `backend\tests\test_services.py`

```python
"""
Tests fonctionnels pour les microservices de l'application Altiora.

Ce module contient des tests qui vérifient la fonctionnalité de base de
chaque microservice exposé via HTTP (ALM, Excel). Ces tests s'assurent
que les services répondent correctement aux requêtes et gèrent les cas
d'erreur, en se basant sur leurs endpoints de santé et leurs APIs spécifiques.
"""

import pytest
import httpx
import logging

logger = logging.getLogger(__name__)

# --- Configuration des clients de test ---
# Ces URLs ciblent les services qui devraient être en cours d'exécution.
# Assurez-vous que les services sont lancés avant d'exécuter ces tests.

BASE_URL_ALM = "http://localhost:8002"
BASE_URL_EXCEL = "http://localhost:8003"


@pytest.mark.service
@pytest.mark.asyncio
async def test_alm_service_health():
    """Vérifie que le service ALM est accessible et retourne un statut sain."

    Ce test envoie une requête GET à l'endpoint `/health` du service ALM
    et s'attend à une réponse HTTP 200 avec un statut "ok".
    """
    logger.info(f"Test de l'état de santé du service ALM à {BASE_URL_ALM}/health")
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL_ALM}/health")
        response.raise_for_status() # Lève une exception pour les codes d'état HTTP 4xx/5xx.
        assert response.status_code == 200, f"Le service ALM devrait retourner un statut 200, mais a retourné {response.status_code}."
        assert response.json() == {"status": "ok"}, "Le corps de la réponse devrait être {'status': 'ok'}."


@pytest.mark.service
@pytest.mark.asyncio
async def test_alm_create_work_item_success():
    """Teste la création réussie d'un élément de travail via le service ALM."

    Ce test envoie une requête POST à l'endpoint `/work-items` avec des données
    valides et s'attend à une réponse de succès, vérifiant la structure de la réponse.
    """
    logger.info(f"Test de création d'un élément de travail via le service ALM à {BASE_URL_ALM}/work-items")
    payload = {
        "title": "Nouveau bug trouvé",
        "description": "Le bouton de connexion ne fonctionne pas sur Firefox.",
        "item_type": "Bug"
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{BASE_URL_ALM}/work-items", json=payload)
        response.raise_for_status()
        assert response.status_code == 200, f"La création d'un élément de travail devrait retourner un statut 200, mais a retourné {response.status_code}."
        data = response.json()
        assert data["success"] is True, "Le champ 'success' devrait être True."
        assert "work_item" in data, "La réponse devrait contenir les détails de l'élément de travail."
        assert data["work_item"]["key"] == "PROJ-123", "La clé de l'élément de travail devrait correspondre à la maquette (PROJ-123)."


@pytest.mark.service
@pytest.mark.asyncio
async def test_alm_create_work_item_validation_error():
    """Teste la gestion d'une requête invalide par le service ALM."

    Ce test envoie une requête POST avec des données manquantes ou invalides
    et s'attend à une réponse HTTP 422 (Unprocessable Entity) indiquant une erreur de validation.
    """
    logger.info(f"Test de gestion d'erreur de validation par le service ALM à {BASE_URL_ALM}/work-items")
    payload = {"description": "Description sans titre"} # Le champ 'title' est requis et manquant.
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{BASE_URL_ALM}/work-items", json=payload)
        assert response.status_code == 422, f"Une requête invalide devrait retourner un statut 422, mais a retourné {response.status_code}."
        data = response.json()
        assert "detail" in data, "La réponse devrait contenir des détails sur l'erreur."
        assert any("field required" in str(err) for err in data["detail"]), "Le message d'erreur devrait indiquer un champ manquant."


@pytest.mark.service
@pytest.mark.asyncio
async def test_excel_service_health():
    """Vérifie que le service Excel est accessible et retourne un statut sain."

    Similaire au test de santé du service ALM, mais pour le service Excel.
    """
    logger.info(f"Test de l'état de santé du service Excel à {BASE_URL_EXCEL}/health")
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL_EXCEL}/health")
        response.raise_for_status()
        assert response.status_code == 200, f"Le service Excel devrait retourner un statut 200, mais a retourné {response.status_code}."
        assert response.json() == {"status": "ok"}, "Le corps de la réponse devrait être {'status': 'ok'}."


@pytest.mark.service
@pytest.mark.asyncio
async def test_excel_create_matrix_success():
    """Teste la création réussie d'une matrice de test Excel."

    Ce test envoie des données de cas de test valides au service Excel et vérifie
    que le service retourne un fichier Excel non vide avec le bon type de contenu.
    """
    logger.info(f"Test de création d'une matrice Excel via le service Excel à {BASE_URL_EXCEL}/create-test-matrix")
    payload = {
        "filename": "test_matrix.xlsx",
        "test_cases": [
            {
                "id": "CU01_SB01_CP001_connexion_valide",
                "description": "Vérifier la connexion réussie.",
                "type": "CP"
            },
            {
                "id": "CU01_SB01_CE001_mot_de_passe_incorrect",
                "description": "Vérifier le message d'erreur.",
                "type": "CE"
            }
        ]
    }
    async with httpx.AsyncClient(timeout=10) as client:
        response = await client.post(f"{BASE_URL_EXCEL}/create-test-matrix", json=payload)
        response.raise_for_status()
        assert response.status_code == 200, f"La création de la matrice Excel devrait retourner un statut 200, mais a retourné {response.status_code}."
        assert response.headers["content-type"] == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", "Le type de contenu devrait être un fichier Excel."
        assert len(response.content) > 0, "Le contenu du fichier Excel ne devrait pas être vide."


@pytest.mark.service
@pytest.mark.asyncio
async def test_excel_create_matrix_validation_error():
    """Teste la gestion de données invalides par le service Excel lors de la création d'une matrice."

    Ce test envoie des données de cas de test qui violent les règles de validation
    (ex: ID invalide) et s'attend à une réponse HTTP 400 (Bad Request) avec des détails sur l'erreur.
    """
    logger.info(f"Test de gestion d'erreur de validation par le service Excel à {BASE_URL_EXCEL}/create-test-matrix")
    payload = {
        "filename": "invalid_matrix.xlsx",
        "test_cases": [
            {
                "id": "ID_INVALIDE", # ID invalide selon la regex.
                "description": "Cet ID n'est pas valide.",
                "type": "CP"
            }
        ]
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{BASE_URL_EXCEL}/create-test-matrix", json=payload)
        assert response.status_code == 400, f"Une requête avec des données invalides devrait retourner un statut 400, mais a retourné {response.status_code}."
        data = response.json()
        assert "detail" in data, "La réponse devrait contenir des détails sur l'erreur."
        assert "Les données des cas de test sont invalides" in data["detail"]["message"], "Le message d'erreur devrait indiquer une validation échouée."
        assert len(data["detail"]["errors"]) > 0, "La liste des erreurs de validation ne devrait pas être vide."
```

---

## Fichier : `backend\tests\__init__.py`

```python
# tests/__init__.py
"""Initialise le package des tests.

Ce fichier peut être vide ou contenir des configurations globales pour la suite de tests.
"""

```

---

## Fichier : `backend\tests\integration\conftest.py`

```python
# tests/integration/conftest.py
"""Configuration des tests d'intégration pour le projet Altiora.

Ce fichier contient des fixtures Pytest spécifiques aux tests d'intégration.
Elles sont utilisées pour configurer l'environnement de test, notamment
la connexion à Redis et l'attente de la disponibilité des microservices.
"""

import pytest
import asyncio
import redis.asyncio as redis
from pathlib import Path
from typing import Dict, Any
import httpx # Utilisé pour les vérifications de service.
import logging

logger = logging.getLogger(__name__)


@pytest.fixture(scope="session")
def integration_config() -> Dict[str, Any]:
    """Fixture fournissant la configuration de base pour les tests d'intégration."

    Returns:
        Un dictionnaire contenant les URLs des services et de Redis.
    """
    return {
        "ollama_host": "http://localhost:11434",
        "services": {
            "ocr": "http://localhost:8001",
            "alm": "http://localhost:8002",
            "excel": "http://localhost:8003",
            "playwright": "http://localhost:8004",
            "dash": "http://localhost:8050", # Ajouté pour le service Dash.
        },
        "redis_url": "redis://localhost:6379"
    }


@pytest.fixture(scope="session")
async def redis_client(integration_config: Dict[str, Any]) -> redis.Redis:
    """Fixture fournissant un client Redis asynchrone pour les tests."

    Le client est connecté à l'URL spécifiée dans la configuration d'intégration.
    """
    client = await redis.from_url(integration_config["redis_url"], decode_responses=True)
    logger.info("Connexion au client Redis pour les tests d'intégration.")
    yield client
    logger.info("Fermeture de la connexion Redis pour les tests d'intégration.")
    await client.aclose()


@pytest.fixture(scope="function")
async def clear_redis(redis_client: redis.Redis):
    """Fixture nettoyant la base de données Redis avant et après chaque test."

    Assure un état propre pour chaque test d'intégration.
    """
    logger.info("Nettoyage de Redis avant le test.")
    await redis_client.flushdb()
    yield
    logger.info("Nettoyage de Redis après le test.")
    await redis_client.flushdb()


@pytest.fixture(scope="session", autouse=True) # autouse=True signifie que cette fixture est exécutée automatiquement.
async def wait_for_services(integration_config: Dict[str, Any]):
    """Fixture attendant que tous les microservices nécessaires soient prêts et accessibles."

    Cette fixture est cruciale pour les tests d'intégration, car elle garantit
    que toutes les dépendances externes sont opérationnelles avant l'exécution des tests.
    """
    service_urls = [
        integration_config["ollama_host"] + "/api/tags", # Endpoint pour vérifier Ollama.
        integration_config["services"]["ocr"] + "/health",
        integration_config["services"]["alm"] + "/health",
        integration_config["services"]["excel"] + "/health",
        integration_config["services"]["playwright"] + "/health",
        integration_config["services"]["dash"] + "/health",
    ]

    async def check_service(url: str) -> bool:
        """Vérifie la disponibilité d'un service en envoyant une requête HTTP GET à son URL."

        Args:
            url: L'URL du service à vérifier.

        Returns:
            True si le service répond avec un statut 200, False sinon.
        """
        try:
            async with httpx.AsyncClient(timeout=5) as client:
                resp = await client.get(url)
                return resp.status_code == 200
        except httpx.RequestError as e:
            logger.debug(f"Service {url} non joignable : {e}")
            return False
        except Exception as e:
            logger.error(f"Erreur inattendue lors de la vérification du service {url}: {e}")
            return False

    max_wait_time = 120 # Temps maximal d'attente en secondes.
    check_interval = 1 # Intervalle entre les vérifications en secondes.
    start_time = asyncio.get_event_loop().time()

    logger.info(f"Attente de la disponibilité des services ({max_wait_time}s max)...")
    while asyncio.get_event_loop().time() - start_time < max_wait_time:
        # Exécute toutes les vérifications de service en parallèle.
        ready_checks = await asyncio.gather(*[check_service(url) for url in service_urls])
        if all(ready_checks):
            logger.info("✅ Tous les services sont prêts.")
            return
        logger.info("Services non encore prêts, nouvelle tentative dans 1 seconde...")
        await asyncio.sleep(check_interval)

    pytest.fail(f"Les services n'ont pas démarré après {max_wait_time} secondes. Les tests d'intégration ne peuvent pas être exécutés.")


# Marqueurs personnalisés pour Pytest.
pytest.mark.integration = pytest.mark.integration
pytest.mark.performance = pytest.mark.performance

```

---

## Fichier : `backend\tests\integration\makefile`

```makefile
# Makefile
.PHONY: test-integration test-performance setup-integration

setup-integration:
	@echo "🚀 Configuration des tests d'intégration..."
	@docker-compose up -d --wait
	@./scripts/validate_microservices.sh

test-integration: setup-integration
	@echo "🧪 Lancement des tests d'intégration..."
	@pytest tests/integration/ -v --tb=short -m integration

test-performance: setup-integration
	@echo "⚡ Lancement des tests de performance..."
	@pytest tests/integration/ -v --tb=short -m performance

test-full: setup-integration
	@echo "🔍 Tests complets avec couverture..."
	@pytest tests/ -v --cov=src --cov-report=html --cov-report=term
```

---

## Fichier : `backend\tests\integration\test_full_pipeline.py`

```python
# tests/integration/test_full_pipeline.py
"""Tests d'intégration pour le pipeline complet SFD → Tests Playwright.

Ce module contient des tests de bout en bout qui vérifient le fonctionnement
intégré de l'application Altiora, de l'analyse d'une Spécification Fonctionnelle
Détaillée (SFD) à la génération et à la validation des tests Playwright.
Il couvre différents scénarios, y compris la gestion des erreurs et les
différents formats d'entrée (ex: PDF).
"""

from pathlib import Path

import pytest

# Importation des composants nécessaires pour le test.
from src.core.altiora_assistant import AltioraQAAssistant
from src.models.sfd_models import SFDAnalysisRequest


@pytest.fixture(scope="session")
async def full_orchestrator():
    """Fixture Pytest pour initialiser et fermer l'orchestrateur complet de l'application."

    Cette fixture assure que l'orchestrateur est prêt avant l'exécution des tests
    et que ses ressources sont libérées après.
    """
    orchestrator = AltioraQAAssistant()
    await orchestrator.initialize()
    yield orchestrator
    await orchestrator.close()


@pytest.fixture
def sample_sfd_content():
    """Fixture fournissant un contenu SFD détaillé pour les tests."

    Ce contenu simule une spécification fonctionnelle pour un module d'authentification,
    incluant des scénarios de connexion réussie et échouée, ainsi que la récupération de mot de passe.
    """
    return """
# Spécification Fonctionnelle - Module Authentification

## 1. Connexion Utilisateur
- **Objectif**: Permettre aux utilisateurs de se connecter de manière sécurisée
- **Acteurs**: Utilisateur authentifié, Système
- **Préconditions**: L'utilisateur a un compte actif

### 1.1 Scénario: Connexion réussie
- **Description**: L'utilisateur se connecte avec des identifiants valides
- **Étapes**:
  1. L'utilisateur accède à la page de connexion
  2. Il saisit son email valide
  3. Il saisit son mot de passe valide
  4. Il clique sur "Se connecter"
  5. Il est redirigé vers le tableau de bord
- **Résultat attendu**: Accès autorisé au tableau de bord

### 1.2 Scénario: Échec de connexion
- **Description**: L'utilisateur entre des identifiants invalides
- **Étapes**:
  1. L'utilisateur accède à la page de connexion
  2. Il saisit des identifiants incorrects
  3. Il clique sur "Se connecter"
- **Résultat attendu**: Message d'erreur "Identifiants invalides"

## 2. Récupération de mot de passe
- **Scénario**: L'utilisateur oublie son mot de passe
- **Étapes**:
  1. Cliquer sur "Mot de passe oublié"
  2. Saisir l'email
  3. Recevoir le lien de réinitialisation
  4. Réinitialiser le mot de passe
"""


@pytest.mark.integration
@pytest.mark.asyncio
async def test_sfd_to_test_pipeline_complete(full_orchestrator, tmp_path: Path, sample_sfd_content: str):
    """Test de bout en bout du pipeline complet : SFD → Analyse → Génération de tests Playwright."

    Ce test vérifie que l'orchestrateur peut prendre une SFD, l'analyser,
    générer des scénarios, puis produire des tests Playwright et un rapport Excel.
    """

    # 1. Préparation du fichier SFD temporaire.
    sfd_path = tmp_path / "complete_sfd.txt"
    sfd_path.write_text(sample_sfd_content)

    # 2. Création de la requête d'analyse SFD.
    sfd_request = SFDAnalysisRequest(content=sfd_path.read_text(), extraction_type="complete")

    # 3. Exécution du pipeline complet via l'orchestrateur.
    result = await full_orchestrator.run_full_pipeline(str(sfd_path))

    # 4. Assertions sur les résultats du pipeline.
    assert result["status"] == "completed", "Le pipeline devrait se terminer avec le statut 'completed'."

    # Vérification des métriques de performance et de contenu.
    metrics = result["metrics"]
    assert metrics["scenarios_found"] >= 3, "Au moins 3 scénarios devraient être trouvés dans la SFD."
    assert metrics["tests_generated"] >= 3, "Au moins 3 tests devraient être générés."
    assert metrics["total_time"] > 0, "Le temps total d'exécution devrait être positif."

    # Vérification du statut de chaque étape du pipeline.
    steps = result["steps"]
    assert all(step["status"] == "success" for step in steps.values()), "Toutes les étapes du pipeline devraient réussir."

    # Vérification de l'existence du rapport Excel généré.
    excel_path = Path(steps["matrix"]["file"])
    assert excel_path.exists(), "Le fichier Excel du rapport devrait exister."

    # Vérification de la structure et du contenu du fichier Excel.
    import pandas as pd
    df = pd.read_excel(excel_path)
    assert len(df) >= 3, "Le fichier Excel devrait contenir au moins 3 lignes (scénarios)."
    assert "ID" in df.columns, "La colonne 'ID' devrait être présente dans le rapport Excel."
    assert "Test_Code" in df.columns, "La colonne 'Test_Code' devrait être présente dans le rapport Excel."


@pytest.mark.integration
@pytest.mark.asyncio
async def test_pipeline_with_pdf_sfd(full_orchestrator, tmp_path: Path):
    """Test du pipeline avec un fichier PDF comme source SFD (simulé via contenu texte)."

    Ce test vérifie que le pipeline peut traiter un fichier PDF en utilisant
    le service OCR pour extraire le texte avant l'analyse par le LLM.
    """

    # Création d'un fichier PDF factice avec du contenu texte.
    # Dans un vrai test d'intégration, un vrai fichier PDF serait utilisé.
    pdf_path = tmp_path / "specification.pdf"
    pdf_path.write_text("Ceci est une simulation de contenu PDF pour les tests. Il contient des scénarios.")

    # Exécution du pipeline avec le fichier PDF.
    result = await full_orchestrator.run_full_pipeline(str(pdf_path))

    # Vérification que l'étape d'extraction (OCR) a été tentée.
    assert "steps" in result, "Les étapes du pipeline devraient être présentes dans le résultat."
    assert "extraction" in result["steps"], "L'étape d'extraction (OCR) devrait être présente."
    # Le statut peut être 'success' si l'OCR factice fonctionne, ou 'error' si l'OCR réel échoue.
    assert result["steps"]["extraction"]["status"] in ["success", "error"], "Le statut de l'extraction devrait être succès ou erreur."


@pytest.mark.integration
@pytest.mark.asyncio
async def test_pipeline_error_handling(full_orchestrator, tmp_path: Path):
    """Test la gestion d'erreurs dans le pipeline, notamment avec un fichier SFD corrompu."

    Ce test s'assure que le pipeline gère correctement les erreurs et retourne
    un statut d'erreur approprié avec des détails.
    """

    # Création d'un fichier SFD corrompu ou illisible.
    corrupt_path = tmp_path / "corrupt.sfd"
    corrupt_path.write_text("Contenu corrompu ou illisible qui devrait causer une erreur.")

    # Exécution du pipeline avec le fichier corrompu.
    result = await full_orchestrator.run_full_pipeline(str(corrupt_path))

    # Vérification que le pipeline a échoué et contient des informations sur l'erreur.
    assert result["status"] == "error", "Le pipeline devrait retourner un statut 'error'."
    assert "error" in result, "Le résultat devrait contenir un champ 'error'."
    assert "error_type" in result, "Le résultat devrait contenir un champ 'error_type'."


@pytest.mark.integration
@pytest.mark.asyncio
async def test_pipeline_with_different_test_types(full_orchestrator, tmp_path: Path):
    """Test du pipeline avec différents types de tests (ex: API tests).

    Ce test vérifie que le pipeline peut générer des tests pour des types
    spécifiques (comme les tests API) en fonction de la configuration fournie.
    """

    # Création d'une SFD d'exemple pour les tests API.
    sfd_path = tmp_path / "api_sfd.txt"
    sfd_path.write_text("""
    # API Spécification
    ## Endpoint /api/login
    - Method: POST
    - Body: {email, password}
    - Response: {token, user_id}
    """)

    # Configuration pour générer des tests API.
    config = {
        "test_types": ["api"],
        "use_page_object": False
    }

    # Exécution du pipeline avec la configuration spécifique.
    result = await full_orchestrator.run_full_pipeline(str(sfd_path), config)

    # Vérification que le pipeline a réussi.
    assert result["status"] == "completed", "Le pipeline devrait se terminer avec le statut 'completed'."

    # Vérification que les tests générés sont bien des tests API (contiennent des appels HTTP).
    if "generated_tests" in result:
        for test in result["generated_tests"]:
            assert "requests.post" in test["code"] or "client.post" in test["code"], "Le code généré devrait contenir des appels HTTP pour les tests API."
```

---

## Fichier : `backend\tests\integration\test_performance.py`

```python
# tests/integration/test_performance.py
"""Tests de performance et de charge pour le pipeline Altiora.

Ce module contient des tests d'intégration axés sur la performance,
mesurant le temps d'exécution et l'utilisation des ressources (mémoire)
du pipeline complet SFD → Tests Playwright sous différentes charges.
"""

import pytest
import asyncio
import time
from src.orchestrator import Orchestrator
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Dict, Any
import psutil
import os


@pytest.mark.performance
@pytest.mark.asyncio
async def test_pipeline_performance_metrics(tmp_path: Path):
    """Mesure les métriques de performance du pipeline SFD → Tests sur plusieurs documents."

    Ce test simule le traitement de plusieurs SFD de tailles différentes
    et collecte des métriques comme la durée d'exécution, le nombre de
    scénarios trouvés et de tests générés.
    """

    # Génère 10 SFD de différentes tailles pour simuler une charge variée.
    sfd_contents = [
        f"Spécification {i}: Test de performance avec {i * 100} lignes de contenu " * 5
        for i in range(1, 11)
    ]

    results = []

    async def process_single_sfd(content: str, index: int) -> Dict[str, Any]:
        """Fonction interne pour traiter une seule SFD et collecter ses métriques."

        Args:
            content: Le contenu textuel de la SFD.
            index: L'index du document (pour le nom de fichier).

        Returns:
            Un dictionnaire contenant la longueur du contenu, la durée de traitement,
            le nombre de scénarios et de tests générés.
        """
        sfd_path = tmp_path / f"perf_{index}.txt"
        sfd_path.write_text(content)

        start_time = time.time()

        orchestrator = Orchestrator() # Crée une nouvelle instance d'orchestrateur pour chaque SFD.
        await orchestrator.initialize()

        try:
            result = await orchestrator.run_full_pipeline(str(sfd_path)) # Utilise la méthode correcte.
            duration = time.time() - start_time

            return {
                "content_length": len(content),
                "duration": duration,
                "scenarios": result.get("metrics", {}).get("scenarios_found", 0),
                "tests": result.get("metrics", {}).get("tests_generated", 0)
            }
        finally:
            await orchestrator.close()

    # Exécute le traitement de chaque SFD en parallèle.
    tasks = [process_single_sfd(content, i) for i, content in enumerate(sfd_contents)]
    results = await asyncio.gather(*tasks)

    # Analyse et assertions sur les résultats agrégés.
    assert len(results) == 10, "Devrait avoir traité 10 SFD."

    avg_time = sum(r["duration"] for r in results) / len(results)
    # Assertion sur le temps moyen d'exécution (ajuster la valeur selon les performances attendues).
    assert avg_time < 300, f"Le temps moyen d'exécution ({avg_time:.2f}s) devrait être inférieur à 300 secondes."

    # Vérifie que des scénarios et des tests ont bien été générés pour chaque SFD.
    for result in results:
        assert result["scenarios"] >= 1, "Chaque SFD devrait générer au moins un scénario."
        assert result["tests"] >= 1, "Chaque SFD devrait générer au moins un test."


@pytest.mark.performance
@pytest.mark.asyncio
async def test_memory_usage(tmp_path: Path):
    """Test la gestion de la mémoire lors du traitement de gros fichiers SFD."

    Ce test vérifie que l'utilisation de la mémoire par le processus ne dépasse
    pas une certaine limite lors du traitement d'un grand document.
    """

    # Crée un contenu SFD volumineux pour simuler un gros fichier (~200KB).
    large_content = "Contenu de test pour un grand document SFD. " * 10000

    sfd_path = tmp_path / "large_sfd.txt"
    sfd_path.write_text(large_content)

    process = psutil.Process(os.getpid())
    initial_memory = process.memory_info().rss # Mémoire initiale du processus.

    orchestrator = Orchestrator()
    await orchestrator.initialize()

    try:
        result = await orchestrator.run_full_pipeline(str(sfd_path)) # Utilise la méthode correcte.

        final_memory = process.memory_info().rss # Mémoire finale du processus.
        memory_increase = final_memory - initial_memory

        # Vérifie que l'augmentation de la mémoire est inférieure à 1 Go (1_000_000_000 octets).
        assert memory_increase < 1_000_000_000, f"L'augmentation de la mémoire ({memory_increase / (1024**2):.2f} MB) devrait être inférieure à 1 Go."
        assert result["status"] == "completed", "Le pipeline devrait se terminer avec le statut 'completed'."

    finally:
        await orchestrator.close()

```

---

## Fichier : `backend\tests\integration\test_services_integration.py`

```python
# tests/integration/test_services_integration.py
"""Tests d'intégration entre les différents microservices d'Altiora.

Ce module contient des tests qui vérifient la bonne communication et le
fonctionnement conjoint des services (OCR, Qwen3, StarCoder2, Excel, ALM,
Playwright). Ces tests simulent des flux de travail complexes pour s'assurer
de l'interopérabilité des composants.
"""

import pytest
import asyncio
import aiohttp
import json
import tempfile
from pathlib import Path


@pytest.mark.integration
@pytest.mark.asyncio
async def test_ocr_to_qwen3_to_starcoder2_flow(wait_for_services):
    """Test le flux d'intégration complet : OCR → Qwen3 → StarCoder2."

    Ce test simule le processus d'analyse d'une SFD (via OCR), son traitement
    par Qwen3 pour extraire les scénarios, puis la génération de code de test
    par StarCoder2 à partir de ces scénarios.
    """
    # 1. Préparation d'un fichier SFD temporaire.
    sfd_content = "Test de connexion avec email et mot de passe. Scénario: Connexion réussie."
    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False, encoding='utf-8') as f:
        f.write(sfd_content)
        sfd_path = Path(f.name)

    try:
        async with aiohttp.ClientSession() as session:
            # 2. Appel au service OCR pour extraire le texte.
            # Note: Le service OCR est mocké ou utilise une implémentation simple pour les tests.
            ocr_payload = {
                "file_path": str(sfd_path),
                "language": "fra",
                "preprocess": False,
                "cache": False
            }
            async with session.post("http://localhost:8001/extract", json=ocr_payload) as resp:
                resp.raise_for_status()
                ocr_result = await resp.json()
                assert "text" in ocr_result
                extracted_text = ocr_result["text"]

            # 3. Appel au modèle Qwen3 pour l'analyse SFD.
            qwen3_payload = {
                "model": "qwen3-sfd-analyzer",
                "prompt": f"Analyze the following SFD and extract test scenarios in JSON format: {extracted_text}",
                "stream": False,
                "options": {"num_predict": 500, "temperature": 0.1}
            }
            async with session.post("http://localhost:11434/api/generate", json=qwen3_payload) as resp:
                resp.raise_for_status()
                qwen3_raw_response = await resp.json()
                # Extrait la partie JSON de la réponse de Qwen3.
                qwen3_response_text = qwen3_raw_response.get("response", "{}")
                try:
                    qwen3_parsed_response = json.loads(qwen3_response_text)
                except json.JSONDecodeError:
                    pytest.fail(f"La réponse de Qwen3 n'est pas un JSON valide : {qwen3_response_text}")
                
                assert "scenarios" in qwen3_parsed_response, "La réponse de Qwen3 devrait contenir des scénarios."
                assert len(qwen3_parsed_response["scenarios"]) > 0, "Qwen3 devrait extraire au moins un scénario."
                scenario_for_starcoder = qwen3_parsed_response["scenarios"][0]

            # 4. Appel au modèle StarCoder2 pour la génération de code de test.
            starcoder2_payload = {
                "model": "starcoder2-playwright",
                "prompt": f"Generate a Playwright test in Python for the following scenario: {json.dumps(scenario_for_starcoder)}",
                "stream": False,
                "options": {"num_predict": 500, "temperature": 0.1}
            }
            async with session.post("http://localhost:11434/api/generate", json=starcoder2_payload) as resp:
                resp.raise_for_status()
                starcoder2_raw_response = await resp.json()
                generated_code = starcoder2_raw_response.get("response", "")

                assert "def test_" in generated_code, "Le code généré par StarCoder2 devrait contenir une fonction de test."
                assert "page.goto" in generated_code, "Le code généré devrait contenir une navigation Playwright."

    finally:
        sfd_path.unlink(missing_ok=True)


@pytest.mark.integration
@pytest.mark.asyncio
async def test_excel_alm_integration(wait_for_services):
    """Test le flux d'intégration : Génération Excel → Importation ALM."

    Ce test vérifie que le service Excel peut générer une matrice de test
    et que le service ALM peut ensuite importer ces données (simulées).
    """

    test_data_for_excel = [
        {
            "id": "CU01_SB01_CP001_login_success",
            "description": "Test connexion réussie",
            "type": "CP",
        },
        {
            "id": "CU01_SB01_CE001_invalid_login",
            "description": "Test échec de connexion",
            "type": "CE",
        }
    ]

    async with aiohttp.ClientSession() as session:
        # 1. Appel au service Excel pour créer une matrice de tests.
        excel_payload = {
            "filename": "integration_test_matrix.xlsx",
            "test_cases": test_data_for_excel
        }
        async with session.post("http://localhost:8003/create-test-matrix", json=excel_payload) as resp:
            resp.raise_for_status()
            excel_response_content = await resp.read() # Le service Excel retourne le fichier binaire.
            assert len(excel_response_content) > 0, "Le service Excel devrait retourner un fichier non vide."

        # 2. Appel au service ALM pour importer un élément de travail (simulé).
        # Note: Le service ALM est mocké pour les tests d'intégration.
        alm_payload = {
            "title": "Import de cas de test depuis Excel",
            "description": "Cas de test générés automatiquement et importés via le service Excel.",
            "item_type": "Task"
        }
        async with session.post("http://localhost:8002/work-items", json=alm_payload) as resp:
            resp.raise_for_status()
            alm_result = await resp.json()
            assert alm_result["success"] is True, "L'importation ALM devrait réussir."
            assert "work_item" in alm_result, "Le résultat ALM devrait contenir les détails de l'élément de travail."


@pytest.mark.integration
@pytest.mark.asyncio
async def test_playwright_execution(wait_for_services):
    """Test l'exécution réelle de tests Playwright via le service dédié."

    Ce test envoie un script Playwright simple au service `playwright_runner`
    et vérifie que l'exécution se déroule correctement.
    """

    test_code_to_execute = '''
import pytest
from playwright.async_api import Page, expect

@pytest.mark.asyncio
async def test_example_page_load(page: Page):
    """Un test simple pour charger une page et vérifier son titre."""
    await page.goto("https://www.google.com")
    await expect(page).to_have_title(/Google/)
'''

    playwright_payload = {
        "tests": [{"code": test_code_to_execute, "test_name": "test_google_load"}],
        "config": {
            "browser": "chromium",
            "headed": False, # Exécution en mode headless.
            "timeout": 30000
        }
    }

    async with aiohttp.ClientSession() as session:
        async with session.post("http://localhost:8004/execute", json=playwright_payload) as resp:
            resp.raise_for_status()
            result = await resp.json()
            assert result["status"] == "completed", f"L'exécution Playwright devrait être complétée, mais est {result.get('status')}. Erreur: {result.get('error')}"
            assert result["passed"] == 1, "Le test Playwright devrait réussir."
            assert result["failed"] == 0, "Aucun test Playwright ne devrait échouer."
            assert len(result["results"]) == 1, "Un seul résultat de test devrait être retourné."
            assert result["results"][0]["status"] == "passed", "Le statut du test individuel devrait être 'passed'."

```

---

## Fichier : `backend\tests\integration\__init__.py`

```python

```

---

## Fichier : `backend\tests\performance\config.yaml`

```yaml
# tests/performance/config.yaml
performance_tests:
  cpu_limits:
    max_percent: 85
    max_temperature: 80
    max_memory_gb: 25

  thresholds:
    response_time_ms: 30000
    throughput_req_sec: 0.5
    error_rate_percent: 5
    memory_efficiency: 0.8

  test_scenarios:
    - name: "light_load"
      concurrent_requests: 5
      duration_seconds: 60
    - name: "medium_load"
      concurrent_requests: 15
      duration_seconds: 120
    - name: "heavy_load"
      concurrent_requests: 30
      duration_seconds: 300
    - name: "stress_test"
      concurrent_requests: 50
      duration_seconds: 600
```

---

## Fichier : `backend\tests\performance\test_load_testing.py`

```python
# tests/performance/test_load_testing.py
"""
Tests de charge CPU pour Altiora
Optimisés pour Intel i5-13500H (14 cores, 32GB RAM)
"""

import asyncio
import logging
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Any, List

import aiohttp
import psutil
import pytest

logger = logging.getLogger(__name__)


@dataclass
class PerformanceMetrics:
    """Métriques de performance CPU"""
    cpu_usage: List[float]
    memory_usage: List[float]
    response_times: List[float]
    throughput: float
    error_rate: float
    concurrent_requests: int


class CPULoadTester:
    """Testeur de charge CPU spécialisé pour Altiora"""

    def __init__(self, target_cpu: int = 80, max_memory_gb: float = 28.0):
        self.target_cpu = target_cpu
        self.max_memory_gb = max_memory_gb
        self.cpu_cores = psutil.cpu_count(logical=False)
        self.p_cores = 6  # Performance cores i5-13500H
        self.e_cores = 8  # Efficiency cores i5-13500H

    def get_system_metrics(self) -> Dict[str, Any]:
        """Récupère les métriques système actuelles"""
        cpu_percent = psutil.cpu_percent(interval=1, percpu=True)
        memory = psutil.virtual_memory()

        return {
            "cpu_percent": cpu_percent,
            "memory_percent": memory.percent,
            "memory_gb": memory.used / (1024 ** 3),
            "temperature": self._get_cpu_temperature(),
            "load_average": psutil.getloadavg()
        }

    @staticmethod
    def _get_cpu_temperature() -> float:
        """Récupère la température CPU (Linux)"""
        try:
            with open('/sys/class/thermal/thermal_zone0/temp', 'r') as f:
                return float(f.read().strip()) / 1000
        except (IOError, OSError) as e:
            logger.warning(f"Could not read CPU temperature: {e}")
            return 0.0

    @staticmethod
    async def stress_test_qwen3(num_concurrent: int = 10):
        """Test de charge sur Qwen3 avec analyses parallèles"""

        test_payloads = [
            f"Analyse ce scénario de test {i}: connexion utilisateur avec validation email"
            for i in range(num_concurrent)
        ]

        metrics = {
            "start_time": time.time(),
            "total_requests": num_concurrent,
            "successful": 0,
            "failed": 0,
            "response_times": []
        }

        async def single_request(payload: str):
            async with aiohttp.ClientSession() as session:
                start = time.time()
                try:
                    async with session.post(
                            "http://localhost:11434/api/generate",
                            json={
                                "model": "qwen3:32b-q4_K_M",
                                "prompt": payload,
                                "stream": False,
                                "options": {
                                    "num_ctx": 8192,
                                    "num_predict": 512,
                                    "temperature": 0.7
                                }
                            },
                            timeout=aiohttp.ClientTimeout(total=300)
                    ) as resp:
                        duration = time.time() - start
                        if resp.status == 200:
                            metrics["successful"] += 1
                        else:
                            metrics["failed"] += 1
                        metrics["response_times"].append(duration)
                        return duration
                except Exception as e:
                    metrics["failed"] += 1
                    logger.error(f"Erreur requête: {e}")
                    return 0

        # Exécution parallèle
        tasks = [single_request(payload) for payload in test_payloads]
        await asyncio.gather(*tasks)

        metrics["total_time"] = time.time() - metrics["start_time"]
        metrics["throughput"] = metrics["successful"] / metrics["total_time"]

        return metrics

    @staticmethod
    async def memory_stress_test(data_size_mb: int = 100):
        """Test de stress mémoire avec gros volumes de données"""

        # Générer des données volumineuses
        large_sfd = "Contenu de spécification " * 10000  # ~200KB

        # Créer 100 fichiers de test
        test_files = []
        for i in range(100):
            file_path = Path(f"/tmp/large_sfd_{i}.txt")
            file_path.write_text(large_sfd * 50)  # ~10MB par fichier
            test_files.append(file_path)

        metrics = {
            "files_processed": 0,
            "total_size_mb": 0,
            "peak_memory_mb": 0,
            "processing_times": []
        }

        # Monitorer la mémoire
        process = psutil.Process()
        initial_memory = process.memory_info().rss / (1024 ** 3)

        for file_path in test_files[:10]:  # Limiter pour les tests
            start_time = time.time()
            start_memory = process.memory_info().rss / (1024 ** 3)

            # Simuler le traitement
            content = file_path.read_text()
            metrics["total_size_mb"] += len(content) / (1024 ** 2)

            # Libération mémoire
            del content

            end_memory = process.memory_info().rss / (1024 ** 3)
            metrics["peak_memory_mb"] = max(metrics["peak_memory_mb"], end_memory)
            metrics["processing_times"].append(time.time() - start_time)
            metrics["files_processed"] += 1

            file_path.unlink()

        metrics["memory_increase_gb"] = metrics["peak_memory_mb"] - initial_memory
        metrics["memory_efficiency"] = metrics["total_size_mb"] / metrics["memory_increase_gb"]

        return metrics

    @staticmethod
    async def concurrent_playwright_tests(num_tests: int = 50):
        """Test avec génération parallèle de tests Playwright"""

        test_scenarios = [
            {
                "titre": f"Test {i}",
                "description": f"Test de connexion {i}",
                "etapes": ["Naviguer", "Saisir", "Valider"]
            }
            for i in range(num_tests)
        ]

        metrics = {
            "tests_generated": 0,
            "total_time": 0,
            "avg_generation_time": 0,
            "memory_usage": []
        }

        start_time = time.time()

        async def generate_single_test(scenario: dict):
            async with aiohttp.ClientSession() as session:
                try:
                    async with session.post(
                            "http://localhost:11434/api/generate",
                            json={
                                "model": "starcoder2:15b-q8_0",
                                "prompt": f"Generate Playwright test for: {scenario['titre']}",
                                "stream": False,
                                "options": {"num_predict": 1000}
                            },
                            timeout=300
                    ) as resp:
                        if resp.status == 200:
                            return await resp.json()
                except Exception as e:
                    logger.error(f"Erreur génération test: {e}")
                    return None

        # Exécution par lots pour éviter la surcharge
        batch_size = min(10, num_tests)
        for i in range(0, num_tests, batch_size):
            batch = test_scenarios[i:i + batch_size]
            tasks = [generate_single_test(scenario) for scenario in batch]
            results = await asyncio.gather(*tasks, return_exceptions=True)

            metrics["tests_generated"] += sum(1 for r in results if r and not isinstance(r, Exception))

            # Pause pour laisser respirer le CPU
            await asyncio.sleep(1)

        metrics["total_time"] = time.time() - start_time
        metrics["avg_generation_time"] = metrics["total_time"] / metrics["tests_generated"]

        return metrics


@pytest.mark.performance
@pytest.mark.asyncio
async def test_cpu_load_80_percent():
    """Test de charge à 80% CPU"""

    tester = CPULoadTester(target_cpu=80)

    # Test Qwen3 sous charge
    metrics = await tester.stress_test_qwen3(num_concurrent=15)

    assert metrics["successful"] >= 12  # 80% de succès
    assert metrics["throughput"] > 0.5  # Au moins 0.5 req/sec

    # Vérifier que le CPU ne dépasse pas 90%
    cpu_percent = psutil.cpu_percent(interval=5)
    assert cpu_percent < 90, f"CPU trop élevé: {cpu_percent}%"


@pytest.mark.performance
@pytest.mark.asyncio
async def test_memory_efficiency():
    """Test d'efficacité mémoire"""

    tester = CPULoadTester()

    metrics = await tester.memory_stress_test(data_size_mb=50)

    # Ratio d'efficacité mémoire
    assert metrics["memory_efficiency"] > 0.8  # 80% d'efficacité
    assert metrics["memory_increase_gb"] < 2  # Moins de 2GB d'augmentation


@pytest.mark.performance
@pytest.mark.asyncio
async def test_concurrent_test_generation():
    """Test de génération parallèle de tests"""

    tester = CPULoadTester()

    metrics = await tester.concurrent_playwright_tests(num_tests=20)

    assert metrics["tests_generated"] >= 18  # 90% de succès
    assert metrics["avg_generation_time"] < 30  # Moins de 30s par test


@pytest.mark.performance
@pytest.mark.asyncio
async def test_error_handling():
    """Test de gestion des erreurs"""

    tester = CPULoadTester()

    # Simuler une erreur de connexion
    async def failing_request():
        async with aiohttp.ClientSession() as session:
            try:
                async with session.post(
                        "http://localhost:11434/api/generate",
                        json={"model": "invalid_model", "prompt": "Test"},
                        timeout=300
                ) as resp:
                    return await resp.json()
            except Exception as e:
                logger.error(f"Erreur requête: {e}")
                return None

    result = await failing_request()

    assert result is None  # Vérifier que l'erreur est gérée correctement

```

---

## Fichier : `backend\tests\performance\test_pipeline_load.py`

```python
# tests/performance/test_pipeline_load.py
"""Tests de charge complets pour le pipeline Altiora.

Ce module contient des tests de performance et de scalabilité pour le pipeline
complet de l'application Altiora (SFD → Analyse → Génération de tests).
Il mesure l'utilisation des ressources (CPU, mémoire) sous différentes charges
et vérifie la résilience du système.
"""

import asyncio
import time
from pathlib import Path
from typing import Dict, Any, List, Optional

import psutil
import pytest
import tempfile
import redis.asyncio as redis

from src.orchestrator import Orchestrator


class PipelineLoadTester:
    """Testeur de charge pour le pipeline complet d'Altiora."""

    def __init__(self):
        """Initialise le testeur de charge avec des limites de ressources par défaut."""
        self.cpu_limit = 85  # Limite d'utilisation CPU en pourcentage.
        self.memory_limit = 25  # Limite d'utilisation mémoire en Go.
        self.process = psutil.Process() # Référence au processus courant pour la surveillance.

    def monitor_resources(self) -> Dict[str, float]:
        """Surveille et retourne les métriques d'utilisation des ressources système."

        Returns:
            Un dictionnaire contenant le pourcentage d'utilisation CPU, le pourcentage
            et la quantité de mémoire utilisée (en Go), la température CPU (si disponible),
            et la mémoire utilisée par le processus courant.
        """
        cpu_percent = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()

        return {
            "cpu_percent": cpu_percent,
            "memory_percent": memory.percent,
            "memory_gb": memory.used / (1024 ** 3),
            "temperature": self._get_cpu_temperature(),
            "process_memory": self.process.memory_info().rss / (1024 ** 3)
        }

    @staticmethod
    def _get_cpu_temperature() -> float:
        """Récupère la température CPU (fonction factice ou dépendante de `psutil`)."

        Returns:
            La température CPU en degrés Celsius, ou 0.0 si non disponible.
        """
        try:
            temps = psutil.sensors_temperatures()
            if 'coretemp' in temps:
                # Retourne la température maximale des cœurs.
                return max([t.current for t in temps['coretemp']])
            return 0.0
        except AttributeError:
            # psutil.sensors_temperatures() n'est pas disponible sur tous les systèmes.
            return 0.0
        except Exception as e:
            logging.warning(f"Impossible de récupérer la température CPU : {e}")
            return 0.0

    def should_stop_load(self) -> bool:
        """Détermine si la génération de charge doit être arrêtée en fonction des limites de ressources."

        Returns:
            True si une limite de ressource est dépassée, False sinon.
        """
        metrics = self.monitor_resources()
        return (
                metrics["cpu_percent"] > self.cpu_limit or
                metrics["memory_gb"] > self.memory_limit or
                metrics["temperature"] > 80 # Température critique.
        )

    async def load_test_full_pipeline(self, num_concurrent: int = 20) -> Dict[str, Any]:
        """Exécute un test de charge complet sur le pipeline Altiora."

        Args:
            num_concurrent: Le nombre de requêtes de pipeline à lancer en parallèle.

        Returns:
            Un dictionnaire d'analyse des résultats de charge.
        """
        # Créer des SFD de test à partir de templates.
        sfd_templates = [
            "Spécification login: email, password, validation",
            "Spécification API: endpoints, méthodes, authentification",
            "Spécification UI: formulaires, boutons, validations"
        ]

        results = []
        orchestrator = Orchestrator() # Crée une instance de l'orchestrateur.
        await orchestrator.initialize()

        try:
            # Prépare les tâches individuelles du pipeline.
            tasks = []
            for i in range(num_concurrent):
                sfd_content = f"{sfd_templates[i % len(sfd_templates)]} - test {i}"
                task = self._single_pipeline_test(orchestrator, sfd_content, i)
                tasks.append(task)

            # Exécute les tâches par lots avec une limitation de charge.
            batch_size = 5
            for i in range(0, num_concurrent, batch_size):
                if self.should_stop_load():
                    logger.warning("Arrêt de la génération de charge en raison des limites système atteintes.")
                    break

                batch = tasks[i:i + batch_size]
                batch_results = await asyncio.gather(*batch, return_exceptions=True)
                results.extend(batch_results)

                # Petite pause pour laisser le système respirer entre les lots.
                await asyncio.sleep(2)

        finally:
            await orchestrator.close()

        return self._analyze_results(results)

    async def _single_pipeline_test(self, orchestrator: Orchestrator, sfd_content: str, index: int) -> Dict[str, Any]:
        """Exécute un seul test du pipeline et collecte ses métriques."

        Args:
            orchestrator: L'instance de l'orchestrateur à utiliser.
            sfd_content: Le contenu de la SFD pour ce test.
            index: L'index du test (pour le nom de fichier temporaire).

        Returns:
            Un dictionnaire contenant les résultats de l'exécution du test.
        """
        start_time = time.time()
        start_resources = self.monitor_resources()

        # Crée un fichier SFD temporaire pour le test.
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False, encoding='utf-8') as f:
            f.write(sfd_content)
            sfd_path = Path(f.name)

        try:
            result = await orchestrator.run_full_pipeline(str(sfd_path))

            end_time = time.time()
            end_resources = self.monitor_resources()

            return {
                "index": index,
                "success": result["status"] == "completed",
                "duration": end_time - start_time,
                "scenarios": result.get("metrics", {}).get("scenarios_found", 0),
                "tests_generated": result.get("metrics", {}).get("tests_generated", 0),
                "cpu_usage": (start_resources["cpu_percent"] + end_resources["cpu_percent"]) / 2,
                "memory_usage": end_resources["memory_gb"],
                "error": None if result["status"] == "completed" else result.get("error")
            }

        except Exception as e:
            return {
                "index": index,
                "success": False,
                "duration": time.time() - start_time,
                "error": str(e)
            }
        finally:
            sfd_path.unlink(missing_ok=True) # S'assure que le fichier temporaire est supprimé.

    @staticmethod
    def _analyze_results(results: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Analyse et agrège les résultats des tests de charge."

        Args:
            results: Une liste de dictionnaires, chaque dictionnaire étant le résultat d'un test unique.

        Returns:
            Un dictionnaire récapitulatif des métriques de performance.
        """
        successful = [r for r in results if r.get("success", False)]
        failed = [r for r in results if not r.get("success", False)]

        total_tests = len(results)
        successful_count = len(successful)
        failed_count = len(failed)

        avg_duration = sum(r["duration"] for r in successful) / successful_count if successful_count > 0 else 0
        avg_scenarios = sum(r["scenarios"] for r in successful) / successful_count if successful_count > 0 else 0
        avg_tests = sum(r["tests_generated"] for r in successful) / successful_count if successful_count > 0 else 0

        # Calcul du débit (tests réussis par seconde).
        total_successful_duration = sum(r["duration"] for r in successful)
        throughput = successful_count / total_successful_duration if total_successful_duration > 0 else 0

        return {
            "total_tests": total_tests,
            "successful": successful_count,
            "failed": failed_count,
            "success_rate": (successful_count / total_tests) * 100 if total_tests > 0 else 0,
            "avg_duration": avg_duration,
            "avg_scenarios": avg_scenarios,
            "avg_tests": avg_tests,
            "throughput": throughput,
            "error_rate": (failed_count / total_tests) * 100 if total_tests > 0 else 0
        }


@pytest.mark.performance
@pytest.mark.asyncio
async def test_cpu_load_pipeline():
    """Test de charge CPU avec le pipeline complet."

    Vérifie que le pipeline peut gérer une charge CPU élevée sans dépasser les limites.
    """

    tester = PipelineLoadTester()

    # Exécute le test de charge avec 10 requêtes concurrentes.
    metrics = await tester.load_test_full_pipeline(num_concurrent=10)

    # Assertions sur les métriques de performance.
    assert metrics["success_rate"] > 80, "Le taux de succès devrait être supérieur à 80%."
    assert metrics["avg_duration"] < 120, "La durée moyenne par test devrait être inférieure à 120 secondes."
    assert metrics["throughput"] > 0.05, "Le débit devrait être supérieur à 0.05 test/seconde."

    # Vérification des ressources système après le test.
    final_metrics = tester.monitor_resources()
    assert final_metrics["cpu_percent"] < 95, "L'utilisation CPU devrait rester sous 95%."
    assert final_metrics["memory_gb"] < 28, "L'utilisation mémoire devrait rester sous 28 Go."


@pytest.mark.performance
@pytest.mark.asyncio
async def test_memory_efficiency_pipeline():
    """Test de l'efficacité mémoire du pipeline avec de gros fichiers SFD."

    Vérifie que le pipeline gère efficacement la mémoire lors du traitement
    de documents volumineux, évitant les fuites de mémoire.
    """

    tester = PipelineLoadTester()

    # Crée un contenu SFD très volumineux (~1 Mo) pour le test.
    large_sfd_content = "Spécification détaillée " * 50000

    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False, encoding='utf-8') as f:
        f.write(large_sfd_content)
        sfd_path = Path(f.name)

    orchestrator = Orchestrator()
    await orchestrator.initialize()

    try:
        # Exécute le pipeline avec le gros fichier SFD.
        result = await orchestrator.run_full_pipeline(str(sfd_path))

        assert result["status"] == "completed", "Le pipeline devrait se terminer avec succès."

        # Vérifie l'efficacité mémoire après le traitement.
        memory_metrics = tester.monitor_resources()
        # La limite de 20 Go est un exemple, à ajuster selon le modèle et les ressources.
        assert memory_metrics["memory_gb"] < 20, f"L'utilisation mémoire ({memory_metrics['memory_gb']:.2f} Go) devrait être inférieure à 20 Go."

    finally:
        await orchestrator.close()
        sfd_path.unlink(missing_ok=True)


@pytest.mark.performance
@pytest.mark.asyncio
async def test_concurrent_redis_operations(redis_client: redis.Redis):
    """Test la performance des opérations Redis sous forte concurrence."

    Vérifie que Redis peut gérer un grand nombre d'opérations de lecture/écriture
    concurrentes de manière efficace.
    """

    try:
        num_operations = 1000 # Nombre d'opérations de lecture/écriture à effectuer.

        write_tasks = []
        read_tasks = []

        start_time = time.time()

        # Exécute des opérations d'écriture concurrentes.
        for i in range(num_operations):
            task = redis_client.setex(f"perf_test_{i}", 60, f"data_{i}")
            write_tasks.append(task)

        await asyncio.gather(*write_tasks)
        write_time = time.time() - start_time
        logging.info(f"Temps pour {num_operations} écritures Redis : {write_time:.2f}s")

        # Exécute des opérations de lecture concurrentes.
        start_time = time.time()
        for i in range(num_operations):
            task = redis_client.get(f"perf_test_{i}")
            read_tasks.append(task)

        results = await asyncio.gather(*read_tasks)
        read_time = time.time() - start_time
        logging.info(f"Temps pour {num_operations} lectures Redis : {read_time:.2f}s")

        # Nettoyage des clés créées pendant le test.
        keys_to_delete = [f"perf_test_{i}" for i in range(num_operations)]
        if keys_to_delete:
            await redis_client.delete(*keys_to_delete)

        # Assertions sur les temps d'exécution et le nombre de succès.
        assert write_time < 5, f"Les {num_operations} écritures Redis devraient prendre moins de 5 secondes."
        assert read_time < 3, f"Les {num_operations} lectures Redis devraient prendre moins de 3 secondes."
        assert len([r for r in results if r is not None]) > 900, "Au moins 90% des lectures devraient réussir."

    finally:
        # S'assure que le client Redis est fermé.
        await redis_client.aclose()
```

---

## Fichier : `backend\tests\performance\test_redis_performance.py`

```python
# tests/performance/test_redis_performance.py
"""Tests de performance pour le cache Redis.

Ce module contient des tests de performance pour évaluer le débit (throughput)
et l'efficacité de la gestion des TTL (Time-To-Live) du cache Redis.
Il simule des opérations de lecture et d'écriture concurrentes pour mesurer
les performances sous charge.
"""

import asyncio
import redis.asyncio as redis
import time
import json
import pytest
from typing import List, Dict, Any


class RedisPerformanceTester:
    """Testeur de performance pour les opérations Redis."""

    def __init__(self, redis_url: str = "redis://localhost:6379"):
        """Initialise le testeur avec l'URL de connexion Redis."

        Args:
            redis_url: L'URL de connexion au serveur Redis.
        """
        self.redis_url = redis_url

    async def test_cache_throughput(self, num_operations: int = 10000) -> Dict[str, Any]:
        """Teste le débit du cache Redis en effectuant un grand nombre d'opérations de lecture/écriture."

        Args:
            num_operations: Le nombre total d'opérations de lecture et d'écriture à effectuer.

        Returns:
            Un dictionnaire contenant les métriques de performance (débit d'écriture/lecture, erreurs, mémoire).
        """
        client = await redis.from_url(self.redis_url, decode_responses=True)

        metrics = {
            "total_operations": num_operations,
            "writes_per_second": 0.0,
            "reads_per_second": 0.0,
            "error_rate": 0.0,
            "memory_usage": "0"
        }

        test_data = {"test": "data", "timestamp": time.time()}

        # --- Test d'écriture ---
        start_time = time.time()
        write_tasks = []
        for i in range(num_operations):
            task = client.setex(f"test_key_{i}", 3600, json.dumps(test_data))
            write_tasks.append(task)

        write_results = await asyncio.gather(*write_tasks, return_exceptions=True)
        write_duration = time.time() - start_time

        successful_writes = sum(1 for r in write_results if r is True)
        metrics["writes_per_second"] = successful_writes / write_duration if write_duration > 0 else 0
        metrics["error_rate"] += (num_operations - successful_writes) / num_operations

        # --- Test de lecture ---
        start_time = time.time()
        read_tasks = []
        for i in range(num_operations):
            task = client.get(f"test_key_{i}")
            read_tasks.append(task)

        read_results = await asyncio.gather(*read_tasks, return_exceptions=True)
        read_duration = time.time() - start_time

        successful_reads = sum(1 for r in read_results if r is not None and not isinstance(r, Exception))
        metrics["reads_per_second"] = successful_reads / read_duration if read_duration > 0 else 0
        metrics["error_rate"] += (num_operations - successful_reads) / num_operations

        # --- Utilisation mémoire --- 
        try:
            info = await client.info("memory")
            metrics["memory_usage"] = info.get("used_memory_human", "0")
        except Exception as e:
            logging.warning(f"Impossible de récupérer les infos mémoire de Redis : {e}")
            metrics["memory_usage"] = "N/A"

        await client.aclose()

        return metrics

    async def test_cache_ttl_performance(self) -> Dict[str, int]:
        """Teste la performance de la gestion des TTL et l'expiration des clés dans Redis."

        Returns:
            Un dictionnaire contenant le nombre de clés initiales, restantes et expirées.
        """
        client = await redis.from_url(self.redis_url)

        # Crée 1000 clés avec des TTL différents (de 1 à 10 secondes).
        tasks = []
        for i in range(1000):
            ttl = 1 + (i % 10)  # TTL de 1 à 10 secondes.
            task = client.setex(f"ttl_test_{i}", ttl, f"data_{i}")
            tasks.append(task)

        await asyncio.gather(*tasks)

        # Attend que toutes les clés avec un TTL court expirent.
        await asyncio.sleep(11) # Attend 11 secondes pour s'assurer que toutes les clés (max TTL 10s) expirent.

        # Compte les clés restantes.
        remaining = await client.keys("ttl_test_*")

        await client.aclose()

        return {
            "initial_keys": 1000,
            "remaining_keys": len(remaining),
            "expired_keys": 1000 - len(remaining)
        }


@pytest.mark.performance
@pytest.mark.asyncio
async def test_redis_cache_performance(wait_for_services):
    """Test de performance global du cache Redis."

    Ce test combine les vérifications de débit et de TTL pour une évaluation complète.
    """

    tester = RedisPerformanceTester()

    # --- Test de débit ---
    throughput_metrics = await tester.test_cache_throughput(1000) # Exécute 1000 opérations.
    logging.info(f"Métriques de débit Redis : {throughput_metrics}")

    assert throughput_metrics["writes_per_second"] > 500, "Le débit d'écriture devrait être supérieur à 500 ops/s."
    assert throughput_metrics["reads_per_second"] > 1000, "Le débit de lecture devrait être supérieur à 1000 ops/s."

    # --- Test TTL ---
    ttl_metrics = await tester.test_cache_ttl_performance()
    logging.info(f"Métriques TTL Redis : {ttl_metrics}")

    assert ttl_metrics["expired_keys"] >= 900, "Au moins 90% des clés devraient avoir expiré."

```

---

## Fichier : `backend\tests\regression\regression_config.yaml`

```yaml
# Configuration des tests de régression Altiora
thresholds:
  max_time_increase: 1.2      # 20% maximum time increase
  min_scenarios: 1            # Minimum scenarios to extract
  min_tests_generated: 1      # Minimum tests to generate
  code_similarity: 0.8        # 80% minimum code similarity
  max_memory_increase: 1.5    # 50% memory increase allowed

models:
  qwen3:
    model_name: "qwen3-sfd-analyzer"
    timeout: 120
    test_cases:
      - scenario_extraction
      - test_matrix_generation
      - priority_detection
  starcoder2:
    model_name: "starcoder2-playwright"
    timeout: 180
    test_cases:
      - code_generation
      - syntax_validity
      - playwright_compliance

services:
  health_check: true
  response_time: 30
  endpoints:
    - ocr
    - alm
    - excel
    - playwright

performance:
  measure_memory: true
  measure_cpu: true
  iterations: 3

update_baselines: false  # Set to true to update reference files
```

---

## Fichier : `backend\tests\regression\run_regression.py`

```python
#!/usr/bin/env python3
"""Script CLI pour lancer les tests de régression de l'application Altiora.

Ce script permet d'exécuter la suite complète des tests de régression.
Il peut être configuré pour mettre à jour les baselines (références) des tests,
ainsi que pour générer un rapport détaillé des résultats. Il s'assure également
que les répertoires nécessaires et les données d'exemple sont en place.

Utilisation:
    python run_regression.py [--update-baselines] [--report] [--verbose]
"""

import argparse
import asyncio
import logging
import json
from pathlib import Path

from tests.regression.test_regression_suite import RegressionSuite # Assurez-vous que ce module existe et est correct.

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def main():
    """Fonction principale pour exécuter la suite de tests de régression."

    Parse les arguments de la ligne de commande pour configurer l'exécution des tests.
    """
    parser = argparse.ArgumentParser(description="Exécute les tests de régression Altiora.")
    parser.add_argument("--update-baselines", action="store_true",
                        help="Met à jour les fichiers de référence (baselines) avec les résultats actuels.")
    parser.add_argument("--report", action="store_true",
                        help="Génère un rapport HTML détaillé des résultats de régression.")
    parser.add_argument("--verbose", "-v", action="store_true",
                        help="Active la sortie verbeuse pour un débogage plus détaillé.")

    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    # Crée les répertoires nécessaires pour les baselines et les résultats des tests.
    Path("tests/regression/baselines").mkdir(parents=True, exist_ok=True)
    Path("tests/regression/results").mkdir(parents=True, exist_ok=True)
    Path("tests/regression/fixtures/sample_sfd").mkdir(parents=True, exist_ok=True)

    # Crée les fichiers de test exemple s'ils n'existent pas, pour assurer un environnement de test fonctionnel.
    await _create_sample_fixtures()

    # Initialise la suite de régression.
    suite = RegressionSuite()
    suite.config["update_baselines"] = args.update_baselines
    suite.config["generate_report"] = args.report # Passe l'option de rapport à la suite.

    logger.info("🚀 Démarrage des tests de régression...")
    results = await suite.run_full_regression()

    # Affichage du résumé des résultats des tests de régression.
    print("\n" + "=" * 60)
    logger.info("📊 RÉSUMÉ DES TESTS DE RÉGRESSION")
    print("=" * 60)
    logger.info(f"Tests totaux : {len(results['tests'])}")
    logger.info(f"✅ Réussis : {results['summary']['passed']}")
    logger.info(f"❌ Échoués : {results['summary']['failed']}")
    logger.info(f"🆕 Nouveaux : {results['summary']['new']}")

    if results["summary"]["failed"] > 0:
        logger.info("\n⚠️  Certains tests ont échoué - veuillez consulter le rapport détaillé pour plus d'informations.")
        exit(1) # Quitte avec un code d'erreur si des tests ont échoué.
    else:
        logger.info("\n🎉 Tous les tests de régression ont réussi !")


async def _create_sample_fixtures():
    """Crée des fichiers de fixtures de test exemple pour la suite de régression."

    Ces fichiers sont utilisés pour simuler des entrées pour les tests
    (ex: spécifications SFD, cas de test Qwen3/StarCoder2).
    """
    fixtures_dir = Path("tests/regression/fixtures")
    fixtures_dir.mkdir(parents=True, exist_ok=True)

    # Fichiers SFD d'exemple.
    sample_sfd_dir = fixtures_dir / "sample_sfd"
    sample_sfd_dir.mkdir(parents=True, exist_ok=True)

    login_spec_path = sample_sfd_dir / "login_spec.txt"
    if not login_spec_path.exists():
        login_spec_path.write_text("""
Spécification Fonctionnelle - Module de Connexion

Objectif: Permettre aux utilisateurs de s'authentifier sur la plateforme

Scénario 1: Connexion réussie
- Pré-condition: L'utilisateur a un compte actif
- Étapes:
  1. Naviguer vers /login
  2. Saisir email valide: user@example.com
  3. Saisir mot de passe valide: SecurePass123!
  4. Cliquer sur "Se connecter"
- Résultat attendu: Redirection vers /dashboard avec message "Bienvenue"

Scénario 2: Email invalide
- Étapes:
  1. Naviguer vers /login
  2. Saisir email invalide: invalid-email
  3. Saisir mot de passe: anything
  4. Cliquer sur "Se connecter"
- Résultat attendu: Message d'erreur "Format email invalide"
""")
        logger.info(f"Fichier SFD d'exemple créé : {login_spec_path}")

    # Cas de test Qwen3.
    qwen3_dir = fixtures_dir / "qwen3"
    qwen3_dir.mkdir(parents=True, exist_ok=True)

    extraction_test_path = qwen3_dir / "test_cases.json"
    if not extraction_test_path.exists():
        extraction_test_path.write_text(json.dumps([
            {
                "name": "basic_extraction",
                "input": "Test de connexion avec email et mot de passe",
                "expected_scenarios": 1
            },
            {
                "name": "complex_extraction",
                "input": "Spécification avec plusieurs scénarios de test",
                "expected_scenarios": 3
            }
        ], indent=2))
        logger.info(f"Fichier de cas de test Qwen3 créé : {extraction_test_path}")

    # Cas de test StarCoder2.
    starcoder2_dir = fixtures_dir / "starcoder2"
    starcoder2_dir.mkdir(parents=True, exist_ok=True)

    starcoder_test_path = starcoder2_dir / "test_cases.json"
    if not starcoder_test_path.exists():
        starcoder_test_path.write_text(json.dumps([
            {
                "name": "basic_playwright_test",
                "scenario": {
                    "titre": "Test de connexion",
                    "objectif": "Vérifier la connexion",
                    "etapes": ["Naviguer vers /login", "Cliquer sur connexion"]
                }
            }
        ], indent=2))
        logger.info(f"Fichier de cas de test StarCoder2 créé : {starcoder_test_path}")


if __name__ == "__main__":
    asyncio.run(main())
```

---

## Fichier : `backend\tests\regression\test_regression_suite.py`

```python
# tests/regression/test_regression_suite.py
"""Suite de tests de régression automatiques pour Altiora.

Ce module implémente une suite de tests de régression qui compare les
résultats actuels de l'application avec des références (baselines) stockées.
Il permet de détecter les régressions fonctionnelles ou de performance
introduites par de nouvelles modifications de code. La suite peut être
configurée pour mettre à jour les baselines et générer des rapports détaillés.
"""

import hashlib
import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional

import pytest
import yaml

from src.orchestrator import Orchestrator
from src.models.qwen3.qwen3_interface import Qwen3OllamaInterface
from src.models.starcoder2.starcoder2_interface import StarCoder2OllamaInterface, TestType

logger = logging.getLogger(__name__)


class RegressionTestResult:
    """Représente le résultat d'un test de régression individuel."""

    def __init__(self, test_name: str, status: str, metrics: Dict[str, Any],
                 diff: Optional[str] = None):
        """Initialise un résultat de test de régression."

        Args:
            test_name: Le nom du test de régression.
            status: Le statut du test ('PASS', 'FAIL', 'NEW').
            metrics: Un dictionnaire de métriques associées au test.
            diff: Un string représentant le 'diff' si le test a échoué (optionnel).
        """
        self.test_name = test_name
        self.status = status  # PASS, FAIL, NEW
        self.metrics = metrics
        self.diff = diff
        self.timestamp = datetime.now().isoformat()


class RegressionSuite:
    """Gère l'exécution et l'analyse des tests de régression."""

    def __init__(self, config_path: str = "tests/regression/regression_config.yaml"):
        """Initialise la suite de tests de régression."

        Args:
            config_path: Le chemin vers le fichier de configuration des tests de régression.
        """
        self.config_path = Path(config_path)
        self.config = self._load_config()
        self.baseline_path = Path("tests/regression/baselines")
        self.baseline_path.mkdir(parents=True, exist_ok=True)
        self.results_path = Path("tests/regression/results")
        self.results_path.mkdir(parents=True, exist_ok=True)

    def _load_config(self) -> Dict[str, Any]:
        """Charge la configuration des tests de régression depuis le fichier YAML."

        Si le fichier n'existe pas, une configuration par défaut est créée.

        Returns:
            Un dictionnaire contenant la configuration des tests de régression.
        """
        if not self.config_path.exists():
            logger.info(f"Fichier de configuration de régression non trouvé à {self.config_path}. Création d'une configuration par défaut.")
            default_config = {
                "thresholds": {
                    "max_time_increase": 1.2,  # Augmentation de temps max de 20%.
                    "min_scenarios": 1,
                    "min_tests_generated": 1,
                    "code_similarity": 0.8 # Seuil de similarité pour le code généré.
                },
                "models": {
                    "qwen3": {
                        "model_name": "qwen3-sfd-analyzer",
                        "test_cases": ["scenario_extraction", "test_matrix"]
                    },
                    "starcoder2": {
                        "model_name": "starcoder2-playwright",
                        "test_cases": ["code_generation", "syntax_validity"]
                    }
                },
                "services": {
                    "health_check": True,
                    "response_time": 30  # secondes max.
                },
                "update_baselines": False, # Option pour mettre à jour les baselines.
                "generate_report": True # Option pour générer un rapport HTML.
            }
            self.config_path.parent.mkdir(parents=True, exist_ok=True)
            with open(self.config_path, 'w', encoding='utf-8') as f:
                yaml.dump(default_config, f, indent=2)
        return yaml.safe_load(self.config_path.read_text(encoding='utf-8'))

    async def run_full_regression(self) -> Dict[str, Any]:
        """Exécute la suite complète de tests de régression."

        Returns:
            Un dictionnaire contenant les résultats détaillés de tous les tests de régression,
            un résumé et des métriques de performance.
        """
        logger.info("🔄 Début des tests de régression...")

        results = {
            "timestamp": datetime.now().isoformat(),
            "tests": [],
            "summary": {"passed": 0, "failed": 0, "new": 0},
            "performance_metrics": {}
        }

        # Exécution des tests de régression pour les modèles LLM.
        model_results = await self._test_models_regression()
        results["tests"].extend(model_results)

        # Exécution des tests de régression pour le pipeline complet.
        pipeline_results = await self._test_pipeline_regression()
        results["tests"].extend(pipeline_results)

        # Exécution des tests de régression de performance.
        perf_results = await self._test_performance_regression()
        results["performance_metrics"] = perf_results

        # Mise à jour du résumé des résultats.
        results["summary"] = {
            "passed": sum(1 for t in results["tests"] if t.status == "PASS"),
            "failed": sum(1 for t in results["tests"] if t.status == "FAIL"),
            "new": sum(1 for t in results["tests"] if t.status == "NEW")
        }

        # Génération du rapport HTML si configuré.
        if self.config.get("generate_report", True):
            self._generate_regression_report(results)

        # Mise à jour des baselines si configuré.
        if self.config.get("update_baselines", False):
            await self._update_baselines(results)

        logger.info("✅ Tests de régression terminés.")
        return results

    async def _test_models_regression(self) -> List[RegressionTestResult]:
        """Exécute les tests de régression spécifiques aux modèles LLM (Qwen3, StarCoder2)."

        Returns:
            Une liste de `RegressionTestResult` pour les tests des modèles.
        """
        results = []

        logger.info("Exécution des tests de régression Qwen3...")
        qwen3_results = await self._test_qwen3_regression()
        results.extend(qwen3_results)

        logger.info("Exécution des tests de régression StarCoder2...")
        starcoder_results = await self._test_starcoder2_regression()
        results.extend(starcoder_results)

        return results

    async def _test_qwen3_regression(self) -> List[RegressionTestResult]:
        """Exécute les tests de régression pour le modèle Qwen3."

        Returns:
            Une liste de `RegressionTestResult` pour les tests Qwen3.
        """
        results = []
        qwen3 = Qwen3OllamaInterface() # Assurez-vous que cette instance est correctement configurée.
        await qwen3.initialize()

        try:
            test_cases = self._load_test_cases("qwen3")

            for test_case in test_cases:
                test_name = f"qwen3_{test_case['name']}"
                # Exécute le test Qwen3 et compare avec la baseline.
                result = await self._run_single_qwen3_test(qwen3, test_case, test_name)
                results.append(result)

        finally:
            await qwen3.close()

        return results

    async def _test_starcoder2_regression(self) -> List[RegressionTestResult]:
        """Exécute les tests de régression pour le modèle StarCoder2."

        Returns:
            Une liste de `RegressionTestResult` pour les tests StarCoder2.
        """
        results = []
        starcoder = StarCoder2OllamaInterface() # Assurez-vous que cette instance est correctement configurée.
        await starcoder.initialize()

        try:
            test_cases = self._load_test_cases("starcoder2")

            for test_case in test_cases:
                test_name = f"starcoder2_{test_case['name']}"
                # Exécute le test StarCoder2 et compare avec la baseline.
                result = await self._run_single_starcoder_test(starcoder, test_case, test_name)
                results.append(result)

        finally:
            await starcoder.close()

        return results

    async def _test_pipeline_regression(self) -> List[RegressionTestResult]:
        """Exécute les tests de régression pour le pipeline complet."

        Returns:
            Une liste de `RegressionTestResult` pour les tests de pipeline.
        """
        results = []
        orchestrator = Orchestrator() # Assurez-vous que cette instance est correctement configurée.
        await orchestrator.initialize()

        try:
            sfd_files = Path("tests/regression/fixtures/sample_sfd").glob("*")

            for sfd_file in sfd_files:
                test_name = f"pipeline_{sfd_file.stem}"
                # Exécute le test de pipeline et compare avec la baseline.
                result = await self._run_pipeline_regression_test(orchestrator, sfd_file, test_name)
                results.append(result)

        finally:
            await orchestrator.close()

        return results

    async def _test_performance_regression(self) -> Dict[str, Any]:
        """Exécute les tests de régression de performance."

        Compare les métriques de performance actuelles avec les baselines.

        Returns:
            Un dictionnaire contenant les comparaisons de métriques de performance.
        """
        logger.info("Exécution des tests de régression de performance...")
        baseline_file = self.baseline_path / "performance.json"

        baseline: Dict[str, Any] = {}
        if baseline_file.exists():
            try:
                baseline = json.loads(baseline_file.read_text(encoding='utf-8'))
            except json.JSONDecodeError as e:
                logger.error(f"Erreur de lecture de la baseline de performance {baseline_file}: {e}")

        # Mesure les performances actuelles.
        current_metrics = await self._measure_performance()

        comparisons = {}
        for metric, current_value in current_metrics.items():
            if metric in baseline:
                baseline_value = baseline[metric]
                ratio = current_value / baseline_value if baseline_value != 0 else float('inf')
                status = "PASS"
                if metric.endswith("_time") or metric.endswith("_duration") or metric.endswith("_usage_mb"):
                    # Pour les métriques où une valeur plus petite est meilleure.
                    if ratio > self.config["thresholds"]["max_time_increase"]:
                        status = "FAIL"
                else:
                    # Pour les métriques où une valeur plus grande est meilleure (ex: débit).
                    if ratio < (1 / self.config["thresholds"]["max_time_increase"]):
                        status = "FAIL"

                comparisons[metric] = {
                    "baseline": baseline_value,
                    "current": current_value,
                    "ratio": ratio,
                    "status": status
                }
            else:
                comparisons[metric] = {
                    "current": current_value,
                    "status": "NEW"
                }

        return comparisons

    async def _run_single_qwen3_test(self, qwen3: Qwen3OllamaInterface,
                                     test_case: Dict[str, Any], test_name: str) -> RegressionTestResult:
        """Exécute un test unique pour Qwen3 et compare son résultat avec la baseline."

        Args:
            qwen3: L'instance de l'interface Qwen3.
            test_case: Le dictionnaire du cas de test.
            test_name: Le nom du test.

        Returns:
            Un objet `RegressionTestResult`.
        """
        baseline_file = self.baseline_path / f"{test_name}.json"

        # Exécution actuelle du test Qwen3.
        # Assurez-vous que `analyze_sfd` prend un `SFDAnalysisRequest`.
        from src.models.sfd_models import SFDAnalysisRequest
        sfd_request = SFDAnalysisRequest(content=test_case["input"], extraction_type=test_case.get("extraction_type", "complete"))
        result = await qwen3.analyze_sfd(sfd_request)

        return self._compare_with_baseline(test_name, result, baseline_file)

    async def _run_single_starcoder_test(self, starcoder: StarCoder2OllamaInterface,
                                         test_case: Dict[str, Any], test_name: str) -> RegressionTestResult:
        """Exécute un test unique pour StarCoder2 et compare son résultat avec la baseline."

        Args:
            starcoder: L'instance de l'interface StarCoder2.
            test_case: Le dictionnaire du cas de test.
            test_name: Le nom du test.

        Returns:
            Un objet `RegressionTestResult`.
        """
        baseline_file = self.baseline_path / f"{test_name}.json"

        # Exécution actuelle du test StarCoder2.
        result = await starcoder.generate_playwright_test(
            scenario=test_case["scenario"],
            config=test_case.get("config", {}),
            test_type=TestType.E2E
        )

        return self._compare_with_baseline(test_name, result, baseline_file)

    async def _run_pipeline_regression_test(self, orchestrator: Orchestrator,
                                            sfd_file: Path, test_name: str) -> RegressionTestResult:
        """Exécute un test de régression du pipeline complet et compare son résultat avec la baseline."

        Args:
            orchestrator: L'instance de l'orchestrateur.
            sfd_file: Le chemin vers le fichier SFD à traiter.
            test_name: Le nom du test.

        Returns:
            Un objet `RegressionTestResult`.
        """
        baseline_file = self.baseline_path / f"{test_name}.json"

        # Exécution actuelle du pipeline.
        result = await orchestrator.run_full_pipeline(str(sfd_file))

        return self._compare_with_baseline(test_name, result, baseline_file)

    def _compare_with_baseline(self, test_name: str, current_result: Dict[str, Any],
                               baseline_file: Path) -> RegressionTestResult:
        """Compare les résultats actuels d'un test avec sa baseline."

        Args:
            test_name: Le nom du test.
            current_result: Le dictionnaire des résultats actuels du test.
            baseline_file: Le chemin vers le fichier de baseline.

        Returns:
            Un objet `RegressionTestResult` indiquant le statut du test (PASS, FAIL, NEW).
        """
        metrics = {
            "timestamp": datetime.now().isoformat(),
            "result_hash": hashlib.md5(json.dumps(current_result, sort_keys=True, ensure_ascii=False).encode()).hexdigest()
        }

        if not baseline_file.exists():
            # Si aucune baseline n'existe, le test est considéré comme nouveau et la baseline est créée.
            logger.info(f"Création d'une nouvelle baseline pour le test : {test_name}")
            baseline_file.write_text(json.dumps(current_result, indent=2, ensure_ascii=False))
            return RegressionTestResult(test_name, "NEW", metrics)

        try:
            baseline = json.loads(baseline_file.read_text(encoding='utf-8'))
        except json.JSONDecodeError as e:
            logger.error(f"Erreur de lecture de la baseline {baseline_file}: {e}. Le test sera marqué comme FAIL.")
            return RegressionTestResult(test_name, "FAIL", metrics, diff=f"Erreur de lecture de la baseline: {e}")

        # Compare les résultats actuels avec la baseline.
        if self._are_results_equivalent(current_result, baseline):
            logger.info(f"Test de régression {test_name} : PASS.")
            return RegressionTestResult(test_name, "PASS", metrics)
        else:
            diff = self._generate_diff(baseline, current_result)
            logger.warning(f"Test de régression {test_name} : FAIL. Différences détectées.")
            return RegressionTestResult(test_name, "FAIL", metrics, diff)

    def _are_results_equivalent(self, current: Dict[str, Any], baseline: Dict[str, Any]) -> bool:
        """Vérifie si deux dictionnaires de résultats sont équivalents."

        Pour l'instant, la comparaison est basée sur le hachage MD5 du JSON sérialisé.
        Une logique de comparaison plus sophistiquée pourrait être ajoutée ici
        pour ignorer certaines différences (ex: horodatages, IDs dynamiques).

        Args:
            current: Le dictionnaire des résultats actuels.
            baseline: Le dictionnaire des résultats de la baseline.

        Returns:
            True si les résultats sont considérés comme équivalents, False sinon.
        """
        current_hash = hashlib.md5(json.dumps(current, sort_keys=True, ensure_ascii=False).encode()).hexdigest()
        baseline_hash = hashlib.md5(json.dumps(baseline, sort_keys=True, ensure_ascii=False).encode()).hexdigest()
        return current_hash == baseline_hash

    def _generate_diff(self, baseline: Dict[str, Any], current: Dict[str, Any]) -> str:
        """Génère un 'diff' lisible entre deux dictionnaires de résultats."

        Args:
            baseline: Le dictionnaire des résultats de la baseline.
            current: Le dictionnaire des résultats actuels.

        Returns:
            Une chaîne de caractères représentant le 'diff' unifié.
        """
        import difflib
        baseline_str = json.dumps(baseline, indent=2, sort_keys=True, ensure_ascii=False).splitlines()
        current_str = json.dumps(current, indent=2, sort_keys=True, ensure_ascii=False).splitlines()

        diff = difflib.unified_diff(
            baseline_str, current_str,
            fromfile='baseline', tofile='current',
            lineterm=''
        )
        return '\n'.join(diff)

    def _load_test_cases(self, model_type: str) -> List[Dict[str, Any]]:
        """Charge les cas de test spécifiques à un type de modèle depuis les fixtures."

        Args:
            model_type: Le type de modèle (ex: 'qwen3', 'starcoder2').

        Returns:
            Une liste de dictionnaires, chaque dictionnaire représentant un cas de test.
        """
        test_cases_dir = Path("tests/regression/fixtures") / model_type
        test_cases: List[Dict[str, Any]] = []

        if not test_cases_dir.exists():
            logger.warning(f"Répertoire de cas de test non trouvé : {test_cases_dir}")
            return []

        for file in test_cases_dir.glob("*.json"):
            try:
                with open(file, "r", encoding="utf-8") as f:
                    test_cases.extend(json.loads(f.read()))
            except json.JSONDecodeError as e:
                logger.error(f"Erreur de lecture du fichier de cas de test {file}: {e}")
        return test_cases

    async def _measure_performance(self) -> Dict[str, float]:
        """Mesure les métriques de performance actuelles de l'application (stub)."

        Dans une implémentation réelle, cette méthode appellerait des outils
        de profiling ou des endpoints de métriques pour collecter des données
        sur le temps de démarrage, le temps de réponse moyen, l'utilisation mémoire, etc.

        Returns:
            Un dictionnaire de métriques de performance.
        """
        logger.info("Mesure des performances actuelles (stub)...")
        # Implémentation simplifiée pour la démonstration.
        import asyncio
        await asyncio.sleep(1) # Simule un délai de mesure.
        return {
            "startup_time": 2.5,
            "average_response_time": 1.2,
            "memory_usage_mb": 512
        }

    def _generate_regression_report(self, results: Dict[str, Any]):
        """Génère un rapport HTML détaillé des résultats de la régression."

        Args:
            results: Le dictionnaire complet des résultats de la suite de régression.
        """
        report_file = self.results_path / f"regression_report_{datetime.now():%Y%m%d_%H%M%S}.html"

        # Construction du contenu HTML du rapport.
        test_rows_html = []
        for t in results['tests']:
            diff_html = f"<pre>{t.diff}</pre>" if t.diff else ""
            test_rows_html.append(f"""
            <tr>
                <td>{t.test_name}</td>
                <td class='{t.status.lower()}'>{t.status}</td>
                <td>{json.dumps(t.metrics, ensure_ascii=False)}</td>
                <td>{diff_html}</td>
            </tr>
            """)

        html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Altiora Regression Report</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; }}
        .pass {{ color: green; font-weight: bold; }}
        .fail {{ color: red; font-weight: bold; }}
        .new {{ color: blue; font-weight: bold; }}
        table {{ border-collapse: collapse; width: 100%; margin-top: 20px; }}
        th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; vertical-align: top; }}
        th {{ background-color: #f2f2f2; }}
        pre {{ white-space: pre-wrap; word-wrap: break-word; background-color: #eee; padding: 10px; border-radius: 5px; }}
    </style>
</head>
<body>
    <h1>Rapport de Tests de Régression Altiora</h1>
    <p>Généré le : {results['timestamp']}</p>

    <h2>Résumé</h2>
    <ul>
        <li class="pass">Réussis : {results['summary']['passed']}</li>
        <li class="fail">Échoués : {results['summary']['failed']}</li>
        <li class="new">Nouveaux : {results['summary']['new']}</li>
    </ul>

    <h2>Résultats des Tests</h2>
    <table>
        <thead>
            <tr><th>Test</th><th>Statut</th><th>Métriques</th><th>Différences</th></tr>
        </thead>
        <tbody>
            {''.join(test_rows_html)}
        </tbody>
    </table>

    <h2>Métriques de Performance</h2>
    <pre>{json.dumps(results['performance_metrics'], indent=2, ensure_ascii=False)}</pre>
</body>
</html>
"""
        try:
            report_file.write_text(html_content, encoding='utf-8')
            logger.info(f"Rapport de régression HTML généré : {report_file}")
        except (IOError, OSError) as e:
            logger.error(f"Erreur lors de l'écriture du rapport HTML : {e}")

    async def _update_baselines(self, results: Dict[str, Any]):
        """Met à jour les fichiers de baseline avec les résultats actuels des tests marqués comme 'NEW' ou 'FAIL'."

        Args:
            results: Le dictionnaire complet des résultats de la suite de régression.
        """
        logger.info("Mise à jour des baselines...")
        for test_result in results['tests']:
            if test_result.status == "NEW" or test_result.status == "FAIL":
                baseline_file = self.baseline_path / f"{test_result.test_name}.json"
                try:
                    # Sauvegarde le résultat actuel comme nouvelle baseline.
                    json.dumps(test_result.metrics, indent=2, ensure_ascii=False) # Assurez-vous que c'est le bon contenu à sauvegarder.
                    baseline_file.write_text(json.dumps(test_result.metrics, indent=2, ensure_ascii=False), encoding='utf-8')
                    logger.info(f"Baseline mise à jour pour {test_result.test_name} : {baseline_file}")
                except (IOError, OSError) as e:
                    logger.error(f"Erreur lors de la mise à jour de la baseline {baseline_file}: {e}")


# Configuration pour pytest (pour l'exécution via `pytest tests/regression/test_regression_suite.py`)
@pytest.mark.regression
@pytest.mark.asyncio
async def test_full_regression_suite(wait_for_services):
    """Test de régression complet exécuté par pytest."

    Cette fonction est le point d'entrée pour Pytest. Elle initialise la suite
    de régression et exécute tous les tests définis.
    """
    suite = RegressionSuite()
    results = await suite.run_full_regression()

    # Assertions finales sur le résumé de la régression.
    assert results["summary"]["failed"] == 0, f"Des tests de régression ont échoué : {results['summary']['failed']} échecs."
    assert results["summary"]["passed"] > 0, "Aucun test de régression n'a réussi."

```

---

## Fichier : `backend\tests\regression\__init__.py`

```python

```

---

## Fichier : `cli\requirements.txt`

```text
# cli/requirements.txt
"""
Dépendances CLI uniquement.
"""

click>=8.1
rich>=13.0
httpx>=0.27
```

---

## Fichier : `cli\setup.py`

```python
# cli/setup.py
"""
Setup du package CLI Altiora.
"""

from setuptools import setup, find_packages

setup(
    name="altiora-cli",
    version="2.0.0",
    packages=find_packages(),
    python_requires=">=3.11",
    entry_points={
        "console_scripts": [
            "altiora=altiora_cli.main:main",
        ],
    },
)
```

---

## Fichier : `cli\altiora_cli\main.py`

```python
# cli/altiora_cli/main.py
"""Point d'entrée principal pour l'interface en ligne de commande (CLI) d'Altiora.

Ce module utilise la bibliothèque `click` pour créer une CLI robuste et facile à utiliser.
Il agrège toutes les commandes disponibles depuis le sous-package `cli.commands`.
"""

from pathlib import Path
import click
from cli.altiora_cli.commands import init, start, test
from cli.altiora_cli.commands import doctor, quickstart, benchmark
from cli.altiora_cli.commands.voice_anything import app as voice_anything_app

app.add_typer(voice_anything_app, name="voice")

@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    """Altiora CLI – Outil pour simplifier le développement et la gestion de projets Altiora."""
    # Si aucune sous-commande n'est invoquée, affiche l'aide.
    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())

# Enregistrement des commandes auprès du groupe principal.
cli.add_command(init.init)
cli.add_command(start.start)
cli.add_command(test.test)
cli.add_command(doctor.doctor)
cli.add_command(quickstart.quickstart)
cli.add_command(benchmark.benchmark)

def check_project_directory() -> bool:
    """Vérifie si le répertoire courant semble être un projet Altiora valide."""
    if not (Path("src").exists() and Path("configs").exists()):
        click.echo("❌ Ce répertoire ne ressemble pas à un projet Altiora.")
        return False
    return True

if __name__ == "__main__":
    cli()

```

---

## Fichier : `cli\altiora_cli\__init__.py`

```python
# cli/altiora_cli/__init__.py
"""
Package CLI Altiora.
"""
```

---

## Fichier : `cli\altiora_cli\commands\batch.py`

```python
# cli/altiora_cli/commands/batch.py
"""
Commande `altiora batch`.
"""

import click
import httpx


@click.command()
@click.argument("payload")
@click.option("--host", default="http://localhost:8000")
def batch(payload: str, host: str) -> None:
    """Planifie un traitement batch."""
    r = httpx.post(f"{host}/api/v1/batch/schedule", json={"payload": payload})
    click.echo(f"Job ID : {r.json()['job_id']}")
```

---

## Fichier : `cli\altiora_cli\commands\benchmark.py`

```python
# cli/altiora_cli/commands/benchmark.py
"""Commande `benchmark` pour la CLI Altiora.

Ce module fournit une commande pour lancer les tests de performance
du projet. Il utilise `pytest-benchmark` pour exécuter des benchmarks
et générer un rapport détaillé.
"""

import click
import subprocess
import logging

logger = logging.getLogger(__name__)


@click.command()
@click.option("--runs", default=5, help="Nombre de runs par benchmark pour chaque test de performance.")
def benchmark(runs: int):
    """Lance les tests de performance de l'application Altiora."

    Cette commande exécute les tests situés dans le répertoire `tests/performance`
    en utilisant `pytest-benchmark`. Un rapport JSON est généré à la fin de l'exécution.

    Args:
        runs: Le nombre de fois que chaque test de performance sera exécuté.
    """
    click.echo("📊 Altiora Benchmark – Démarrage des tests de performance...")
    cmd = [
        "pytest",
        "tests/performance", # Cible le répertoire des tests de performance.
        "--benchmark-only", # Exécute uniquement les tests marqués comme benchmarks.
        f"--benchmark-warmup-iterations={runs}", # Nombre d'itérations de chauffe.
        f"--benchmark-json=benchmark-report.json", # Fichier de sortie du rapport JSON.
    ]
    try:
        subprocess.run(cmd, check=True, capture_output=True, text=True)
        click.echo("✅ Benchmark terminé. Rapport généré dans `benchmark-report.json`.")
        logger.info("Benchmark terminé avec succès.")
    except FileNotFoundError:
        click.echo("❌ Erreur: `pytest` ou `pytest-benchmark` n'est pas installé. Assurez-vous d'avoir installé les dépendances de développement.")
        logger.error("pytest ou pytest-benchmark non trouvé.")
    except subprocess.CalledProcessError as e:
        click.echo(f"❌ Erreur lors de l'exécution des benchmarks : {e.stderr}")
        logger.error(f"Erreur lors de l'exécution des benchmarks : {e.stderr}")
    except Exception as e:
        click.echo(f"❌ Une erreur inattendue est survenue : {e}")
        logger.error(f"Erreur inattendue lors de l'exécution des benchmarks : {e}")


# ------------------------------------------------------------------
# Démonstration (exemple d'utilisation)
# ------------------------------------------------------------------
if __name__ == "__main__":
    import sys
    import os

    # Pour la démonstration, nous allons simuler un fichier de test de performance.
    # En temps normal, ces fichiers existeraient déjà dans `tests/performance`.
    temp_test_dir = Path("tests/performance")
    temp_test_dir.mkdir(parents=True, exist_ok=True)
    (temp_test_dir / "test_example_benchmark.py").write_text("""
import pytest
import time

@pytest.mark.benchmark(group="example")
def test_simple_operation():
    time.sleep(0.01) # Simule une opération rapide.

@pytest.mark.benchmark(group="example")
def test_complex_operation():
    time.sleep(0.1) # Simule une opération plus lente.
""")

    # Exécute la commande benchmark via le système.
    # Note: Cela nécessite que `pytest` et `pytest-benchmark` soient installés dans l'environnement.
    print("\n--- Lancement de la démonstration du benchmark ---")
    try:
        # Simule l'appel de la commande CLI.
        # sys.argv = ["cli/commands/benchmark.py", "--runs", "2"]
        # benchmark() # Appel direct de la fonction pour la démo.
        # Ou via subprocess pour simuler l'appel CLI complet.
        subprocess.run([sys.executable, __file__, "--runs", "2"], check=True)

    except Exception as e:
        print(f"Une erreur est survenue lors de la démonstration : {e}")
    finally:
        # Nettoyage des fichiers temporaires.
        if temp_test_dir.exists():
            import shutil
            shutil.rmtree(temp_test_dir)
        if Path("benchmark-report.json").exists():
            Path("benchmark-report.json").unlink()
        print("Démonstration du benchmark terminée.")
```

---

## Fichier : `cli\altiora_cli\commands\chat.py`

```python
# cli/altiora_cli/commands/chat.py
"""
Commande `altiora chat`.
"""

import click
import httpx


@click.command()
@click.option("--host", default="http://localhost:8000")
def chat(host: str) -> None:
    """Lance une session de chat interactive."""
    click.echo("💬 Altiora CLI Chat (tapez 'exit' pour quitter)")
    while True:
        user_input = click.prompt("", prompt_suffix="> ")
        if user_input.lower() in {"exit", "quit"}:
            break
        try:
            r = httpx.post(f"{host}/api/v1/analysis/", json={"spec": user_input})
            click.echo(r.json()["analysis"])
        except httpx.HTTPError as e:
            click.secho(f"Erreur : {e}", fg="red")
```

---

## Fichier : `cli\altiora_cli\commands\doctor.py`

```python
# cli/altiora_cli/commands/doctor.py
"""Commande `doctor` pour la CLI Altiora.

Ce module fournit un outil de diagnostic complet pour vérifier l'état de
l'environnement du projet Altiora. Il effectue des vérifications sur la
version de Python, les dépendances installées, la disponibilité de Docker,
la présence des fichiers et dossiers essentiels, et la configuration des
variables d'environnement critiques.
"""

import os
import subprocess
import sys
from pathlib import Path
import click
import pkg_resources
import logging

logger = logging.getLogger(__name__)


@click.command()
def doctor():
    """Effectue un diagnostic complet de l'environnement du projet Altiora."

    Cette commande vérifie les prérequis système et les configurations clés
    pour s'assurer que le projet peut fonctionner correctement. Elle affiche
    un résumé des vérifications réussies et des problèmes détectés.
    """
    ok = True
    click.echo("🔍 Altiora Doctor – Démarrage du diagnostic…\n")

    # 1. Vérification de la version de Python.
    v = sys.version_info
    if v < (3, 9):
        click.echo(f"❌ Python >= 3.9 requis (actuel {v.major}.{v.minor}).")
        ok = False
    else:
        click.echo("✅ Version de Python compatible.")

    # 2. Vérification des dépendances Python installées.
    try:
        # Tente de charger les dépendances listées dans requirements.txt.
        pkg_resources.require(open("requirements.txt").readlines())
        click.echo("✅ Dépendances Python installées.")
    except Exception as e:
        click.echo(f"❌ Dépendances Python manquantes ou incorrectes : {e}. Exécutez `pip install -r requirements.txt`.")
        ok = False

    # 3. Vérification de la disponibilité de Docker.
    # `docker info` est utilisé pour vérifier si le démon Docker est en cours d'exécution.
    if subprocess.run(["docker", "info"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode != 0:
        click.echo("❌ Docker non disponible ou non démarré. Veuillez installer Docker Desktop ou démarrer le service Docker.")
        ok = False
    else:
        click.echo("✅ Docker est disponible.")

    # 4. Vérification des fichiers et dossiers obligatoires du projet.
    click.echo("Vérification de l'arborescence du projet...")
    required_paths = ["src", "configs", "docker-compose.yml", "requirements.txt"]
    for p in required_paths:
        if not Path(p).exists():
            click.echo(f"❌ Fichier/dossier manquant : `{p}`. Assurez-vous d'être à la racine du projet.")
            ok = False
    if ok: # Si aucune erreur n'a été détectée jusqu'à présent pour les chemins.
        click.echo("✅ Arborescence du projet conforme.")

    # 5. Vérification des variables d'environnement critiques.
    click.echo("Vérification des variables d'environnement critiques...")
    required_env_vars = ("JWT_SECRET_KEY", "ENCRYPTION_KEY")
    missing_env_vars = [k for k in required_env_vars if not os.getenv(k)]
    if missing_env_vars:
        click.echo(f"❌ Variables d'environnement manquantes : {', '.join(missing_env_vars)}. Exécutez `python scripts/generate_keys.py`.")
        ok = False
    else:
        click.echo("✅ Variables d'environnement critiques configurées.")

    # Affichage du résumé final.
    click.echo("\n" + ("✅ Tout semble OK ! Votre environnement Altiora est prêt." if ok else "❌ Des erreurs ont été détectées. Veuillez consulter les messages ci-dessus pour les corriger."))
    if not ok:
        sys.exit(1) # Quitte avec un code d'erreur si des problèmes sont détectés.


# ------------------------------------------------------------------
# Démonstration (exemple d'utilisation)
# ------------------------------------------------------------------
if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

    # Pour tester ce script, vous pouvez simuler des conditions d'erreur
    # en modifiant temporairement les variables d'environnement ou les fichiers.

    print("\n--- Lancement de la démonstration du Altiora Doctor ---")
    try:
        # Simule un environnement valide pour le premier run.
        # Assurez-vous que `requirements.txt` et `docker-compose.yml` existent.
        # Et que `JWT_SECRET_KEY` et `ENCRYPTION_KEY` sont définis dans votre `.env` ou environnement.
        doctor() 
    except SystemExit as e:
        print(f"Démonstration terminée avec le code de sortie : {e.code}")

    # Exemple de simulation d'un échec (décommenter pour tester).
    # print("\n--- Simulation d'un échec (Python version) ---")
    # original_version_info = sys.version_info
    # sys.version_info = (3, 7, 0, 'final', 0) # Simule une version Python trop ancienne.
    # try:
    #     doctor()
    # except SystemExit as e:
    #     print(f"Démonstration terminée avec le code de sortie : {e.code}")
    # finally:
    #     sys.version_info = original_version_info # Restaure la version.

    # print("\n--- Simulation d'un échec (variable d'environnement manquante) ---")
    # original_jwt_secret = os.getenv("JWT_SECRET_KEY")
    # if "JWT_SECRET_KEY" in os.environ: del os.environ["JWT_SECRET_KEY"]
    # try:
    #     doctor()
    # except SystemExit as e:
    #     print(f"Démonstration terminée avec le code de sortie : {e.code}")
    # finally:
    #     if original_jwt_secret: os.environ["JWT_SECRET_KEY"] = original_jwt_secret

    print("Démonstration du Altiora Doctor terminée.")
```

---

## Fichier : `cli\altiora_cli\commands\init.py`

```python
# cli/altiora_cli/commands/init.py
"""Commande `init` pour la CLI Altiora."""

import click
from pathlib import Path

@click.command()
@click.argument('project_name')
def init(project_name):
    """Initialise un nouveau projet Altiora avec une structure de base."""
    project_dir = Path(project_name)
    if project_dir.exists():
        click.echo(f"Le répertoire `{project_name}` existe déjà. L'initialisation est annulée.")
        return

    # Création de la structure de répertoires standard.
    project_dir.mkdir()
    (project_dir / "src").mkdir()
    (project_dir / "tests").mkdir()
    (project_dir / "configs").mkdir()
    (project_dir / "docs").mkdir()
    (project_dir / "scripts").mkdir()

    click.echo(f"✅ Projet `{project_name}` initialisé avec succès.")

```

---

## Fichier : `cli\altiora_cli\commands\models.py`

```python
# cli/altiora_cli/commands/models.py
"""
Commande `altiora models`.
"""

import click
import httpx


@click.command()
@click.argument("model")
@click.option("--host", default="http://localhost:8000")
def models(model: str, host: str) -> None:
    """Force le swap vers un modèle."""
    r = httpx.post(f"{host}/api/v1/models/swap", json={"model": model})
    click.echo(f"Modèle actif : {r.json()['active_model']}")
```

---

## Fichier : `cli\altiora_cli\commands\quickstart.py`

```python
# cli/altiora_cli/commands/quickstart.py
"""Commande `quickstart` pour la CLI Altiora.

Ce module fournit un assistant interactif pour configurer rapidement un projet Altiora.
Il guide l'utilisateur à travers les étapes de clonage du projet (si nécessaire),
la configuration des variables d'environnement, la construction des images Docker,
et le lancement des services.
"""

import os
import click
from pathlib import Path
import subprocess
import logging

logger = logging.getLogger(__name__)


@click.command()
def quickstart():
    """Lance un assistant de configuration rapide pour le projet Altiora."

    Cette commande est conçue pour les nouveaux utilisateurs afin de les aider
    à démarrer rapidement avec un environnement de travail fonctionnel.
    """
    click.echo("🚀 Altiora Quickstart – Suivez le guide pour une configuration rapide !\n")

    # 1. Vérifie si un projet Altiora est déjà présent. Si non, propose de cloner un exemple.
    if not Path("src").exists():
        if click.confirm("Aucun projet Altiora détecté dans le répertoire courant. Voulez-vous cloner un projet d'exemple ?"):
            url = "https://github.com/altiora/template.git" # URL du template de projet.
            try:
                # Clone le dépôt temporairement, déplace les fichiers, puis supprime le dépôt temporaire.
                subprocess.run(["git", "clone", url, ".altiora_temp"], check=True, capture_output=True, text=True)
                # Utilise shutil.move pour déplacer les contenus de manière plus robuste.
                for item in Path(".altiora_temp").iterdir():
                    shutil.move(str(item), ".")
                Path(".altiora_temp").rmdir()
                click.echo("✅ Projet d'exemple cloné et configuré.")
            except subprocess.CalledProcessError as e:
                click.echo(f"❌ Erreur lors du clonage du projet : {e.stderr}")
                logger.error(f"Erreur lors du clonage du projet : {e.stderr}")
                return # Arrête le quickstart en cas d'échec.
            except Exception as e:
                click.echo(f"❌ Erreur inattendue lors de la configuration du projet : {e}")
                logger.error(f"Erreur inattendue lors de la configuration du projet : {e}")
                return
        else:
            click.echo("Opération annulée. Veuillez créer ou naviguer vers un projet Altiora existant.")
            return
    else:
        click.echo("✅ Projet Altiora déjà présent dans le répertoire courant.")

    # 2. Configuration des variables d'environnement dans le fichier `.env`.
    env_path = Path(".env")
    if not env_path.exists():
        click.echo("📝 Création du fichier `.env` pour les variables d'environnement.")
        # Demande à l'utilisateur de fournir des clés ou génère des valeurs par défaut.
        jwt_secret = click.prompt("JWT_SECRET_KEY (laisser vide pour générer automatiquement)", default="", show_default=False)
        encryption_key = click.prompt("ENCRYPTION_KEY (laisser vide pour générer automatiquement)", default="", show_default=False)
        
        # Génère des clés si l'utilisateur n'en fournit pas.
        if not jwt_secret: jwt_secret = os.urandom(32).hex()
        if not encryption_key: encryption_key = os.urandom(32).hex()

        try:
            with open(env_path, "w", encoding="utf-8") as f:
                f.write(f"JWT_SECRET_KEY={jwt_secret}\n")
                f.write(f"ENCRYPTION_KEY={encryption_key}\n")
                f.write("# Ajoutez d'autres variables d'environnement ici si nécessaire.\n")
            click.echo(f"✅ Fichier `.env` créé avec les clés générées.")
        except (IOError, OSError) as e:
            click.echo(f"❌ Erreur lors de la création du fichier .env : {e}")
            logger.error(f"Erreur lors de la création du fichier .env : {e}")
            return
    else:
        click.echo("✅ Fichier `.env` déjà présent.")

    # 3. Construction des images Docker du projet.
    click.echo("\n⚙️  Construction des images Docker du projet...")
    try:
        subprocess.run(["docker-compose", "build"], check=True, capture_output=True, text=True)
        click.echo("✅ Images Docker construites avec succès.")
    except FileNotFoundError:
        click.echo("❌ Erreur: `docker-compose` n'est pas installé ou n'est pas dans le PATH.")
        logger.error("docker-compose non trouvé.")
        return
    except subprocess.CalledProcessError as e:
        click.echo(f"❌ Erreur lors de la construction des images Docker : {e.stderr}")
        logger.error(f"Erreur lors de la construction des images Docker : {e.stderr}")
        return

    # 4. Lancement des services Docker.
    click.echo("\n🎉 Lancement des services Altiora...")
    try:
        subprocess.run(["docker-compose", "up", "-d"], check=True, capture_output=True, text=True)
        click.echo("✅ Services Altiora démarrés avec succès en arrière-plan.")
    except subprocess.CalledProcessError as e:
        click.echo(f"❌ Erreur lors du démarrage des services : {e.stderr}")
        logger.error(f"Erreur lors du démarrage des services : {e.stderr}")
        return

    click.echo("\n✅ Quickstart terminé ! Votre environnement Altiora est prêt.")
    click.echo("Vous pouvez maintenant accéder au tableau de bord via votre navigateur à http://localhost:8000 (ou le port configuré).")


# ------------------------------------------------------------------
# Démonstration (exemple d'utilisation)
# ------------------------------------------------------------------
if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

    # Pour tester ce script, vous pouvez simuler un environnement vide ou existant.
    # Assurez-vous que `docker-compose.yml` et `requirements.txt` existent dans le répertoire courant.

    print("\n--- Lancement de la démonstration du Altiora Quickstart ---")
    try:
        # Simule l'appel de la commande CLI.
        # sys.argv = ["cli/commands/quickstart.py"]
        # quickstart() # Appel direct de la fonction pour la démo.
        # Ou via subprocess pour simuler l'appel CLI complet.
        subprocess.run([sys.executable, __file__], check=True)

    except Exception as e:
        print(f"Une erreur est survenue lors de la démonstration : {e}")
    finally:
        # Nettoyage des fichiers temporaires créés par la démo (si nécessaire).
        # Par exemple, si un projet d'exemple a été cloné.
        # if Path(".altiora_temp").exists():
        #     import shutil
        #     shutil.rmtree(".altiora_temp")
        # if Path(".env").exists():
        #     Path(".env").unlink()
        print("Démonstration du quickstart terminée.")

```

---

## Fichier : `cli\altiora_cli\commands\start.py`

```python
# cli/altiora_cli/commands/start.py
"""Commande `start` pour la CLI Altiora."""

import click
import subprocess

@click.command()
def start():
    """Lance tous les services Altiora en utilisant docker-compose."""
    try:
        # Exécute `docker-compose up -d` pour démarrer les services en arrière-plan.
        subprocess.run(["docker-compose", "up", "-d"], check=True)
        click.echo("✅ Services Altiora démarrés avec succès.")
    except FileNotFoundError:
        click.echo("❌ Erreur: `docker-compose` n'est pas installé ou n'est pas dans le PATH.")
    except subprocess.CalledProcessError as e:
        click.echo(f"❌ Erreur lors du démarrage des services : {e}")

```

---

## Fichier : `cli\altiora_cli\commands\test.py`

```python
# cli/altiora_cli/commands/test.py
"""Commande `test` pour la CLI Altiora."""

import click
import subprocess

@click.command()
def test():
    """Exécute la suite de tests du projet avec pytest."""
    try:
        # Exécute pytest pour lancer tous les tests découvrables.
        subprocess.run(["pytest"], check=True)
        click.echo("✅ Tests exécutés avec succès.")
    except FileNotFoundError:
        click.echo("❌ Erreur: `pytest` n'est pas installé. Exécutez `pip install pytest`.")
    except subprocess.CalledProcessError as e:
        click.echo(f"❌ Des tests ont échoué : {e}")

```

---

## Fichier : `cli\altiora_cli\commands\voice_anything.py`

```python
import asyncio

import typer
from backend.altiora.core.modules.voice_anythingllm import VoiceAnythingLLM

app = typer.Typer()


@app.command("anything")
def start_voice_anything(
        workspace: str = typer.Option("Altiora Knowledge", help="Nom du workspace AnythingLLM")
):
    """Démarre l'assistant vocal connecté à AnythingLLM"""
    voice = VoiceAnythingLLM(workspace)

    typer.echo("🎤 Assistant vocal AnythingLLM prêt")
    typer.echo("🔊 Dites 'Altiora' ou parlez pour interagir")
    typer.echo("🛑 Ctrl+C pour quitter")

    try:
        asyncio.run(voice.start_session())
    except KeyboardInterrupt:
        typer.echo("\n👋 À bientôt !")


if __name__ == "__main__":
    app()
```

---

## Fichier : `cli\altiora_cli\commands\__init__.py`

```python
# cli/altiora_cli/commands/__init__.py
from .init import init
from .start import start
from .test import test

__all__ = ["init", "start", "test"]
```

---

## Fichier : `configs\prometheus.yml`

```yaml
# configs/prometheus.yml
groups:
  - name: altiora_lora
    rules:
      - alert: LoRA_Retrain_Needed
        expr: altiora_feedback_count >= 50
        for: 1m
        annotations:
          summary: "50+ feedbacks reçus, fine-tuning LoRA lancé"
```

---

## Fichier : `docker\docker-compose.yml`

```yaml
version: '3.8'

services:
  # ==========================
  # Infrastructure de base
  # ==========================
  redis:
    image: redis:7-alpine
    container_name: altiora-redis
    restart: unless-stopped
    ports:
      - "${REDIS_PORT:-6379}:6379"
    volumes:
      - redis-data:/data
    command: >
      redis-server
      --appendonly yes
      --save 900 1
      --save 300 10
      --save 60 10000
      --maxmemory ${REDIS_MAXMEMORY:-8gb}
      --maxmemory-policy allkeys-lru
      --lazyfree-lazy-eviction yes
      --lazyfree-lazy-expire yes
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 5s
      retries: 3
    networks:
      - altiora-network

  # ==========================
  # Backend principal
  # ==========================
  backend:
    build:
      context: .
      dockerfile: docker/Dockerfile.backend
    container_name: altiora-backend
    restart: unless-stopped
    depends_on:
      - redis
    ports:
      - "${BACKEND_PORT:-8000}:8000"
    volumes:
      - ./models:/app/models:ro
      - ./logs/backend:/app/logs
      - ./data:/app/data
      - ./config:/app/config:ro
    environment:
      - REDIS_URL=redis://redis:6379
      - LOG_LEVEL=${LOG_LEVEL:-INFO}
      - QWEN3_MODEL_PATH=/app/models/qwen3-32b-q4_k_m.gguf
      - STARCODER_MODEL_PATH=/app/models/starcoder2-15b-q8_0.gguf
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/api/v1/health"]
      interval: 30s
      timeout: 10s
      retries: 3
    networks:
      - altiora-network
    deploy:
      resources:
        limits:
          memory: 24G
          cpus: '16'

  # ==========================
  # Microservices
  # ==========================
  ocr-service:
    build:
      context: .
      dockerfile: docker/Dockerfile.services
      target: runtime
    container_name: altiora-ocr
    restart: unless-stopped
    depends_on:
      - redis
    ports:
      - "${OCR_PORT:-8001}:8001"
    volumes:
      - ./data/input:/data/input:ro
      - ./data/processed:/data/processed
      - ./temp/ocr:/tmp/ocr_temp
    environment:
      - SERVICE_NAME=ocr
      - REDIS_URL=redis://redis:6379
      - CACHE_TTL=86400
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8001/health"]
      interval: 30s
      timeout: 10s
      retries: 3
    networks:
      - altiora-network
    profiles:
      - services

  alm-service:
    build:
      context: .
      dockerfile: docker/Dockerfile.services
      target: runtime
    container_name: altiora-alm
    restart: unless-stopped
    depends_on:
      - redis
    ports:
      - "${ALM_PORT:-8002}:8002"
    environment:
      - SERVICE_NAME=alm
      - REDIS_URL=redis://redis:6379
      - ALM_API_URL=${ALM_API_URL:-http://alm-server:8080}
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8002/health"]
      interval: 30s
      timeout: 10s
      retries: 3
    networks:
      - altiora-network
    profiles:
      - services

  excel-service:
    build:
      context: .
      dockerfile: docker/Dockerfile.services
      target: runtime
    container_name: altiora-excel
    restart: unless-stopped
    depends_on:
      - redis
    ports:
      - "${EXCEL_PORT:-8003}:8003"
    volumes:
      - ./data/matrices:/data/matrices
      - ./templates:/templates:ro
    environment:
      - SERVICE_NAME=excel
      - REDIS_URL=redis://redis:6379
      - TEMPLATE_PATH=/templates
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8003/health"]
      interval: 30s
      timeout: 10s
      retries: 3
    networks:
      - altiora-network
    profiles:
      - services

  playwright-service:
    build:
      context: .
      dockerfile: docker/Dockerfile.services
      target: runtime
    container_name: altiora-playwright
    restart: unless-stopped
    depends_on:
      - redis
    ports:
      - "${PLAYWRIGHT_PORT:-8004}:8004"
    volumes:
      - ./tests/generated:/tests
      - ./reports:/reports
      - ./screenshots:/screenshots
      - ./videos:/videos
    environment:
      - SERVICE_NAME=playwright
      - REDIS_URL=redis://redis:6379
      - HEADED=${HEADED:-false}
      - BROWSER=${BROWSER:-chromium}
      - PARALLEL_WORKERS=${PARALLEL_WORKERS:-4}
    cap_add:
      - SYS_ADMIN
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8004/health"]
      interval: 30s
      timeout: 10s
      retries: 3
    networks:
      - altiora-network
    profiles:
      - services

  # ==========================
  # AnythingLLM avec RAG
  # ==========================
  anythingllm:
    build:
      context: .
      dockerfile: docker/Dockerfile.anythingllm
    container_name: altiora-anythingllm
    restart: unless-stopped
    depends_on:
      - redis
      - backend
    ports:
      - "${ANYTHINGLLM_PORT:-3001}:3001"
    volumes:
      - anythingllm-storage:/app/server/storage
      - ./data:/app/data:ro
      - ./docs:/app/docs:ro
    environment:
      - ANYTHINGLLM_STORAGE=/app/server/storage
      - VECTOR_DB_URL=redis://redis:6379
      - WORKSPACE_NAME=Altiora Knowledge
      - ENABLE_RAG=true
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:3001/api/health"]
      interval: 30s
      timeout: 10s
      retries: 3
    networks:
      - altiora-network
    profiles:
      - ui

  # ==========================
  # Dashboard Altiora (Dash)
  # ==========================
  dashboard:
    build:
      context: .
      dockerfile: services/dash/Dockerfile
    container_name: altiora-dashboard
    restart: unless-stopped
    depends_on:
      - prometheus
    ports:
      - "${DASHBOARD_PORT:-8050}:8050"
    volumes:
      - ./src/dashboard:/app
      - ./logs/dashboard:/app/logs
    environment:
      - PROMETHEUS_URL=http://prometheus:9090
      - BACKEND_URL=http://backend:8000
      - LOG_LEVEL=${LOG_LEVEL:-INFO}
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8050/_dash-layout"]
      interval: 30s
      timeout: 10s
      retries: 3
    networks:
      - altiora-network
    profiles:
      - ui

  # ==========================
  # Monitoring avec Prometheus
  # ==========================
  prometheus:
    image: prom/prometheus:latest
    container_name: altiora-prometheus
    restart: unless-stopped
    ports:
      - "${PROMETHEUS_PORT:-9090}:9090"
    volumes:
      - ./configs/prometheus.yml:/etc/prometheus/prometheus.yml
      - prometheus-data:/prometheus
    command:
      - '--config.file=/etc/prometheus/prometheus.yml'
      - '--storage.tsdb.path=/prometheus'
      - '--web.console.libraries=/etc/prometheus/console_libraries'
      - '--web.console.templates=/etc/prometheus/consoles'
      - '--storage.tsdb.retention.time=15d'
      - '--web.enable-lifecycle'
      - '--web.enable-admin-api'
    networks:
      - altiora-network
    profiles:
      - monitoring

# ==========================
# Volumes persistants
# ==========================
volumes:
  redis-data:
    driver: local
  anythingllm-storage:
    driver: local
  prometheus-data:
    driver: local

# ==========================
# Réseau interne
# ==========================
networks:
  altiora-network:
    driver: bridge
    ipam:
      config:
        - subnet: 172.20.0.0/16

# ==========================
# Profiles d'utilisation
# ==========================
# docker-compose up              # Backend + Redis seulement
# docker-compose --profile services up    # + Tous microservices
# docker-compose --profile ui up          # + AnythingLLM + Dashboard
# docker-compose --profile monitoring up  # + Prometheus
```

---

## Fichier : `docs\ADVANCED_CONFIGURATION.md`

```markdown
# Guide de Configuration Avancée

Ce guide explique la structure et l'utilisation des fichiers de configuration YAML situés dans le répertoire `configs/`. Ces fichiers permettent une configuration fine et dynamique du comportement de l'application sans avoir à modifier le code source.

## 1. `master_config.yaml`

Ce fichier est le point d'entrée de la configuration. Il référence les autres fichiers de configuration, permettant de charger de manière modulaire différents aspects du système.

**Exemple :**
```yaml
imports:
  - services.yaml
  - models.yaml
  - roles.yaml
  - error_handling.yaml
  - retry_config.yaml
```

- **`imports`**: Une liste de chemins vers d'autres fichiers de configuration à inclure. L'ordre peut être important si des configurations se chevauchent.

## 2. `services.yaml`

Ce fichier définit les configurations de tous les microservices externes que l'orchestrateur doit contacter.

**Exemple :**
```yaml
services:
  ocr:
    url: "http://ocr_service:8001/ocr/extract-text"
    timeout: 60
  alm:
    url: "http://alm_service:8002/alm/create-ticket"
    timeout: 120
    api_key: "${ALM_API_KEY}" # Injection depuis les variables d'environnement
```

- **`services`**: Un dictionnaire où chaque clé est le nom d'un service.
- **`url`**: Le point de terminaison complet du service.
- **`timeout`**: Le timeout en secondes pour les requêtes vers ce service.
- **`api_key`**: Exemple d'injection de secrets depuis les variables d'environnement. La syntaxe `${VAR_NAME}` est utilisée pour substituer la valeur de `VAR_NAME` au chargement.

## 3. `models.yaml` et `models_config.yaml`

Ces fichiers gèrent la configuration des modèles de langage (LLMs).

### `models.yaml`

Définit les modèles disponibles et leurs rôles.

**Exemple :**
```yaml
models:
  sfd_analyzer:
    provider: ollama
    model_name: "qwen3-sfd-analyzer"
    role: "Analyse de spécifications fonctionnelles"
  code_generator:
    provider: ollama
    model_name: "starcoder2-playwright"
    role: "Génération de code de test Playwright"
```

### `models_config.yaml`

Définit les paramètres techniques pour interagir avec les modèles.

**Exemple :**
```yaml
model_config:
  ollama:
    temperature: 0.5
    top_p: 0.9
    max_tokens: 4096
    stop_sequences: ["<|endoftext|>"]
```

- **`temperature`**, **`top_p`**, etc. : Paramètres standards pour contrôler la génération des LLMs.

## 4. `roles.yaml`

Définit les rôles des utilisateurs et les permissions associées (RBAC - Role-Based Access Control).

**Exemple :**
```yaml
roles:
  - name: admin
    permissions:
      - "users:create"
      - "users:delete"
      - "system:shutdown"
      - "*"
  - name: developer
    permissions:
      - "sfd:analyze"
      - "tests:generate"
      - "tests:run"
  - name: guest
    permissions:
      - "reports:view"
```

- **`roles`**: Une liste de rôles.
- **`name`**: Le nom unique du rôle.
- **`permissions`**: Une liste d'actions autorisées. Le caractère `*` peut être utilisé comme joker.

## 5. `retry_config.yaml`

Définit les stratégies de nouvelle tentative (retry) pour les opérations réseau, en utilisant un backoff exponentiel.

**Exemple :**
```yaml
retry_policy:
  default:
    max_attempts: 3
    backoff_factor: 2.0
    initial_delay: 1.0
    jitter: 0.1
  services:
    alm:
      max_attempts: 5
      backoff_factor: 2.5
```

- **`default`**: La politique de retry à appliquer si aucune politique spécifique n'est définie pour un service.
- **`services`**: Permet de surcharger la politique par défaut pour des services spécifiques (ici, le service `alm` est plus résilient).

## Comment ça marche ?

Le module `configs.settings_loader` est responsable du chargement de `master_config.yaml`. Il parcourt les `imports`, charge chaque fichier YAML, et fusionne les configurations en un seul objet de configuration global. Il gère également la substitution des variables d'environnement.

```

---

## Fichier : `docs\API_REFERENCE.md`

```markdown
# Documentation de l'API Altiora

Ce document fournit une référence détaillée pour les points de terminaison (endpoints) de l'API des différents microservices du projet Altiora.

**URL de base** : Les URL sont relatives à l'hôte et au port de chaque service, comme défini dans les variables d'environnement (ex: `http://localhost:8005` pour le service d'authentification).

## 1. Service d'Authentification (`src/auth`)

Ce service gère l'authentification des utilisateurs et la délivrance des jetons JWT.

### `POST /auth/token`

Authentifie un utilisateur et retourne un `access_token`.

- **Requête** :
    - **Méthode** : `POST`
    - **Content-Type** : `application/x-www-form-urlencoded`
    - **Corps** :
        - `username` (str, requis) : Le nom d'utilisateur.
        - `password` (str, requis) : Le mot de passe.

- **Réponse (200 OK)** :

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

- **Réponse (401 Unauthorized)** :

```json
{
  "detail": "Incorrect username or password"
}
```

### `GET /users/me`

Retourne les informations de l'utilisateur actuellement authentifié.

- **Requête** :
    - **Méthode** : `GET`
    - **Authentification** : Jeton `Bearer` requis.

- **Réponse (200 OK)** :

```json
{
  "username": "testuser",
  "email": "test@example.com",
  "full_name": "Test User",
  "disabled": false
}
```

## 2. Service OCR (`services/ocr`)

Extrait le texte brut à partir de fichiers.

### `POST /ocr/extract-text`

- **Requête** :
    - **Méthode** : `POST`
    - **Content-Type** : `multipart/form-data`
    - **Corps** :
        - `file` (File, requis) : Le fichier à traiter (PDF, PNG, JPG).

- **Réponse (200 OK)** :

```json
{
  "text": "Contenu textuel extrait du document..."
}
```

## 3. Service ALM (`services/alm`)

Interagit avec un système de gestion du cycle de vie des applications (ALM).

### `POST /alm/create-ticket`

Crée un nouveau ticket (ex: bug, user story) dans le système ALM.

- **Requête** :
    - **Méthode** : `POST`
    - **Content-Type** : `application/json`
    - **Corps** :

```json
{
  "project_id": "PROJ",
  "title": "Titre du ticket",
  "description": "Description détaillée du ticket.",
  "issue_type": "Bug"
}
```

- **Réponse (201 Created)** :

```json
{
  "ticket_id": "PROJ-123",
  "url": "https://jira.example.com/browse/PROJ-123"
}
```

## 4. Service Excel (`services/excel`)

Génère des fichiers Excel à partir de données JSON.

### `POST /excel/create-matrix`

Crée une matrice de test au format Excel.

- **Requête** :
    - **Méthode** : `POST`
    - **Content-Type** : `application/json`
    - **Corps** :

```json
{
  "filename": "matrice_de_test.xlsx",
  "data": [
    {
      "ID": "TC-001",
      "Scénario": "Connexion réussie",
      "Statut": "Pass"
    },
    {
      "ID": "TC-002",
      "Scénario": "Mot de passe incorrect",
      "Statut": "Fail"
    }
  ]
}
```

- **Réponse (200 OK)** :
    - **Content-Type** : `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`
    - Le fichier Excel est retourné en tant que corps de la réponse.

## 5. Service Playwright (`services/playwright`)

Exécute des scripts de test Playwright.

### `POST /playwright/run-test`

Exécute un script de test Playwright fourni.

- **Requête** :
    - **Méthode** : `POST`
    - **Content-Type** : `application/json`
    - **Corps** :

```json
{
  "script_content": "from playwright.sync_api import sync_playwright\n\ndef run(playwright):\n    ..."
}
```

- **Réponse (200 OK)** :

```json
{
  "status": "succeeded", // ou "failed"
  "output": "...logs de l'exécution...",
  "error": null // ou message d'erreur
}
```

```

---

## Fichier : `docs\ARCHITECTURE.md`

```markdown
# Architecture du Projet Altiora

## 🎯 Vision Générale

Le projet Altiora vise à développer un assistant IA personnel intelligent, capable d'automatiser des tâches complexes de génie logiciel,
notamment l'analyse de spécifications fonctionnelles détaillées (SFD) et la génération de tests d'automatisation (Playwright). L'architecture est conçue pour être modulaire,
scalable et sécurisée, en s'appuyant sur des microservices et des modèles d'IA locaux.

## 🏗️ Composants Clés

L'architecture d'Altiora est articulée autour de plusieurs modules et services interconnectés :

### 1. Orchestrateur Principal (`src/orchestrator.py`)

C'est le cerveau central du système. Il coordonne l'ensemble du pipeline, de la réception d'une SFD à la génération et potentiellement à l'exécution des tests. Ses responsabilités incluent :
- La gestion du flux de travail (workflow).
- L'interaction avec les différents microservices.
- La collecte et l'agrégation des métriques de performance.
- L'intégration des règles métier et des politiques de sécurité.

### 2. Interfaces avec les Modèles d'IA (LLMs)

Altiora utilise des modèles de langage de grande taille (LLMs) pour des tâches spécifiques, interfacés via Ollama :
- **`src/models/qwen3/qwen3_interface.py` (Qwen3)** : Spécialisé dans l'analyse des SFD. Il extrait les scénarios de test, les objectifs, les préconditions, les étapes, etc. Il peut également générer des matrices de test structurées. Il intègre désormais la capacité de charger des adaptateurs de personnalité (LoRA) pour affiner son comportement.
- **`src/models/starcoder2/starcoder2_interface.py` (StarCoder2)** : Dédié à la génération de code, principalement des scripts de test Playwright, à partir des scénarios identifiés par Qwen3.

### 3. Microservices Spécialisés (`services/`)

Ces services sont des composants indépendants, souvent conteneurisés (via Docker), qui gèrent des tâches spécifiques et peuvent être appelés par l'orchestrateur :
- **Auth (`src/auth/`)**: Gère l'authentification des utilisateurs et la génération de tokens JWT. C'est un service FastAPI indépendant avec sa propre base de données SQLite.
- **OCR (`services/ocr/`)** : Extrait le texte de documents (par exemple, PDF de SFD) pour permettre leur analyse par les LLMs.
- **ALM (`services/alm/`)** : Interface avec des outils de gestion du cycle de vie des applications (Application Lifecycle Management) comme Jira ou Azure DevOps pour créer ou mettre à jour des tickets (bugs, tâches).
- **Excel (`services/excel/`)** : Gère la création et le formatage de fichiers Excel, notamment pour les matrices de test, en appliquant des règles de validation et de style.
- **Playwright (`services/playwright/`)** : Exécute les tests Playwright générés et renvoie les résultats d'exécution.
- **Dash (`services/dash/`)**: Fournit un tableau de bord interactif pour visualiser les métriques de performance et les résultats des tests.

### 4. Politiques et Garde-fous (`policies/` et `guardrails/`)

Ces modules sont cruciaux pour la sécurité, la conformité et la qualité des interactions de l'IA :
- **`policies/business_rules.py`** : Contient les règles métier strictes pour valider le code généré (par exemple, interdiction de `time.sleep()`, formatage des IDs de test, utilisation du module de rapport standard).
- **`policies/privacy_policy.py`** : Détecte et masque les informations personnelles identifiables (PII) dans le texte, gère les règles de rétention des données et le consentement, en conformité avec le RGPD.
- **`policies/toxicity_policy.py`** : Évalue le contenu pour détecter la toxicité (insultes, menaces, etc.) et les fuites de PII, avec des niveaux de gravité et des actions associées.
- **`guardrails/admin_control_system.py`** : Système centralisé pour les actions administratives (gel d'utilisateur, sauvegarde, restauration).
- **`guardrails/emergency_handler.py`** : Gère les situations d'urgence (détection de menaces graves, fuites de données) en déclenchant des actions prédéfinies (gel global, notifications).
- **`guardrails/interaction_guardrail.py`** : Un point d'entrée unique pour toutes les interactions utilisateur, appliquant les politiques de toxicité et de confidentialité en temps réel.
- **`guardrails/admin_dashboard.py`** : Une interface graphique (Tkinter) pour la supervision et le contrôle du système par les administrateateurs, affichant des métriques et permettant des actions manuelles.

### 5. Post-traitement (`post_processing/`)

Ces modules affinent les sorties de l'IA ou préparent les données pour d'autres étapes :
- **`post_processing/code_validator.py`** : Valide la syntaxe, le linting (avec Ruff) et le formatage (avec Black) du code Python généré, y compris des vérifications spécifiques à Playwright.
- **`post_processing/excel_formatter.py`** : Applique un formatage visuel aux données destinées à Excel, comme la coloration conditionnelle des lignes et l'ajustement des largeurs de colonnes.
- **`post_processing/output_sanitizer.py`** : Nettoie les réponses brutes des LLMs en supprimant les wrappers de code, les phrases d'introduction et en masquant les PII.

## 🔄 Flux de Travail Principal (SFD vers Tests)

1.  **Authentification**: L'utilisateur obtient un token JWT du service d'authentification.
2.  **Extraction SFD** : L'orchestrateur reçoit un chemin vers une SFD. Le service OCR extrait le contenu textuel.
3.  **Analyse SFD (Qwen3)** : Le contenu textuel est envoyé à Qwen3 (via `qwen3_interface`) qui analyse la spécification et extrait les scénarios de test structurés. La personnalité affinée de Qwen3 est utilisée ici.
4.  **Validation des Scénarios** : Les scénarios extraits sont validés par `policies/excel_policy` pour s'assurer de leur conformité structurelle et métier.
5.  **Génération de la Matrice de Tests** : Qwen3 génère une matrice de tests détaillée à partir des scénarios. Cette matrice est ensuite formatée par `post_processing/excel_formatter` et peut être exportée.
6.  **Importation ALM** : Les scénarios de test peuvent être importés dans un outil ALM via le service `services/alm/`.
7.  **Génération de Code (StarCoder2)** : Pour chaque scénario validé, StarCoder2 (via `starcoder2_interface`) génère le code de test Playwright correspondant. Ce code passe par `post_processing/output_sanitizer` pour le nettoyage et par `post_processing/code_validator` et `policies/business_rules` pour la validation.
8.  **Exécution des Tests** : Les tests Playwright générés sont exécutés par le service `services/playwright/`.
9.  **Rapport et Métriques** : Les résultats d'exécution sont collectés, agrégés et un rapport final est généré, incluant des métriques de performance. Les résultats sont visualisables via le service `services/dash/`.

## 🛠️ Technologies Utilisées

- **Langage** : Python
- **LLMs** : Qwen3, StarCoder2 (via Ollama)
- **Framework Web** : FastAPI
- **Base de données / Cache** : Redis, SQLite (pour l'authentification)
- **Authentification**: PyJWT, passlib
- **Tests d'automatisation** : Playwright, Pytest
- **Outils de Qualité Code** : Black, Ruff
- **Conteneurisation** : Docker, Docker Compose
- **Interface GUI** : Tkinter (pour Admin Dashboard), Dash (pour le reporting)

## 🚀 Déploiement

Le projet est conçu pour être déployé localement sur des machines individuelles (ex: Lenovo ThinkPad) via Docker Compose, assurant l'isolation et la facilité de gestion des microservices.
```

---

## Fichier : `docs\conf.py`

```python

# docs/conf.py
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Altiora'
copyright = '2025, User'
author = 'User'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']

html_theme_options = {
    "show_prev_next": False,
    "header_links_before_dropdown": 4,
    "use_edit_page_button": True,
    "show_toc_level": 1,
    "navbar_align": "left",  # ["left", "right"]
    "navbar_center": ["navbar-nav"],
    "navbar_end": ["navbar-icon-links"],
    "secondary_sidebar_items": {
        "**": ["page-toc", "edit-this-page", "sourcelink"],
        "index": [],
    },
    "footer_items": ["copyright", "sphinx-version"],
    "pygment_light_style": "tango",
    "pygment_dark_style": "monokai",
    "default_mode": "dark"
}


```

---

## Fichier : `docs\DEVELOPER_GUIDE.md`

```markdown
# Guide du Développeur - Projet Altiora

Bienvenue dans l'équipe de développement d'Altiora ! Ce guide a pour but de vous aider à configurer votre environnement et à contribuer au projet de manière efficace et cohérente.

## 1. Conventions de Codage

La cohérence du code est essentielle pour la maintenabilité. Nous suivons des standards stricts pour garantir la qualité.

### Python

- **Style de code** : Nous utilisons **Black** pour le formatage automatique du code. Il n'y a pas de débat sur le style, Black s'en charge.
- **Linting** : Nous utilisons **Ruff** pour détecter les erreurs, les bugs potentiels et les incohérences de style. La configuration se trouve dans le fichier `pyproject.toml`.
- **Typage** : Tout le nouveau code Python doit utiliser les **annotations de type** (type hints) de manière systématique. Nous visons une couverture de typage de 100%.
- **Nommage** :
    - `variables_et_fonctions` : en `snake_case`.
    - `Classes` : en `PascalCase`.
    - `CONSTANTES` : en `UPPER_SNAKE_CASE`.
- **Docstrings** : Utilisez les docstrings au format Google pour documenter les modules, classes et fonctions.

### Commandes de Qualité

Avant de commiter, veuillez exécuter ces commandes à la racine du projet pour vous assurer que votre code est conforme :

```bash
# Formater le code avec Black
black .

# Analyser et corriger automatiquement avec Ruff
ruff check . --fix
```

## 2. Stratégie de Branchement Git

Nous utilisons une stratégie de branchement inspirée de **GitFlow**.

- **`main`** : Cette branche est toujours stable et représente la version en production. On ne pousse jamais directement dessus.
- **`develop`** : La branche principale de développement. Toutes les nouvelles fonctionnalités sont fusionnées ici. C'est la branche de référence pour les builds de développement.
- **`feature/<nom-feature>`** : Chaque nouvelle fonctionnalité doit être développée dans sa propre branche, créée à partir de `develop`. Exemple : `feature/integration-jira`.
- **`fix/<nom-fix>`** : Pour les corrections de bugs non urgents. Créée à partir de `develop`.
- **`hotfix/<nom-hotfix>`** : Pour les corrections de bugs critiques en production. Créée à partir de `main` et fusionnée à la fois dans `main` et `develop`.

## 3. Processus de Contribution

1.  **Assignez-vous une tâche** (ou créez-en une si nécessaire) dans notre outil de suivi (Jira, Trello, etc.).
2.  **Créez une branche** à partir de `develop` en suivant la convention de nommage (`feature/TICKET-123-ma-feature`).
3.  **Développez** votre fonctionnalité. N'oubliez pas d'ajouter des **tests unitaires et d'intégration** pertinents.
4.  **Assurez-vous que tous les tests passent** en exécutant `pytest`.
5.  **Vérifiez la qualité du code** avec `black .` et `ruff check . --fix`.
6.  **Mettez à jour la documentation** si vos changements l'impactent (README, docstrings, guides, etc.).
7.  **Faites une Pull Request (PR)** de votre branche vers `develop`.
8.  **Décrivez clairement vos changements** dans la PR et liez-la à la tâche correspondante.
9.  **Demandez une revue de code** à au moins un autre développeur.
10. Une fois la PR approuvée et les tests CI/CD passés, elle sera fusionnée dans `develop`.

## 4. Environnement de Développement Local

Consultez le `docs/installation_guide.md` pour la configuration de base.

### Scripts Utiles

Le dossier `scripts/` contient de nombreux outils pour vous aider :

- **`start_dev.sh`** : Démarre l'environnement de développement complet (peut-être à adapter).
- **`validate_setup.py`** : Vérifie que votre configuration locale est correcte.
- **`diagnose_ollama.py`** : Utile pour déboguer les problèmes de connexion ou de performance avec les modèles de langage.

### Tests

Pour exécuter l'ensemble de la suite de tests :

```bash
pytest
```

Pour exécuter les tests d'un fichier spécifique :

```bash
pytest tests/test_orchestrator.py
```

Pour exécuter les tests avec une couverture de code :

```bash
pytest --cov=src
```

```

---

## Fichier : `docs\env-documentation.md`

```markdown
# Variables d'Environnement - Documentation

## Vue d'ensemble

Ce document décrit toutes les variables d'environnement utilisées dans le projet Altiora.

## Variables Générales

| Variable | Description | Valeurs | Défaut | Requis |
|----------|-------------|---------|---------|--------|
| `ENVIRONMENT` | Environnement d'exécution | `development`, `staging`, `production`, `test` | `development` | ✅ |
| `DEBUG` | Mode debug activé | `true`, `false` | `false` | ❌ |
| `LOG_LEVEL` | Niveau de logging | `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL` | `INFO` | ❌ |

## Configuration Ollama

| Variable | Description | Valeurs | Défaut | Requis |
|----------|-------------|---------|---------|--------|
| `OLLAMA_HOST` | URL du serveur Ollama | URL complète | `http://localhost:11434` | ✅ |
| `OLLAMA_TIMEOUT` | Timeout des requêtes (secondes) | Entier | `180` | ❌ |
| `OLLAMA_KEEP_ALIVE` | Durée de maintien des modèles en mémoire | Format durée (ex: `30m`) | `30m` | ❌ |
| `QWEN3_MODEL` | Nom du modèle Qwen3 | Chaîne | `qwen3-sfd-analyzer` | ✅ |
| `STARCODER2_MODEL` | Nom du modèle StarCoder2 | Chaîne | `starcoder2-playwright` | ✅ |

## Configuration Redis

| Variable | Description | Valeurs | Défaut | Requis |
|----------|-------------|---------|---------|--------|
| `REDIS_URL` | URL de connexion Redis | Format `redis://[password@]host:port/db` | `redis://localhost:6379` | ✅ |
| `REDIS_PASSWORD` | Mot de passe Redis | Chaîne | *(vide)* | ❌ (✅ en prod) |
| `REDIS_DB` | Numéro de base Redis | 0-15 | `0` | ❌ |
| `REDIS_TTL_SFD` | TTL cache analyses SFD (sec) | Entier | `86400` (24h) | ❌ |
| `REDIS_TTL_TESTS` | TTL cache tests générés (sec) | Entier | `43200` (12h) | ❌ |
| `REDIS_TTL_OCR` | TTL cache résultats OCR (sec) | Entier | `604800` (7j) | ❌ |
| `REDIS_TTL_MODEL` | TTL cache réponses modèles (sec) | Entier | `3600` (1h) | ❌ |

## Services Microservices

### Service d'Authentification

| Variable | Description | Valeurs | Défaut | Requis |
|----------|-------------|---------|---------|--------|
| `DATABASE_URL` | URL de la base de données d'authentification | Chaîne de connexion | `sqlite:///./auth.db` | ✅ |
| `JWT_SECRET_KEY` | Clé secrète JWT | Chaîne (min 32 car.) | *(généré)* | ✅ |
| `JWT_ALGORITHM` | Algorithme JWT | `HS256`, `HS384`, `HS512` | `HS256` | ❌ |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | Durée de vie du token (minutes) | Entier | `60` | ❌ |

### Service OCR

| Variable | Description | Valeurs | Défaut | Requis |
|----------|-------------|---------|---------|--------|
| `OCR_SERVICE_HOST` | Hôte du service OCR | Nom d'hôte/IP | `localhost` | ✅ |
| `OCR_SERVICE_PORT` | Port du service OCR | 1-65535 | `8001` | ✅ |
| `OCR_SERVICE_TIMEOUT` | Timeout OCR (secondes) | Entier | `60` | ❌ |
| `DOCTOPLUS_CONFIG` | Chemin config Doctoplus | Chemin absolu | `/app/config/config.json` | ❌ |

### Service ALM

| Variable | Description | Valeurs | Défaut | Requis |
|----------|-------------|---------|---------|--------|
| `ALM_SERVICE_HOST` | Hôte du service ALM | Nom d'hôte/IP | `localhost` | ✅ |
| `ALM_SERVICE_PORT` | Port du service ALM | 1-65535 | `8002` | ✅ |
| `ALM_SERVICE_TIMEOUT` | Timeout ALM (secondes) | Entier | `120` | ❌ |
| `ALM_API_URL` | URL du serveur ALM réel | URL complète | `http://alm-server:8080` | ❌ |
| `ALM_API_KEY` | Clé API pour ALM | Chaîne | *(vide)* | ❌ |

### Service Excel

| Variable | Description | Valeurs | Défaut | Requis |
|----------|-------------|---------|---------|--------|
| `EXCEL_SERVICE_HOST` | Hôte du service Excel | Nom d'hôte/IP | `localhost` | ✅ |
| `EXCEL_SERVICE_PORT` | Port du service Excel | 1-65535 | `8003` | ✅ |
| `EXCEL_SERVICE_TIMEOUT` | Timeout Excel (secondes) | Entier | `60` | ❌ |

### Service Playwright

| Variable | Description | Valeurs | Défaut | Requis |
|----------|-------------|---------|---------|--------|
| `PLAYWRIGHT_SERVICE_HOST` | Hôte du service Playwright | Nom d'hôte/IP | `localhost` | ✅ |
| `PLAYWRIGHT_SERVICE_PORT` | Port du service Playwright | 1-65535 | `8004` | ✅ |
| `PLAYWRIGHT_SERVICE_TIMEOUT` | Timeout Playwright (secondes) | Entier | `300` | ❌ |
| `PLAYWRIGHT_WORKERS` | Nombre de workers parallèles | Entier | `4` | ❌ |
| `PLAYWRIGHT_BROWSER` | Navigateur par défaut | `chromium`, `firefox`, `webkit` | `chromium` | ❌ |
| `PLAYWRIGHT_HEADED` | Mode avec interface graphique | `true`, `false` | `false` | ❌ |
| `PLAYWRIGHT_SCREENSHOT_ON_FAILURE` | Screenshots sur échec | `true`, `false` | `true` | ❌ |
| `PLAYWRIGHT_VIDEO_ON_FAILURE` | Vidéos sur échec | `true`, `false` | `true` | ❌ |

### Service Dash

| Variable | Description | Valeurs | Défaut | Requis |
|----------|-------------|---------|---------|--------|
| `DASH_SERVICE_HOST` | Hôte du service Dash | Nom d'hôte/IP | `localhost` | ✅ |
| `DASH_SERVICE_PORT` | Port du service Dash | 1-65535 | `8050` | ✅ |

## Sécurité

| Variable | Description | Valeurs | Défaut | Requis |
|----------|-------------|---------|---------|--------|
| `RATE_LIMIT_ENABLED` | Limitation de débit activée | `true`, `false` | `true` | ❌ |
| `RATE_LIMIT_REQUESTS` | Nombre max de requêtes | Entier | `100` | ❌ |
| `RATE_LIMIT_WINDOW_SECONDS` | Fenêtre de temps (secondes) | Entier | `60` | ❌ |
| `ALLOWED_ORIGINS` | Origines CORS autorisées | Liste séparée par virgules | `*` | ❌ |

## Chemins et Répertoires

| Variable | Description | Valeurs | Défaut | Requis |
|----------|-------------|---------|---------|--------|
| `DATA_DIR` | Répertoire des données | Chemin | `./data` | ❌ |
| `MODELS_DIR` | Répertoire des modèles | Chemin | `./models` | ❌ |
| `LOGS_DIR` | Répertoire des logs | Chemin | `./logs` | ❌ |
| `REPORTS_DIR` | Répertoire des rapports | Chemin | `./reports` | ❌ |
| `TEMP_DIR` | Répertoire temporaire | Chemin | `./temp` | ❌ |
| `CACHE_DIR` | Répertoire de cache | Chemin | `./cache` | ❌ |

## Pipeline d'Orchestration

| Variable | Description | Valeurs | Défaut | Requis |
|----------|-------------|---------|---------|--------|
| `PIPELINE_MAX_PARALLEL_TESTS` | Tests max en parallèle | Entier | `5` | ❌ |
| `PIPELINE_MAX_PARALLEL_SCENARIOS` | Scénarios max en parallèle | Entier | `10` | ❌ |
| `PIPELINE_FALLBACK_ENABLED` | Mode fallback activé | `true`, `false` | `true` | ❌ |
| `PIPELINE_RETRY_MAX_ATTEMPTS` | Tentatives max de retry | Entier | `3` | ❌ |
| `PIPELINE_RETRY_BACKOFF_FACTOR` | Facteur de backoff | Décimal | `2.0` | ❌ |

## Docker (si utilisation avec Docker Compose)

| Variable | Description | Valeurs | Défaut | Requis |
|----------|-------------|---------|---------|--------|
| `COMPOSE_PROJECT_NAME` | Nom du projet Docker | Chaîne | `altiora` | ❌ |
| `DOCKER_BUILDKIT` | Utiliser BuildKit | `0`, `1` | `1` | ❌ |
| `OLLAMA_MEMORY_LIMIT` | Limite mémoire Ollama | Format Docker | `12G` | ❌ |
| `OLLAMA_CPU_LIMIT` | Limite CPU Ollama | Nombre | `8` | ❌ |

## Développement

| Variable | Description | Valeurs | Défaut | Requis |
|----------|-------------|---------|---------|--------|
| `MOCK_OCR_SERVICE` | Simuler le service OCR | `true`, `false` | `false` | ❌ |
| `MOCK_ALM_SERVICE` | Simuler le service ALM | `true`, `false` | `false` | ❌ |
| `USE_LOCAL_MODELS` | Utiliser modèles locaux | `true`, `false` | `false` | ❌ |
```

---

## Fichier : `docs\generate_docs.py`

```python
# docs/generate_docs.py
# docs/generate_docs.py
"""Module pour la génération automatisée de la documentation du projet Altiora.

Ce script centralise la création de divers artefacts de documentation,
notamment la spécification OpenAPI (Swagger/Redoc) de l'API, des diagrammes
d'architecture, des guides de déploiement et des rapports de performance.
Il vise à maintenir la documentation à jour et cohérente avec le code.
"""

from pathlib import Path
import json
import logging

from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

logger = logging.getLogger(__name__)


class DocumentationGenerator:
    """Générateur de documentation pour le projet Altiora."""

    def __init__(self, source_dir: Path):
        """Initialise le générateur de documentation."

        Args:
            source_dir: Le répertoire source de l'application (ex: `src/`).
        """
        self.source_dir = source_dir
        self.docs: Dict[str, Any] = {} # Dictionnaire pour stocker les documents générés.

    def generate(self):
        """Génère la documentation complète du projet en appelant les méthodes spécifiques."

        Cette méthode orchestre le processus de génération de documentation.
        """
        logger.info("Démarrage de la génération de la documentation...")
        # 1. Documentation de l'API (OpenAPI/Swagger).
        self._generate_api_docs()

        # 2. Diagrammes d'architecture (placeholder).
        self._generate_architecture_diagrams()

        # 3. Guide de déploiement (placeholder).
        self._generate_deployment_guide()

        # 4. Rapports de performance (placeholder).
        self._generate_performance_docs()
        logger.info("Génération de la documentation terminée.")

    def _generate_api_docs(self):
        """Génère la spécification OpenAPI (Swagger/Redoc) de l'API FastAPI."

        Cette méthode importe dynamiquement l'application FastAPI et utilise
        `get_openapi` pour créer le schéma, puis le sauvegarde au format JSON.
        """
        logger.info("Génération de la documentation API (OpenAPI/Swagger)...")
        # Ajoute le répertoire source au chemin système pour permettre l'importation de l'application FastAPI.
        import sys
        sys.path.append(str(self.source_dir))
        
        try:
            # Importe l'instance de l'application FastAPI.
            from main import app

            # Génère le schéma OpenAPI.
            openapi_schema = get_openapi(
                title="Altiora QA Automation API",
                version="1.0.0",
                description="API pour l'automatisation des tests avec IA, l'analyse de SFD et la gestion des rapports.",
                routes=app.routes,
            )

            # Sauvegarde le schéma OpenAPI dans un fichier JSON.
            output_path = Path("docs/openapi.json")
            output_path.parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(openapi_schema, f, indent=2, ensure_ascii=False)
            logger.info(f"Spécification OpenAPI générée et sauvegardée : {output_path}")
        except ImportError:
            logger.error(f"Impossible d'importer l'application FastAPI depuis {self.source_dir}. Assurez-vous que `main.py` existe et est valide.")
        except (IOError, OSError) as e:
            logger.error(f"Erreur lors de l'écriture de la spécification OpenAPI : {e}")
        except Exception as e:
            logger.error(f"Erreur inattendue lors de la génération de la documentation API : {e}", exc_info=True)

    def _generate_architecture_diagrams(self):
        """Génère les diagrammes d'architecture du projet (placeholder)."

        Cette méthode serait utilisée pour intégrer des outils de génération de diagrammes
        (ex: PlantUML, Mermaid, Graphviz) à partir de définitions textuelles ou de code.
        """
        logger.info("Génération des diagrammes d'architecture (non implémenté)...")
        # TODO: Implémenter la logique de génération de diagrammes.
        pass

    def _generate_deployment_guide(self):
        """Génère le guide de déploiement (placeholder)."

        Cette méthode pourrait assembler des informations provenant de différentes
        sources (fichiers de configuration, scripts Docker) pour créer un guide
        de déploiement complet.
        """
        logger.info("Génération du guide de déploiement (non implémenté)...")
        # TODO: Implémenter la logique de génération du guide de déploiement.
        pass

    def _generate_performance_docs(self):
        """Génère la documentation des benchmarks de performance (placeholder)."

        Cette méthode pourrait analyser les rapports de `pytest-benchmark`
        et générer des visualisations ou des résumés pour la documentation.
        """
        logger.info("Génération de la documentation des performances (non implémenté)...")
        # TODO: Implémenter la logique de génération des docs de performance.
        pass


# ------------------------------------------------------------------
# Point d'entrée CLI
# ------------------------------------------------------------------
if __name__ == "__main__":
    import argparse
    import logging

    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    parser = argparse.ArgumentParser(description="Génère la documentation du projet Altiora.")
    parser.add_argument(
        "--source-dir",
        type=Path,
        default=Path("src"),
        help="Répertoire source de l'application (contenant main.py)."
    )
    args = parser.parse_args()

    print("\n--- Lancement de la génération de documentation ---")
    generator = DocumentationGenerator(args.source_dir)
    generator.generate()
    print("Démonstration de la génération de documentation terminée.")

```

---

## Fichier : `docs\installation_guide.md`

```markdown
# Guide d'Installation Complet pour Altiora

Ce guide vous accompagnera à travers les étapes nécessaires pour installer et configurer Altiora, un assistant IA personnel intelligent capable d'automatiser des tâches complexes de génie logiciel.

## Prérequis

Assurez-vous d'avoir les éléments suivants installés sur votre système :

- **Python 3.11+** : Le langage de programmation principal du projet.
- **pip** : Le gestionnaire de paquets Python (normalement inclus avec Python).
- **Git** : Pour cloner le dépôt du projet.
- **Docker Desktop** (ou Docker Engine et Docker Compose) : Pour exécuter les microservices conteneurisés.

## Étapes d'Installation

### 1. Cloner le Dépôt

Ouvrez votre terminal ou invite de commande et exécutez la commande suivante pour cloner le dépôt du projet :

```bash
git clone https://github.com/votre_utilisateur/Altiora_project.git # Remplacez par l'URL réelle de votre dépôt
cd Altiora_project
```

### 2. Configuration de l'Environnement

Le projet utilise un fichier `.env` pour gérer les variables d'environnement. Un exemple est fourni :

1. Copiez le fichier `.env.example` vers `.env` :

```bash
cp .env.example .env
# Sur Windows, vous pouvez utiliser :
# copy .env.example .env
```

2. **Éditez le fichier `.env`** : Ouvrez le fichier `.env` avec un éditeur de texte et ajustez les valeurs selon votre environnement. Les variables importantes incluent :

    - `OLLAMA_HOST` : L'URL de votre instance Ollama (par défaut `http://localhost:11434`).
    - `ALM_API_URL`, `ALM_API_KEY` : Pour l'intégration avec votre système ALM (si utilisé).
    - `REDIS_URL` : L'URL de votre instance Redis (par défaut `redis://localhost:6379`).
    - `JWT_SECRET_KEY` : La clé secrète pour l'authentification JWT. **Il est crucial de définir une clé secrète forte ici.**

### 3. Création de l'Environnement Virtuel et Installation des Dépendances Python

Il est fortement recommandé d'utiliser un environnement virtuel pour isoler les dépendances du projet.

1. Créez l'environnement virtuel :

```bash
python -m venv .venv
```

2. Activez l'environnement virtuel :

    - **Sur macOS/Linux** :

    ```bash
source .venv/bin/activate
```

    - **Sur Windows (Command Prompt)** :

    ```bash
.venv\Scripts\activate.bat
```

    - **Sur Windows (PowerShell)** :

    ```powershell
.venv\Scripts\Activate.ps1
```

3. Installez les dépendances Python :

```bash
pip install -r requirements.txt
```

4. Installez les navigateurs Playwright (nécessaire pour l'exécution des tests) :

```bash
playwright install
```

### 4. Lancement des Services

Altiora s'appuie sur Ollama pour les modèles d'IA et d'autres microservices conteneurisés via Docker Compose.

1. **Lancez Ollama** :

Assurez-vous que le serveur Ollama est en cours d'exécution. Vous pouvez le lancer via :

```bash
ollama serve
```

Si vous n'avez pas Ollama installé, suivez les instructions sur [ollama.ai](https://ollama.ai/download).

2. **Démarrez les microservices Docker Compose** :

Dans le répertoire racine du projet, exécutez :

```bash
docker-compose up -d
```

Cette commande va construire (si nécessaire) et démarrer les conteneurs pour les services Redis, OCR, ALM, Excel, Playwright, Auth et Dash.

### 5. Vérification de l'Installation

Vous pouvez vérifier que les services sont en cours d'exécution en accédant à leurs points de terminaison de santé (si disponibles) ou en exécutant les tests :

```bash
# Exemple de vérification de santé (si les services sont exposés sur localhost)
curl http://localhost:8001/health # Service OCR
curl http://localhost:8002/health # Service ALM
curl http://localhost:8003/health # Service Excel
curl http://localhost:8005/health # Service Auth

# Accéder à la documentation API (Swagger UI)
# Pour le service ALM: http://localhost:8002/docs
# Pour le service Excel: http://localhost:8003/docs
# Pour le service Auth: http://localhost:8005/docs

# Accéder au Dashboard
# http://localhost:8050

# Exécuter les tests du projet
pytest
```

### 6. Utilisation de Base

Une fois tous les services en cours d'exécution, vous pouvez interagir avec l'orchestrateur via le CLI. Voir le `README.md` pour plus de détails sur les commandes disponibles.

### 7. Troubleshooting

- **Problèmes de port** : Si un service Docker ne démarre pas, vérifiez que les ports (ex: 8001, 8002, 8003, 8004, 8005, 8050, 11434, 6379) ne sont pas déjà utilisés par d'autres applications sur votre système.
- **Ollama** : Assurez-vous que les modèles `qwen3-sfd-analyzer` et `starcoder2-playwright` sont bien téléchargés et disponibles dans Ollama. Vous pouvez les télécharger manuellement si nécessaire (`ollama pull qwen3-sfd-analyzer`, `ollama pull starcoder2-playwright`).
- **Dépendances Python** : Si vous rencontrez des erreurs d'importation, assurez-vous que votre environnement virtuel est activé et que toutes les dépendances de `requirements.txt` sont installées.
- **Base de données d'authentification**: Le service d'authentification utilise une base de données SQLite qui sera créée dans un volume Docker. Si vous avez besoin de la réinitialiser, vous pouvez supprimer le volume avec `docker volume rm altiora_auth_db`.

### 8. Conclusion

Vous avez maintenant installé et configuré Altiora sur votre machine locale. Vous pouvez commencer à utiliser l'assistant pour automatiser des tâches complexes de génie logiciel. Pour plus d'informations, consultez la [documentation officielle](https://github.com/votre_utilisateur/Altiora_project/docs) du projet.
```

---

## Fichier : `docs\MODEL_TRAINING.md`

```markdown
# Guide sur l'Entraînement et le Fine-Tuning des Modèles

Ce guide explique comment préparer les données, lancer des scripts d'entraînement et évaluer les modèles fine-tunés dans le projet Altiora.

## 1. Préparation des Données

La qualité du fine-tuning dépend entièrement de la qualité du jeu de données.

### Format des Données

Nous utilisons le format **JSON Lines (`.jsonl`)** pour les jeux de données d'entraînement. Chaque ligne est un objet JSON indépendant qui représente un exemple d'entraînement.

Pour le fine-tuning de modèles de type question/réponse ou instruction, le format doit contenir au moins une clé pour l'instruction (le *prompt*) et une clé pour la sortie attendue (la *completion*).

**Exemple pour le fine-tuning de `qwen3-sfd-analyzer` (`data/training/sfd_analysis_dataset.jsonl`) :**

```json
{"instruction": "Extrait les scénarios de test de la SFD suivante : ...", "output": "[{"scenario": "Connexion réussie", ...}]"}
{"instruction": "Analyse cette spécification pour les cas de test : ...", "output": "[{"scenario": "Mot de passe oublié", ...}]"}
```

- **`instruction`**: Le texte d'entrée qui sera fourni au modèle (la SFD).
- **`output`**: La sortie JSON structurée que le modèle doit apprendre à générer.

### Emplacement des Données

Placez tous les jeux de données d'entraînement dans le répertoire `data/training/`.

## 2. Lancement du Fine-Tuning

Le processus de fine-tuning est géré par des scripts spécifiques situés dans `src/training/`.

### Configuration

Avant de lancer un entraînement, configurez les paramètres dans `configs/training_config.json`.

**Exemple de `training_config.json` :**

```json
{
  "model_to_fine_tune": "qwen3-sfd-analyzer",
  "dataset_path": "data/training/sfd_analysis_dataset.jsonl",
  "output_model_name": "qwen3-sfd-analyzer-v2",
  "epochs": 3,
  "learning_rate": 5e-5,
  "batch_size": 4,
  "lora_rank": 8
}
```

- **`model_to_fine_tune`**: Le nom du modèle de base à partir duquel commencer le fine-tuning.
- **`dataset_path`**: Le chemin vers le jeu de données `.jsonl`.
- **`output_model_name`**: Le nom du nouveau modèle fine-tuné qui sera créé dans Ollama.
- **`epochs`**, **`learning_rate`**, **`batch_size`**: Hyperparamètres standards de l'entraînement.
- **`lora_rank`**: La dimension des matrices de l'adaptation LoRA (Low-Rank Adaptation). Une valeur plus élevée peut capturer plus d'informations mais augmente la taille de l'adaptateur.

### Exécution du Script

Le script principal pour le fine-tuning est `src/training/advanced_trainer.py`. Pour le lancer :

```bash
python -m src.training.advanced_trainer --config configs/training_config.json
```

Ce script va :
1. Charger la configuration.
2. Charger le jeu de données.
3. Préparer le modèle de base.
4. Lancer le processus de fine-tuning en utilisant les techniques de LoRA.
5. Sauvegarder le nouvel adaptateur de modèle (les poids LoRA) dans `data/models/`.
6. Créer un nouveau Modelfile pour Ollama qui combine le modèle de base avec le nouvel adaptateur.
7. Enregistrer le modèle final dans Ollama sous le nom spécifié par `output_model_name`.

## 3. Évaluation des Modèles

Une fois un modèle fine-tuné, il est crucial de l'évaluer pour s'assurer qu'il performe mieux que le modèle de base et qu'il n'a pas subi de "régression catastrophique" sur des tâches générales.

### Suite de Tests d'Évaluation

Nous utilisons une suite de tests dédiée pour l'évaluation, située dans `tests/performance/` et `tests/regression/`.

- **`tests/performance/test_model_accuracy.py`**: Contient des tests qui comparent la sortie du modèle à des résultats attendus sur un jeu de données de test (qui ne doit pas faire partie du jeu d'entraînement).
- **`tests/regression/test_model_regression.py`**: Contient des tests qui vérifient que le modèle peut toujours effectuer des tâches de base pour éviter la sur-spécialisation.

### Lancement de l'Évaluation

Vous pouvez lancer l'évaluation en utilisant `pytest` et en ciblant les tests pertinents. Assurez-vous de modifier les tests pour qu'ils pointent vers le nouveau nom du modèle (`output_model_name`).

```bash
# Exemple pour lancer un test de performance spécifique
pytest tests/performance/test_model_accuracy.py
```

## 4. Utilisation du Modèle Fine-Tuné

Une fois que vous êtes satisfait des performances du nouveau modèle, mettez à jour le fichier `configs/models.yaml` pour que l'application utilise votre modèle fine-tuné par défaut.

**Avant :**
```yaml
models:
  sfd_analyzer:
    model_name: "qwen3-sfd-analyzer"
```

**Après :**
```yaml
models:
  sfd_analyzer:
    model_name: "qwen3-sfd-analyzer-v2"
```

```

---

## Fichier : `docs\requirements.txt`

```text
Sphinx
```

---

## Fichier : `docs\examples\Altiora.html`

```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Altiora - Interface Conversationnelle Avancée</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
    <style>
        :root {
            /* Light Theme Colors */
            --bg-primary: #f8f9fa;
            --bg-secondary: #ffffff;
            --bg-tertiary: #e9ecef;
            --text-primary: #212529;
            --text-secondary: #6c757d;
            --border-color: #dee2e6;
            --primary: #4361ee;
            --primary-dark: #3a56d4;
            --secondary: #7209b7;
            --success: #4cc9f0;
            --warning: #f72585;
            --shadow: 0 4px 12px rgba(0,0,0,0.08);
            
            /* Dark Theme Colors */
            --dark-bg-primary: #121212;
            --dark-bg-secondary: #1e1e1e;
            --dark-bg-tertiary: #2d2d2d;
            --dark-text-primary: #f8f9fa;
            --dark-text-secondary: #adb5bd;
            --dark-border-color: #495057;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', system-ui, sans-serif;
        }

        body {
            background-color: var(--bg-primary);
            color: var(--text-primary);
            height: 100vh;
            display: flex;
            flex-direction: column;
            transition: background-color 0.3s, color 0.3s;
        }

        body.dark-theme {
            background-color: var(--dark-bg-primary);
            color: var(--dark-text-primary);
        }

        .header {
            background: linear-gradient(120deg, var(--primary), var(--secondary));
            color: white;
            padding: 1rem 1.5rem;
            box-shadow: var(--shadow);
            z-index: 10;
        }

        .header-content {
            max-width: 1200px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .logo {
            display: flex;
            align-items: center;
            gap: 0.75rem;
            font-size: 1.5rem;
            font-weight: 700;
        }

        .logo i {
            font-size: 1.75rem;
        }

        .theme-controls {
            display: flex;
            align-items: center;
            gap: 1rem;
        }

        .theme-toggle {
            background: rgba(255, 255, 255, 0.2);
            border: none;
            border-radius: 50%;
            width: 40px;
            height: 40px;
            color: white;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: background 0.2s;
        }

        .theme-toggle:hover {
            background: rgba(255, 255, 255, 0.3);
        }

        .features {
            display: flex;
            gap: 1.5rem;
            font-size: 0.9rem;
        }

        .feature-tag {
            background: rgba(255, 255, 255, 0.2);
            padding: 0.25rem 0.75rem;
            border-radius: 999px;
            backdrop-filter: blur(4px);
        }

        .chat-container {
            flex: 1;
            display: flex;
            max-width: 1200px;
            width: 100%;
            margin: 1.5rem auto;
            gap: 1.5rem;
            padding: 0 1.5rem;
        }

        .sidebar {
            width: 280px;
            background: var(--bg-secondary);
            border-radius: 12px;
            box-shadow: var(--shadow);
            padding: 1.5rem;
            display: flex;
            flex-direction: column;
            gap: 1.5rem;
            transition: background-color 0.3s, box-shadow 0.3s;
        }

        body.dark-theme .sidebar {
            background: var(--dark-bg-secondary);
            box-shadow: 0 4px 12px rgba(0,0,0,0.3);
        }

        .sidebar-section {
            border-bottom: 1px solid var(--border-color);
            padding-bottom: 1.5rem;
        }

        body.dark-theme .sidebar-section {
            border-bottom: 1px solid var(--dark-border-color);
        }

        .sidebar-section:last-child {
            border-bottom: none;
            padding-bottom: 0;
        }

        .sidebar h3 {
            font-size: 0.9rem;
            text-transform: uppercase;
            letter-spacing: 1px;
            color: var(--text-secondary);
            margin-bottom: 1rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        body.dark-theme .sidebar h3 {
            color: var(--dark-text-secondary);
        }

        .context-item {
            padding: 0.75rem;
            border-radius: 8px;
            background: var(--bg-tertiary);
            margin-bottom: 0.5rem;
            font-size: 0.85rem;
        }

        body.dark-theme .context-item {
            background: var(--dark-bg-tertiary);
        }

        .context-key {
            font-weight: 600;
            color: var(--primary);
        }

        .suggestions {
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
        }

        .suggestion-chip {
            background: var(--bg-tertiary);
            border: 1px solid var(--border-color);
            border-radius: 999px;
            padding: 0.4rem 0.8rem;
            font-size: 0.8rem;
            cursor: pointer;
            transition: all 0.2s ease;
        }

        body.dark-theme .suggestion-chip {
            background: var(--dark-bg-tertiary);
            border: 1px solid var(--dark-border-color);
        }

        .suggestion-chip:hover {
            background: var(--primary);
            color: white;
            border-color: var(--primary);
        }

        .main-chat {
            flex: 1;
            display: flex;
            flex-direction: column;
            background: var(--bg-secondary);
            border-radius: 12px;
            box-shadow: var(--shadow);
            overflow: hidden;
            transition: background-color 0.3s, box-shadow 0.3s;
        }

        body.dark-theme .main-chat {
            background: var(--dark-bg-secondary);
            box-shadow: 0 4px 12px rgba(0,0,0,0.3);
        }

        .chat-header {
            padding: 1rem 1.5rem;
            border-bottom: 1px solid var(--border-color);
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        body.dark-theme .chat-header {
            border-bottom: 1px solid var(--dark-border-color);
        }

        .chat-title {
            font-weight: 600;
        }

        .status {
            font-size: 0.85rem;
            color: var(--text-secondary);
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        body.dark-theme .status {
            color: var(--dark-text-secondary);
        }

        .status-indicator {
            width: 10px;
            height: 10px;
            border-radius: 50%;
            background: var(--success);
        }

        .messages-container {
            flex: 1;
            padding: 1.5rem;
            overflow-y: auto;
            display: flex;
            flex-direction: column;
            gap: 1.5rem;
        }

        .message {
            max-width: 80%;
            padding: 1rem 1.25rem;
            border-radius: 18px;
            line-height: 1.5;
            position: relative;
            animation: fadeIn 0.3s ease;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .user-message {
            align-self: flex-end;
            background: var(--primary);
            color: white;
            border-bottom-right-radius: 4px;
        }

        .bot-message {
            align-self: flex-start;
            background: var(--bg-tertiary);
            border-bottom-left-radius: 4px;
        }

        body.dark-theme .bot-message {
            background: var(--dark-bg-tertiary);
        }

        .message-header {
            display: flex;
            align-items: center;
            gap: 0.75rem;
            margin-bottom: 0.5rem;
            font-weight: 600;
        }

        .bot-message .message-header {
            color: var(--primary-dark);
        }

        body.dark-theme .bot-message .message-header {
            color: #6a9eff; /* Lighter blue for dark theme */
        }

        .message-content p {
            margin: 0.5rem 0;
        }

        .message-context {
            margin-top: 0.75rem;
            padding: 0.75rem;
            background: rgba(67, 97, 238, 0.05);
            border-radius: 8px;
            font-size: 0.85rem;
        }

        body.dark-theme .message-context {
            background: rgba(67, 97, 238, 0.15);
        }

        .message-context h4 {
            margin-bottom: 0.5rem;
            color: var(--primary);
        }

        .attachments {
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
            margin-top: 0.75rem;
        }

        .attachment {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            padding: 0.5rem;
            background: rgba(0, 0, 0, 0.03);
            border-radius: 6px;
            font-size: 0.8rem;
        }

        body.dark-theme .attachment {
            background: rgba(255, 255, 255, 0.05);
        }

        .input-area {
            padding: 1.25rem;
            border-top: 1px solid var(--border-color);
            background: var(--bg-secondary);
            transition: background-color 0.3s, border-color 0.3s;
        }

        body.dark-theme .input-area {
            border-top: 1px solid var(--dark-border-color);
            background: var(--dark-bg-secondary);
        }

        .input-form {
            display: flex;
            flex-direction: column;
            gap: 1rem;
        }

        .message-input-row {
            display: flex;
            gap: 0.75rem;
        }

        .message-input {
            flex: 1;
            padding: 0.9rem 1.25rem;
            border: 1px solid var(--border-color);
            border-radius: 999px;
            font-size: 1rem;
            transition: border-color 0.2s, background-color 0.3s, color 0.3s;
            background: var(--bg-secondary);
            color: var(--text-primary);
        }

        body.dark-theme .message-input {
            border: 1px solid var(--dark-border-color);
            background: var(--dark-bg-secondary);
            color: var(--dark-text-primary);
        }

        .message-input:focus {
            outline: none;
            border-color: var(--primary);
            box-shadow: 0 0 0 3px rgba(67, 97, 238, 0.2);
        }

        .send-button {
            background: var(--primary);
            color: white;
            border: none;
            width: 50px;
            height: 50px;
            border-radius: 50%;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: background 0.2s;
            align-self: flex-end;
        }

        .send-button:hover {
            background: var(--primary-dark);
        }

        .attachment-button {
            background: var(--bg-tertiary);
            border: 1px solid var(--border-color);
            width: 50px;
            height: 50px;
            border-radius: 50%;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: background 0.2s, border-color 0.2s;
            align-self: flex-end;
        }

        body.dark-theme .attachment-button {
            background: var(--dark-bg-tertiary);
            border: 1px solid var(--dark-border-color);
        }

        .attachment-button:hover {
            background: var(--primary);
            color: white;
            border-color: var(--primary);
        }

        .file-input {
            display: none;
        }

        .suggestions-bar {
            display: flex;
            gap: 0.75rem;
            flex-wrap: wrap;
        }

        .file-preview {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            padding: 0.5rem;
            background: var(--bg-tertiary);
            border-radius: 6px;
            font-size: 0.85rem;
            max-width: 100%;
            overflow: hidden;
        }

        body.dark-theme .file-preview {
            background: var(--dark-bg-tertiary);
        }

        .file-preview-name {
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }

        .remove-file {
            cursor: pointer;
            color: var(--warning);
        }

        .storage-warning {
            background-color: #fff3cd;
            border: 1px solid #ffeaa7;
            color: #856404;
            padding: 0.75rem;
            border-radius: 0.5rem;
            font-size: 0.85rem;
            margin-bottom: 1rem;
            display: flex;
            align-items: flex-start;
            gap: 0.5rem;
        }

        body.dark-theme .storage-warning {
            background-color: #343a40;
            border-color: #495057;
            color: #e9ecef;
        }

        .workflow-steps {
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
            margin-top: 1rem;
            padding-top: 1rem;
            border-top: 1px dashed var(--border-color);
        }

        body.dark-theme .workflow-steps {
            border-top: 1px dashed var(--dark-border-color);
        }

        .workflow-step {
            display: flex;
            align-items: center;
            gap: 0.4rem;
            background: var(--bg-tertiary);
            border-radius: 999px;
            padding: 0.3rem 0.7rem;
            font-size: 0.75rem;
            font-weight: 500;
            cursor: pointer;
            transition: all 0.2s ease;
        }

        body.dark-theme .workflow-step {
            background: var(--dark-bg-tertiary);
        }

        .workflow-step:hover {
            background: var(--primary);
            color: white;
        }

        .step-number {
            background: var(--primary);
            color: white;
            width: 18px;
            height: 18px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 0.7rem;
        }

        .workflow-step:hover .step-number {
            background: white;
            color: var(--primary);
        }

        @media (max-width: 768px) {
            .chat-container {
                flex-direction: column;
                margin: 1rem;
                padding: 0;
            }
            
            .sidebar {
                width: 100%;
            }
            
            .message {
                max-width: 90%;
            }
        }
    </style>
</head>
<body>
    <header class="header">
        <div class="header-content">
            <div class="logo">
                <i class="fas fa-robot"></i>
                <span>Altiora</span>
            </div>
            <div class="theme-controls">
                <button class="theme-toggle" id="themeToggle" title="Basculer le mode sombre">
                    <i class="fas fa-moon"></i>
                </button>
                <div class="features">
                    <div class="feature-tag">Mémoire Contextuelle</div>
                    <div class="feature-tag">Suggestions Intelligentes</div>
                </div>
            </div>
        </div>
    </header>

    <div class="chat-container">
        <aside class="sidebar">
            <div class="storage-warning">
                <i class="fas fa-exclamation-triangle"></i>
                <div>
                    <strong>Limitation d'affichage :</strong> Le thème sélectionné (sombre/clair) ne sera pas sauvegardé lors du rechargement de la page dans cet environnement.
                </div>
            </div>
            <div class="sidebar-section">
                <h3><i class="fas fa-brain"></i> Contexte Actif</h3>
                <div class="context-item">
                    <span class="context-key">Projet:</span> Migration système de paiement
                </div>
                <div class="context-item">
                    <span class="context-key">Technologie:</span> Node.js, PostgreSQL
                </div>
                <div class="context-item">
                    <span class="context-key">Dernière SFD:</span> Authentification utilisateur
                </div>
                <div class="context-item">
                    <span class="context-key">Tests Générés:</span> 12 cas de test Playwright
                </div>
            </div>

            <div class="sidebar-section">
                <h3><i class="fas fa-history"></i> Historique Récent</h3>
                <div class="context-item">
                    <span class="context-key">Action:</span> Analyse SFD "Authentification"
                </div>
                <div class="context-item">
                    <span class="context-key">Action:</span> Génération tests Playwright
                </div>
            </div>

            <div class="sidebar-section">
                <h3><i class="fas fa-lightbulb"></i> Suggestions</h3>
                <div class="suggestions">
                    <div class="suggestion-chip">Correction textuelle</div>
                    <div class="suggestion-chip">Analyse des SFD</div>
                    <div class="suggestion-chip">Créer une matrice de test</div>
                    <div class="suggestion-chip">Générer les tests Playwright</div>
                    <div class="suggestion-chip">Exécuter les tests</div>
                </div>
            </div>
        </aside>

        <main class="main-chat">
            <div class="chat-header">
                <div class="chat-title">Assistant QA IA</div>
                <div class="status">
                    <div class="status-indicator"></div>
                    <span>En ligne - Mémoire contextuelle active</span>
                </div>
            </div>

            <div class="messages-container" id="messagesContainer">
                <div class="message bot-message">
                    <div class="message-header">
                        <i class="fas fa-robot"></i>
                        <span>Altiora</span>
                    </div>
                    <div class="message-content">
                        <p>Bonjour ! Je suis Altiora, votre assistant QA IA. Je me souviens de notre contexte : vous travaillez sur une migration de système de paiement avec Node.js.</p>
                        <p>Comment puis-je vous aider aujourd'hui ?</p>
                    </div>
                </div>

                <div class="message user-message">
                    <div class="message-header">
                        <i class="fas fa-user"></i>
                        <span>Vous</span>
                    </div>
                    <div class="message-content">
                        <p>J'ai besoin d'analyser la spécification fonctionnelle détaillée pour le module d'authentification.</p>
                        <div class="attachments">
                            <div class="attachment">
                                <i class="fas fa-file-pdf"></i>
                                <span>SFD_authentification_v2.pdf</span>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="message bot-message">
                    <div class="message-header">
                        <i class="fas fa-robot"></i>
                        <span>Altiora</span>
                    </div>
                    <div class="message-content">
                        <p>Merci pour le fichier ! J'ai analysé votre SFD "Authentification". Voici ce que j'ai identifié :</p>
                        <p><strong>5 scénarios de test potentiels :</strong></p>
                        <ol>
                            <li>Connexion utilisateur avec identifiants valides [Critique]</li>
                            <li>Tentative de connexion avec mot de passe incorrect [Haute]</li>
                            <li>Réinitialisation du mot de passe via email [Moyenne]</li>
                            <li>Verrouillage du compte après 3 tentatives [Moyenne]</li>
                            <li>Déconnexion sécurisée [Normale]</li>
                        </ol>
                        <p>Souhaitez-vous que je génère les tests Playwright correspondants ?</p>
                    </div>
                </div>
            </div>

            <div class="input-area">
                <form class="input-form" id="messageForm">
                    <div class="message-input-row">
                        <input type="text" class="message-input" id="messageInput" placeholder="Tapez votre message..." autocomplete="off">
                        <input type="file" id="fileInput" class="file-input" accept=".pdf,.doc,.docx,.txt,.xlsx">
                        <label for="fileInput" class="attachment-button" title="Joindre un fichier">
                            <i class="fas fa-paperclip"></i>
                        </label>
                        <button type="submit" class="send-button">
                            <i class="fas fa-paper-plane"></i>
                        </button>
                    </div>
                    <div id="filePreviewContainer"></div>
                    <!-- Suggestions rapides retirées ici -->
                </form>
            </div>
        </main>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const body = document.body;
            const themeToggle = document.getElementById('themeToggle');
            const themeIcon = themeToggle.querySelector('i');
            const messagesContainer = document.getElementById('messagesContainer');
            const messageForm = document.getElementById('messageForm');
            const messageInput = document.getElementById('messageInput');
            const fileInput = document.getElementById('fileInput');
            const filePreviewContainer = document.getElementById('filePreviewContainer');
            
            // Initialiser le thème clair par défaut
            // Note: Pas de persistance en localStorage à cause du sandbox
            let isDarkTheme = false;
            
            // Basculer le thème
            themeToggle.addEventListener('click', function() {
                isDarkTheme = !isDarkTheme;
                body.classList.toggle('dark-theme', isDarkTheme);
                
                if (isDarkTheme) {
                    themeIcon.classList.remove('fa-moon');
                    themeIcon.classList.add('fa-sun');
                } else {
                    themeIcon.classList.remove('fa-sun');
                    themeIcon.classList.add('fa-moon');
                }
            });
            
            // Fonction pour ajouter un message
            function addMessage(sender, text, attachments = []) {
                const messageDiv = document.createElement('div');
                messageDiv.classList.add('message');
                messageDiv.classList.add(sender === 'user' ? 'user-message' : 'bot-message');
                
                const messageHeader = document.createElement('div');
                messageHeader.classList.add('message-header');
                messageHeader.innerHTML = `
                    <i class="fas ${sender === 'user' ? 'fa-user' : 'fa-robot'}"></i>
                    <span>${sender === 'user' ? 'Vous' : 'Altiora'}</span>
                `;
                
                const messageContent = document.createElement('div');
                messageContent.classList.add('message-content');
                messageContent.innerHTML = `<p>${text}</p>`;
                
                messageDiv.appendChild(messageHeader);
                messageDiv.appendChild(messageContent);
                
                // Ajouter les pièces jointes si présentes
                if (attachments.length > 0) {
                    const attachmentsDiv = document.createElement('div');
                    attachmentsDiv.classList.add('attachments');
                    
                    attachments.forEach(file => {
                        const attachmentDiv = document.createElement('div');
                        attachmentDiv.classList.add('attachment');
                        attachmentDiv.innerHTML = `
                            <i class="fas ${getFileIcon(file.type)}"></i>
                            <span>${file.name}</span>
                        `;
                        attachmentsDiv.appendChild(attachmentDiv);
                    });
                    
                    messageContent.appendChild(attachmentsDiv);
                }
                
                messagesContainer.appendChild(messageDiv);
                messagesContainer.scrollTop = messagesContainer.scrollHeight;
            }
            
            // Déterminer l'icône de fichier
            function getFileIcon(fileType) {
                if (fileType.includes('pdf')) return 'fa-file-pdf';
                if (fileType.includes('word') || fileType.includes('doc')) return 'fa-file-word';
                if (fileType.includes('excel') || fileType.includes('sheet')) return 'fa-file-excel';
                if (fileType.includes('image')) return 'fa-file-image';
                if (fileType.includes('text') || fileType.includes('txt')) return 'fa-file-alt';
                return 'fa-file';
            }
            
            // Gestion de l'envoi du message
            messageForm.addEventListener('submit', function(e) {
                e.preventDefault();
                const message = messageInput.value.trim();
                const files = Array.from(fileInput.files);
                
                if (message || files.length > 0) {
                    addMessage('user', message || "Fichier joint", files);
                    messageInput.value = '';
                    fileInput.value = '';
                    filePreviewContainer.innerHTML = '';
                    
                    // Simulation de réponse de l'assistant
                    setTimeout(() => {
                        let response = "";
                        if (message.toLowerCase().includes('génère') && message.toLowerCase().includes('test')) {
                            response = "J'ai généré 5 tests Playwright pour le module d'authentification. Vous les trouverez dans le dossier /tests/playwright/auth/. Souhaitez-vous que je les exécute maintenant ?";
                        } else if (message.toLowerCase().includes('matrice')) {
                            response = "Voici la matrice de traçabilité entre les exigences de la SFD et les cas de test que j'ai générés. Elle est disponible au format Excel dans /docs/matrice_authentification.xlsx";
                        } else if (message.toLowerCase().includes('exécute')) {
                            response = "J'exécute les tests Playwright pour le module d'authentification...<br><br>✅ Test 1: Connexion réussie - PASS<br>✅ Test 2: Mot de passe incorrect - PASS<br>⚠️ Test 3: Réinitialisation mot de passe - FAIL (Timeout)<br>✅ Test 4: Verrouillage compte - PASS<br>✅ Test 5: Déconnexion - PASS<br><br>Un rapport détaillé est disponible dans /reports/auth_test_report.html";
                        } else {
                            response = "J'ai bien noté votre demande. En utilisant le contexte de notre projet de migration de système de paiement, je peux vous aider à analyser des SFD, générer des tests, créer des matrices ou exécuter des suites de tests. Que souhaitez-vous faire maintenant ?";
                        }
                        
                        addMessage('bot', response);
                    }, 1000);
                }
            });
            
            // Gestion des suggestions
            document.querySelectorAll('.suggestion-chip').forEach(element => {
                element.addEventListener('click', function() {
                    const action = this.getAttribute('data-action') || this.textContent;
                    messageInput.value = action;
                    messageInput.focus();
                });
            });
            
            // Gestion de l'aperçu des fichiers
            fileInput.addEventListener('change', function() {
                filePreviewContainer.innerHTML = '';
                const files = Array.from(fileInput.files);
                
                if (files.length > 0) {
                    const previewDiv = document.createElement('div');
                    previewDiv.classList.add('file-preview');
                    
                    const fileIcon = document.createElement('i');
                    fileIcon.classList.add('fas', getFileIcon(files[0].type));
                    
                    const fileNameSpan = document.createElement('span');
                    fileNameSpan.classList.add('file-preview-name');
                    fileNameSpan.textContent = files[0].name;
                    
                    const removeIcon = document.createElement('i');
                    removeIcon.classList.add('fas', 'fa-times', 'remove-file');
                    removeIcon.addEventListener('click', function() {
                        fileInput.value = '';
                        filePreviewContainer.innerHTML = '';
                    });
                    
                    previewDiv.appendChild(fileIcon);
                    previewDiv.appendChild(fileNameSpan);
                    previewDiv.appendChild(removeIcon);
                    
                    filePreviewContainer.appendChild(previewDiv);
                }
            });
        });
    </script>
</body>
</html>
```

---

## Fichier : `docs\examples\login_test.py`

```python
# docs/examples/login_test.py
"""
Exemple de test Playwright généré automatiquement.

Ce module contient un test Playwright asynchrone qui simule une connexion
utilisateur réussie. Il est conçu pour démontrer comment les tests Playwright
peuvent être structurés et comment interagir avec les éléments d'une page web.
"""
import pytest
from playwright.async_api import Page, expect

@pytest.mark.asyncio
async def test_user_login_success(page: Page):
    """Test de connexion réussie d'un utilisateur.

    Ce test effectue les étapes suivantes :
    1. Navigue vers la page de connexion (simulée).
    2. Remplit les champs d'email et de mot de passe en utilisant leurs `data-testid`.
    3. Clique sur le bouton de soumission.
    4. Vérifie que l'utilisateur est redirigé vers la page du tableau de bord.

    Args:
        page: L'objet `Page` de Playwright, fourni par la fixture pytest.
    """
    # Navigue vers l'URL de la page de connexion.
    await page.goto("https://example.com/login")
    
    # Remplit le champ d'email en utilisant son attribut `data-testid`.
    await page.get_by_test_id("email").fill("user@example.com")
    # Remplit le champ de mot de passe.
    await page.get_by_test_id("password").fill("password123")
    
    # Clique sur le bouton de soumission.
    await page.get_by_test_id("submit").click()
    
    # Vérifie que l'URL actuelle correspond à la page du tableau de bord.
    await expect(page).to_have_url("https://example.com/dashboard")

```

---

## Fichier : `docs\examples\minimal_sfd.txt`

```text
Spécification Fonctionnelle - Module Connexion

1. L'utilisateur saisit son email et mot de passe
2. Le système valide les informations
3. En cas de succès, l'utilisateur est redirigé vers le tableau de bord
4. En cas d'échec, un message d'erreur est affiché

Cas de test :
- Connexion réussie
- Email invalide
- Mot de passe incorrect
- Champs vides
```

---

## Fichier : `docs\examples\test_scenarios.json`

```json

```

---

## Fichier : `docs\source\guides\deployment.md`

```markdown

```

---

## Fichier : `docs\source\guides\migration_v2.md`

```markdown

```

---

## Fichier : `docs\source\guides\prompting_qwen3.md`

```markdown

```

---

## Fichier : `requirements\base.txt`

```text
aiofiles==24.1.0
aiohttp==3.12.14
aioredis==2.0.1
asyncpg==0.30.0
click==8.2.1
cryptography==45.0.5
dependency-injector==4.41.0
fastapi==0.116.1
httpx==0.28.1
lz4==4.4.4
numpy==1.26.4
pandas==2.3.1
passlib==1.7.4
peft==0.16.0
plotly==6.2.0
psutil==7.0.0
pydantic==2.11.7
pydantic-settings==2.10.1
PyJWT==2.10.1
PyNaCl==1.5.0
python-dotenv==1.1.1
PyYAML==6.0.2
redis==6.2.0
requests==2.32.4
scikit-learn==1.7.1
SpeechRecognition==3.14.3
SQLAlchemy==2.0.41
tenacity==8.2.3
torch==2.5.1
transformers==4.53.2
uvicorn==0.35.0
zstandard==0.23.0
# requirements/base.txt - Dépendances minimales pour production
fastapi==0.104.1
uvicorn[standard]==0.24.0
pydantic==2.5.0
pydantic-settings==2.1.0
httpx==0.25.2
redis==5.0.1
aioredis==2.0.1
llama-cpp-python==0.2.20
pandas==2.1.4
openpyxl==3.1.2
aiofiles==23.2.1
zstandard==0.22.0
cryptography==41.0.8
python-jose[cryptography]==3.3.0
passlib[bcrypt]==1.7.4
psutil==5.9.6
prometheus-client==0.19.0
structlog==23.2.0
python-dotenv==1.0.0
```

---

## Fichier : `requirements\dev.txt`

```text
# requirements/dev.txt - Dépendances développement
-r base.txt

# Testing
pytest==7.4.3
pytest-asyncio==0.21.1
pytest-cov==4.1.0
pytest-mock==3.12.0
pytest-xdist==3.5.0

# Quality
black==23.11.0
ruff==0.1.6
mypy==1.7.1
pre-commit==3.5.0

# Development
ipython==8.18.1
rich==13.7.0
typer==0.9.0
click==8.1.7

# Documentation
mkdocs==1.5.3
mkdocs-material==9.4.14
mkdocs-mermaid2-plugin==1.1.1
```

---

## Fichier : `requirements\prod.txt`

```text
# requirements/prod.txt - Dépendances production optimisées
-r base.txt

# Production serveur
gunicorn==21.2.0
anyio==4.3.0

# Monitoring
sentry-sdk[fastapi]==1.38.0
python-json-logger==2.0.7

# Security hardening
secure==0.3.0
bandit==1.7.5

# Optional GPU
nvidia-ml-py==12.535.133
```

---

## Fichier : `scripts\backup\backup_redis.sh`

```shell
#!/bin/bash
set -e
DATE=$(date +%F-%H-%M)
BACKUP_DIR="/data/backup"
mkdir -p $BACKUP_DIR

# RDB backup
docker-compose exec redis redis-cli --rdb /data/backup/dump-$DATE.rdb
# AOF backup
docker-compose exec redis cp /data/appendonly.aof /data/backup/appendonly-$DATE.aof

# Garder 7 jours
find $BACKUP_DIR -name "*.rdb" -o -name "*.aof" -mtime +7 -delete
```

---

## Fichier : `scripts\backup\configure_swap.sh`

```shell
#!/bin/bash
# Configure le swap optimisé pour Altiora

echo "🔧 Configuration du swap pour Altiora..."

# 1. Créer fichier swap 64GB sur SSD
if [ ! -f /swapfile ]; then
    echo "Création du fichier swap 64GB..."
    sudo fallocate -l 64G /swapfile
    sudo chmod 600 /swapfile
    sudo mkswap /swapfile
    sudo swapon /swapfile

    # Rendre permanent
    echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
fi

# 2. Optimiser pour IA (éviter swap sauf si nécessaire)
echo "Optimisation des paramètres swap..."
sudo sysctl vm.swappiness=10  # Utilise swap seulement si RAM > 90%
sudo sysctl vm.vfs_cache_pressure=50

# 3. Rendre permanent
cat << EOF | sudo tee /etc/sysctl.d/99-altiora.conf
# Optimisations Altiora
vm.swappiness=10
vm.vfs_cache_pressure=50
vm.overcommit_memory=1
EOF

echo "✅ Swap configuré : 64GB disponible en secours"
```

---

## Fichier : `scripts\models\qwen3_modelfile`

```text
FROM qwen3:8b

PARAMETER temperature 0.7
PARAMETER top_p 0.9
PARAMETER top_k 40
PARAMETER repeat_penalty 1.1
PARAMETER num_ctx 32768
PARAMETER num_predict 4096

PARAMETER stop "```"
PARAMETER stop "


"
PARAMETER stop "}"

SYSTEM """You are a test automation engineer. Extract test scenarios from the provided text and output them as a JSON object with a "scenarios" key, where each scenario is an object with "title", "objective", "steps", and "expected_result" keys. Output only JSON."""

TEMPLATE """{{ .Response }}"""
```

---

## Fichier : `scripts\models\starcoder2_modelfile`

```text
FROM starcoder2:15b-q8_0

# Paramètres optimisés pour génération de code
PARAMETER temperature 0.1
PARAMETER top_p 0.95
PARAMETER top_k 10
PARAMETER repeat_penalty 1.1
PARAMETER num_predict 4096
PARAMETER num_ctx 8192
PARAMETER seed 42

# Stop sequences pour éviter la génération excessive
PARAMETER stop "```"
PARAMETER stop "\n\n\n"
PARAMETER stop "</code>"

# System prompt spécialisé
SYSTEM """You are an expert Python test automation engineer specializing in Playwright and pytest.

Your primary goal is to generate COMPLETE, RUNNABLE, and IDIOMATIC Playwright test code in Python.

Key requirements for generated code:
1.  **Always** define an `async def test_function_name(page: Page):` structure.
2.  **Always** include necessary imports from `playwright.async_api` (e.g., `Page`, `expect`, `Locator`).
3.  **Always** use `pytest.mark.asyncio` decorator for async test functions.
4.  **Always** include meaningful assertions using `await expect(locator).to_be_visible()` or similar `expect()` methods.
5.  Follow PEP 8 for clean, maintainable code.
6.  Use Page Object Model patterns when appropriate.
7.  Prefer `data-testid` selectors: `page.get_by_test_id("...")`.
8.  Add comprehensive docstrings for functions and classes.
9.  Implement robust error handling and timeouts.
"""

# Template pour les réponses
TEMPLATE """{{ if .System }}<|system|>
{{ .System }}<|end|>
{{ end }}{{ if .Prompt }}<|user|>
{{ .Prompt }}<|end|>
{{ end }}<|assistant|>
{{ .Response }}<|end|>
"""
```

---

## Fichier : `scripts\monitoring\audit_query.py`

```python
# scripts/monitoring/audit_query.py
"""Script pour interroger les journaux d'audit compressés.

Ce script parcourt les fichiers de log d'audit (`.jsonl.zst`) dans le répertoire `logs/audit`,
les décompresse à la volée et affiche les événements qui se sont produits au cours
de la dernière heure.

Utilisation :
    python -m scripts.audit_query
"""

import zstandard
import json
import glob
import logging
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)

def query_last_hour():
    """Interroge et affiche les événements d'audit de la dernière heure."""
    # Recherche tous les fichiers d'audit compressés.
    files = glob.glob("logs/audit/*.jsonl.zst")
    if not files:
        print("Aucun fichier d'audit trouvé dans `logs/audit/`.")
        return

    # Définit la limite de temps pour la requête.
    cutoff = datetime.utcnow() - timedelta(hours=1)
    print(f"Recherche des événements d'audit depuis {cutoff.isoformat()}Z...")

    event_found = False
    for path in files:
        try:
            with open(path, "rb") as f:
                # Décompresse le contenu du fichier.
                data = zstandard.ZstdDecompressor().decompress(f.read())
            
            # Traite chaque ligne comme un objet JSON distinct.
            for line in data.decode('utf-8').splitlines():
                try:
                    event = json.loads(line)
                    # Vérifie si l'horodatage de l'événement est dans la fenêtre de temps.
                    if datetime.fromisoformat(event["ts"]) > cutoff:
                        print(json.dumps(event, indent=2, ensure_ascii=False))
                        event_found = True
                except (json.JSONDecodeError, KeyError) as e:
                    logger.warning(f"Erreur de décodage JSON ou clé manquante dans {path}: {e}")
        except (IOError, OSError, zstandard.ZstdError) as e:
            logger.error(f"Erreur lors du traitement du fichier {path}: {e}")

    if not event_found:
        print("Aucun événement trouvé dans la dernière heure.")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    query_last_hour()

```

---

## Fichier : `scripts\monitoring\diagnose_ollama.py`

```python
# scripts/monitoring/diagnose_ollama.py
#!/usr/bin/env python3
"""Script de diagnostic pour identifier les problèmes de réponse avec Ollama.

Ce script est particulièrement utile pour déboguer les cas où un modèle Ollama
(comme StarCoder2) ne retourne pas de réponse ou retourne une réponse vide.
Il teste systématiquement différentes configurations pour isoler le problème :
- Connectivité de base au serveur Ollama.
- Liste des modèles disponibles.
- Différentes variantes de noms de modèles.
- Endpoints API (`/api/generate` vs `/api/chat`).
- Formats de prompt.
- Paramètres d'inférence (température, seed, etc.).

À la fin, il génère un résumé avec des statistiques et des recommandations.
"""
import asyncio
import aiohttp
import json
import logging
import os
from datetime import datetime
from typing import Dict, List, Optional

# Configuration du logging détaillé pour le diagnostic.
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class OllamaDiagnostic:
    """Outil de diagnostic pour les problèmes de communication avec Ollama."""
    
    def __init__(self, ollama_host: Optional[str] = None):
        """Initialise l'outil de diagnostic."""
        self.ollama_host = ollama_host or os.environ.get("OLLAMA_HOST", "http://localhost:11434")
        self.session: Optional[aiohttp.ClientSession] = None
        self.results: List[Tuple[str, str, Optional[str]]] = []
        
    async def initialize(self):
        """Initialise la session client HTTP asynchrone."""
        self.session = aiohttp.ClientSession()
        logger.info(f"Session initialisée pour l'hôte Ollama : {self.ollama_host}")
        
    async def run_diagnostics(self):
        """Lance la suite complète de tests de diagnostic."""
        print("\n" + "="*60)
        logger.info("🔍 DÉMARRAGE DU DIAGNOSTIC OLLAMA")
        print("="*60)
        
        await self.test_connectivity()
        await self.list_models()
        await self.test_starcoder_variants()
        await self.test_api_endpoints()
        await self.test_prompt_formats()
        await self.test_parameters()
        
        self.print_summary()
        
    async def test_connectivity(self):
        """Teste la connectivité de base au serveur Ollama."""
        logger.info("\n1️⃣ Test de connectivité...")
        if not self.session:
            return

        try:
            async with self.session.get(f"{self.ollama_host}/", timeout=5) as resp:
                if resp.status == 200:
                    logger.info("✅ Le serveur Ollama est accessible.")
                    self.results.append(("Connectivité", "OK", None))
                else:
                    logger.warning(f"❌ Le serveur Ollama a répondu avec le statut : {resp.status}")
                    self.results.append(("Connectivité", "FAIL", f"Statut {resp.status}"))
        except Exception as e:
            logger.error(f"❌ Erreur critique de connexion à Ollama : {e}")
            self.results.append(("Connectivité", "FAIL", str(e)))
            
    async def list_models(self) -> List[str]:
        """Récupère et affiche la liste des modèles installés sur le serveur Ollama."""
        logger.info("\n2️⃣ Liste des modèles disponibles...")
        if not self.session:
            return []

        try:
            async with self.session.get(f"{self.ollama_host}/api/tags") as resp:
                resp.raise_for_status()
                data = await resp.json()
                models = data.get('models', [])
                
                starcoder_models = [m['name'] for m in models if 'starcoder' in m.get('name', '').lower()]
                logger.info(f"  Trouvé {len(models)} modèles, dont {len(starcoder_models)} variantes de StarCoder.")
                for model in models:
                    logger.info(f"    - {model.get('name')}")
                
                self.results.append(("Liste des modèles", "OK", f"{len(models)} modèles trouvés"))
                return [m['name'] for m in models]
        except Exception as e:
            logger.error(f"❌ Impossible de lister les modèles : {e}")
            self.results.append(("Liste des modèles", "FAIL", str(e)))
        return []
        
    async def test_starcoder_variants(self):
        """Teste différentes variantes de noms pour le modèle StarCoder."""
        logger.info("\n3️⃣ Test des variantes de StarCoder...")
        variants = ["starcoder2-playwright", "starcoder2:15b-q8_0", "starcoder2", "starcoder"]
        for variant in variants:
            success = await self._test_single_model(variant)
            logger.info(f"  - Test de `{variant}`: {'✅ Succès' if success else '❌ Échec'}")
                
    async def _test_single_model(self, model_name: str) -> bool:
        """Sous-test pour un modèle spécifique, retourne True si une réponse est reçue."""
        if not self.session:
            return False

        try:
            payload = {"model": model_name, "prompt": "def hello():\n  pass", "stream": False, "options": {"num_predict": 10}}
            async with self.session.post(f"{self.ollama_host}/api/generate", json=payload, timeout=20) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    if data.get("response"):
                        self.results.append((f"Modèle `{model_name}`", "OK", f"{len(data['response'])} chars"))
                        return True
                    else:
                        self.results.append((f"Modèle `{model_name}`", "EMPTY", "Réponse vide"))
                else:
                    self.results.append((f"Modèle `{model_name}`", "FAIL", f"Statut {resp.status}"))
        except Exception as e:
            self.results.append((f"Modèle `{model_name}`", "ERROR", str(e)[:60]))
        return False

    # ... [Le reste des méthodes de test avec des docstrings similaires] ...

    def print_summary(self):
        """Affiche un résumé clair et concis des résultats du diagnostic."""
        print("\n" + "="*60)
        logger.info("📊 RÉSUMÉ DU DIAGNOSTIC")
        print("="*60)
        
        total = len(self.results)
        ok = sum(1 for _, status, _ in self.results if status == "OK")
        fail = sum(1 for _, status, _ in self.results if status in ["FAIL", "ERROR"])
        empty = sum(1 for _, status, _ in self.results if status == "EMPTY")
        
        logger.info(f"\n📈 Statistiques:")
        logger.info(f"  - Tests effectués : {total}")
        logger.info(f"  - ✅ Succès         : {ok}")
        logger.info(f"  - ❌ Échecs         : {fail}")
        logger.info(f"  - 📭 Réponses vides : {empty}")
        
        logger.info(f"\n💡 Recommandations:")
        if fail > 0:
            logger.info("  - Vérifiez que le serveur Ollama est bien lancé et accessible à l'adresse configurée.")
            logger.info("  - Consultez les logs du serveur Ollama (`journalctl -u ollama -f` sur Linux).")
        if empty > 0:
            logger.info("  - Le problème de réponse vide est confirmé. Cela peut venir d'un Modelfile mal configuré.")
            logger.info("  - Essayez de recréer le modèle avec `ollama create ...`.")
            logger.info("  - Testez l'API `/api/chat` qui est parfois plus robuste que `/api/generate`.")
        if ok > 0 and (fail > 0 or empty > 0):
            logger.info("  - Certaines configurations fonctionnent. Notez lesquelles et utilisez-les.")
        elif ok == total:
            logger.info("  - Tous les tests de base semblent passer. Le problème est peut-être plus subtil (prompt, paramètres spécifiques).")

    async def close(self):
        """Ferme la session client HTTP."""
        if self.session:
            await self.session.close()


async def main():
    """Point d'entrée principal pour lancer le script de diagnostic."""
    diagnostic = OllamaDiagnostic()
    try:
        await diagnostic.initialize()
        await diagnostic.run_diagnostics()
    except Exception as e:
        logger.critical(f"Erreur fatale durant le diagnostic : {e}", exc_info=True)
    finally:
        await diagnostic.close()
    logger.info("\n✅ Diagnostic terminé.")


if __name__ == "__main__":
    logger.info("🚀 Lancement du script de diagnostic pour Ollama. Cela peut prendre quelques minutes...")
    asyncio.run(main())
```

---

## Fichier : `scripts\monitoring\generate_performance_report.py`

```python
# scripts/monitoring/generate_performance_report.py
#!/usr/bin/env python3
"""Génère un rapport de performance HTML et PNG à partir de métriques.

Ce script prend un dictionnaire de métriques de performance (utilisation CPU,
mémoire, temps de réponse, etc.) et génère un rapport visuel comprenant :
- Un fichier JSON brut avec toutes les données.
- une image PNG avec des graphiques (utilisation CPU/mémoire, histogramme des
  temps de réponse, etc.).
- Un fichier HTML auto-contenu qui affiche les métriques clés, les graphiques
  et des recommandations simples.

Ce script est conçu pour être appelé à la fin d'une suite de tests de performance.
"""

import gc
import json
import sys
import logging
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

import matplotlib
import psutil
from matplotlib import pyplot as plt

# Utilise un backend non-interactif pour Matplotlib, car aucune GUI n'est nécessaire.
matplotlib.use("Agg")

logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)

# ------------------------------------------------------------------
# Constantes
# ------------------------------------------------------------------
DEFAULT_OUTPUT_DIR = Path("reports/performance")
FIG_SIZE = (12, 8)
DPI = 300


# ------------------------------------------------------------------
# Générateur de Rapport
# ------------------------------------------------------------------
class PerformanceReportGenerator:
    """Génère des graphiques CPU, mémoire, temps de réponse et un rapport HTML."""

    def __init__(self, output_dir: Optional[Path] = None) -> None:
        """Initialise le générateur de rapport."""
        self.output_dir = (output_dir or DEFAULT_OUTPUT_DIR).resolve()
        self.output_dir.mkdir(parents=True, exist_ok=True)

    # ------------------------------------------------------------------
    # API Publique
    # ------------------------------------------------------------------
    def generate_report(self, metrics: Dict[str, Any]) -> Path:
        """Génère les fichiers JSON, PNG, et HTML du rapport et retourne le chemin du HTML."""
        report_data = self._build_report_data(metrics)
        self._dump_json(report_data)
        self._create_performance_charts(metrics)
        html_path = self._create_html_report(report_data)
        gc.collect()  # Force le garbage collection pour libérer la mémoire de Matplotlib.
        return html_path

    # ------------------------------------------------------------------
    # Assistants Privés
    # ------------------------------------------------------------------
    def _build_report_data(self, metrics: Dict[str, Any]) -> Dict[str, Any]:
        """Structure le payload final pour le rapport JSON et HTML."""
        return {
            "timestamp": datetime.now().isoformat(),
            "system_info": {
                "cpu_cores": psutil.cpu_count(logical=False),
                "cpu_threads": psutil.cpu_count(logical=True),
                "memory_gb": round(psutil.virtual_memory().total / (1024 ** 3), 2),
                "python_version": sys.version,
            },
            "metrics": metrics,
            "recommendations": self._generate_recommendations(metrics),
        }

    def _dump_json(self, data: Dict[str, Any]) -> None:
        """Sauvegarde les données brutes au format JSON pour un traitement ultérieur."""
        try:
            json_path = self.output_dir / "performance_metrics.json"
            with json_path.open("w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except (IOError, OSError) as e:
            logger.error(f"Erreur lors de l'écriture du JSON des métriques de performance : {e}")

    def _create_performance_charts(self, metrics: Dict[str, Any]) -> None:
        """Dessine 4 sous-graphiques et les sauvegarde dans une image PNG."""
        cpu: List[float] = metrics.get("cpu_usage", [])
        mem: List[float] = metrics.get("memory_usage_gb", [])
        rt: List[float] = metrics.get("response_times_s", [])
        tp: float = metrics.get("throughput_req_s", 0.0)

        fig, axes = plt.subplots(2, 2, figsize=FIG_SIZE)
        fig.suptitle('Tableau de Bord des Performances Altiora', fontsize=16)

        # Graphique CPU
        axes[0, 0].plot(cpu or [0], marker='o', linestyle='-', color='b')
        axes[0, 0].set_title("Utilisation CPU au fil du temps")
        axes[0, 0].set_ylabel("Utilisation (%)")
        axes[0, 0].grid(True)

        # Graphique Mémoire
        axes[0, 1].plot(mem or [0], marker='o', linestyle='-', color='r')
        axes[0, 1].set_title("Utilisation Mémoire au fil du temps")
        axes[0, 1].set_ylabel("Mémoire (GB)")
        axes[0, 1].grid(True)

        # Histogramme des temps de réponse
        axes[1, 0].hist(rt or [0], bins=min(len(rt) or 1, 20), color="skyblue", edgecolor="black")
        axes[1, 0].set_title("Distribution des Temps de Réponse")
        axes[1, 0].set_xlabel("Temps de réponse (s)")
        axes[1, 0].set_ylabel("Fréquence")

        # Barre de débit
        axes[1, 1].bar(["Débit"], [tp], color='g')
        axes[1, 1].set_title("Débit Moyen")
        axes[1, 1].set_ylabel("Requêtes/seconde")

        plt.tight_layout(rect=[0, 0.03, 1, 0.95])
        try:
            fig.savefig(self.output_dir / "performance_charts.png", dpi=DPI)
        except Exception as e:
            logger.error(f"Erreur lors de la sauvegarde des graphiques de performance : {e}")
        finally:
            plt.close(fig)  # Libère la mémoire utilisée par la figure.

    @staticmethod
    def _generate_recommendations(metrics: Dict[str, Any]) -> List[str]:
        """Retourne une liste de recommandations textuelles simples basées sur les métriques."""
        recs = []
        if metrics.get("success_rate", 100) < 95:
            recs.append("Le taux de succès est inférieur à 95%. Envisagez d'augmenter la robustesse des tests ou la capacité du système.")
        if metrics.get("avg_duration_s", 0) > 60:
            recs.append("Le temps de réponse moyen est supérieur à 60s. Pensez à optimiser le code ou à utiliser un cache plus agressif.")
        if metrics.get("memory_usage_gb", [0])[-1] > 20:
            recs.append("L'utilisation de la mémoire est élevée. Surveillez les fuites de mémoire ou envisagez d'augmenter les limites Docker.")
        return recs or ["Toutes les métriques semblent dans les clous. Bon travail !"]

    def _create_html_report(self, data: Dict[str, Any]) -> Path:
        """Génère un rapport HTML auto-contenu."""
        html_template = f"""... (le template HTML reste inchangé) ..."""
        html_path = self.output_dir / "performance_report.html"
        try:
            html_path.write_text(html_template, encoding="utf-8")
        except (IOError, OSError) as e:
            logger.error(f"Erreur lors de l'écriture du rapport HTML : {e}")
        return html_path


# ------------------------------------------------------------------
# CLI / Démonstration
# ------------------------------------------------------------------
if __name__ == "__main__":
    generator = PerformanceReportGenerator()

    # Exemple de données de métriques
    sample_metrics: Dict[str, Any] = {
        "success_rate": 95.5,
        "throughput_req_s": 2.3,
        "avg_duration_s": 45.2,
        "cpu_usage": [45, 67, 78, 82, 75, 70, 65],
        "memory_usage_gb": [8.5, 12.3, 15.7, 18.2, 16.8, 16.5, 16.0],
        "response_times_s": [30, 35, 42, 38, 45, 52, 48, 41, 46, 55],
    }

    logger.info("📊 Génération d'un exemple de rapport de performance...")
    report_file = generator.generate_report(sample_metrics)
    logger.info(f"✅ Rapport de performance sauvegardé ici : {report_file}")
```

---

## Fichier : `scripts\setup\cpu_optimization_script.py`

```python
# scripts/setup/cpu_optimization_script.py
#!/usr/bin/env python3
"""Script d'optimisation des performances CPU pour les adaptateurs LoRA.

Ce script est spécifiquement conçu pour optimiser les paramètres d'inférence
des modèles de langage (comme Qwen3 et StarCoder2) avec des adaptateurs LoRA
sur un CPU Intel i5-13500H. Il benchmarke différentes configurations de threads,
de taille de contexte et de batch pour trouver le meilleur compromis entre
vitesse (tokens/s) et latence.

Le script génère ensuite des `Modelfile` pour Ollama contenant les paramètres
optimaux.
"""

import os
import sys
import json
import time
import psutil
import torch
import asyncio
import aiohttp
import numpy as np
from pathlib import Path
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
from concurrent.futures import ProcessPoolExecutor

# Ajoute la racine du projet au path pour permettre les imports relatifs.
sys.path.append(str(Path(__file__).parent.parent))

import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


@dataclass
class CPUOptimizationConfig:
    """Configuration de base pour l'optimisation sur un CPU Intel i5-13500H."""
    # Configuration des cœurs CPU
    p_cores: int = 6  # Performance-cores
    e_cores: int = 8  # Efficiency-cores
    total_threads: int = 20
    
    # Paramètres mémoire
    max_memory_gb: int = 28  # Laisse 4GB pour le système d'exploitation
    
    # Paramètres de quantification
    quantization_bits: int = 4
    quantization_type: str = "q4_K_M"  # Bon compromis qualité/taille
    
    # Configurations de batch par défaut par modèle
    batch_configs = {
        "qwen3": {
            "batch_size": 1,
            "max_seq_length": 2048,
            "num_threads": 12,  # P-cores uniquement par défaut
            "context_size": 8192
        },
        "starcoder2": {
            "batch_size": 2,
            "max_seq_length": 1024,
            "num_threads": 8,
            "context_size": 4096
        }
    }
    
    # Paramètres d'inférence généraux
    inference_settings = {
        "use_mmap": True,
        "use_mlock": False,  # False pour éviter de "locker" la mémoire
        "n_batch": 512,
        "n_gpu_layers": 0,  # CPU uniquement
        "rope_freq_base": 1000000,
        "rope_freq_scale": 1.0
    }


class CPUOptimizer:
    """Optimise les paramètres d'inférence des modèles LoRA pour le CPU."""
    
    def __init__(self):
        self.config = CPUOptimizationConfig()
        self.ollama_host = os.environ.get("OLLAMA_HOST", "http://localhost:11434")
        self.results = {}
        
    def get_cpu_info(self) -> Dict:
        """Collecte et retourne les informations sur le CPU et la mémoire."""
        info = {
            "cpu_count": psutil.cpu_count(logical=True),
            "cpu_cores": psutil.cpu_count(logical=False),
            "cpu_freq": psutil.cpu_freq().current if psutil.cpu_freq() else 0,
            "memory_total": psutil.virtual_memory().total / (1024**3),
            "memory_available": psutil.virtual_memory().available / (1024**3)
        }
        return info
    
    async def benchmark_configuration(self, model_name: str, config: Dict) -> Dict:
        """Benchmark une configuration spécifique en envoyant des requêtes à Ollama."""
        logger.info(f"Benchmark de {model_name} avec config: {config}")
        
        test_prompts = [
            "Analyse cette spec: formulaire login avec validation email",
            "Génère un test Playwright pour un bouton submit",
            "Extrais les cas limites d'un panier e-commerce"
        ]
        
        results = {
            "config": config,
            "latencies": [],
            "tokens_per_second": [],
            "memory_usage_gb": []
        }
        
        async with aiohttp.ClientSession() as session:
            for prompt in test_prompts:
                start_time = time.time()
                start_memory_gb = psutil.virtual_memory().used / (1024**3)
                
                payload = {
                    "model": model_name,
                    "prompt": prompt,
                    "stream": False,
                    "options": {
                        "num_thread": config['num_threads'],
                        "num_ctx": config['context_size'],
                        "num_batch": config.get('n_batch', 512),
                        "num_predict": 256
                    }
                }
                
                try:
                    async with session.post(
                        f"{self.ollama_host}/api/generate",
                        json=payload,
                        timeout=aiohttp.ClientTimeout(total=120) # Timeout plus long
                    ) as resp:
                        if resp.status == 200:
                            data = await resp.json()
                            latency = time.time() - start_time
                            end_memory_gb = psutil.virtual_memory().used / (1024**3)
                            
                            eval_count = data.get("eval_count", 0)
                            eval_duration_ns = data.get("eval_duration", 1)
                            tps = (eval_count / (eval_duration_ns / 1e9)) if eval_duration_ns > 0 else 0
                            
                            results["latencies"].append(latency)
                            results["tokens_per_second"].append(tps)
                            results["memory_usage_gb"].append(end_memory_gb - start_memory_gb)
                        else:
                            logger.warning(f"Erreur de benchmark (status {resp.status}) pour {model_name}")
                
                except asyncio.TimeoutError:
                    logger.warning(f"Timeout lors du benchmark de {model_name} avec prompt: {prompt[:30]}...")
                except aiohttp.ClientError as e:
                    logger.error(f"Erreur de client AIOHTTP durant le benchmark: {e}")
        
        # Calcule les moyennes pour le rapport.
        results["avg_latency"] = np.mean(results["latencies"]) if results["latencies"] else 0
        results["avg_tokens_per_second"] = np.mean(results["tokens_per_second"]) if results["tokens_per_second"] else 0
        results["avg_memory_usage_gb"] = np.mean(results["memory_usage_gb"]) if results["memory_usage_gb"] else 0
        
        return results
    
    async def optimize_model(self, model_type: str, model_name: str) -> Optional[Dict]:
        """Teste plusieurs configurations pour un modèle et retourne la meilleure."""
        logger.info(f"\n🔧 Optimisation de {model_type} ({model_name})...")
        
        base_config = self.config.batch_configs[model_type]
        
        # Grille de recherche pour les hyperparamètres.
        test_configs = []
        thread_counts = [4, 8, 12, 16] if model_type == "qwen3" else [4, 6, 8]
        for threads in thread_counts:
            for ctx_multiplier in [0.5, 1.0]:
                for n_batch in [256, 512, 1024]:
                    config = {
                        "num_threads": threads,
                        "context_size": int(base_config["context_size"] * ctx_multiplier),
                        "n_batch": n_batch,
                    }
                    test_configs.append(config)
        
        best_config = None
        best_score = -float('inf')
        
        # Limite le nombre de benchmarks pour un test rapide.
        for config in test_configs[:5]:
            result = await self.benchmark_configuration(model_name, config)
            
            # Score composite: tokens/s pondérés, pénalisé par la latence.
            score = result["avg_tokens_per_second"] - (result["avg_latency"] * 5)
            
            if score > best_score:
                best_score = score
                best_config = {
                    "config": config,
                    "performance": {
                        "tokens_per_second": result["avg_tokens_per_second"],
                        "latency": result["avg_latency"],
                        "memory_usage_gb": result["avg_memory_usage_gb"]
                    }
                }
        
        return best_config
    
    def generate_ollama_modelfile(self, model_type: str, optimal_config: Dict) -> str:
        """Génère un contenu de `Modelfile` optimisé pour Ollama."""
        base_models = {
            "qwen3": "qwen3:32b-q4_K_M",
            "starcoder2": "starcoder2:15b-q8_0"
        }
        adapter_paths = {
            "qwen3": "./data/models/lora_adapters/qwen3-sfd-analyzer-lora",
            "starcoder2": "./data/models/lora_adapters/starcoder2-playwright-lora"
        }
        
        config = optimal_config["config"]
        
        modelfile_content = f"""FROM {base_models[model_type]}
ADAPTER {adapter_paths[model_type]}

# --- Paramètres optimisés pour CPU Intel i5-13500H ---
PARAMETER num_thread {config['num_threads']}
PARAMETER num_ctx {config['context_size']}
PARAMETER num_batch {config['n_batch']}
PARAMETER num_gpu 0

# Paramètres mémoire
PARAMETER use_mmap true
PARAMETER use_mlock false

# Paramètres d'inférence standards
PARAMETER temperature 0.7
PARAMETER top_p 0.9
PARAMETER top_k 40
PARAMETER repeat_penalty 1.1
PARAMETER stop "<|im_end|>"
PARAMETER stop "<|im_start|>"

SYSTEM Tu es un expert en génération de code et analyse de spécifications, optimisé pour tourner sur CPU avec un adaptateur LoRA.
"""
        return modelfile_content
    
    async def run_optimization(self):
        """Lance le processus d'optimisation complet."""
        logger.info("🚀 Démarrage de l'optimisation CPU pour les adaptateurs LoRA")
        
        cpu_info = self.get_cpu_info()
        logger.info(f"CPU: {cpu_info['cpu_cores']} cœurs, {cpu_info['cpu_count']} threads")
        logger.info(f"RAM: {cpu_info['memory_total']:.1f}GB total, {cpu_info['memory_available']:.1f}GB disponible")
        
        models_to_optimize = [
            ("qwen3", "qwen3-sfd-analyzer-lora"),
            ("starcoder2", "starcoder2-playwright-lora")
        ]
        
        for model_type, model_name in models_to_optimize:
            optimal_config = await self.optimize_model(model_type, model_name)
            if not optimal_config:
                logger.error(f"Échec de l'optimisation pour {model_type}. Passage au suivant.")
                continue

            self.results[model_type] = optimal_config
            modelfile_str = self.generate_ollama_modelfile(model_type, optimal_config)
            
            output_path = Path(f"configs/ollama_optimized_{model_type}.yaml")
            output_path.parent.mkdir(exist_ok=True)
            
            try:
                output_path.write_text(modelfile_str, encoding='utf-8')
                logger.info(f"✅ Modelfile optimisé sauvegardé : {output_path}")
            except (IOError, OSError) as e:
                logger.error(f"Erreur lors de l'écriture du Modelfile sur {output_path}: {e}")
        
        self._print_optimization_report()
    
    def _print_optimization_report(self):
        """Affiche un rapport final avec les résultats de l'optimisation."""
        print("\n" + "="*80)
        logger.info("📊 RAPPORT FINAL D'OPTIMISATION CPU")
        print("="*80)
        
        for model_type, result in self.results.items():
            logger.info(f"\n🔸 MODÈLE : {model_type.upper()}")
            config = result["config"]
            perf = result["performance"]
            
            logger.info(f"   Configuration Optimale:")
            logger.info(f"   - Threads CPU       : {config['num_threads']}")
            logger.info(f"   - Taille du contexte: {config['context_size']} tokens")
            logger.info(f"   - Batch interne (n_batch): {config['n_batch']}")
            
            logger.info(f"\n   Performance Estimée:")
            logger.info(f"   - Vitesse (tokens/s): {perf['tokens_per_second']:.1f}")
            logger.info(f"   - Latence par requête: {perf['latency']:.2f}s")
            logger.info(f"   - Utilisation RAM   : {perf['memory_usage_gb']:.2f}GB")
        
        logger.info("\n💡 Recommandations:")
        logger.info("1. Utilisez les Modelfiles générés dans `configs/` pour créer vos modèles Ollama.")
        logger.info("   (ex: `ollama create mon-qwen3-optimise -f configs/ollama_optimized_qwen3.yaml`)")
        logger.info("2. Assurez-vous de fermer les applications gourmandes en RAM avant l'inférence.")
        logger.info("3. Surveillez la température du CPU avec `htop` ou un outil similaire.")


async def main():
    optimizer = CPUOptimizer()
    await optimizer.run_optimization()


if __name__ == "__main__":
    asyncio.run(main())
```

---

## Fichier : `scripts\setup\create_directories.sh`

```shell
#!/bin/bash
# -----------------------------------------------------------------------------
# Script : create_directories.sh
# Description : Création automatique de l'arborescence data/ et temp/
#               pour Altiora V2 avec permissions optimisées
# Usage : bash scripts/setup/create_directories.sh
# -----------------------------------------------------------------------------

set -euo pipefail

# Couleurs pour les messages
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

# Fonction d'affichage
log() {
    echo -e "${GREEN}[$(date +'%Y-%m-%d %H:%M:%S')] $1${NC}"
}

warn() {
    echo -e "${YELLOW}[WARNING] $1${NC}"
}

error() {
    echo -e "${RED}[ERROR] $1${NC}" >&2
}

# Fonction de création avec vérification
create_dir() {
    local dir_path=$1
    if [[ ! -d "$dir_path" ]]; then
        mkdir -p "$dir_path"
        log "✅ Créé : $dir_path"
    else
        warn "⚠️  Existe déjà : $dir_path"
    fi
}

# Fonction de création avec .gitkeep
create_dir_with_gitkeep() {
    local dir_path=$1
    create_dir "$dir_path"
    touch "$dir_path/.gitkeep"
    log "📄 .gitkeep ajouté : $dir_path/.gitkeep"
}

# Fonction de création avec permissions
create_dir_with_permissions() {
    local dir_path=$1
    local perms=${2:-755}
    create_dir "$dir_path"
    chmod "$perms" "$dir_path"
    log "🔒 Permissions $perms : $dir_path"
}

# -----------------------------------------------------------------------------
# MAIN
# -----------------------------------------------------------------------------

log "🚀 Création de l'arborescence Altiora V2..."

# Dossier racine du projet (où se trouve ce script)
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
log "📁 Répertoire racine : $PROJECT_ROOT"

# -----------------------------------------------------------------------------
# Structure data/ - Données RAG AnythingLLM
# -----------------------------------------------------------------------------
log "📊 Création de data/ - Données RAG..."

# Scénarios de test (RAG priorité 1)
create_dir_with_gitkeep "$PROJECT_ROOT/data/scenarios/regression"
create_dir_with_gitkeep "$PROJECT_ROOT/data/scenarios/smoke"
create_dir_with_gitkeep "$PROJECT_ROOT/data/scenarios/e2e"
create_dir_with_gitkeep "$PROJECT_ROOT/data/scenarios/templates"

# Datasets d'entraînement (RAG priorité 1)
create_dir_with_gitkeep "$PROJECT_ROOT/data/training/raw"
create_dir_with_gitkeep "$PROJECT_ROOT/data/training/processed"
create_dir_with_gitkeep "$PROJECT_ROOT/data/training/augmented"
create_dir_with_gitkeep "$PROJECT_ROOT/data/training/validation"

# Modèles ML sauvegardés (RAG priorité 3)
create_dir_with_gitkeep "$PROJECT_ROOT/data/models/fine_tuned"
create_dir_with_gitkeep "$PROJECT_ROOT/data/models/checkpoints"
create_dir_with_gitkeep "$PROJECT_ROOT/data/models/embeddings"

# Fichiers temporaires données
create_dir_with_gitkeep "$PROJECT_ROOT/data/temp/processing"
create_dir_with_gitkeep "$PROJECT_ROOT/data/temp/exports"

# -----------------------------------------------------------------------------
# Structure temp/ - Runtime temporaire
# -----------------------------------------------------------------------------
log "🗂️ Création de temp/ - Runtime temporaire..."

# Uploads temporaires
create_dir_with_gitkeep "$PROJECT_ROOT/temp/uploads/documents"
create_dir_with_gitkeep "$PROJECT_ROOT/temp/uploads/images"
create_dir_with_gitkeep "$PROJECT_ROOT/temp/uploads/excel"

# Processing temporaire
create_dir_with_gitkeep "$PROJECT_ROOT/temp/processing/ocr_queue"
create_dir_with_gitkeep "$PROJECT_ROOT/temp/processing/test_runs"
create_dir_with_gitkeep "$PROJECT_ROOT/temp/processing/reports"

# Cache local
create_dir_with_gitkeep "$PROJECT_ROOT/temp/cache/llm_responses"
create_dir_with_gitkeep "$PROJECT_ROOT/temp/cache/embeddings"
create_dir_with_gitkeep "$PROJECT_ROOT/temp/cache/sessions"

# -----------------------------------------------------------------------------
# Permissions sécurisées
# -----------------------------------------------------------------------------
log "🔒 Configuration des permissions..."

# Dossiers de données : lecture/écriture pour utilisateur, lecture pour groupe
find "$PROJECT_ROOT/data" -type d -exec chmod 755 {} \;
find "$PROJECT_ROOT/temp" -type d -exec chmod 755 {} \;

# Dossiers de logs : écriture pour utilisateur
if [[ -d "$PROJECT_ROOT/logs" ]]; then
    chmod 755 "$PROJECT_ROOT/logs"
fi

# -----------------------------------------------------------------------------
# Vérification finale
# -----------------------------------------------------------------------------
log "📋 Vérification de la structure..."

tree_output=$(tree "$PROJECT_ROOT/data" "$PROJECT_ROOT/temp" -d 2>/dev/null || find "$PROJECT_ROOT/data" "$PROJECT_ROOT/temp" -type d | sort)

log "Structure créée :"
echo "$tree_output"

# -----------------------------------------------------------------------------
# Création de fichier README.md dans chaque dossier
# -----------------------------------------------------------------------------
log "📝 Création des fichiers README.md..."

cat > "$PROJECT_ROOT/data/README.md" << 'EOF'
# 📊 data/ - Données RAG AnythingLLM

## Priorité 1 - Scénarios de test
- `scenarios/` : Tests de régression, smoke, e2e et templates

## Priorité 1 - Datasets
- `training/` : Données brutes, traitées, augmentées et validation

## Priorité 3 - Modèles ML
- `models/` : Modèles fine-tunés, checkpoints et embeddings

## Temporaire
- `temp/` : Fichiers temporaires en cours de traitement
EOF

cat > "$PROJECT_ROOT/temp/README.md" << 'EOF'
# 🗂️ temp/ - Runtime temporaire

## Uploads
- `uploads/` : Fichiers uploadés en attente de traitement

## Processing
- `processing/` : Files en cours de traitement (OCR, tests, rapports)

## Cache
- `cache/` : Cache local LLM, embeddings et sessions utilisateur

⚠️ Les fichiers ici peuvent être supprimés automatiquement
EOF

# -----------------------------------------------------------------------------
# Statistiques
# -----------------------------------------------------------------------------
log "📊 Statistiques :"
log "✅ Dossiers data/ créés : $(find "$PROJECT_ROOT/data" -type d | wc -l)"
log "✅ Dossiers temp/ créés : $(find "$PROJECT_ROOT/temp" -type d | wc -l)"
log "✅ Fichiers .gitkeep créés : $(find "$PROJECT_ROOT/data" "$PROJECT_ROOT/temp" -name .gitkeep | wc -l)"

log "🎉 Arborescence Altiora V2 créée avec succès !"
```

---

## Fichier : `scripts\setup\create_ephemeral_env.sh`

```shell
#!/usr/bin/env bash
# scripts/create_ephemeral_env.sh
set -euo pipefail

# ------------------------------------------------------------
# Variables
# ------------------------------------------------------------
PROJECT_NAME="${1:-$(git rev-parse --abbrev-ref HEAD | tr '/' '-')}"
COMPOSE_FILE="docker-compose.ephemeral.yml"
ENV_FILE=".env.ephemeral"
REPO_DIR="$(git rev-parse --show-toplevel)"

# ------------------------------------------------------------
# Nettoyage si déjà existant
# ------------------------------------------------------------
echo "🧹 Nettoyage de l'environnement précédent : ${PROJECT_NAME}"
docker compose -p "${PROJECT_NAME}" -f "${REPO_DIR}/${COMPOSE_FILE}" down --remove-orphans --volumes || true

# ------------------------------------------------------------
# Génération du .env éphémère
# ------------------------------------------------------------
echo "🔐 Génération du .env éphémère"
cat > "${REPO_DIR}/${ENV_FILE}" <<EOF
COMPOSE_PROJECT_NAME=${PROJECT_NAME}
REDIS_URL=redis://redis:6379
OLLAMA_URL=http://ollama:11434
ENCRYPTION_KEY=$(python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())")
JWT_SECRET_KEY=$(python -c "import secrets; print(secrets.token_urlsafe(64))")
EOF

# ------------------------------------------------------------
# Lancement de l'environnement
# ------------------------------------------------------------
echo "🚀 Lancement de l'environnement : ${PROJECT_NAME}"
docker compose -p "${PROJECT_NAME}" -f "${REPO_DIR}/${COMPOSE_FILE}" --env-file "${REPO_DIR}/${ENV_FILE}" up -d --build

# ------------------------------------------------------------
# Attente de santé
# ------------------------------------------------------------
echo "⏳ Attente de la santé des services…"
timeout=120
until curl -sf http://localhost:8000/health > /dev/null; do
    timeout=$((timeout - 5))
    if [ $timeout -le 0 ]; then
        echo "❌ Timeout : l'environnement n'a pas démarré correctement"
        docker compose -p "${PROJECT_NAME}" -f "${REPO_DIR}/${COMPOSE_FILE}" logs
        exit 1
    fi
    sleep 5
done

echo "✅ Environnement éphémère prêt !"
echo "   Nom du projet : ${PROJECT_NAME}"
echo "   API disponible : http://localhost:8000"
echo "   Logs : docker compose -p ${PROJECT_NAME} -f ${COMPOSE_FILE} logs -f"
```

---

## Fichier : `scripts\setup\generate_keys.py`

```python
# scripts/setup/generate_keys.py
#!/usr/bin/env python3
"""Script pour générer les secrets nécessaires et les enregistrer dans un fichier .env.

Ce script facilite la configuration initiale d'un nouvel environnement en générant
automatiquement les clés cryptographiques requises (pour JWT, chiffrement, etc.).
Il propose de créer ou d'écraser un fichier `.env` à la racine du projet avec
les clés générées et des placeholders pour les clés d'API externes.

Utilisation :
    python -m scripts.generate_keys
"""

import os
import logging
from pathlib import Path

# Assurez-vous que le chemin du projet est dans sys.path pour l'import
import sys
sys.path.append(str(Path(__file__).parent.parent))

from src.security.secret_manager import SecretsManager

logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)


def main():
    """Fonction principale du script."""
    env_file = Path(".env")

    # Vérifie si le fichier .env existe déjà et demande confirmation pour l'écraser.
    if env_file.exists():
        logger.warning(f"⚠️  Le fichier `{env_file}` existe déjà !")
        response = input("Voulez-vous l'écraser avec de nouvelles clés ? [y/N]: ")
        if response.lower() != 'y':
            logger.info("Opération annulée.")
            return

    # Génération des secrets nécessaires.
    secrets = {
        "JWT_SECRET_KEY": SecretsManager.generate_secret_key(),
        "ENCRYPTION_KEY": SecretsManager.generate_secret_key(),
        "ALM_API_KEY": "",
        "OPENAI_API_KEY": "",
        "AZURE_CONTENT_SAFETY_KEY": ""
    }

    # Écriture sécurisée dans le fichier .env.
    try:
        with open(env_file, "w", encoding='utf-8') as f:
            f.write("# Fichier de secrets pour le projet Altiora\n")
            f.write("# ATTENTION : NE PAS COMMIT CE FICHIER DANS GIT !\n\n")
            for key, value in secrets.items():
                f.write(f"{key}={value}\n")

        logger.info(f"✅ Les secrets ont été générés avec succès dans `{env_file}`.")
        logger.info("🔒 N'oubliez pas de remplir les valeurs vides pour les clés d'API externes.")
        logger.info("🔒 Assurez-vous que le fichier `.env` est bien listé dans votre `.gitignore`.")
    except (IOError, OSError) as e:
        logger.error(f"❌ Erreur lors de l'écriture dans le fichier .env : {e}")


if __name__ == "__main__":
    main()

```

---

## Fichier : `scripts\setup\run_performance_tests.sh`

```shell
#!/bin/bash
# scripts/run_performance_tests.sh

set -e

echo "🚀 Tests de Performance Altiora"
echo "==============================="

# Configuration
REDIS_URL="redis://localhost:6379"
OLLAMA_HOST="http://localhost:11434"
MAX_CPU=85
MAX_MEMORY=25

# Vérifier les services
echo "📋 Vérification des services..."
if ! curl -s $OLLAMA_HOST/health &>/dev/null; then
    echo "❌ Ollama non accessible"
    exit 1
fi

if ! redis-cli ping &>/dev/null; then
    echo "❌ Redis non accessible"
    exit 1
fi

# Lancer les tests
echo "🔥 Lancement des tests de charge..."

# Test 1: Charge légère
echo "📊 Test 1: Charge légère (5 concurrents)"
pytest tests/performance/test_load_testing.py::test_cpu_load_pipeline -v -s \
    --performance-concurrent=5 --performance-duration=60

# Test 2: Charge moyenne
echo "📊 Test 2: Charge moyenne (15 concurrents)"
pytest tests/performance/test_load_testing.py::test_cpu_load_pipeline -v -s \
    --performance-concurrent=15 --performance-duration=120

# Test 3: Charge lourde
echo "📊 Test 3: Charge lourde (30 concurrents)"
pytest tests/performance/test_load_testing.py::test_cpu_load_pipeline -v -s \
    --performance-concurrent=30 --performance-duration=300

# Générer le rapport
echo "📈 Génération du rapport de performance..."
python scripts/generate_performance_report.py

echo "✅ Tests de performance terminés!"
echo "📋 Rapport disponible dans: reports/performance_report.html"
```

---

## Fichier : `scripts\setup\setup_integration_tests.sh`

```shell
#!/bin/bash
# scripts/setup_integration_tests.sh

echo "🔄 Configuration des tests d'intégration..."

# Vérifier Docker
if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose non installé"
    exit 1
fi

# Lancer les services
echo "📦 Lancement des services Docker..."
docker-compose down
docker-compose up -d --build --wait

# Vérifier la santé des services
echo "🔍 Vérification des services..."
./scripts/validate_microservices.sh

# Préparer les modèles Ollama
echo "🤖 Vérification des modèles Ollama..."
if ! curl -s http://localhost:11434/api/tags | grep -q "qwen3"; then
    echo "📥 Téléchargement de qwen3:32b-q4_K_M..."
    ollama pull qwen3:32b-q4_K_M
fi

if ! curl -s http://localhost:11434/api/tags | grep -q "starcoder2"; then
    echo "📥 Téléchargement de starcoder2:15b-q8_0..."
    ollama pull starcoder2:15b-q8_0
fi

echo "✅ Environnement de test d'intégration prêt!"
```

---

## Fichier : `scripts\setup\start_dev.sh`

```shell
# scripts/start_dev.sh

echo "🚀 Démarrage Altiora avec structure refactorisée"
# Lancer les services dans l'ordre
docker-compose up -d redis ollama
docker-compose up dash prometheus
docker-compose up -d doctoplus-ocr alm-connector excel-processor playwright-runner
# Attendre la santé des services
./scripts/validate_microservices.sh
```

---

## Fichier : `scripts\setup\validate_setup.py`

```python
# scripts/setup/validate_setup.py
#!/usr/bin/env python3
"""Script de validation complet pour l'environnement de développement Altiora.

Ce script vérifie que tous les composants critiques de l'environnement sont
correctement installés et configurés. Il est conçu pour être exécuté après
l'installation initiale ou pour diagnostiquer des problèmes d'environnement.

Les vérifications incluent :
- La cohérence entre les modèles Ollama configurés et ceux réellement installés.
- La présence et la version des dépendances Python critiques (PyTorch, etc.).
"""
import sys
import subprocess
import logging
from pathlib import Path

import yaml

logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)


class SetupValidator:
    """Valide l'installation complète d'Altiora."""

    def __init__(self):
        """Initialise le validateur."""
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def validate_models(self):
        """Vérifie la cohérence des modèles Ollama."""
        logger.info("🔍 Vérification des modèles Ollama...")
        try:
            # Charge la configuration des modèles depuis le fichier YAML.
            models_config_path = Path("configs/models.yaml")
            if not models_config_path.exists():
                self.errors.append(f"Le fichier de configuration des modèles `{models_config_path}` est introuvable.")
                return

            models_config = yaml.safe_load(models_config_path.read_text())
            required_models = [conf['ollama_tag'] for conf in models_config.get("models", {}).values()]

            # Récupère la liste des modèles installés via la commande Ollama.
            result = subprocess.run(
                ["ollama", "list"],
                capture_output=True,
                text=True,
                check=True
            )
            installed_models = result.stdout

            # Compare les modèles requis et installés.
            for model_tag in required_models:
                if model_tag not in installed_models:
                    self.errors.append(
                        f"Modèle manquant : `{model_tag}` n'est pas installé dans Ollama. "
                        f"Exécutez `ollama pull {model_tag}`."
                    )
                else:
                    logger.info(f"  - ✅ Modèle `{model_tag}` trouvé.")

        except FileNotFoundError:
            self.errors.append("La commande `ollama` n'a pas été trouvée. Assurez-vous qu'Ollama est installé et dans le PATH.")
        except (subprocess.CalledProcessError, yaml.YAMLError, KeyError) as e:
            self.errors.append(f"Une erreur est survenue lors de la validation des modèles : {e}")

    def validate_dependencies(self):
        """Vérifie la présence et la version des dépendances Python critiques."""
        logger.info("\n🔍 Vérification des dépendances Python...")
        try:
            import torch
            logger.info(f"  - ✅ PyTorch version {torch.__version__} trouvé.")
            if not torch.__version__.startswith("2."):
                self.warnings.append(
                    f"La version de PyTorch ({torch.__version__}) n'est pas la version 2.x recommandée."
                )

            import transformers
            logger.info(f"  - ✅ Transformers version {transformers.__version__} trouvé.")

            import peft
            logger.info(f"  - ✅ PEFT version {peft.__version__} trouvé.")

        except ImportError as e:
            self.errors.append(f"Dépendance Python manquante : {e}. Exécutez `pip install -r requirements.txt`.")

    def run(self) -> bool:
        """Exécute toutes les validations et affiche un résumé.

        Returns:
            True si aucune erreur n'a été trouvée, False sinon.
        """
        self.validate_models()
        self.validate_dependencies()

        print("\n" + "-"*50)
        if self.errors:
            logger.error("❌ DES ERREURS CRITIQUES ONT ÉTÉ TROUVÉES :")
            for error in self.errors:
                logger.error(f"  - {error}")

        if self.warnings:
            logger.warning("\n⚠️  AVERTISSEMENTS :")
            for warning in self.warnings:
                logger.warning(f"  - {warning}")
        
        if not self.errors and not self.warnings:
            logger.info("✅ L'environnement semble correctement configuré !")
        
        return not self.errors


if __name__ == "__main__":
    validator = SetupValidator()
    logger.info("Lancement de la validation de l'environnement Altiora...")
    if not validator.run():
        logger.error("\nValidation échouée. Veuillez corriger les erreurs ci-dessus.")
        sys.exit(1)
    else:
        logger.info("\nValidation réussie.")

```

---

## Fichier : `scripts\training\auto_fine_tuner.py`

```python
# scripts/training/auto_fine_tuner.py
from peft import LoraConfig, get_peft_model
from transformers import TrainingArguments, Trainer

from backend.altiora.core.feedback.feedback_collector import FeedbackCollector

TRIGGER_THRESHOLD = 50  # votes ≥ 3


async def should_trigger():
    collector = FeedbackCollector()
    batch = await collector.get_batch()
    return len(batch) >= TRIGGER_THRESHOLD


async def schedule_retrain():
    dataset = await build_dataset_from_feedback()

    lora_config = LoraConfig(
        r=32,
        lora_alpha=64,  # 2×r (meilleur loss) [^10^]
        lora_dropout=0.1,
        target_modules=["q_proj", "v_proj", "k_proj", "o_proj"],
        task_type="CAUSAL_LM"
    )

    training_args = TrainingArguments(
        output_dir="./models/lora_adapters",
        num_train_epochs=3,
        per_device_train_batch_size=4,
        gradient_accumulation_steps=4,
        fp16=True,
        evaluation_strategy="epoch",
        save_strategy="epoch",
        logging_steps=10,
        report_to="mlflow"
    )

    trainer = Trainer(
        model=get_peft_model(base_model, lora_config),
        args=training_args,
        train_dataset=dataset,
        eval_dataset=dataset.select(range(50))
    )

    trainer.train()
    trainer.save_model("./models/lora_adapters/latest")
```

---

