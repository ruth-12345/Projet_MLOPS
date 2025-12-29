# tests/test_api.py
"""
Tests pour l'API Flask
"""

import pytest
import sys
import os

# Ajouter le chemin parent pour les imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from api.app import app

@pytest.fixture
def client():
    """Créer un client de test Flask"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    """Test de la page d'accueil"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Churn' in response.data

def test_predict_endpoint_valid_data(client):
    """Test de prédiction avec des données valides"""
    data = {
        'tenure': 12,
        'monthly_charges': 65.50,
        'total_charges': 786.00,
        'contract': 'Month-to-month',
        'payment_method': 'Electronic check',
        'internet_service': 'Fiber optic',
        'paperless_billing': 'Yes'
    }
    
    response = client.post('/predict', data=data)
    assert response.status_code == 200

def test_predict_endpoint_missing_data(client):
    """Test de prédiction avec des données manquantes"""
    data = {
        'tenure': 12,
        'monthly_charges': 65.50,
        'paperless_billing': 'Yes'
        # Données manquantes
    }
    
    response = client.post('/predict', data=data)
    # Devrait retourner une erreur ou gérer les données manquantes
    assert response.status_code in [200, 400]

def test_predict_high_churn_risk(client):
    """Test avec un profil à haut risque de churn"""
    data = {
        'tenure': 1,  # Nouveau client
        'monthly_charges': 100.00,  # Frais élevés
        'total_charges': 100.00,
        'contract': 'Month-to-month',  # Contrat mensuel
        'payment_method': 'Electronic check',
        'internet_service': 'Fiber optic',
        'paperless_billing': 'Yes'  # Facturation électronique
    }
    
    response = client.post('/predict', data=data)
    assert response.status_code == 200

def test_predict_low_churn_risk(client):
    """Test avec un profil à faible risque de churn"""
    data = {
        'tenure': 60,  # Client fidèle
        'monthly_charges': 25.00,  # Frais faibles
        'total_charges': 1500.00,
        'contract': 'Two year',  # Contrat long
        'payment_method': 'Bank transfer (automatic)',
        'internet_service': 'DSL',
        'paperless_billing': 'No'  # Facturation papier
    }
    
    response = client.post('/predict', data=data)
    assert response.status_code == 200