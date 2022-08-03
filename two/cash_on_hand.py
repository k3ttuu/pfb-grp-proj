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
exchange_rate=(float(closed_data['5. exchange rate']))
fp=Path.cwd()/"Two folder"
file_path=Path.cwd()/"Two folder"/"cash-on-hand_usd.csv"
#print(fp.exists())
with file_path.open(mode = "r",encoding = "UTF-8", newline="") as file:
    Readers = csv.reader(file)
    next(Readers)
    empty_list=[]
    flag_list=[]
    for line in Readers:
        empty_list.append(line)