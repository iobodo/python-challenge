#%%
import csv

# Read the budget data from the CSV file
filename = r'C:\Users\Isaac Technology\Desktop\Data Analytics Boot Camp\Week 3\python-challenge\Starter_Code (3)\Starter_Code\PyBank\Resources\budget_data.csv'

# Initialize variables
total_months = 0
net_total_profit_losses = 0
changes = []
greatest_increase = 0
greatest_increase_date = ""
greatest_decrease = 0
greatest_decrease_date = ""

# Open the file and skip the header row
file = open(filename, 'r')
csv_reader = csv.reader(file)
next(csv_reader)

# Loop through each row in the CSV file
for row in csv_reader:
    # Increment the total number of months
    total_months += 1
    
    # Add the profit/loss to the net total
    net_total_profit_losses += int(row[1])
    
    # Calculate the change compared to the previous month
    if total_months > 1:
        current_profit_loss = int(row[1])
        previous_profit_loss = int(previous_row[1])
        change = current_profit_loss - previous_profit_loss
        changes.append(change)
        
        # Check for the greatest increase and decrease
        if change > greatest_increase:
            greatest_increase = change
            greatest_increase_date = row[0]
        if change < greatest_decrease:
            greatest_decrease = change
            greatest_decrease_date = row[0]
    
    # Store the current row for the next iteration
    previous_row = row

# Calculate the average change
average_change = sum(changes) / len(changes)

# Print the analysis to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Net Total Amount of Profit/Losses: ${net_total_profit_losses}")
print(f"Average Change: ${average_change}")
print("Greatest Increase in Profits:")
print(f"Date: {greatest_increase_date}")
print(f"Amount: ${greatest_increase}")
print("Greatest Decrease in Profits:")
print(f"Date: {greatest_decrease_date}")
print(f"Amount: ${greatest_decrease}")

# Export the results to a text file
output_file = "financial_analysis.txt"
with open(output_file, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Net Total Amount of Profit/Losses: ${net_total_profit_losses}\n")
    file.write(f"Average Change: ${average_change}\n")
    file.write("Greatest Increase in Profits:\n")
    file.write(f"Date: {greatest_increase_date}\n")
    file.write(f"Amount: ${greatest_increase}\n")
    file.write("Greatest Decrease in Profits:\n")
    file.write(f"Date: {greatest_decrease_date}\n")
    file.write(f"Amount: ${greatest_decrease}\n")

print("Analysis has been exported to", output_file)

# Close the file
file.close()
