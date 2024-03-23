from os import wait
import os
from flask import Flask, jsonify, request, send_file
from nvidia_stock_prediction.model_random_forest import train_nvidia_model
from flask_cors import CORS
import sys
from nvidia_stock_prediction.utils import report_daily, save_to_csv
from nvidia_stock_prediction.model_random_forest import train_nvidia_model, get_todays_nvidia_prediction
from nvidia_stock_prediction.get_nvda_data import get_nvidia_data
import time

app = Flask(__name__)
CORS(app)

# Define a route for your API endpoint
@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello, World!'})

@app.route('/getCurrentDir', methods=['GET'])
def currDir():
    dir = str(os.listdir(sys.path[0]))
    print(dir)
    return dir


# Happens when app loads
@app.before_first_request
@app.route('/initialize_data', methods=['GET'])
def initialize_data():
    # Get todays NVIDIA data and save to a CSV
    save_to_csv(get_nvidia_data('2021-01-01', None), sys.path[0]+'/nvidia_stock_prediction/latest_nvidia_data.csv')

    # Train the model
    train_nvidia_model()

    # Report on the model with todays prediction
    report_daily(get_todays_nvidia_prediction())

# Stock predictor route
@app.route('/nvidia_prediction', methods=['GET'])
def nvidia_predictor():
    # Pass the JSON data to a function in another file
    
    image = get_todays_nvidia_prediction()
    # Return the response in JSON format
    return send_file(image, as_attachment=True)

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
    
