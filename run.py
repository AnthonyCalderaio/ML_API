from flask import Flask, jsonify, request
from stock_prediction.get_nvda_data import get_nvidia_data;

app = Flask(__name__)

# Define a route for your API endpoint
@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello, World!'})

# Stock predictor route
# Define a route for your API endpoint
@app.route('/nvidia_prediction', methods=['GET'])
def nvidia_predictor():

 # Get the JSON data from the POST request
    json_data = request.get_json()

    # Pass the JSON data to a function in another file
    response_data = get_nvidia_data()

    # Return the response in JSON format
    return jsonify(response_data)


if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)