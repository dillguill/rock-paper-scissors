import random

# Main game loop
while True:
    # Get and normalize user input
    my_answer = input("Choose - Rock, Paper, or Scissors: ").lower()

    # Check if the user wants to quit
    if my_answer == "quit":
        break

    # Validate user input using the 'in' operator
    valid_choices = ["rock", "paper", "scissors"]  # Array of valid choices
    if my_answer not in valid_choices:  # Compare string to an array
        print("Please choose a correct answer (rock, paper, or scissors).")
        continue

    # Computer's random choice
    computer_answer = random.choice(valid_choices)
    print(f"Computer chose: {computer_answer}")

    # Determine game outcome
    if my_answer == computer_answer:
        print("You tied!")
    elif (my_answer == "paper" and computer_answer == "rock") or \
         (my_answer == "rock" and computer_answer == "scissors") or \
         (my_answer == "scissors" and computer_answer == "paper"):
        print("You win!")
        break
    else:
        print("You lose. Try again!")