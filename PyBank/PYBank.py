
# Import Dependencies
import os
import csv

# Declare file location through path library and assign a variable to file
input_file = os.path.join( "Resources","budget_data.csv")

# Create a variable and save to a file path
output_file = os.path.join("Analysis", "Financial_Analysis_Summary.txt")

# Initialize variables by assiging an initial value of 0
# Keeping track of total number of months
total_months = 0

# keeping track of profit and loss
total_profit_loss = 0

# Keep track of profit/loss value from previous row to calculate the change
change_value = 0

# Keep track of change in profit/loss between months
total_change = 0

# Create a empty list to store dates and monthly changes in profit/loss
dates = []
profit_loss = []

# open the csv reader
with open(input_file, newline='') as csvfile:

    # CSV reader stores the data in the budget_data.csv in the csvreader variable
    csv_reader = csv.reader(csvfile, delimiter = ',')

    # to skip the header row so that we can iterate with the values
    header = next(csv_reader)

    # Initialize the first row
    # Read the first row of data after the header
    first_row = next(csv_reader)
    # Increment total months by 1
    total_months += 1
    # Add profit or loss of the first row to total profit or loss column
    total_profit_loss += int(first_row[1])
    # set a value in the profit or loss of the 1st row for future changes
    change_value = int(first_row[1])

    # Iterate through each row of the csv file
    for row in csv_reader:

     # Append date from current row to the dates list with index 0
        dates.append(row[0])
     # Calculate the change in profit or loss from the previous month then sotre it in the change list
        total_change = int(row[1]) - change_value
     # Append the new calculated change to the profits list
        profit_loss.append(total_change)
    # Update vslue to current month profit or loss for the next iteration
        change_value = int(row[1])
    # Increment total number of months by 1
        total_months += 1
    # Add current months profit or loss to total profit or loss 
        total_profit_loss += int(row[1])

# To track the month with the greatest increase in profit we create a variable equal to max profit
greatest_increase = max(profit_loss)
# Use a index to find the index of the first greatest increase in the profit 
greatest_index = profit_loss.index(greatest_increase)
# Create a variable to store the date that matches with the greatest increase
greatest_date = dates[greatest_index]

# To track the month with the greatest decrease in profit we create a variable equal to min profit
greatest_decrease = min(profit_loss)
# Use a index to find the index of the first greatest decrease in the profit 
lowest_index = profit_loss.index(greatest_decrease)
# Create a variable to store the date that matches with the greatest decrease
lowest_date = dates[lowest_index]


# Now we need to calculate the average change in profit or loss between the month over the entire period.
average_change = sum(profit_loss) / len(profit_loss)

# Print out calculations
output = (
    f"Financial Analysis\n"
    f"---------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_profit_loss:,}\n"
    f"Average Change: ${average_change:,.2f}\n"
    f"Greatest Increase in Profits: {greatest_date} (${greatest_increase:,})\n"
    f"Greatest Decrease in Profits: {lowest_date} (${greatest_decrease:,})"
)

# Print output
print(output)

# Export to a text file
output_file = "Financial_Analysis_Summary.txt"


# Create a output text that contains the analysis to export to a file using code from above
output_text = (
    f"Financial Analysis\n"
    f"---------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_profit_loss}\n"
    f"Average Change: ${round(average_change, 2)}\n"
    f"Greatest Increase in Profits: {greatest_date} (${greatest_increase})\n"
    f"Greatest Decrease in Profits: {lowest_date} (${greatest_decrease})\n"
)
# Now write the output test to send to the text file
with open(output_file, "w") as output_file:
    output_file.write(output)