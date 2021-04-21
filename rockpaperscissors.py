import random
import os


def display(graph):
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

    if graph == 0 or graph == "rock":
        print(rock)
    elif graph == 1 or graph == "paper":
        print(paper)
    elif graph == 2 or graph == "scissors":
        print(scissors)
    else:
        print("illegal input")


def who_win(human, machine):
    human = 0 if human == "rock" else 1 if human == "paper" else 2
    print("Your choice is ")
    display(human)
    print("Machine's choice is ")
    display(machine)

    if human == 0:
        if machine == 0:
            return 0
        elif machine == 1:
            return -1
        else:
            return 1
    elif human == 1:
        if machine == 0:
            return 1
        elif machine == 1:
            return 0
        else:
            return -1
    else:
        if machine == 0:
            return -1
        elif machine == 1:
            return 1
        else:
            return 0


i = 1
streak = 0
computer_streak = 0
computer = [_ for _ in range(3)]

while True:
    try:
        rounds = int(input("How many rounds would you like to play: "))
        break
    except:
        print("Please enter a number")

while i <= rounds:
    print("Choose rock, paper, or scissors ")
    # print(rock + paper + scissors)
    user_input = input("Enter your choice: ").lower()
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")
    print("You choose " + user_input)
    if user_input not in ("rock", "paper", "scissors"):
        print("Please enter only rock, paper, or scissors")
        continue

    computer_choice = random.choice(computer)
    round_winer = who_win(user_input, computer_choice)
    if round_winer == 1:
        streak += 1
        print("You win this time! 😇\n")
    elif round_winer == -1:
        print("You lose this time! ☠️\n")
        computer_streak += 1
    else:
        print("tied this time.\n")

    print("Your current score: " + str(streak))
    print("Computer current score: " + str(computer_streak))

    print("\n-----------------\n")

    i += 1

print("Your final score: " + str(streak))
print("Computer final score: " + str(computer_streak))
print("tied times is ", rounds-streak-computer_streak)
if streak > computer_streak:
    print("You win!")
elif streak == computer_streak:
    print("You tied!")
else:
    print("You lost!")
