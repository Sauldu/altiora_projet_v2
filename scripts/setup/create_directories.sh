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