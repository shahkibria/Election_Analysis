# Election_Analysis
Election data analysis using Python

### Overview of the Election Audit

For this project, I were given a scenario where a Colorado Board of Elections employee requested my help in completing an election audit of a recent local congressional election. The following tasks were performd by me to be included in the completed election audit:
1. Calculate the total number of votes cast
2. Calculate the list of candidates who received votes
3. Calculate the list of counties were votes were cast
4. Calculate the total number and percentage of votes each candidate received
5. Calculate the total number and percentage of votes that were cast in each county
6. Determine the winner of the election based on popular vote. 
7. Determine the county that received the highest number of votes
8. Present our outcome printed to the terminal and a separate output text file. 

In order to execute this anlaysis, we obtained a .CSV file of the election results. We imported the data into python, ran the code we created and extracted the results into an output .txt file. 

### Election Audit Results

We have summerized the results of our analysis below. We have also added screenshots and links to the code as well as the output text file. 

 - There were a total of 369,711 votes cast
 - There were three candidates: Charles Casper Stockham, Diana DeGette and Raymon Anthony Doane. 
 - There were three counties were votes were cast: Arapahoe, Denver and Jefferson
 - The total number and percentages of votes for each candidate cast was: 
    - Charles Casper Stockham: 23.0% (85,213 votes)
    - Dianna DeGette: 73.8% (272,892 votes)
    - Raymon Anthony Doane: 3.1% (11,606 votes)
 -  The total number and percentages of votes cast in each county was: 
    - Jefferson: 10.51% (38,855 votes)
    - Denver: 82.78% (306,055 votes)
    - Arapahoe: 6.71% (24,801 votes)
 - The winner of the election was Dianna DeGette 
 - The county that received the highest number of votes was Denver. 
 
A screenshot of our output text file [Election Analysis](https://github.com/shahkibria/Election_Analysis/blob/main/Analysis/election_analysis.txt) is included below: 
 
 ![](https://github.com/shahkibria/Election_Analysis/blob/main/Analysis/election_analysis.png)
 
The specific Python Code [PyPoll Challenge](https://github.com/shahkibria/Election_Analysis/blob/main/Analysis/election_analysis.txt) has also been added to the repository. 


 ### Election Audit Summary
 
The election commission can use our code to calculate the results of any election. The code is designed to create a list of unique candidates within any election population data and calculate the number and percentage of votes (or rather count the number of instances and calculate a percentage) each unique candidate receives. In order to use this script for another election, we will have to change two things: 
 - the location and name of the input .CSV file
 - the column number for the candidate name depending on which colume the data is located. 
 
 
 
 
 
 
 
