import os 
import csv

budget_path = os.path.join("/Users/rinabitas/Documents/python-challenge/PyBank/Resources/budget_data.csv")

totalmonths = 0
total_amount_loss = 0
previous_amount_loss = 0
profitchanges = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999]

with open(budget_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)

    prev_profit = -1
    for row in csvreader:
        
        totalmonths = totalmonths + 1
        total_amount_loss = total_amount_loss + int(row[1])
        profitdelta = int(row[1]) - prev_profit
        if prev_profit != -1:
            profitchanges.append(profitdelta)
        prev_profit = int(row[1])
        

print(totalmonths)
print(total_amount_loss)
print(profitchanges)
print(previous_amount_loss)


profit_average = sum(profitchanges) / len(profitchanges)
print(profit_average) 


        
        
