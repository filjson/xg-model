# xg-model

# Expected Goals (xG) Model & Streamlit App

This project builds an **Expected Goals (xG)** model using football shot data and provides an **interactive Streamlit web app** where users can input shot characteristics to predict the probability of scoring.

## Project Overview
The goal of this project is to demonstrate a complete data science workflow used in football analytics:

- Data cleaning & feature engineering  
- Model training (XGBoost)  
- Predicting xG for individual shots  
- Deploying an interactive Streamlit application  

The Streamlit app lets users test different shot situations by adjusting:
- Shot distance  
- Shot angle  
- Pressure  
- One-on-one situations  
- Body part  
- Shot technique  
- Player position  
- Match period  

## Live Streamlit App
 https://xg-model.streamlit.app/

## Repository Structure
events_all.parquet
xg-model/
│
├── xg_app.py # Streamlit application

├── events_all.parquet # Some data
├── xg_model.pkl # Trained machine learning model
├── Expected Goals (xG) model.ipynb # Full notebook for data prep & training
├── requirements.txt # Python dependencies for deployment
└── README.md # Project documentation (this file)

## How to Run Locally
1. Install requirements:
pip install -r requirements.txt

2. Run the Streamlit app:
streamlit run xg_app.py

3. The app will open in your browser at:
http://localhost:8501

## Model
The xG model is trained using features such as:
- Shot angle  
- Shot distance  
- Body part  
- Technique  
- Defensive pressure  
- One-on-one situations  
- Positional context  
- Match period  

The model outputs a probability between **0 and 1**, representing the chance of the shot becoming a goal.

## Technologies Used
- **Python**
- **Streamlit**
- **Pandas**
- **XGBoost**
- **Scikit-learn**
- **Joblib**

## Author
Filip
