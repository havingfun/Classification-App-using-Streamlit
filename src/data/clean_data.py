# Reading the raw file and then putting it in the clean dataset as X and y
import pandas as pd

def clean():
    # Importing the dataset
    dataset = pd.read_csv('../data/raw/Social_Network_Ads.csv')
    X = dataset.iloc[:, [2, 3]]
    y = dataset.iloc[:, 4]

    X.to_csv('../data/clean/X.csv', index=False)
    y.to_csv('../data/clean/y.csv', index=False)
    print("Cleaning Done")