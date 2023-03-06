# Guess the number (computer)
# Created by: Dylan Prole 
# Time taken: 10 minutes

from random import random

psr_choices = ['p', 's', 'r']
psr_mapping = {'p':'paper', 's':'scissors', 
                'r':'rock'}

valid_input = False
while not valid_input:
    user_choice = input('Paper, Scissors, Rock...(p/s/r): ')
    if user_choice in psr_choices:
        valid_input = True
        
computer_choice = psr_choices[int(random()*2.99)]
    
if computer_choice == user_choice:
    print(f"The computer chose {psr_mapping[computer_choice]}, it's a draw!!")
elif (computer_choice == 'p' and user_choice == 'r') or (computer_choice == 's' and user_choice == 'p') or (computer_choice == 'r'
    and user_choice == 's'):
    print(f"The computer chose {psr_mapping[computer_choice]}, you lose!!")
else:
    print(f"The computer chose {psr_mapping[computer_choice]}, you win!!")