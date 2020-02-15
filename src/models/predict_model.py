# This file is responsible for abstraction of predictions
import joblib
import numpy as np

# First generate features required
# Then do the encoding using the encoders from models
# Finally generate the output

# Creating a simple function for predicting single data points
def predict(X):
    try:
        if type(X) != 'numpy.ndarray':
            X = np.array(X)
        X_scalar = joblib.load('../models/encoders/X_scalar.pkl')
        classifier = joblib.load('../models/classifier.pkl')
        return classifier.predict(X_scalar.transform(X))
    except:
        return "Error in classifying the entry. Please pass a python list or numpy.ndarray with 2 columns"

