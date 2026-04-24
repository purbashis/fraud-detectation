# 🛡️ Fraud Detection System

An end-to-end Machine Learning pipeline and interactive web application for detecting fraudulent financial transactions.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://purbashis-fraud-detectation.streamlit.app/)

## 📖 Overview
This project involves building a robust machine learning model to classify financial transactions as fraudulent or legitimate. The pipeline includes data preprocessing, feature engineering, model training, and a deployed Streamlit web interface for real-time predictions.

## 🛠️ Tech Stack
- **Data Processing & Analysis:** Pandas, NumPy
- **Machine Learning:** Scikit-Learn (`LogisticRegression`, `ColumnTransformer`, `Pipeline`)
- **Visualization:** Plotly, Seaborn, Matplotlib
- **Web Application:** Streamlit
- **Deployment:** Streamlit Community Cloud
- **CI/CD:** GitHub Actions

## 🧠 Model Pipeline
The core ML pipeline (`fraud_detection_pipeline.pkl`) uses a `LogisticRegression` model with balanced class weights to handle the heavily imbalanced dataset. 
It processes the following features:
- **Categorical:** `type` (One-Hot Encoded)
- **Numerical:** `amount`, `oldbalanceOrg`, `newbalanceOrig`, `oldbalanceDest`, `newbalanceDest` (Standard Scaled)

## 🚀 How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/purbashis/fraud-detectation.git
cd fraud-detectation
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit App
```bash
streamlit run fraud_detection.py
```
*The app will automatically open in your default web browser at `http://localhost:8501`.*

## 📁 Project Structure
- `fd.ipynb` / `fd.py` - Exploratory Data Analysis (EDA) and Model Training pipeline.
- `fraud_detection.py` - The Streamlit frontend application.
- `fraud_detection_pipeline.pkl` - The exported, trained ML pipeline.
- `requirements.txt` - Dependencies required to run the project.
- `.github/workflows/` - GitHub Actions for continuous integration.
