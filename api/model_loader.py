# api/model_loader.py
"""
Module pour charger le modèle ML et les encodeurs
"""

import pickle
import os
import pandas as pd
from sklearn.preprocessing import LabelEncoder

class ModelLoader:
    """Classe pour charger et utiliser le modèle de prédiction"""
    
    def __init__(self, model_path='model/churn_model.pkl', encoders_path='model/encoders.pkl'):
        """
        Initialise le chargeur de modèle
        
        Args:
            model_path: Chemin vers le fichier du modèle
            encoders_path: Chemin vers les encodeurs
        """
        self.model_path = model_path
        self.encoders_path = encoders_path
        self.model = None
        self.encoders = None
        
    def load_model(self):
        """Charge le modèle ML depuis le fichier pickle"""
        try:
            if os.path.exists(self.model_path):
                with open(self.model_path, 'rb') as f:
                    self.model = pickle.load(f)
                print(f" Modèle chargé depuis {self.model_path}")
                return True
            else:
                print(f" Fichier modèle non trouvé: {self.model_path}")
                return False
        except Exception as e:
            print(f" Erreur lors du chargement du modèle: {e}")
            return False
    
    def load_encoders(self):
        """Charge les encodeurs pour les variables catégorielles"""
        try:
            if os.path.exists(self.encoders_path):
                with open(self.encoders_path, 'rb') as f:
                    self.encoders = pickle.load(f)
                print(f" Encodeurs chargés depuis {self.encoders_path}")
                return True
            else:
                print(f" Fichier encodeurs non trouvé: {self.encoders_path}")
                return False
        except Exception as e:
            print(f" Erreur lors du chargement des encodeurs: {e}")
            return False
    
    def preprocess_input(self, input_data):
        """
        Prétraite les données d'entrée
        
        Args:
            input_data: Dictionnaire avec les données du client
            
        Returns:
            DataFrame prétraité prêt pour la prédiction
        """
        # Créer un DataFrame
        df = pd.DataFrame([input_data])
        
        # Encoder les variables catégorielles si les encodeurs sont chargés
        if self.encoders:
            categorical_cols = ['Contract', 'PaymentMethod', 'InternetService', 'Paper_lessBilling']
            for col in categorical_cols:
                if col in df.columns and col in self.encoders:
                    df[col] = self.encoders[col].transform(df[col])
        
        return df
    
    def predict(self, input_data):
        """
        Fait une prédiction
        
        Args:
            input_data: Dictionnaire avec les données du client
            
        Returns:
            Tuple (prédiction, probabilité)
        """
        if self.model is None:
            raise ValueError("Le modèle n'est pas chargé. Appelez load_model() d'abord.")
        
        # Prétraiter les données
        df = self.preprocess_input(input_data)
        
        # Faire la prédiction
        prediction = self.model.predict(df)[0]
        proba = self.model.predict_proba(df)[0]
        
        # Retourner la probabilité de churn (classe 1)
        churn_proba = proba[1] if len(proba) > 1 else proba[0]
        
        return int(prediction), float(churn_proba)
    
    def is_loaded(self):
        """Vérifie si le modèle est chargé"""
        return self.model is not None


# Instance globale du modèle (singleton)
model_loader = ModelLoader()