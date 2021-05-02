hundred = []

number = 2 




def prime_number(number):

    print("Prime number")

    if number <= 0:
        print("Please enter a positive number")
    elif number == 1:
        print("The number you entered is not a prime number")
        return False
    elif number == 2:
        print("The number you entered is a prime number")
        return True
    p = 0

    i = 2

    while i <= (number - 1):

        answer = number % i
    

        if answer != 0:

                p += 1
        else:

            print("The number you entered is not a prime number")
            return False
            break 

        i += 1
            

        if p == number-2:

            print("The number you entered is a prime number")
            return True

while len(hundred) <= 99:
    if prime_number(number):
        hundred.append(number)
    number += 1

print(hundred)