import streamlit as st
import pandas as pd
import joblib
import shap
import matplotlib.pyplot as plt
import io

# --- Page Config (first line) ---
st.set_page_config(page_title="💳 Credit Card Fraud Detection", layout="wide")

# --- Load Model ---
@st.cache_resource
def load_model():
    return joblib.load("fraud_xgb_model.pkl")

model = load_model()

# --- Title ---
st.title("💳 Credit Card Fraud Detection Dashboard")
st.write("Upload transaction data and get fraud predictions with explainability.")

# --- Upload CSV File ---
uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])
if uploaded_file:
    data = pd.read_csv(uploaded_file)

    # --- Preprocess Data ---
    X = data.drop(columns=['Class'], errors='ignore')
    feature_order = ['Time','V1','V2','V3','V4','V5','V6','V7','V8','V9',
                     'V10','V11','V12','V13','V14','V15','V16','V17','V18',
                     'V19','V20','V21','V22','V23','V24','V25','V26','V27',
                     'V28','Amount']
    X = X[feature_order]

    # --- Predictions ---
    preds = model.predict(X)
    probs = model.predict_proba(X)[:, 1]
    data["Fraud_Prediction"] = preds
    data["Fraud_Probability"] = probs
    data["Fraud_Prediction_Label"] = data["Fraud_Prediction"].map({0: "Legit", 1: "Fraud"})

    # --- Metrics Cards ---
    total_tx = len(data)
    fraud_count = data["Fraud_Prediction"].sum()
    avg_prob = data["Fraud_Probability"].mean()

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Transactions", total_tx, delta_color="normal")  # Blue
    col2.metric("Detected Frauds", fraud_count, delta_color="inverse")  # Red
    col3.metric("Average Fraud Probability", f"{avg_prob:.2f}", delta_color="normal")  # Blue

    # --- Tabs Layout ---
    tab1, tab2 = st.tabs(["📊 Overview", "🔍 Transaction Explainability"])

    # --- Tab 1: Overview ---
    with tab1:
        st.subheader("📂 Uploaded Data Preview")
        st.dataframe(data.head(10).style.applymap(
            lambda val: 'color: red; font-weight: bold' if val=="Fraud" else 'color: green; font-weight: bold',
            subset=['Fraud_Prediction_Label']
        ))

        st.subheader("⚠️ High-Risk Transactions (Probability > 0.8)")
        high_risk = data[data["Fraud_Probability"] > 0.8]
        st.dataframe(high_risk.style.applymap(
            lambda val: 'color: red; font-weight: bold' if val=="Fraud" else 'color: green; font-weight: bold',
            subset=['Fraud_Prediction_Label']
        ))

        st.subheader("📈 Fraud Probability Distribution (Top 50 Transactions)")
        st.bar_chart(
            data.sort_values("Fraud_Probability", ascending=False)["Fraud_Probability"].head(50)
        )

        # --- SHAP Feature Importance ---
        st.subheader("📊 SHAP Feature Importance (Sample 100 rows)")
        sample_data = X.sample(min(100, len(X)), random_state=42)
        explainer = shap.TreeExplainer(model)
        shap_values = explainer.shap_values(sample_data)

        fig, ax = plt.subplots()
        shap.summary_plot(shap_values, sample_data, plot_type="bar", show=False)
        st.pyplot(fig)

        # --- SHAP Download ---
        buf = io.BytesIO()
        fig.savefig(buf, format="png")
        buf.seek(0)
        st.download_button("📥 Download SHAP Summary Plot", data=buf, file_name="shap_summary.png", mime="image/png")

    # --- Tab 2: Transaction Explainability ---
    with tab2:
        st.subheader("Select Transaction Row")
        transaction_index = st.number_input(
            f"Enter Transaction Row Number (0 to {len(X)-1})",
            min_value=0, max_value=len(X)-1, value=0, step=1
        )

        selected_transaction = X.iloc[[transaction_index]]
        selected_pred = data["Fraud_Prediction"].iloc[transaction_index]
        selected_prob = data["Fraud_Probability"].iloc[transaction_index]
        selected_label = "Fraud" if selected_pred == 1 else "Legit"

        st.write(f"**Prediction:** {selected_label} | **Fraud Probability:** {selected_prob:.2f}")

        # SHAP force plot
        shap_values_single = explainer.shap_values(selected_transaction)
        fig2, ax2 = plt.subplots()
        shap.force_plot(
            explainer.expected_value,
            shap_values_single,
            selected_transaction,
            matplotlib=True,
            show=False
        )
        st.pyplot(fig2)

    # --- Download Predictions ---
    st.subheader("📥 Download Results")
    csv = data.to_csv(index=False).encode('utf-8')
    st.download_button("Download CSV with Predictions", data=csv, file_name="fraud_predictions.csv", mime="text/csv")
