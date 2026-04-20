import json
import yfinance as yf
import pandas as pd

apple = yf.Ticker("AAPL")

get https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/data/apple.json


with open('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/data/apple.json') as jason_file:
    apple_info = json.load(jason_file)
    print(apple_info)