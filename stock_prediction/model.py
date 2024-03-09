from get_nvda_data import get_nvidia_data

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import pandas as pd
import numpy as np
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

# import the data
dataset = pd.read_csv('stock_prediction/nvidia_stock_data.csv')

# define the data
X = dataset.iloc[:, [0, 1, 2, 4, 5]].values
y = dataset.iloc[:, [3]].values

# split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Random Forest Regressor
rf_regressor = RandomForestRegressor(n_estimators=100, random_state=42)

# fit the data
# np.ravel turns from 2d array to 1d array
rf_regressor.fit(X_train, np.ravel(y_train))

# # predict the data
print('x_test')
print(X_test[0:1, :])
y_pred = rf_regressor.predict(X_test)

# # evaluation
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

# functions
def predict_todays_price():
    # return 'test';
    todays_prices = get_nvidia_data()
    x = todays_prices.iloc[:, [0, 1, 2, 4, 5]].values
    return rf_regressor.predict(x)

# print('predicted:',predict_todays_price())
