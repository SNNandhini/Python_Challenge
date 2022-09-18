# Download the required built-in modules
import os
import csv
import datetime

# Variable used to append the datetimestamp to the output file name
date = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

# Variable used for the source file name
source_file = "election_data.csv"

# Variable used for the output file name
output_file = f"election_data_analysis_{date}.txt"

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
    
#   Copy the candidates data only, into a list for easy access
    candidates = [i[2] for i in data]

#   Identify the unique list of candidates    
    unique_candidates = set(candidates)

#   Create a dictionary with the unique candidates list and their corresponding votes
    votes_count = dict.fromkeys(unique_candidates,0)
    for i in candidates:
        votes_count[i] = votes_count[i] + 1
    
#   Calculation of Total Votes, Winner    
    total_votes = len(candidates)
    winner = max(votes_count,key=votes_count.get)

#   Function to print the results (can be used for both console and file printing)
    def print_lines():
        lines2 = []
        lines1 = [f"Election Results",
                  f"-------------------------",
                  f"Total Votes: {total_votes}",
                  f"-------------------------"]
#       From the dictionary, identify each candidate and their corresponding voteas and percentages
        for i in sorted(votes_count.keys()):   
            lines2.append(f"{i}: {round((votes_count[i]/total_votes)*100,3)}% ({votes_count[i]})") 
        lines3 = [f"-------------------------",
                  f"Winner: {winner}",
                  f"-------------------------"]
        return lines1, lines2, lines3

#   Call the print function to print the results on console
    console_lines1, console_lines2, console_lines3 = print_lines()
    print("\n")
    print("\n".join(console_lines1))
    print("\n".join(console_lines2))
    print("\n".join(console_lines3))
    print("\n")   

# Variable used for the path of the output text file
txtpath = os.path.join(".","Analysis",output_file)

# Open the file in write mode using the path above
with open(txtpath, "w") as external_file:

#   Call the print function to print results in the text file    
    write_lines1, write_lines2, write_lines3 = print_lines()
    external_file.write("\n".join(write_lines1))
    external_file.write("\n")
    external_file.write("\n".join(write_lines2))
    external_file.write("\n")
    external_file.write("\n".join(write_lines3))
