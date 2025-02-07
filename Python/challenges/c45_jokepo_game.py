import random

print("---" * 10)
print("JAKEPO")
print("---" * 10)

# Game instructions and rules
print("*Game Instructions*")
print("You start with 3 points")
print("Each win = +1 point | Each loss = -1 point")
print("If you reach 6 points, you WIN :)\nIf you drop to 0 points, you LOSE :(")
print("A - Rock(1) beats Scissors(3) (by smashing it)")
print("B - Scissors(3) beat Paper(2) (by cutting it)")
print("C - Paper(2) beats Rock(1) (by wrapping it)")

# Initialize points and match counter
points = 3
match = 1

# Game loop
while 0 < points < 6:
    try:
        print("\nLET'S START:")
        print(f"Match: {match}")
        print(f"Points: {points}")
        print("1 - Rock")
        print("2 - Paper")
        print("3 - Scissors")
        
        # User choice
        user_choice = int(input("Choose an option: "))

        # Validate user input
        if user_choice < 1 or user_choice > 3:
            print("Error! Please choose a valid number (1 - 3)")
            continue

    except ValueError:
        print("Error! Please enter a valid number")
        continue

    # System random choice
    system_choice = random.randint(1, 3)

    # Map choices to names
    choices = {1: "1 - Rock", 2: "2 - Paper", 3: "3 - Scissors"}
    user_choice_name = choices[user_choice]
    system_choice_name = choices[system_choice]

    # Display choices
    print(f"You chose: {user_choice_name}")
    print(f"The system chose: {system_choice_name}")

    # Determine outcome
    if user_choice == system_choice:
        print("It's a draw! :| Try again.")
    else:
        # Winning conditions
        if ((user_choice == 1 and system_choice == 3) or
            (user_choice == 2 and system_choice == 1) or
            (user_choice == 3 and system_choice == 2)):
            print(f"You won match {match}! :)\n")
            points += 1
        # Losing conditions
        else:
            print(f"You lost match {match}! :(\n")
            points -= 1

        # Increment match counter
        match += 1

# Check end-game conditions
if points == 6:
    print("Congratulations! You won the game! :)")
elif points == 0:
    print("Game over! You lost. :(")