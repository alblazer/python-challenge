#Bring in Dependencies
import os
import csv
#Define some variables
months = []
profit_loss_changes = []
count_months = 0
net_profit_loss = 0
last_months_profit_loss = 0
current_months_profit_loss = 0
profit_loss_change = 0



# Grab the csv file in the Resources folder 
csv_path = os.path.join("Resources", "budget_data.csv")

# Open and read csv
with open(csv_path, newline="") as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")

    # Read the header row first
    csv_header = next(csvfile)

    # Read through each row of data after the header
    for row in csv_reader:
        # Keep a count of months
        count_months += 1
        # Count the total amount of "Profit/Losses" over the whole file
        current_month_profit_loss = int(row[1])
        net_profit_loss += current_month_profit_loss
        if (count_months == 1):
            # Make the value of the last month equal the current month
            last_month_profit_loss = current_month_profit_loss
            continue
        else:
            # Find the change in profit loss 
            profit_loss_change = current_month_profit_loss - last_month_profit_loss
            # Append each month to the months[]
            months.append(row[0])
            # Append each profit_loss_change to profit_loss_changes[]
            profit_loss_changes.append(profit_loss_change)
            # Set last_month_profit_loss as the current_month_profit_loss for the next loop
            last_month_profit_loss = current_month_profit_loss
    #sum and average of the changes in "Profit/Losses" over the entire period
    sum_profit_loss = sum(profit_loss_changes)
    average_profit_loss = round(sum_profit_loss/(count_months - 1), 2)
    # highest and lowest changes in "Profit/Losses" over the entire period
    highest_change = max(profit_loss_changes)
    lowest_change = min(profit_loss_changes)
    # Locate the index value of highest and lowest changes in "Profit/Losses" over the entire period
    highest_month_index = profit_loss_changes.index(highest_change)
    lowest_month_index = profit_loss_changes.index(lowest_change)
    # Assign best and worst month
    best_month = months[highest_month_index]
    worst_month = months[lowest_month_index]

#Print the analysis to the terminal
print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(len(months)))
print(f"Total:  ${net_profit_loss}")
print(f"Average Change:  ${average_profit_loss}")
print(f"Greatest Increase in Profits:  {best_month} (${highest_change})")
print(f"Greatest Decrease in Losses:  {worst_month} (${lowest_change})")

#Export a text file with the results
budget_file = os.path.join("Analysis", "budget_data.txt")
with open(budget_file, "w") as outfile:
    outfile.write("Financial Analysis\n")
    outfile.write("----------------------------\n")
    outfile.write("Total Months: " + str(len(months)))
    outfile.write("\n")
    outfile.write(f"Total:  ${net_profit_loss}\n")
    outfile.write(f"Average Change:  ${average_profit_loss}\n")
    outfile.write(f"Greatest Increase in Profits:  {best_month} (${highest_change})\n")
    outfile.write(f"Greatest Decrease in Losses:  {worst_month} (${lowest_change})\n")
