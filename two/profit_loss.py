from pathlib import Path
import csv

def pl_function(x):
    file_path = Path.cwd()/"csv reports"/"profit-and-loss-usd.csv"
    with file_path.open(mode="r", encoding="UTF-8", newline="") as file:
        Readers = csv.reader(file)
        next(Readers)
        empty_list = []
        for line in Readers:
            empty_list.append(line)
            
        for i in range(0, len(empty_list)-1):
            # -1 since there is no 6th index value
            if int(empty_list[i+1][4]) < int(empty_list[i][4]):
                # integer value of next line, netprofit value < integer value of current line, netprofit value
                deficit = int(empty_list[i][4]) - int(empty_list[i+1][4])
                # netprofit value of current line - netprofit value of next line
                day = empty_list[i+1][0]
                # day of next line
                print("[PROFIT DEFICIT] DAY: {day}, AMOUNT: SGD'{deficit*x}")
        else:
            print('[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY')

