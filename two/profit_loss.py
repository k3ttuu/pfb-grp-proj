from pathlib import Path
import csv

def pl_function(x):
    file_path = Path.cwd()/"csv reports"/"profit-and-loss-usd.csv"
    with file_path.open(mode="r", encoding="UTF-8", newline="") as file:
        Readers = csv.reader(file)
        next(Readers)
        list = []
        for line in Readers:
            list.append(line)
            
        for i in range(0, len(list)-1):
            # -1 since there is no 6th index value
            if int(list[i+1][4]) < int(list[i][4]):
                # integer value of next line, netprofit value < integer value of current line, netprofit value
                deficit = int(list[i][4]) - int(list[i+1][4])
                # netprofit value of current line - netprofit value of next line
                day = list[i+1][0]
                # day of next line
                print("[PROFIT DEFICIT] DAY: {day}, AMOUNT: SGD'{deficit*x}")
        else:
            print('[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY')

