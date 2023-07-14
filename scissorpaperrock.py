import random

user_action = input("enter your choice(rock,paper,scissor):")
possible_action = ["rock","paper","scissor"]
computer_action = random.choice(possible_action)
print(f"\nyou choose {user_action} and the computer chose {computer_action}.\n")
if user_action == computer_action:
     print("you both chose same so it's a tie")
elif user_action == "rock":
    if computer_action == "scissor":
        print("rock smashes the  scissor So You win!")
    else:
        print("you lose!")
elif user_action =="paper":
     if computer_action == "rock":
        print("The  paper covers the rock So You win!")
     else:
        print("you lose!")
elif user_action == "scissor":
     if computer_action == "paper":
        print("scissors cuts the  paper So You win!")
     else:
        print("You lose!")
