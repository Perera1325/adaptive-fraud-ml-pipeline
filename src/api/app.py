from fastapi import FastAPI
import pickle
import numpy as np
import os

app = FastAPI()

# Load model safely
model_path = os.path.join("src", "models", "fraud_model.pkl")

with open(model_path, "rb") as f:
    model = pickle.load(f)


# Root endpoint
@app.get("/")
def home():
    return {"message": "Fraud Detection API is running"}


# Prediction endpoint
@app.post("/predict")
def predict(data: dict):
    """
    Expected input:
    {
        "amount": 5000,
        "text_length": 200
    }
    """

    # Extract inputs
    amount = data.get("amount", 0)
    text_length = data.get("text_length", 0)

    # IMPORTANT: match model feature size (101 features)
    features = np.zeros((1, 101))

    features[0][0] = amount
    features[0][1] = text_length

    # Prediction
    prediction = model.predict(features)[0]

    return {
        "fraud_prediction": int(prediction),
        "message": "Fraud detected" if prediction == 1 else "Not fraud"
    }