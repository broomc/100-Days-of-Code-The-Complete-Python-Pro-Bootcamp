#Rock Paper Scissor Game
import random

player_choice = input("Please enter Rock, Paper or Scissors\n").lower()
print(player_choice)

options = ["rock","paper","scissors"]
computer_choice = random.choice(options)
print(computer_choice)

if (player_choice == computer_choice):
    print("It's a draw game ")
elif (player_choice == "rock" and computer_choice == "scissors"):
    print("You Win , Rock Beats Scissors")
elif (player_choice == "scissors" and computer_choice == "rock"):
    print("Computer Wins , Rock Beats Scissors")
