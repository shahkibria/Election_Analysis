import csv
import os



import csv
import os
#Select the file to access the data
file_to_load = os.path.join("Resources", "election_results.csv")
#Select the file to write
file_to_save = os.path.join("Analysis", "election_analysis.txt")

#1. Assign first variable total_vote as zero
total_vote = 0
#Determine the individual candidates. The candidates are in third colume so in the list they have index 2. We are creating a new list of candidate options
candidate_option = []
#To determine total votes, we will create a dictionary where they key is each candidate's name and vote count for the candidate is the value for the key
candidate_vote = {}
#Add variables to present the winning Count and Candidate
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#2. Open election results and read the file
with open (file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    #Read the Header Row
    header=next(file_reader)
    #Print each row in File_Reader
    for row in file_reader:
        #Add to the total vote count
        total_vote += 1
        #Print candidate name from third colume (i.e they have index of [2])
        candidate_name = row[2]
        #Add the candidate name to the candidate list if not already added
        if candidate_name not in candidate_option:
            candidate_option.append(candidate_name)
            #Start counting the vote count for the unique candidate
            candidate_vote[candidate_name] = 0
        candidate_vote[candidate_name] +=1
    for candidate_name in candidate_vote:
        
        vote = candidate_vote[candidate_name]
        vote_percentage = (float(vote)/float(total_vote))*100
        print(f"{candidate_name}: {vote_percentage:.1f}% ({vote:,})\n")

        if (vote>winning_count) and (vote_percentage>winning_percentage):
            winning_count = vote
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
            winning_candidate_summary = (
                f"-------------------\n"
                f"Winner:{winning_candidate}\n"
                f"Winning Vote Count:{winning_count}\n"
                f"Winning Percentage: {winning_percentage:.1f}%\n"
                f"-------------------\n")
print(winning_candidate_summary)







