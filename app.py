import streamlit as st # type: ignore
import joblib # type: ignore
import numpy as np # type: ignore


model = joblib.load("model.pkl")

st.title("House Price Prediction App")

st.divider()

st.write("This app created by Merve Gamze Cinar for predicting house price with given features of the house.")

st.divider()

bedrooms = st.number_input("Number of bedrooms", min_value = 0, value = 0)
bathrooms = st.number_input("Number of bathrooms", min_value = 0, value = 0)
livingarea = st.number_input("Living area", min_value = 0, value = 2000)
condition = st.number_input("Condition", min_value = 0, value = 3)
numberofschools = st.number_input("Number of schools nearby ", min_value = 0, value = 0)

st.divider()

X = [[bedrooms, bathrooms, livingarea, condition, numberofschools]]

predictbutton = st.button("Predict!")

if predictbutton:

    st.balloons()
    
    X_array = np.array(X)

    prediction = model.predict(X_array)

    st.write(f"Price prediction is{prediction:,.2f} ")

else:
    st.write("Please use predict button after entering values")
    





# Order of X['number of bedrooms', 'number of bathrooms', 'living area',
      # 'condition of the house', 'Number of schools nearby']