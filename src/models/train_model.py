# Final place to do the ML modeling including encoding/scaling/writing model
# Later on we can separate the encoding and scaling part to separate file but that will require storing scaled datasets separately
import pandas as pd
import numpy as np
import joblib

def train():
    # Read the datasets to encode
    X = pd.read_csv('../data/processed/X.csv').values
    y = pd.read_csv('../data/processed/y.csv').values

    # If y is 1D we will have to flatten the array
    y = y.ravel()

    # This is to convert the dataset to a mixed format including scaling/normalization/labelencoding/onehotencoding
    from sklearn.preprocessing import StandardScaler
    sc = StandardScaler()
    X = sc.fit_transform(X)

    # Fitting Logistic Regression to the Training set
    from sklearn.linear_model import LogisticRegression
    classifier = LogisticRegression(random_state = 0)
    classifier.fit(X, y)

    # TODO: Save results of the cross validation output
    from sklearn.model_selection import cross_val_score
    cv = cross_val_score(estimator=classifier,X=X, y=y,cv=10, scoring='accuracy')
    print("Cross Validation Scores - " + str(tuple(cv)))

    # Saving the encoder
    joblib.dump(sc, '../models/encoders/X_scalar.pkl')

    # Saving the model
    classifier_model = open('../models/classifier.pkl', 'wb')
    joblib.dump(classifier, classifier_model)
    print("Training Complete")
    
    return cv

