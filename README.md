💳 Credit Card Fraud Detection Dashboard

Detect fraudulent credit card transactions in real-time with explainability!

This Streamlit app allows you to upload transaction data, get fraud predictions, and explore insights with SHAP feature importance. The dashboard is designed like a banking monitoring system with metrics cards, high-risk alerts, and interactive visualizations.

📂 Demo Dataset

For GitHub, we provide a sample CSV for testing the app:

File: creditcard_sample.csv (~10,000 rows, <25MB)

Columns: Time, V1–V28, Amount, Class (optional)

⚠️ The full dataset (~143MB) is too large for GitHub. You can download it here:
Full Credit Card Dataset on Kaggle

💡 You can test the app with the demo dataset, or download the full dataset to run larger analyses.

🚀 Features

Upload CSV and get predictions: Fraud (1) or Legit (0)

Dashboard metrics: Total Transactions, Detected Frauds, Average Fraud Probability

High-risk transactions: Probability > 0.8

SHAP explainability: Feature importance visualization for top transactions

Download results: Export predictions as CSV

📝 How to Use

Install dependencies

pip install -r requirements.txt


Run the Streamlit app

streamlit run app.py


Upload your CSV file

Use the demo dataset (creditcard_sample.csv) or your own CSV

The Overview section will display:

Total Transactions

Detected Frauds

Average Fraud Probability

Transaction Explainability

Click on Transaction Explainability

Enter any Transaction Row Number (0 to total rows)

View the prediction: Fraud or Legit and the Fraud Probability

Explore why the transaction is flagged in the High-Risk Transactions section

SHAP Feature Importance

Visualize the most important features contributing to fraud predictions

Helps understand which patterns increase fraud risk

Download Results

Export all predictions and probabilities as a CSV for further analysis

✅ This app is interactive, polished, and ready to use, giving both real-time predictions and explainable insights for credit card fraud detection.

All links in this README, including the Kaggle dataset link, are clickable on GitHub.

If you want, I can also add visuals and icons for each section to make it look more like a professional banking dashboard guide.

Do you want me to do that next?
