# main.py
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import os

app = FastAPI(title="Diabetes Prediction API")

MODEL_PATH = "diabetes_model.pkl"
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError("❌ Model file not found! Train it first using train.py")

model = joblib.load(MODEL_PATH)

class DiabetesInput(BaseModel):
    Pregnancies: int
    Glucose: float
    BloodPressure: float
    SkinThickness: float
    Insulin: float
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int

@app.get("/")
def read_root():
    return {"message": "Diabetes Prediction API is live 🎯"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/predict")
def predict(data: DiabetesInput):
    input_data = np.array([[
        data.Pregnancies,
        data.Glucose,
        data.BloodPressure,
        data.SkinThickness,
        data.Insulin,
        data.BMI,
        data.DiabetesPedigreeFunction,
        data.Age
    ]])
    prediction = model.predict(input_data)[0]
    return {"diabetic": bool(prediction)}

