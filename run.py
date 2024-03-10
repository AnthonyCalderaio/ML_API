from os import wait
import os
from flask import Flask, jsonify, request, send_file
from stock_prediction.model import train_nvidia_model
from flask_cors import CORS
import sys
from stock_prediction.utils import report_daily, save_to_csv
from stock_prediction.model import train_nvidia_model, get_todays_prediction
from stock_prediction.get_nvda_data import get_nvidia_data
import time


app = Flask(__name__)
CORS(app)

# Define a route for your API endpoint
@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello, World!'})

@app.route('/initialize_data', methods=['GET'])
def initialize_data():
    save_to_csv(get_nvidia_data('2021-01-01', None), sys.path[0]+'/stock_prediction/latest_nvidia_data.csv')
    time.sleep(10) 
    train_nvidia_model()
    time.sleep(10) 
    report_daily(get_todays_prediction())
    time.sleep(10)
    print('Directory contents:',os.listdir())
    time.sleep(10)
    return 'complete'

# Stock predictor route
# Define a route for your API endpoint
@app.route('/nvidia_prediction', methods=['GET'])
def nvidia_predictor():
    # Pass the JSON data to a function in another file
    
    image = get_todays_prediction()
    # Return the response in JSON format
    return send_file(image, as_attachment=True)

if __name__ == '__main__':
    # Run the Flask app
    save_to_csv(get_nvidia_data('2021-01-01', None), sys.path[0]+'/stock_prediction/latest_nvidia_data.csv')
    time.sleep(10) 
    train_nvidia_model()
    time.sleep(10) 
    report_daily(get_todays_prediction())
    time.sleep(10)
    print('Directory contents:',os.listdir())
    time.sleep(10)
    # os.chdir(sys.path[0]+'/stock_prediction')
    # print('Directory contents:',os.listdir())
    app.run(debug=True)
    
