import streamlit as st
import pandas as pd
import joblib
import shap
import matplotlib.pyplot as plt

# Load the trained model
model = joblib.load("model/xgb_churn_model.pkl")

# Load test data
data = pd.read_csv("data/data.csv")

# Drop identifier columns
if "customerID" in data.columns:
    data = data.drop("customerID", axis=1)

# Save target if present
if "Churn" in data.columns:
    data = data.drop("Churn", axis=1)

# One-hot encode
X_encoded = pd.get_dummies(data)

# Align columns with model's training features
model_features = model.get_booster().feature_names
X_encoded = X_encoded.reindex(columns=model_features, fill_value=0)

# SHAP explainer
explainer = shap.TreeExplainer(model)

# Streamlit UI
st.title("📊 Customer Churn Risk Dashboard")

customer_id = st.selectbox("Select customer index", X_encoded.index)

if st.button("Predict and Explain"):
    customer = X_encoded.loc[[customer_id]]

    prediction = model.predict(customer)[0]
    probability = model.predict_proba(customer)[0][1]

    st.markdown(f"### Prediction: {'🟥 Churn' if prediction == 1 else '🟩 Not Churn'}")
    st.markdown(f"**Probability of Churn:** {probability * 100:.2f}%")

    # SHAP values
    shap_values = explainer(customer)

    # Waterfall plot instead of force_plot
    st.markdown("### 📌 Feature Attribution (SHAP - Waterfall)")
    fig1, ax1 = plt.subplots(figsize=(8, 6))
    shap.plots.waterfall(shap_values[0], show=False)
    st.pyplot(fig1)


    # Summary plot
    st.markdown("### 🔍 Feature Impact Summary")
    fig2 = plt.figure()
    shap.summary_plot(shap_values, customer, plot_type="bar", show=False)
    st.pyplot(fig2)
