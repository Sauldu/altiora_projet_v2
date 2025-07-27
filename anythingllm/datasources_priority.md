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
