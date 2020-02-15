import os, sys
PACKAGE_DIR = os.path.dirname(os.path.dirname(os.path.abspath("__file__")))
sys.path.append(PACKAGE_DIR)

from flask import Flask, render_template, request
from src.models import predict_model
from jobs import pipeline

app = Flask(__name__)

@app.route('/')
def index():
    output = predict_model.predict([[15, 150000]])[0]
    return render_template('index.html')
  
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        age = request.form['age']
        salary = request.form['salary']
    output = predict_model.predict([[age, salary]])[0]
    return render_template('index.html', age=age, salary=salary, output=output)

@app.route('/train')
def train():
    cls = pipeline.ClassifierPipeline()
    cls.start()
    return "Training Complete"

if __name__ == '__main__':
    app.run(debug=True)
    