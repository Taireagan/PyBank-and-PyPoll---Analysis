# Import Dependencies
import os
import csv
from pathlib import Path

# Declare file location through path library 
# File Path : "C:\Repos\PyBank-and-PyPoll---Analysis\PyPoll\Resources\election_data.csv"
input_path = Path("Resources", "election_data.csv")
# Write the results to a file and save it
OUTPUT_PATH = Path("Analysis", "Election_Results_Summary.txt")

# Declare Variables
# Start a counter for the total number of votes to zero
total_votes = 0

# create a empty dictionary {} to store the number of votes for each individual candidate
candidate_votes = {}

os.chdir(os.path.dirname(os.path.realpath(__file__)))
# Open the csv file for reading using the with statement adding in newline characters and utf-8 encoding to read the file.
with open(input_path) as input_file:

    # create a csv.read to read the file and separate the values with commas
    csvreader = csv.reader(input_file)

    # skip the header row so that we can iterate with the values
    next(csvreader)

    # start by iterating each row in the csv file
    for row in csvreader:

         # add the total votes by 1 for each row 
        total_votes += 1

        # Grab candidates name from the third column (index 2) of the row
        candidate = row[2]

        # Check candidates name to see if it is already in the dictionary
        if candidate not in candidate_votes:

            # If candidate is not in dictionary add them with an inital vote of zero
            candidate_votes[candidate] = 0

        # If candidate is in dictionary add their vote by 1
        candidate_votes[candidate] += 1

# Find the winner by finding the candidate with the most amount of votes by using max function
winner = max(candidate_votes, key=candidate_votes.get)


# Print out the results of the election
print("Election Results")
print("----------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------")

# Start a loop that will go through each candidate with their vote count
for candidate, votes in candidate_votes.items():

    # Calculate percentage of total votes that each candidate recieved
    percent = (votes / total_votes) * 100

    # Write a print statement that prints our candidate's name plus the percentage of their votes round by 2 places and add their total number of votes
    print(f"{candidate}: {percent:.2f}% ({votes})")

# Print out the name of the candidates with the highest number of votes
print("----------------------------")
print(f"Winner: {winner}")
print("----------------------------")



# Use a with statement to open the output file for writing using w mode.
with OUTPUT_PATH.open("w") as file:
    # Write out election results to the file using the same format as the printed output
    file.write("Election Results\n")
    file.write("----------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("----------------------------\n")

# Start a loop that will go through each candidate with their vote count
    for candidate, votes in candidate_votes.items():

         # Calculate percentage of total votes that each candidate recieved
        percent = (votes / total_votes) * 100
        file.write(f"{candidate}: {percent:.2f}% ({votes})\n")

    # Print out the name of the candidates with the highest number of votes
    file.write("----------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("----------------------------\n")






