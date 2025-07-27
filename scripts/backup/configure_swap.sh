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