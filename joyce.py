import sys

i = 1
Fibonacci_sequence = [0, 1]
Fibonacci_list = []

try:
    rounds = int(input("How many th number of the Fibonacci sequence would you like to calculate: "))
    if rounds == 0:
        print("Please enter a positive number")
        
    elif rounds < 0:
        print("Please enter a positive number")
        
        

    number = rounds - 2

    if number == -1:
        print(0)
        print("[0]")
    elif number == 0:
        print(1)
        print("[0, 1]")


    while i <=number:

        
        num1 = Fibonacci_sequence[0]
        num2 = Fibonacci_sequence[1]
        num3 = num1 + num2

        Fibonacci_list.append(Fibonacci_sequence[0])
        
        Fibonacci_sequence.pop(0)
        Fibonacci_sequence.append(num3)
        i += 1

    print(num3)
    Fibonacci_list.append(num2)
    Fibonacci_list.append(num3)
    print(Fibonacci_list)
    
except:
    print("Please enter a number")

