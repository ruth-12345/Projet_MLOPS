from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# Charger le modèle (à adapter selon ton modèle)
# model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Récupérer les données du formulaire
        tenure = int(request.form['tenure'])
        monthly_charges = float(request.form['monthly_charges'])
        total_charges = float(request.form['total_charges'])
        contract = request.form['contract']
        payment_method = request.form['payment_method']
        internet_service = request.form['internet_service']
        paperless_billing = request.form['paperless_billing']
        
        # Créer un dictionnaire avec les données
        input_data = {
            'tenure': tenure,
            'MonthlyCharges': monthly_charges,
            'TotalCharges': total_charges,
            'Contract': contract,
            'PaymentMethod': payment_method,
            'InternetService': internet_service,
            'PaperlessBilling': paperless_billing
        }
        
        # Convertir en DataFrame
        input_df = pd.DataFrame([input_data])
        
        # Faire la prédiction (décommenter quand tu auras ton modèle)
        # prediction = model.predict(input_df)
        # proba = model.predict_proba(input_df)
        
        # Simulation pour tester l'interface
        prediction = 1 if monthly_charges > 70 and contract == 'Month-to-month' else 0
        proba = 0.75 if prediction == 1 else 0.25
        
        result = {
            'churn': 'Oui' if prediction == 1 else 'Non',
            'probabilite': f"{proba * 100:.1f}%",
            'risque': 'Élevé' if proba > 0.6 else 'Moyen' if proba > 0.3 else 'Faible'
        }
        
        return render_template('index.html', prediction=result, input_data=input_data)
    
    except Exception as e:
        return render_template('index.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)