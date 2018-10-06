from sklearn.externals import joblib
from flask import Flask


app = Flask(__name__)

@app.route('/')
def hello_world():

    # Process Data
    scaler = joblib.load('scaler.pkl')

    return 'Hello, World!'


