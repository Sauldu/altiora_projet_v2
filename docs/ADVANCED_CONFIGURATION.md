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
