import random

i = 1
streak = 0
computer_streak = 0
computer = ["rock", "paper", "scissors"]
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

try:
    rounds = int(input("How many rounds would you like to play: "))
except:
    print("Please enter a number")

while i <=rounds:
    print("Choose rock, paper, or scissors ")
    print(rock + paper + scissors)
    user_input = input ("Enter your choice: ")
    user_input=(user_input.lower())
    print("You choose " + user_input)
    if user_input not in ("rock", "paper", "scissors"):
        print("Please enter only rock, paper, or scissors")
        break


    computer_choice = random.choice(computer)
    print("The computer chooses " + computer_choice)

    if user_input == "rock" and computer_choice == "scissors":
        print("You win!")
        streak += 1
        
    elif user_input == "paper" and computer_choice == "rock":
        print("You win!")
        streak += 1
        
    elif user_input == "scissors" and computer_choice == "paper":
        print("You win!")
        streak += 1
        
    elif user_input == "paper" and computer_choice == "paper":
        print("You tied!")
    elif user_input == "rock" and computer_choice == "rock":
        print("You tied!")
    elif user_input == "scissors" and computer_choice == "scissors":
        print("You tied!")
    else:
        print("You lose!")
        
        computer_streak +=1

    print("Score: " + str(streak))
    print("Computer score: " + str(computer_streak))


    print("-----------------")
   
    i += 1

if streak > computer_streak:
    print("You win!")
elif streak == computer_streak:
    print("You tied!")
else:
    print("You lost!")

    