import random

number = int(random.random() * 9) + 1

guessed = False

while not guessed:
    guess = int(input("Choose a number between 1 and 10: "))
    if guess < 1 or guess > 10:
        print("Out of bounds! Try again!")
    elif guess == number:
        print(f"Congrats! The answer was {number}!")
        guessed = True
    elif guess > number: 
        print("Too high! Try lower!")
    elif guess < number: 
        print("Too low! Try higher!")