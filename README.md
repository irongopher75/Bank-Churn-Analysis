# 📊 BANK_CHURN_ANALYSIS

A complete machine learning solution to predict customer churn in a banking context. Built using **XGBoost**, **Streamlit**, and **SHAP**, this dashboard helps visualize churn predictions and explain them with interpretable machine learning techniques.

---

## 🗂️ Project Structure

BANK_CHURN_ANALYSIS/
│
├── 📁 data/ # Raw and SHAP datasets
│ ├── data.csv
│ └── shap_values.csv
│
├── 📁 notebooks/ # Jupyter notebooks
│ └── 01_EDA.ipynb
│
├── app.py # Streamlit dashboard
├── encoder.pkl # (optional) Encoder if used
├── xgb_bank_churn_model.json # Model in JSON format
├── xgb_churn_model.pkl # Trained XGBoost model
├── requirements.txt # Python dependencies
└── README.md # This file


---

## 🚀 Getting Started

### 🔧 Requirements

Install required packages:

```bash
pip install streamlit pandas joblib shap xgboost matplotlib
▶️ Running the App
Clone the Repository:
git clone https://github.com/irongopher75/BANK_CHURN_ANALYSIS.git
cd BANK_CHURN_ANALYSIS
Run the Streamlit App:
streamlit run app.py
Visit in Browser:
http://localhost:8501
📌 Features

Predicts customer churn using an XGBoost model.
Displays churn probability with emoji-coded feedback.
Interactive SHAP waterfall plot for local explanation.
SHAP summary bar plot to understand feature impact.
📊 How It Works

Loads and preprocesses data/data.csv.
Drops unnecessary columns (customerID, Churn).
Performs one-hot encoding and aligns features with model.
Predicts churn probability and explains prediction using SHAP.
Visualizes SHAP values with:
📉 Waterfall plot (per-customer)
📊 Summary plot (feature impact)
📸 Example Screenshots

(Add screenshots of the Streamlit dashboard and SHAP plots here if desired)

✅ Model Info

Model: XGBoost Classifier
Trained on: Processed banking churn dataset
File: xgb_churn_model.pkl
📜 License

This project is licensed under the MIT License.

🙋‍♂️ Author

Vishnu Panicker
GitHub: @irongopher75

💡 Future Improvements

Allow users to upload their own CSVs.
Add a full preprocessing pipeline.
Deploy online via Streamlit Cloud or Hugging Face Spaces.

Let me know if you also want me to generate a proper `.gitignore` or `requirements.txt`.