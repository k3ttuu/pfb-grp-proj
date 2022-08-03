from pathlib import Path
import csv
import requests
key_api = 'BC94UTRLKLJQB8ZA'
url = ''

responses = requests.get(url)

import json
data=responses.json()
print(json.dumps(data,indent=4))

closed_data=data["Real Time Currency Exchange Rate"]
exchange_rate=(float(closed_data['5. exchange rate']))
fp=Path.cwd()/"Two folder"
file_path=Path.cwd()/"Two folder"/"cash-on-hand_usd.csv"
with file_path.open(mode = "r",encoding = "UTF-8", newline="") as file:
    Readers = csv.reader(file)
    next(Readers)
    empty_list=[]
    flag_list=[]
    for line in Readers:
        empty_list.append(line)

previous_figure = float(empty_list[0][1])
days = empty_list
for value in empty_list:
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
        prev_figure = float(value[1])
        cash_on_hand = (day,SGD)
        flag_list.append(cash_on_hand)
        prev_figure = float(value[1])
print(flag_list)