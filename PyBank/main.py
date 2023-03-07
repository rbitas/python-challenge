import csv
import os 

budget_path = os.path.join("...","Resources","budget_data.csv")

totalmonths = 0
totalamount = 0
amount = []
previous_amount = 0
profitchanges = 0 
monthchanges=[]
averageamount = 0
amountlist =[]
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999]

with open(budget_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    for row in csvreader:

        totalmonths = totalmonths + 1
        
