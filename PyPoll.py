# Add dependencies
import csv
import os

# Assign variables to load and save file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter, candidate options, and candidate votes
total_votes = 0
candidate_options = []
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data: 
    file_reader = csv.reader(election_data)
    headers = next(file_reader) # Read the header row.

    # Print each row in the CSV file.
    for row in file_reader:
        total_votes += 1 # Add to the total vote count.
        candidate_name = row[2] # Print the candidate name from each row

        # If the candidate does not match any existing candidate add to the list of candidates.
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
        # Add vote to candidate's vote count.
        candidate_votes[candidate_name] += 1



# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
# Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)


    # Determine the percentage of votes for each candidate:  
    # Loop through counts & Iterate through the candidate list.
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name] # Retrieve vote count of a candidate.
        vote_percentage = float(votes) / float(total_votes) * 100 # Calculate the percentage of votes.
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name


    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)
