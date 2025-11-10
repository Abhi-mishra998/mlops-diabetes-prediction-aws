#!/usr/bin/env python3
# train.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset (replace with your local or Kaggle path)
df = pd.read_csv("/app/data/diabetes.csv")

print("✅ Columns:", df.columns.tolist())

# Prepare data
X = df[[
    "Pregnancies", "Glucose", "BloodPressure",
    "SkinThickness", "Insulin", "BMI",
    "DiabetesPedigreeFunction", "Age"
]]
y = df["Outcome"]

# Split the data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "diabetes_model.pkl")
print("✅ Model saved as diabetes_model.pkl")

