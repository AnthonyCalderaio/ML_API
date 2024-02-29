# Python code to pull historical data from Yahoo Finance API for Nvidia stocks

import yfinance as yf
import os
import pandas as pd
from datetime import datetime, timedelta

def yesterday_and_today():
    # Get today's date
    today = datetime.now().date()

    # Calculate yesterday's date
    yesterday = today - timedelta(days=1)

    # Format dates as strings in 'YYYY-MM-DD' format
    yesterday_str = yesterday.strftime('%Y-%m-%d')
    today_str = today.strftime('%Y-%m-%d')

    # Return dates in a list
    return [yesterday_str, today_str]
    

def get_nvidia_data(start_date = None, end_date = None, download_csv = False):
    # Define the ticker symbol for Nvidia
    name = 'NVDA'
    
    # Define the time period (past year)
    if(not start_date):
        start_date = yesterday_and_today()[0]
    if(not end_date):
        end_date = yesterday_and_today()[1]
    
    # Fetch the historical data from Yahoo Finance API
    nvidia_data = yf.download(name, start=start_date, end=end_date)

    if(download_csv):
        save_to_csv(nvidia_data, 'nvidia_stock_data.csv')
    
    # Return the historical data
    return nvidia_data


def save_to_csv(data_frame, filename):
    # Get the current working directory
    cwd = os.getcwd()
    
    # Define the file path where the CSV file will be saved
    file_path = os.path.join(cwd, filename)
    
    # Save the DataFrame to a CSV file in the working directory
    data_frame.to_csv(file_path, index=False)
    
    print(f"CSV file '{filename}' saved successfully in the working directory.")

# Example usage
# nvidia_stock_data = get_nvidia_data()
# print(nvidia_stock_data.head())  # Display the first few rows of the data

# save_to_csv(nvidia_stock_data, 'nvidia_stock_data.csv')