
from pathlib import Path
import re, csv
key_api= "demo_key"
url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={demo_key}"


#set file path to csv reports folder
fp_read = Path.cwd()
#set file path to create overheads-day-90.csv
fp_write = Path.cwd()/"two folder"
fp_write.touch()

#set a global counter
count = 1

#create search pattern for expenses
pattern_overflow = "overflow.+"

pattern_salary = "salary.+"

pattern_interest = "Interest.+"

pattern_marketing = "Marketing.+"

pattern_rental = "Rental.+"

pattern_penalty = "Penalty.+"

pattern_depreciation = "Depreciation.+"

pattern_shipping = "Shipping.+"

pattern_human_resource = "Human Resource.+"

for file in fp_read.glob("*.txt"):

    with file.open(mode = "r", encoding = "UTF-8") as file:
        data = file.read()
        group_overflow = re.search(pattern = pattern_overflow, string = data).group()
        group_salary = re.search(pattern = pattern_salary, string = data).group()
        group_interest = re.search(pattern = pattern_interest, string = data).group()
        group_marketing= re.search(pattern = pattern_marketing, string = data).group()
        group_rental = re.search(pattern = pattern_rental, string = data).group()
        group_penalty = re.search(pattern = pattern_penalty, string = data).group()
        group_depreciation =re.search(pattern = pattern_depreciation, string = data).group()
        group_shipping = re.search(pattern = pattern_shipping, string = data).group()
        group_human_resource = re.search(pattern = pattern_human_resource, string = data).group()

# for each match item, append to csv reports
with fp_write.open("a", encoding = "UTF-8", newline = "") as file_write:
    #create a writer object
    writer = csv.writer(file_write)
    #write header once using counter variable
    if count == 1:
        headers =["Category","Overheads"]
        writer.writerow(headers)
    writer.writerow(["*expense","overheads"])
    count += 1

def highest_val(num):
    """
    This function will return the highest overhead category and its value
    """
    return num

highest_val = pattern_marketing
Data = Value
num = (highest_val,Value)

print(num)
