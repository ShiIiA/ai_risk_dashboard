# -*- coding: utf-8 -*-
"""app.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1UJWr_jz3WkLX17-lJEs2wu60Ch4zlQq8
"""

import streamlit as st
import plotly.express as px
from risk_model import calculate_risk_score

# Streamlit UI
st.set_page_config(page_title="AI Radiology Risk Assessment", layout="centered")
st.title("🩻 AI Radiology Risk Assessment Dashboard")

st.markdown("### Adjust AI Model Parameters to Assess Risk")

# User Inputs (Sliders)
misclass = st.slider("Misclassification Rate (0-1)", 0.0, 1.0, 0.2, step=0.01)
dataset_bias = st.slider("Dataset Bias (0-1)", 0.0, 1.0, 0.3, step=0.01)
explainability = st.slider("Explainability Score (0-1)", 0.0, 1.0, 0.8, step=0.01)
fairness = st.slider("Fairness Score (0-1)", 0.0, 1.0, 0.7, step=0.01)

# Calculate risk
risk_score = calculate_risk_score(misclass, dataset_bias, explainability, fairness)

# Determine Risk Level
if risk_score <= 30:
    risk_category = "Low Risk 🟢"
    color = "green"
elif risk_score <= 60:
    risk_category = "Medium Risk 🟡"
    color = "orange"
else:
    risk_category = "High Risk 🔴"
    color = "red"

# Display Results
st.metric(label="AI Risk Score", value=f"{risk_score}/100")
st.subheader(f"Risk Level: {risk_category}")

# Visualization of Contributions
risk_factors = ["Misclassification", "Dataset Bias", "Explainability", "Fairness"]
contributions = [misclass, dataset_bias, 1 - explainability, 1 - fairness]

fig = px.bar(
    x=risk_factors,
    y=contributions,
    labels={"x": "Factor", "y": "Risk Contribution"},
    title="Contribution of Each Factor to Risk Score",
    color=risk_factors
)
st.plotly_chart(fig)