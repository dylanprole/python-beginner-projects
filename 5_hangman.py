# Hangman
# Created by: Dylan Prole 
# Time taken: 40 minutes

import string
import random

WORD_LIST = ['peanut', 'flower', 'horse', 'dog']

def is_valid_letter(letter, letters_guessed):
    '''
    letter (str): any letter entered by the user
    letters_guessed (list): list (of letters), which letters have been guessed
    output: True or False
    '''
    letter = letter.lower()
    if len(letter) != 1:
        return False
    elif letter in letters_guessed:
        return False
    elif letter in string.ascii_lowercase:
        return True
    else:
        return False
    
    
def update_tiles(secret_word, letters_guessed):
    '''
    secret_word (str): word the user is guessing
    letters_guessed (list): list (of letters), which letters have been guessed
    returns: list, updated tiles if new letters have been guessed, or same
    '''
    tiles = []
    for letter in secret_word:
        if letter in letters_guessed:
            tiles.append(letter)
        else:
            tiles.append('_')
    return tiles
    
def print_tiles(tiles, letters_guessed, turns_left):
    '''
    tiles (list): the tiles of letters which have and have not been guessed
    letters_guessed (list): list (of letters), which letters have been guessed
    turns_left (int): The remaining turns left for player
    returns: Nothing, prints current tiles to output
    '''
    print('CURRENT TILES')
    for tile in tiles:
        print(tile, end=' ')
    print()
    print('Letters already guessed: ', end='')
    for letter in letters_guessed:
        print(letter, end=' ')
    print()
    print('Turns left: ', end ='')
    print(str(turns_left))
    
def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word (str): word the user is guessing
    letters_guessed (list): list (of letters), which letters have been guessed
    returns: boolean, true if all guessed letters are in word
    '''
    word_guessed = True
    for c in secret_word:
        if c not in letters_guessed:
            word_guessed = False
    return word_guessed
            
if __name__ == '__main__':
    secret_word = WORD_LIST[int(random.random()*(len(WORD_LIST)-0.01))]
    turns = len(secret_word) + 5
    letters_guessed = []
    while turns > 0:
        tiles = update_tiles(secret_word, letters_guessed)
        if is_word_guessed(secret_word, letters_guessed):
            print('Congrats you win!!')
            print(f'The word was: {secret_word}')
            break
        print_tiles(tiles, letters_guessed, turns)
        valid_input = False
        while not valid_input:
            guessed_letter = input('Enter a letter: ')
            if is_valid_letter(guessed_letter, letters_guessed):
                valid_input = True
                letters_guessed.append(guessed_letter)
        turns -= 1
    if turns == 0:
        print('Wuh-wuh you lose :(')
