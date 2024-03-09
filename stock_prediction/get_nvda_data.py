# Python code to pull historical data from Yahoo Finance API for Nvidia stocks


import yfinance as yf
import os
import pandas as pd
from datetime import datetime, timedelta
import smtplib
from email.message import EmailMessage
import time
from env_secrets import config      


# numberToReportTo = str(os.environ.get('number_to_report_to'))

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
    

def get_nvidia_data(start_date = None, end_date = None):
    # Define the ticker symbol for Nvidia
    name = 'NVDA'
    
    # Define the time period (past year)
    if(not start_date):
        start_date = yesterday_and_today()[0]
    if(not end_date):
        end_date = yesterday_and_today()[1]

    # Fetch the historical data from Yahoo Finance API
    nvidia_data = yf.download(name, start=start_date, end=end_date)

    
    # Return the historical data
    return nvidia_data #Type is data_frame


def save_to_csv(data_frame, desiredFileName):
    # Get the current working directory
    cwd = os.getcwd()
    
    # Define the file path where the CSV file will be saved
    file_path = os.path.join(cwd, desiredFileName)
    
    # Save the DataFrame to a CSV file in the working directory
    data_frame.to_csv(file_path, index=False)
    
    print(f"CSV file '{desiredFileName}' saved successfully in the working directory.")

def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(config['sender_email'], config['gmail_app_password'])

    msg = EmailMessage()

    message = 'test message from: '+config['environment']
    msg.set_content(message)
    msg['Subject'] = 'Test'
    msg['From'] = config['sender_email']
    msg['To'] = config['recipient_email']
    print('msg:',msg)
    server.send_message(msg)


def report_daily():
    starttime=time.time()
    interval=86400 
    while True:
        send_email()
        time.sleep(interval - ((time.time() - starttime) % interval))

send_email()
report_daily()


# Example usage:
# 
# save_to_csv(get_nvidia_data(), 'nvidia_stock_data.csv')