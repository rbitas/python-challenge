import csv
import os 

# path
election_path = os.path.join("/Users/rinabitas/Documents/python-challenge/PyPoll/Resources/election_data.csv")
election_path_txt = os.path.join ("/Users/rinabitas/Documents/python-challenge/PyPoll/analysis/election_data.txt")

# define variables
total_votes = 0 
total_candidates = 0 
winner_votes = 0
greatest_vote = ["", 0]
list_candidates = []
votes_for_candidate ={}

with open(election_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)

    for row in csvreader:
        total_votes = total_votes + 1
        total_candidates = row[2]

        if total_candidates not in list_candidates:
            list_candidates.append(total_candidates)
            votes_for_candidate[total_candidates] = 1
        else:
            votes_for_candidate[total_candidates] = votes_for_candidate[total_candidates] + 1

    if total_votes > winner_votes:
        greatest_vote[1] = votes_for_candidate
        greatest_vote[0] = row[2] 

    for candidate in votes_for_candidate:
        print(candidate + " " + str(round(((votes_for_candidate[candidate]/total_votes)*100))) + "%" + " (" + str(votes_for_candidate[candidate]) + ")")

        if total_votes > winner_votes:
            greatest_vote[1] = votes_for_candidate
            greatest_vote[0] = row[2] 

# print to the terminal      
winner = sorted(votes_for_candidate.items(),)
print("Total Votes: " + str(total_votes))
print("Winner: " + str(winner[1]))


# output to txt file
with open(election_path_txt, "w") as txt_file:
    txt_file.write("Election Results")
    txt_file.write("\n")
    txt_file.write("----------------------------------")
    txt_file.write("\n")
    txt_file.write("Total Votes: " + str(total_votes))
    txt_file.write("\n")
    txt_file.write("----------------------------------")
    txt_file.write("\n")
    txt_file.write(candidate + " " + str(round(((votes_for_candidate[candidate]/total_votes)*100))) + "%" + " (" + str(votes_for_candidate[candidate]) + ")")
    txt_file.write(str(winner))
    txt_file.write("\n")
    txt_file.write("----------------------------------")
    txt_file.write("\n")
    txt_file.write("Winner: " + str(winner[1]))




