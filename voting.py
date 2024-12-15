# ABEGAIL ROSE S. BAUTISTA
# KYLE PANGANIBAN
# JOJIT AUSTRIACO
# ONLINE VOTING SYSTEM

# Step 1: Get the number of voters with validation
while True:
    try:
        number_of_voters = int(input("Enter the number of voters: "))
        if number_of_voters > 0:
            break
        else:
            print("Please enter a positive number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Function to validate if the input contains only letters or a single-letter initial with a period
def validate_name(name):
    if not (name.isalpha() or (len(name) == 2 and name[0].isalpha() and name[1] == ".")):
        print("Invalid input. Please enter a valid name without numbers.")
        return False
    return True

# Function to display candidates for President
def name_candidates_president():
    print("Candidates for President:")
    candidates_president = ["Emjay Servan", "June Garcia", "Alexis Balmores"]
    for i, candidate in enumerate(candidates_president, start=1):
        print(f"[{i}] {candidate}")

# Function to display candidates for Vice President
def name_candidates_vice_president():
    print("\nCandidates for Vice President:")
    candidates_vice_president = ["Rhengel Argal", "Ian Quilala", "Justine Sauli"]
    for i, candidate in enumerate(candidates_vice_president, start=1):
        print(f"[{i}] {candidate}")

# Function to display candidates for Secretary
def name_candidates_secretary():
    print("\nCandidates for Secretary:")
    candidates_secretary = ["Wendy Ortega", "Heven Calica", "Gracia Balaoag"]
    for i, candidate in enumerate(candidates_secretary, start=1):
        print(f"[{i}] {candidate}")

# Step 2: Initialize vote counts to 0 for each candidate
votes = {
    "president": [0, 0, 0],  # Emjay, June, Alexis
    "vice_president": [0, 0, 0],  # Rhengel, Ian, Justine
    "secretary": [0, 0, 0],  # Wendy, Heven, Gracia
}

# Step 3: Loop through each voter
for voter in range(number_of_voters):
    print(f"\nVoter {voter + 1} Info:")

    # Get voter's first name, middle name, and last name with validation
    while True:
        nameone = input("Enter Your First Name: ")
        if validate_name(nameone):
            break

    while True:
        nametwo = input("Enter Your Middle Name: ")
        if validate_name(nametwo):
            break

    while True:
        namethree = input("Enter Your Last Name: ")
        if validate_name(namethree):
            break

    # Get voter's age with validation
    while True:
        try:
            age = int(input("Enter Your Age: "))
            if age > 0:
                break
            else:
                print("Please enter a valid positive number for age.")
        except ValueError:
            print("Invalid input. Please enter a valid number for age.")

    # Step 4: Function to check if the voter is qualified to vote
    def voters_info(firstname, middlename, lastname, age):
        print(f"\nHello, {firstname} {middlename} {lastname}")
        if age < 18:
            print("You are not yet eligible to vote.")
            return False
        else:
            print("You are eligible to vote!")
            return True

    # Step 5: If the voter is eligible, they proceed to vote
    if voters_info(nameone, nametwo, namethree, age):
        # Vote for President
        while True:
            name_candidates_president()
            try:
                vote_president = int(input("Enter the number of the candidate you would like to vote for (President): "))
                if 1 <= vote_president <= 3:
                    votes["president"][vote_president - 1] += 1
                    print(f"You voted for candidate {vote_president}!")
                    break
                else:
                    print("Invalid choice. Please select a valid number.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        # Vote for Vice President
        while True:
            name_candidates_vice_president()
            try:
                vote_vice_president = int(input("Enter the number of the candidate you would like to vote for (Vice President): "))
                if 1 <= vote_vice_president <= 3:
                    votes["vice_president"][vote_vice_president - 1] += 1
                    print(f"You voted for candidate {vote_vice_president}!")
                    break
                else:
                    print("Invalid choice. Please select a valid number.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        # Vote for Secretary
        while True:
            name_candidates_secretary()
            try:
                vote_secretary = int(input("Enter the number of the candidate you would like to vote for (Secretary): "))
                if 1 <= vote_secretary <= 3:
                    votes["secretary"][vote_secretary - 1] += 1
                    print(f"You voted for candidate {vote_secretary}!")
                    break
                else:
                    print("Invalid choice. Please select a valid number.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    else:
        print("You are underage.")

# Step 9: Display the results for each candidate
print("\nElection Results:")
print("\nTotal Votes for Presidential Candidates:")
print(f"Emjay Servan: {votes['president'][0]}")
print(f"June Garcia: {votes['president'][1]}")
print(f"Alexis Balmores: {votes['president'][2]}")

print("\nTotal Votes for Vice Presidential Candidates:")
print(f"Rhengel Argal: {votes['vice_president'][0]}")
print(f"Ian Quilala: {votes['vice_president'][1]}")
print(f"Justine Sauli: {votes['vice_president'][2]}")

print("\nTotal Votes for Secretary Candidates:")
print(f"Wendy Ortega: {votes['secretary'][0]}")
print(f"Heven Calica: {votes['secretary'][1]}")
print(f"Gracia Balaoag: {votes['secretary'][2]}")

# Step 10: Announce the winners
def announce_winner(category, candidates):
    max_votes = max(category)
    if category.count(max_votes) > 1:
        print("It's a tie!")
    else:
        winner_index = category.index(max_votes)
        print(f"The winner is {candidates[winner_index]}!")

print("\nPresident:")
announce_winner(votes["president"], ["Emjay Servan", "June Garcia", "Alexis Balmores"])

print("\nVice President:")
announce_winner(votes["vice_president"], ["Rhengel Argal", "Ian Quilala", "Justine Sauli"])

print("\nSecretary:")
announce_winner(votes["secretary"], ["Wendy Ortega", "Heven Calica", "Gracia Balaoag"])