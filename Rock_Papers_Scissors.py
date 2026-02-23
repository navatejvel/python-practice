import random

def determine_winner(player_choice, computer_choice):
    print(f"\nYou chose {player_choice}, computer chose {computer_choice}.")

    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "scissors" and computer_choice == "paper") or \
         (player_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "Computer wins!"


choices = ["rock", "paper", "scissors"]
player_input = input("Enter a choice (rock, paper, scissors): ").lower
computer_pick = random.choice(choices)


if player_input in choices:
  result = determine_winner(player_input, computer_pick)
  print(result)
else:
  print("Invalid choice. Please enter rock, paper, or scissors.")
