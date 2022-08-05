from sys import api_version
import cash_on_hand

from pathlib import Path

fp = Path.cwd()/"Summary_report.txt"
fp.touch()

with fp.open(mode='a',encoding='UTF-8',newline='') as file :
    file.write(f'[REAL TIME CURRENCY CONVERSION RATE] USD1= SGD{api_version}')
    file.write('\n')
    file.write(f'{cash_on_hand.flag_list}')