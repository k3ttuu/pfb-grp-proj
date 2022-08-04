
from pathlib import Path
import re, csv

def overheads_function(x):
    file_path = Path.cwd()/"csv reports"/"overheads-day-90.csv"
    with file_path.open(mode="r", encoding="UTF-8", newline="") as file:
        Readers = csv.reader(file)
        next(Readers)
        list = []
        list1 = []
        for line in Readers:
            list.append(line[1])
            # list would contain only the integer values
            list1.append(line)
            # list contains the data
        maxrow = int(list.index(max(list)))
        # find the index position of the maximum value in list
        data = (list1[maxrow])
        sgd = float(data [1]) 
        #the data with maximum value in the list
        print (f"[HIGHEST OVERHEADS] {data[0].upper()}: SGD{sgd}")


