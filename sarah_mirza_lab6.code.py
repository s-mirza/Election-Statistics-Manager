"""

Author: Sarah Mirza

Program Title: Election Statisics

File Description:

Using code to produce statistics for the lection input provided.

"""

def load_data(file_name):
    file = open(file_name, "r")

    candidates = []
    votes = []

    line = file.readline()

    while(line != ''):
        candidate, vote_count = line.split(",")
        candidates.append(candidate)
        votes.append(int(vote_count))
        line = file.readline()

    file.close()

    return candidates, votes

def LookupCandidateCount(search_name, names, votes):
    result = ''
    for i in range(len(names)):
        if names[i] == search_name:
            print(f"{search_name} drew {votes[i]} in this election")
            result = 'found'
    if result != 'found':
        print("Error: Could not find this candidate in the data.")

def GetElectionWinner(votes):
    max_votes = max(votes)
    return votes.index(max_votes)


def GetTotalVotes(votes):
    total_votes = sum(votes)
    return total_votes


def DisplayElectionStatistics(names, votes):
    total_votes = GetTotalVotes(votes)
    print("     Candidate      Votes Received     % of votes")
    print("-----------------------------------------------------")
    for i in range(len(names)):
        percentage = (votes[i] / total_votes) * 100
        print(f"{names[i]:^20}{votes[i]:^12}{percentage:>13.2f}%")

    

def main():
    candidates, votes = load_data("candidate_votes.txt")
    
    choice = -1
    
    while choice != 4:
        print("Main Menu")
        print("1. Candidate Count Lookup")
        print("2. Get Election Winner")
        print("3. Display Election Statistics")
        print("4. Exit Program")

        choice = int(input("--: "))

        while(choice < 1 or choice > 4):
            choice = int(input("Invalid choice. Type again  --: "))

        print()
    

        if(choice == 1):
            search_name = input("Enter your candidate's last name: ")
            LookupCandidateCount(search_name, candidates, votes)
        
        elif choice == 2:
            winner_index = GetElectionWinner(votes)
            max_votes = votes[winner_index]
            print(f"The winner of this election is {candidates[winner_index]} with {max_votes} votes.")


        elif choice == 3:
            DisplayElectionStatistics(candidates, votes)

        elif choice == 4:
            return
        
        print()

           


main()