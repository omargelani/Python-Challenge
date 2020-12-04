import csv
import os


csvfile = os.path.join("C:/Users/Owner/Desktop/Python_challenge/budget_data.csv")

with open(csvfile, 'r') as csvfile:


    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    print(header)
    total_months = 0
    total_sum = 0
    changelist = []
    prev = 0
    change = 0
    greatest_inc = ["",0]
    greatest_dec = ["",9999]
    for row in csvreader:
        total_months = total_months + 1
        total_sum = total_sum + int(row[1])
        change = int(row[1])-prev
        changelist.append(change)
        prev = int(row[1])
        if change > greatest_inc[1]:
            greatest_inc[0] = row[0]
            greatest_inc[1] = change
        if change < greatest_dec[1]:
            greatest_dec[0] = row[0]
            greatest_dec[1] = change 
    avgchange = sum(changelist[1:])/(len(changelist)-1)
   
    

  
    print("Financial analysis")
    
    print("-------------------")
    
    print(f'total months = {total_months}')
    print(f'total sum = {total_sum}')
    print( f'Average Change = {avgchange}')
    print(f'Greatest Increase in Profits {greatest_inc[0]} ${greatest_inc[1]}')
    print(f'Greatest Decrease in Profits {greatest_dec[0]} ${greatest_dec[1]}')
    
