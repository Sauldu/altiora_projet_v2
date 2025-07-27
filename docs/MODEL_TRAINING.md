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
