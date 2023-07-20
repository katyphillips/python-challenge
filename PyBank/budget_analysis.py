import os
import csv

budget_data_csv = os.path.join("Resources","budget_data.csv")

#Define variables
total_months=0
net_total=0

#Open and read csv file:
with open(budget_data_csv) as csv_file:
    csv_reader=csv.reader(csv_file,delimiter=",")

    #Read the header row first
    csv_header=next(csv_file)
    print(f"Header:{csv_header}")

    #Set initial values
    first_row=previous_row=next(csv_reader)
    total_months+=1
    max_profit_delta=max_loss_delta=initial_profit=net_total=int(first_row[1])
    day_of_max_profit=day_of_max_loss=first_row[0]

    #Print opening lines
    print("Financial Analysis")
    print("----------------------")

    #Read each row in csv file
    for row in csv_reader:
        
        #Find total number of months
        total_months += 1
        
        #Find net total of Profits/Losses
        net_total=net_total+int(row[1])
        
        #Find incremental change in profit
        current_delta=int(row[1])-int(previous_row[1])
        
        #Find Greatest Increase
        if current_delta>max_profit_delta:
            max_profit_delta=current_delta
            day_of_max_profit=row[0]

        #Have previous row move with current row
        previous_row=row
                        
        #Find greatest decrease in profits (date and amount)
        if current_delta<max_loss_delta:
            max_loss_delta=current_delta
            day_of_max_loss=row[0]
        
        #Have previous row move with current row
        previous_row=row
    
    #Find changes in Profits/Losses
    total_change=int(row[1])-initial_profit

    #Average changes in Profits/Losses
    average_change=round(total_change/85, 2)
        
    #Print results to terminal
    print(f"Total Months: {str(total_months)}")
    print(f"Total: ${str(net_total)}")
    print(f"Average Change: ${str(average_change)}")
    print(f"Greatest Increase in Profits: {str(day_of_max_profit)} (${str(max_profit_delta)})")
    print(f"Greatest Decrease in Profits: {str(day_of_max_loss)} (${str(max_loss_delta)})")
    
    #Print results to text file
    with open("budget_data_results.txt","w") as file:
            file.write("Financial Analysis\n")
            file.write("----------------------\n")
            file.write(f"Total Months: {str(total_months)}\n")
            file.write(f"Total: ${str(net_total)}\n")
            file.write(f"Average Change: ${str(average_change)}\n")
            file.write(f"Greatest Increase in Profits: {str(day_of_max_profit)} (${str(max_profit_delta)})\n")
            file.write(f"Greatest Decrease in Profits: {str(day_of_max_loss)} (${str(max_loss_delta)})\n")

            