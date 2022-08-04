from pathlib import Path
import csv
import requests
my_api = "BC94UTRLKLJQB8ZA"
url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={base_url}"

response = requests.get(url)

import json
data = response.json()
json.dumps(data,indent=4)

close_data = data["realtime currency exchange rate"]
exchange_rate =(float(close_data['5. exchange rate']))
fp=Path.cwd()/"try folder"
file_path=Path.cwd()/"try folder"/"profit-and-loss-usd.csv"
#print(fp.exists)
with file_path.open(mode = "r", encoding = "utf-8", newline="") as file: 
    reader = csv.reader(file)
    next(reader)
    empty_list=[]
    flag_list=[]
    for line in reader: 
        empty_list.apprnf(line)

prev_figure=float(empty_list[0][4])
day=empty_list
for value in empty_list:
    if float(value[4]) >= float(prev_figure):
        prev_figure = float(value[4])
    else:
        difference = float(prev_figure) - float(value[4])
        def convertUSD_SGD(USD):
            return USD * exchange_rate
        SGD = (convertUSD_SGD(USD = difference))
        day = value[0]
        prev_figure = float(value[4])
        net_profit = (day,SGD)
        flag_list.append(net_profit)
        prev_figure = float(value[4])

print(flag_list)
