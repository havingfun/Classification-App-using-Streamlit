import os, sys
PACKAGE_DIR = os.path.dirname(os.path.dirname(os.path.abspath("__file__")))
sys.path.append(PACKAGE_DIR)

from src.data import clean_data
from src.features import build_features
from src.models import train_model

class ClassifierPipeline():
    def __init__(self):
        self.version = 1.0
        self.cv_scores = []
        
    def start(self):
        clean_data.clean()
        build_features.build_features()
        cv_scores = train_model.train()
        self.cv_scores = cv_scores
        
if __name__ == "__main__":
    pipeline = ClassifierPipeline()
    pipeline.start()