from nvidia_stock_prediction.get_nvda_data import get_nvidia_data
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys
import math

todays_prediction = ''

def get_todays_nvidia_prediction():
    return str(sys.path[0])+'/nvidia_stock_prediction/figure.png'

def train_nvidia_model():
    # import the data
    dataset = pd.read_csv(sys.path[0]+'/nvidia_stock_prediction/latest_nvidia_data.csv')

    # define the data
    X = dataset.iloc[:, [1, 2, 3, 5, 6]].values
    y = dataset.iloc[:, [4]].values
    
    # split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize the Random Forest Regressor
    rf_regressor = RandomForestRegressor(n_estimators=100, random_state=42)

    # fit the data
    # np.ravel turns from 2d array to 1d array
    rf_regressor.fit(X_train, np.ravel(y_train))

    # # evaluation
    # mse = mean_squared_error(y_test, y_pred)

    today_features = get_nvidia_data(None, None)[['Open', 'High', 'Low', 'Volume','Adj Close']]

    global todays_prediction
    todays_prediction = rf_regressor.predict(today_features)[0];

    todays_actual = today_features.iloc[:, [4]].values[0][0]

    print('Successfully trained the model')
    # move below logic to: download_plot

    last_100 = y[-100:,]

    # plt.ylabel('Closing Price')
    # plt.xlabel('Days')
    # plt.title(
    #       label='NVIDIA Prediction:'+str(math.trunc(todays_prediction))+' Todays actual: '+str(math.trunc(todays_actual))+'',
    #       fontweight=5,
    #       pad='2.0')
    # plt.scatter(range(len(last_100)), last_100, color = 'green')
    # plt.scatter(range(len(last_100)), rf_regressor.predict(X[-100:]), color = 'orange')
    # plt.scatter(100, todays_prediction, color = 'red')
    # plt.scatter(100, todays_actual, color = 'blue')
    # plt.savefig(sys.path[0]+'/nvidia_stock_prediction/figure.png')
    # print('successfully saved the plot')

    # download_plot(rf_regressor.predict(X), X)
    print('returning:',todays_prediction)
    return (todays_prediction)


def todays_prediction_global():
    global todays_prediction
    print('global is:',todays_prediction)
    return todays_prediction