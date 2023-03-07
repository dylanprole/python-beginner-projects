# Hangman
# Created by: Dylan Prole 
# Time taken: x minutes (start 12:36)

import string

word_list = ['peanut', 'flower', 'horse', 'dog']

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
        print('The current letter being checked is: ', end='')
        print(letter, end=', ')
        if letter in letters_guessed:
            tiles.append(letter)
            print('It is in the letters guessed!')
        else:
            tiles.append('_')
            print('It is NOT the letters guessed :(')
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
    print('Turns left: ', end ='')
    print(str(turns_left))
    print('Letters already guessed: ', end='')
    for letter in letters_guessed:
        print(letter, end='')
    
    
    
def is_word_guessed():
    '''
    secret_word (str): word the user is guessing
    letters_guessed (list): list (of letters), which letters have been guessed
    returns: boolean, true if all guessed letters are in word
    '''
    
print_tiles(['c', '_', '_'], 5)
