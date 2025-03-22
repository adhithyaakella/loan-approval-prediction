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

## 🔗 Model & Assets Download

Due to file size limitations on GitHub, the trained model and scaler are hosted on Google Drive.

- [Download Trained Model (random_forest_model.pkl)]([https://drive.google.com/file/d/your_model_file_id/view?usp=sharing](https://drive.google.com/file/d/1mF9fyzcjGbDeSJr_LCJP59Saot6xdG-u/view?usp=drive_link))
- [Download Scaler (scaler.pkl)]([https://drive.google.com/file/d/your_scaler_file_id/view?usp=sharing](https://drive.google.com/file/d/1Mz6oP1HhwcKUll588h8Q9K48dQNxkduS/view?usp=drive_link))

> Please download these files and place them in the project root directory before running `app.py`.

## 🧪 How to Run
```bash
streamlit run app.py
