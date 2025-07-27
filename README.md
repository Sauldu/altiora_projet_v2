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