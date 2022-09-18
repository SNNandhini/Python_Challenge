# Download the required built-in modules
import os
import csv
import datetime

# Variable used to append the datetimestamp to the output file name
date = datetime.datetime.now().strftime("%Y%m%d%H%M%S") #If you want in yyyy_mm_dd then add _

# Variable used for the source file name
source_file = "budget_data.csv"

# Variable used for the output file name
output_file = f"budget_data_analysis_{date}.txt"

# Variable used for path of the csv source file
csvpath = os.path.join(".","Resources",source_file)

# Open the csv file using the filename and path mentioned above
with open(csvpath) as csvfile:

#   Read the contents of the csv file
    csvreader = csv.reader(csvfile,delimiter=",")

#   Place the cursor in the first line of actual data in the file, after header    
    csv_header = next(csvreader)

#   Copy the data from input file to a list    
    data = list(csvreader)

#   Calculation for the changes in Profit/Losses each month
    diff = 0

    for i in range(len(data)):
        if i==0:
            data[i].append(diff)
        else:
            for j in range(len(data[i])):
                if j==0:
                    continue
                else:      
                    diff = int(data[i][j]) - int(data[i-1][j])
        
            data[i].append(diff)
    
#   Copy month, amount and change values to 3 different list for easy access
    month = [i[0] for i in data]
    amount = [eval(i[1]) for i in data]
    change = [i[2] for i in data]

#   Calculation of  Total Months, Total Amount, Average Change, Greatest Increase in Profits and Greatest Decrease in Profits
    total_months = len(month)
    total_amount = sum(amount)
    average_change = sum(change)/(len(change)-1)
    greatest_increase = max(change)
    increase_month = month[change.index(greatest_increase)]
    greatest_decrease = min(change)
    decrease_month = month[change.index(greatest_decrease)]

#   Function to print the results (can be used for both console and file printing)
    def print_lines():
        lines = [f"Financial Analysis",
                 f"----------------------------",
                 f"Total Months: {total_months}",
                 f"Total: ${total_amount}",
                 f"Average Change: ${round(average_change,2)}",
                 f"Greatest Increase in Profits: {increase_month} $({greatest_increase})",
                 f"Greatest Decrease in Profits: {decrease_month} $({greatest_decrease})"]
        return(lines)

#   Call the print function to print the results on console
    console_lines=print_lines()
    print("\n")
    print("\n".join(console_lines))
    print("\n")
    
# Variable used for the path of the output text file
txtpath = os.path.join(".","Analysis",output_file)

# Open the file in write mode using the path above
with open(txtpath, "w") as external_file:

#   Call the print function to print results in the text file    
    write_lines = print_lines()
    external_file.write('\n'.join(write_lines))
