import random
n1=random.randint(1,100)

guess=int(input("Guess the Number:"))

while True:
    if(guess==n1):
        print("Successfully guessed the number")
        break
    elif(guess>n1):
        print("Try again")
        print("Number is too large")
        guess=int(input("Guess the Number:"))
    else:
        print("Try again")
        print("Number is too large")
        guess=int(input("Guess the Number:"))

        

