import streamlit as st
import numpy as np
import joblib

# Load the model and scaler
model = joblib.load("random_forest_model.pkl")
scaler = joblib.load("scaler.pkl")

st.set_page_config(page_title="Loan Approval Prediction", layout="wide")
st.title("🏦 Loan Approval Prediction App")
st.markdown("Predict whether a customer is likely to **default on a loan** based on their financial history.")

# Layout: Two columns for input
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", 18, 75, 30)
    income = st.number_input("Annual Income ($)", 10000, 200000, 50000, step=1000)
    loan_amount = st.number_input("Loan Amount ($)", 5000, 300000, 50000, step=1000)
    credit_score = st.number_input("Credit Score", 300, 850, 700)
    months_employed = st.slider("Months Employed", 0, 120, 24)

with col2:
    num_credit_lines = st.selectbox("Number of Credit Lines", list(range(1, 11)))
    interest_rate = st.slider("Interest Rate (%)", 1, 30, 10)
    dti_ratio = st.slider("Debt-to-Income Ratio", 0.0, 1.0, 0.3)
    has_cosigner = st.radio("Has Co-Signer?", ["Yes", "No"])
    employment_unemployed = st.radio("Employment Status", ["Employed", "Unemployed"])

# Convert categorical to numeric
has_cosigner = 1 if has_cosigner == "Yes" else 0
employment_unemployed = 1 if employment_unemployed == "Unemployed" else 0

# Optional threshold slider
threshold = st.slider("🔧 Risk Tolerance Level", 0.0, 1.0, 0.5, step=0.01)

# Input data formatting
input_data = np.array([[age, income, loan_amount, credit_score, months_employed,
                        num_credit_lines, interest_rate, dti_ratio,
                        has_cosigner, employment_unemployed]])

# Scale and predict
input_scaled = scaler.transform(input_data)
probability = model.predict_proba(input_scaled)[0][1]
predicted_class = int(probability > threshold)

# Prediction display
st.markdown("### 🔍 Prediction Result:")

if predicted_class == 0:
    st.success(f"✅ **Loan Approved**")
    st.info("The customer shows a low risk of default based on the provided information.")
elif 0.4 < probability < 0.6:
    st.warning("⚠️ **Needs Further Review**")
    st.info("This case lies in a borderline zone. Consider reviewing additional documents before approval.")
else:
    st.error("❌ **Loan Denied**")
    st.info("The customer shows a high risk of default. Loan should not be approved.")

st.markdown(f"**Probability of Default:** `{probability:.2f}`  \n**Decision Threshold:** `{threshold}`")
