# Python_Challenge
Python Homework: PyBank and PyPoll

## PyBank and PyPoll Data Analysis
-   PyBank involves analysing the financial records of a company, containing Date and Profit/Losses.
-   PyPoll involves analysing the poll data of a small, rural town. The data contains Voter ID, County and Candidates details.

### Python Script and Results
#### PyBank
1.  The Python script developed for this assignment can be found in Python_Challenge/PyBank/main.py
2.  The data provided for this analysis can be found in Python_Challenge/PyBank/Resources/budget_data.csv
3.  The Python Script does the following:
    -   The data from the source file(budget_data.csv) is read and all data except the headers are copied into a list named data.
    -   The list is then appended to include the Change in Profit/Losses each month. The Change is the difference in Profit/Losses the current month with that of the previous month.
    -   Based on the data in the list above, the calculations for Total Months, Total Amount, Average Change, Greatest Increase in Profits and Greatest Decrease in Profits are done.
    -   The results are then printed on both Console and the output Text File. 
    -   The name of the text file ((budget_data_analysis_<datetimestamp>.txt)) is appended with datetimestamp for easy identification and access. The output Text file can be found in Python_Challenge/PyBank/Analysis/budget_data_analysis_20220918154920.txt
4.  The images of the results (both Console and Text file) can be seen in Python_Challenge/PyBank/Images_PyBank.docx

#### PyPoll
1.  The Python script developed for this assignment can be found in Python_Challenge/PyPoll/main.py
2.  The data provided for this analysis can be found in Python_Challenge/PyPoll/Resources/election_data.csv
3.  The Python Script does the following:
    -   The data from the source file(election_data.csv) is read and all data except the headers are copied into a list named data.
    -   The list is then used to create a dictionary named votes_count containing the unique list of candidates and their corresponding votes.
    -   Based on this data, the calculations for Total Votes, candidates,their corresponding votes, percentages and Winner are done.
    -   The results are then printed on both Console and the output Text File. 
    -   The name of the text file (election_data_analysis_<datetimestamp>.txt) is appended with datetimestamp for easy identification and access. The output Text file can be found in Python_Challenge/PyPoll/Analysis/election_data_analysis_20220918154929.txt
4.  The images of the results (both Console and Text file) can be seen in Python_Challenge/PyPoll/Images_PyPoll.docx

### Files Submitted
#### PyBank
1.  Python Script - Python_Challenge/PyBank/main.py
2.  Source Data - Python_Challenge/PyBank/Resources/budget_data.csv
3.  Output Text File - Python_Challenge/PyBank/Analysis/budget_data_analysis_20220918154920.txt
4.  Result Images - Python_Challenge/PyBank/Images_PyBank.docx

#### PyPoll
1.  Python Script - Python_Challenge/PyPoll/main.py
2.  Source Data - Python_Challenge/PyPoll/Resources/election_data.csv
3.  Output Text File - Python_Challenge/PyPoll/Analysis/election_data_analysis_20220918154929.txt
4.  Result Images - Python_Challenge/PyPoll/Images_PyPoll.docx

### References
1.	geeksforgeeks, 2022. geeksforgeeks. [Online] 
Available at: https://www.geeksforgeeks.org/python-split-nested-list-into-two-lists/
[Accessed 16 September 2022].
2.	geeksforgeeks, 2022. geeksforgeeks. [Online] 
Available at: https://www.geeksforgeeks.org/python-converting-all-strings-in-list-to-integers/
[Accessed 16 September 2022].
3.	pythontutorial, 2022. pythontutorial. [Online] 
Available at: https://www.pythontutorial.net/python-basics/python-write-text-file/
[Accessed 16 September 2022].
4.	stackoverflow, 2014. stackoverflow. [Online] 
Available at: https://stackoverflow.com/questions/24662571/python-import-csv-to-list
[Accessed 16 September 2022].
5.	geeksforgeeks, 2022. geeksforgeeks. [Online] 
Available at: https://www.geeksforgeeks.org/python-get-unique-values-list/
[Accessed 17 September 2022].
6.	Varun, 2022. thispointer. [Online] 
Available at: https://thispointer.com/python-how-to-sort-a-dictionary-by-key-or-value/
[Accessed 17 September 2022].
