import csv
import os



import csv
import os
#Select the file to access the data
file_to_load = os.path.join("Resources", "election_results.csv")
#Select the file to write
file_to_save = os.path.join("Analysis", "election_analysis.txt")
#Open election results and read the file
with open (file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    header=next(file_reader)
    print(header)


#The data we need to retrieve
#The Total number of votes cast
#The complete list of candidates who received votes
#Percentage of Votes each candidate won
#The winner of the election based on popular vote



