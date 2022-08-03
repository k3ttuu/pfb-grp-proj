from pathlib import Path
import csv
import requests
key_api = 'BW8DP6OHTV62MU57'
url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE'

responses = requests.get(url)

import json
data=responses.json()