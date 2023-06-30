#%%
import csv

# Read the CSV file
filename = "C:\\Users\\Isaac Technology\\election_data.csv"

# Initialize variables
total_votes = 0
candidates = {}
winner = ""
max_votes = 0

# Open the CSV file and iterate over the rows
with open(filename, 'r') as file:
    reader = csv.reader(file)

    # Skip the header row
    next(reader)

    for row in reader:
        # Increment the total vote count
        total_votes += 1

        # Get the candidate name from the row
        candidate = row[2]

        # Add the candidate to the dictionary if not present
        if candidate not in candidates:
            candidates[candidate] = 0

        # Increment the candidate's vote count
        candidates[candidate] += 1

# Define the output file path
output_file = "C:\\Users\\Isaac Technology\\vote_analysis.txt"

# Open the output file in write mode
with open(output_file, 'w') as file:
    # Print the total number of votes cast
    output = "Election Results\n"
    output += "-------------------------\n"
    output += "Total Votes: " + str(total_votes) + "\n"
    output += "-------------------------\n"

    # Print the complete list of candidates who received votes
    output += "Candidates:\n"
    for candidate in candidates:
        output += candidate + "\n"
    output += "-------------------------\n"

    # Calculate and print the percentage of votes each candidate won
    output += "Vote Percentage:\n"
    for candidate in candidates:
        vote_percentage = (candidates[candidate] / total_votes) * 100
        output += candidate + ": " + "{:.2f}%".format(vote_percentage) + "\n"
    output += "-------------------------\n"

    # Calculate the total number of votes each candidate won
    output += "Total Votes per Candidate:\n"
    for candidate in candidates:
        output += candidate + ": " + str(candidates[candidate]) + "\n"
    output += "-------------------------\n"

    # Determine the winner based on popular vote
    for candidate in candidates:
        if candidates[candidate] > max_votes:
            max_votes = candidates[candidate]
            winner = candidate

    # Print the winner of the election
    output += "Winner: " + winner + "\n"
    output += "-------------------------\n"

    # Print the analysis to the terminal
    print(output)

    # Write the analysis to the output file
    file.write(output)

print("Analysis has been exported to", output_file)