# Guess the number (computer)
# Created by: Dylan Prole 
# Time taken: 15 minutes

from time import sleep

print("Think of a number between 0 and 100 and I'll guess it in 7 or less guesses...")
sleep(2)

number = 50
lower = -1
upper = 101

guessed = False

guesses = 1

while guesses < 8:
    valid_input = False
    while not valid_input:
        result = input(f"(Guess {guesses}) Is {number} too high, too low, or correct (low, high, correct)?: ")
        if result in ['low', 'high', 'correct']:
            valid_input = True
            guesses += 1
        else:
            print("INVALID INPUT! TRY AGAIN!")

    if result == 'low':
        lower = number
        number = (lower + upper)//2
    elif result == 'high':
        upper = number
        number = (lower + upper)//2
    elif result == 'correct':
        print("Fantastic!")
        guessed = True
        break

if not guessed:
    print("ARRRGHHH I FAILED!! ARRRGHHHH!!")