#import dependencies as usual
import os
import csv

#initialize some variables
candidates = []
num_votes = 0
vote_counts = []

#set path for csv
filepath = os.path.join('Resources', 'election_data.csv')

#open the file
with open(filepath,newline="") as csvfile:
    csvreader = csv.reader(csvfile)
    #skip the header
    line = next(csvreader,None)
    #go through each row, reading each vote
    for row in csvreader:
        #add to total number of votes
        num_votes = num_votes + 1
        #candidate voted for
        candidate = row[2]
        if candidate in candidates:#candidate has other votes then add to vote tally
            candidate_index = candidates.index(candidate)
            vote_counts[candidate_index] = vote_counts[candidate_index] + 1
        else:#create new spot in list for candidate
            candidates.append(candidate)
            vote_counts.append(1)
percentages = []
max_votes = vote_counts[0]
max_index = 0
#find percentage of vote for each candidate and the winner
for count in range(len(candidates)):
    vote_percentage = vote_counts[count]/num_votes*100
    percentages.append(vote_percentage)
    if vote_counts[count] > max_votes:
        max_votes = vote_counts[count]
        print(max_votes)
        max_index = count
winner = candidates[max_index]
#print results
print("Election Results")
print("--------------------------")
print(f"Total Votes: {num_votes}")
for count in range(len(candidates)):
    print(f"{candidates[count]}: {percentages[count]}% ({vote_counts[count]})")
print("---------------------------")
print(f"Winner: {winner}")
print("---------------------------")

#print analysis to text file
poll_file = os.path.join("Analysis", "poll_analysis.txt")
with open(poll_file, "w") as outfile:
    outfile.write("Election Results\n")
    outfile.write("--------------------------\n")
    outfile.write(f"Total Votes: {num_votes}\n")
    for count in range(len(candidates)):
        outfile.write(f"{candidates[count]}: {percentages[count]}% ({vote_counts[count]})\n")
    outfile.write("---------------------------\n")
    outfile.write(f"Winner: {winner}\n")
    outfile.write("---------------------------\n")
