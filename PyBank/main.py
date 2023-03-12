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
        if profitdelta > greatest_increase[1]:
         greatest_increase[1] = profitdelta
         greatest_increase[0] = row[0]
         

        if profitdelta < greatest_decrease[1]:
            greatest_decrease[1] = profitdelta
            greatest_decrease[0] = row[0]
            print(greatest_decrease)
                   

print(totalmonths)
print(total_amount_loss)
print(profitchanges)
print(previous_amount_loss)
print(greatest_increase)
print(greatest_decrease)


profit_average = sum(profitchanges) / len(profitchanges)
print(profit_average) 


print("Financial Analysis")
print("--------------------------------")
print("Total Months: " + str(totalmonths))
print("Total: " + "$" + str(total_amount_loss))
print("Average Change: " + "$" + str(profit_average))
print("Greatest Increase: " + str(greatest_increase[0]) + " ($" + str(greatest_increase[1]) + ")" )
print("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" + str(greatest_decrease[1]) + ")" )
        
        
