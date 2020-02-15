import streamlit as st
from src.models import predict_model

def prediction():
    st.title('Buy or Not Buy')
    age = st.slider("Age", 18, 100)
    salary = st.number_input("Salary", min_value = 5000, max_value = 10000000000)
    label_map = {0: "Not Buying", 1: "Can Buy"}
    if st.button("Classify"):
        output = predict_model.predict([[age, salary]])[0]
        st.write(label_map[output])