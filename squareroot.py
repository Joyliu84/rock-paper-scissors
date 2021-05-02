def square_root(number):
    i = 1
    while i <= number:
            
        answer = number / i

        if answer == i:
            print("The squareroot of " +  str(number) + " is " + str(answer))
            return answer
            
        


        i += 1

    if answer != i:       
        print("The number you entered does not have a squareroot")
    else:
        print("Please enter a positive whole number")


x=6+square_root(9)

print(square_root(9))
