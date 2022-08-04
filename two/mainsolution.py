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







