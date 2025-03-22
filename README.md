# 🏦 Loan Approval Prediction App

A user-friendly Streamlit web application to predict whether a customer is likely to default on a loan using historical financial data.

## 🚀 Features
- Interactive UI with sidebar input
- Adjustable threshold (named “Risk Tolerance Level”)
- Model built using Random Forest (trained on imbalanced dataset)
- Scaled with StandardScaler
- Provides explanation for decision (approve, further investigation, or reject)

## 📊 Input Features
- Age, Income, Credit Score, Loan Amount, etc.

## 🔍 Model
- Random Forest Classifier
- 10 selected features based on importance
- Trained and validated using cross-validation, ROC, PR curves

## 🧪 How to Run
```bash
streamlit run app.py
