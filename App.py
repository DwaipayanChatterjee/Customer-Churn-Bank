import streamlit as st
import pandas as pd
import numpy as np
import joblib


def main():
    st.title("Bank Customers Churn")
    html_temp = """
        <div style="background:#025246 ;padding:10px">
        <h2 style="color:white;text-align:center;">Bank Churn Prediction ML App </h2>
        </div>
        """
    st.markdown(html_temp, unsafe_allow_html = True)

    CustomerId = st.number_input("CustomerId", 0)
    CreditScore = st.number_input("CreditScore", 0)
    Age = st.slider("Age", 10, 100)
    Tenure = st.selectbox("Tenure", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    Balance = st.number_input("Balance", 0)
    NumOfProducts = st.selectbox("NumOfProducts", [1, 2, 3, 4])
    HasChckng = st.selectbox("HasChckng", [0, 1])
    IsActiveMember = st.selectbox("IsActiveMember", [0, 1])
    EstimatedSalary = st.number_input("EstimatedSalary", 0)
    Geography = st.selectbox("Geography", ["Central", "East", "West"])
    Gender = st.selectbox("Gender", ["Male", "Female"])

    if st.button("Predict"):
        row = np.array([CreditScore, Age, Tenure, Balance, NumOfProducts, HasChckng, IsActiveMember, EstimatedSalary, Geography, Gender])
        X = pd.DataFrame([row], columns = features)
        predictions = None
        threshold = 0.5

        cat_model = joblib.load("CAT_Model.pkl")
        predictions = cat_model.predict(X)[:, 1]

        if predictions > threshold:
            st.success(f"Predicted Probability : {output}. \nThis customer is likely to churn :thumbsdown:")
        else:
            st.success(f"Predicted Probability : {output}. \nThis customer isn't likely to churn :thumbsup:")

if __name__=='__main__': 
    main()
