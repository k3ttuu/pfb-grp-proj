from pathlib import Path
import csv
def coh_function(x):
    file_path=Path.cwd()/"csv reports"/"cash-on-hand-usd.csv"
    with file_path.open(mode = "r",encoding = "UTF-8", newline="") as file:
        Readers = csv.reader(file)
        next(Readers)
        list=[]
        for line in Readers:
            list.append(line)

        for i in range(0, len(list)-1):
        # -1 since there is no 6th index value
            if int(list[i+1][1]) < int(list[i][1]):
                # integer value of next line, coh value < integer value of current line, coh value
                deficit = int(list[i][1]) - int(list[i+1][1])
                # coh value of current line - coh value of next line
                day = list[i+1][0]
                # day of next line
                print(f"[CASH DEFICIT] DAY: {day}, AMOUNT: SGD{deficit*x}")    
        else:
            print('[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY')
    
            
