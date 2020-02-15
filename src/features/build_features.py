# Read the cleaned datasets and add features to the datasets
import pandas as pd

def build_features():
    # Importing the dataset
    X = pd.read_csv('../data/clean/X.csv')
    y = pd.read_csv('../data/clean/Y.csv')

    # Applying features to the cleaned dataset


    # Writing to the processed
    X.to_csv('../data/processed/X.csv', index=False)
    y.to_csv('../data/processed/y.csv', index=False)
    print("Feature Addition Done")