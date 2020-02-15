import os, sys
PACKAGE_DIR = os.path.dirname(os.path.dirname(os.path.abspath("__file__")))
sys.path.append(PACKAGE_DIR)

import streamlit as st
from components import prediction
from jobs import pipeline

import pandas as pd
import numpy as np

import joblib

def main():
    """
        Car Buyer Prediction
    """
    
    activity = ["PREDICTION", "RETRAIN"]
    choice = st.sidebar.selectbox("Choose Activity",activity)
    
    #EDA
    if choice == "EDA":
        st.write("EDA")
    #PREDICTION
    elif choice == "PREDICTION":        
        prediction.prediction()
    #METRICS
    elif choice == "VISUALIZATION":
        st.write("VISUALIZATION")
    #RETRAIN
    elif choice == "RETRAIN":
        st.write("RETRAIN")
        if st.button("Start Training"):
            cls = pipeline.ClassifierPipeline()
            cls.start()
            st.write("Training Complete")
            st.write("CV scores " + " ".join([str(a) for a in cls.cv_scores]))
    

    
if __name__ == "__main__":
    main()