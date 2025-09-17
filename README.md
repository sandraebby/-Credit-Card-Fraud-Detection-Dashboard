# 💳 Credit Card Fraud Detection Dashboard

**Detect fraudulent credit card transactions in real-time with explainability!**  

This Streamlit app allows you to upload transaction data, get fraud predictions, and explore insights with SHAP feature importance. The dashboard is designed like a banking monitoring system with metrics cards, high-risk alerts, and interactive visualizations.

---

## 📂 Demo Dataset

For GitHub, we provide a **sample CSV** for testing the app:

- File: `creditcard_sample.csv` (~10,000 rows, <25MB)  
- Columns: `Time, V1–V28, Amount, Class` (optional)  

⚠️ The full dataset (~143MB) is too large for GitHub. You can download it here: [Full Credit Card Dataset](YOUR_DRIVE_LINK_HERE)

---

## 🚀 Features

- **Upload CSV and get predictions:** Fraud (`1`) or Legit (`0`)  
- **Dashboard metrics:** Total Transactions, Detected Frauds, Average Fraud Probability  
- **High-risk transactions:** Probability > 0.8  
- **SHAP explainability:** Feature importance visualization for top transactions  
- **Download results:** Export predictions as CSV  

---

## 📝 How to Use

1. Install dependencies:

```bash
pip install -r requirements.txt
