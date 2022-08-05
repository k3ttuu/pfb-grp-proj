import api, cash_on_hand, profit_loss, overheads
from pathlib import Path
import csv


def main ():
    forex = api.currency_exchange_rate()
    x = forex
    print (f"[REAL TIME CURRENCY CONVERSION RATE] USD1 = SGD {forex}")
    overheads.overheads_function(x)
    cash_on_hand.coh_function(x)
    profit_loss.pl_function(x)



main()
filepath = Path.cwd()/"summary_report.txt"
filepath.touch()
with filepath.open(mode='a',encoding='UTF-8',newline='') as file :
    file.write(f'[REAL TIME CURRENCY CONVERSION RATE] USD1 = SGD{api.currency_exchange_rate}')
    file.write('\n')
    file.write(f'[HIGHEST OVERHEADS] SALARY EXPENSE: {overheads.overheads_function}')
    file.write('\n')
    file.write(f'[CASH SURPLUS] {cash_on_hand.coh_function}')
    file.write('\n')
    file.write(f'[NET PROFIT SURPLUS] {profit_loss.pl_function}')

