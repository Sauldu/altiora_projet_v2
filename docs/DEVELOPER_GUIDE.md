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
