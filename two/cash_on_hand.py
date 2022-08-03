from pathlib import Path
import csv
import requests
key_api = 'BW8DP6OHTV62MU57'
url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE'

responses = requests.get(url)

import json
data=responses.json()
print(json.dumps(data,indent=4))

closed_data=data["REAL TIME CURRENCY EXCHANGE RATE"]
exchange_rate=(float(closed_data['5. Exchange Rate']))
fp=Path.cwd