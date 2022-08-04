from pathlib import Path
import csv
import requests
key_api = 'BC94UTRLKLJQB8ZA'
url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={base_url}'

responses = requests.get(url)

import json
data=responses.json()
print(json.dumps(data,indent=4))

data_1=data["Realtime Currency Exchange Rate"]
exchange_rate=(float(data_1['5. Exchange Rate']))
file_path=Path.cwd()/"csv reports"/"cash-on-hand-usd.csv"
with file_path.open(mode = "r",encoding = "UTF-8", newline="") as file:
    Readers = csv.reader(file)
    next(Readers)
    list=[]
    flag_list=[]
    for line in Readers:
        list.append(line)

previous_figure = float(list[0][1])
days = list
for value in list:
    if float(value[1]) >= float(previous_figure):
        previous_figure = float(value[1])
    else:
        diff = float(previous_figure) - float(value[1])
        def convUSD_SGD(USD):
            """
        Fuction converts USD to SGD by multiplying exchange rate, this will return the coverted value
            """
            return USD * exchange_rate
        SGD = (convUSD_SGD(USD = diff))
        day=value[0]
        previous_figure = float(value[1])
        cash_on_hand = (day,SGD)
        flag_list.append(cash_on_hand)
        previous_figure = float(value[1])
print(flag_list)