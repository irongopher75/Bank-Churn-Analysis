```markdown
# 📊 BANK_CHURN_ANALYSIS

A complete machine learning solution to predict customer churn in a banking context. Built using **XGBoost**, **Streamlit**, and **SHAP**, this dashboard helps visualize churn predictions and explain them with interpretable machine learning techniques.

---

## 🗂️ Project Structure

```
BANK_CHURN_ANALYSIS/
│
├── 📁 data/                   # Raw and processed datasets
│   ├── data.csv
│   ├── encoded_data.csv
│   └── shap_values.csv
│
├── 📁 notebooks/             # Jupyter notebooks
│   └── 01_EDA.ipynb
│
├── 📁 models/                # Trained models and encoders
│   ├── xgb_churn_model.pkl
│   ├── xgb_bank_churn_model.json
│   └── encoder.pkl
│
├── 📁 app/                   # Streamlit or Flask app
│   └── app.py
│
├── 📁 config/ (optional)     # Any config or schema files
│
├── .gitignore
├── requirements.txt
└── README.md

```

---

## 🚀 Getting Started

### 🔧 Requirements

Install required packages:

```bash
pip install streamlit pandas joblib shap xgboost matplotlib
```

---

### ▶️ Running the App

1. **Clone the Repository:**

```bash
git clone https://github.com/irongopher75/BANK_CHURN_ANALYSIS.git
cd BANK_CHURN_ANALYSIS
```

2. **Run the Streamlit App:**

```bash
streamlit run app.py
```

3. **Visit in Browser:**
```
http://localhost:8501
```

---

## 📌 Features

- Predicts **customer churn** using an XGBoost model.
- Displays **churn probability** with emoji-coded feedback.
- Interactive **SHAP waterfall plot** for local explanation.
- SHAP **summary bar plot** to understand feature impact.

---

## 📊 How It Works

1. Loads and preprocesses `data/data.csv`.
2. Drops unnecessary columns (`customerID`, `Churn`).
3. Performs one-hot encoding and aligns features with model.
4. Predicts churn probability and explains prediction using SHAP.
5. Visualizes SHAP values with:
   - 📉 Waterfall plot (per-customer)
   - 📊 Summary plot (feature impact)

---

## 📸 Example Screenshots

*(Add screenshots of the Streamlit dashboard and SHAP plots here)*

---

## ✅ Model Info

- **Model:** XGBoost Classifier
- **Trained on:** Processed banking churn dataset
- **File:** `xgb_churn_model.pkl`

---

## 📜 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

---

## 🙋‍♂️ Author

**Vishnu Panicker**  
GitHub: [@irongopher75](https://github.com/irongopher75)

---

## 💡 Ideas for Future Improvements

- Allow users to upload their own CSVs.
- Add pre-processing pipeline to app.
- Deploy online using Streamlit Cloud or Hugging Face Spaces.

```
