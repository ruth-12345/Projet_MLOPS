# 🔮 Projet MLOps/DevOps - Prédiction de Churn Télécoms

## 📋 Description

Application de prédiction de churn (résiliation) dans l'industrie des télécommunications, combinant MLOps et DevOps avec un pipeline CI/CD automatisé sur AWS.

## 🎯 Objectifs du Projet

- ✅ Construire un modèle ML de prédiction de churn
- ✅ Créer une API REST avec Flask
- ✅ Dockeriser l'application
- ✅ Mettre en place un pipeline CI/CD
- ✅ Déployer sur AWS

## 🏗️ Architecture

```
DEVOPS-MLOPS-AWS-STUDENT/
├── .github/workflows/     # Pipeline CI/CD
│   └── ci.yml
├── api/                   # Application Flask
│   ├── __init__.py
│   ├── app.py            # API principale
│   ├── model_loader.py   # Chargement du modèle
│   └── templates/
│       └── index.html    # Interface web
├── docker/               # Configuration Docker
│   └── Dockerfile
├── model/                # Modèles ML sauvegardés
├── notebooks/            # Jupyter notebooks
├── tests/                # Tests unitaires
│   └── test_api.py
├── requirements.txt      # Dépendances Python
└── README.md
```

## 🚀 Installation Locale

### Prérequis

- Python 3.11+
- pip
- Docker (optionnel)

### Étapes

```bash
# Cloner le repository
git clone <votre-repo>
cd DEVOPS-MLOPS-AWS-STUDENT

# Créer un environnement virtuel
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

# Installer les dépendances
pip install -r requirements.txt

# Lancer l'application
python api/app.py
```

Ouvrir: `http://localhost:5000`

## 📊 Variables de Prédiction

Le modèle utilise **7 variables** pour prédire le churn :

| Variable | Description | Type |
|----------|-------------|------|
| `tenure` | Ancienneté (mois) | Numérique |
| `MonthlyCharges` | Frais mensuels (€) | Numérique |
| `TotalCharges` | Frais totaux (€) | Numérique |
| `Contract` | Type de contrat | Catégorielle |
| `PaymentMethod` | Méthode de paiement | Catégorielle |
| `InternetService` | Service internet | Catégorielle |
| `PaperlessBilling` | Facturation électronique | Catégorielle |

## 🧪 Tests

```bash
# Lancer tous les tests
pytest tests/ -v

# Test de couverture
pytest --cov=api tests/
```

## 🐳 Docker

```bash
# Construire l'image
docker build -f docker/Dockerfile -t churn-prediction .

# Lancer le container
docker run -p 5000:5000 churn-prediction

# Avec docker-compose (si configuré)
docker-compose up
```

## 🔄 Pipeline CI/CD

Le pipeline GitHub Actions s'exécute automatiquement sur chaque push et comprend :

1. **Test** : Exécution des tests unitaires
2. **Build** : Construction de l'image Docker
3. **Deploy** : Déploiement sur AWS (main branch uniquement)

## ☁️ Déploiement AWS

### Services AWS utilisés

- **EC2** : Hébergement de l'application
- **CloudWatch** : Monitoring

### Commandes de déploiement

```bash
# À venir - Configuration AWS
```

## 📁 Données

Le dataset contient des informations sur les clients télécoms :
- 7043 clients
- 21 variables
- Variable cible : `Churn` (Oui/Non)

## 🛠️ Technologies Utilisées

- **Backend** : Flask, Python 3.11
- **ML** : scikit-learn, pandas, numpy
- **DevOps** : Docker, GitHub Actions
- **Cloud** : AWS (EC2)
- **Tests** : pytest

## 📈 Métriques du Modèle

- **Accuracy** : À calculer
- **Precision** : À calculer
- **Recall** : À calculer
- **F1-Score** : À calculer

## 👥 Auteur

Votre Nom - devops-mlops-aws-student-project

## 📝 Licence

Ce projet est à usage éducatif uniquement.

## 🔗 Liens Utiles

- [Documentation Flask](https://places-sneeze-rvg.craft.me/0LjhmCAekzVH3Y)
- [Documentation scikit-learn](https://scikit-learn.org/)
- [AWS Learner Lab](https://us-east-1.console.aws.amazon.com/ec2/home?region=us-east-1#Instances:)
- [AWS Learner Lab][Le lien vers l'application fonctionnelle sur AWS](http://3.223.78.97:5000)
- [Le lien vers l'application Flask fonctionnel en local](http://localhost:5000)
- [GitHub Actions](https://github.com/ruth-12345/Projet_MLOPS)