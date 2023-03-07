# Tic Tac Toe (random)
# Created by: Dylan Prole 
# Time taken: 45 minutes

import numpy as np
import random 
from time import sleep

def print_board(board):
    print('-------------')
    for i in range(3):
        print('| ', end='')
        for j in range(3):
            print(board[i][j], end=' | ')
        print()
        print('-------------')
        
def create_board():
    board = np.zeros((3,3), dtype=str)
    n = 1
    for i in range(3):
        for j in range(3):
            board[i][j] = str(n)
            n += 1
    return board
    
def change_board(board, pos, player):
    if int(board[(pos-1)//3][(pos-1)%3]) in range(10):
        board[(pos-1)//3][(pos-1)%3] = player

def check_win(board):
    # Check row/column wins
    for i in range(3):
        row_value = board[i][0]
        column_value = board[0][i]
        if (board[i][1] == row_value and board[i][2] == row_value):
            if row_value == 'O':
                return True, 'computer'
            if row_value == 'X':
                return True, 'player'
        if (board[1][i] == column_value and board[2][i] == column_value):
            if column_value == 'O':
                return True, 'computer'
            if column_value == 'X':
                return True, 'player'
    # Check diagonal wins
    diagonal_value = board[1][1]
    if (board[0][0] == diagonal_value and board[2][2] == diagonal_value) or (board[0][2] == diagonal_value and board[2][0] == diagonal_value):
        if diagonal_value == 'O':
            return True, 'computer'
        if diagonal_value == 'X':
            return True, 'player'
    return (False, 'None')
    
def check_draw(board):
    valid_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in range(3):
        for j in range(3):
            if board[i][j] in valid_list:
                return False
    return True
        
def get_score(board):
    row_scores = [[0,0,0], [['1','2','3'], ['4','5','6'], ['7','8','9']]]
    col_scores = [[0,0,0], [['1','4','7'], ['2','5','8'], ['3','6','9']]]
    dia_scores = [[0,0], [['1','5','9'],['3','5','7']]]
    
    # row scores
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X':
                row_scores[0][i] += 1
            if board[i][j] == 'O':
                row_scores[0][i] -= 1
            
        
symbols = {'player':'X', 'computer':'O'}
new_board = create_board()

turn = 'player'
win, player = check_win(new_board)

while not win:
    if check_draw(new_board):
        break
    print_board(new_board)
    if turn == 'player':
        # do something
        valid_input = False
        while not valid_input:
            position = input('Enter a pos: ')
            if str(position) in new_board:
                valid_input = True
        change_board(new_board, int(position), symbols[turn])
        win, player = check_win(new_board)
        turn = 'computer'
    
    elif turn == 'computer':
        # do something
        print('Computer is thinking....')
        sleep(2)
        valid_input = False
        while not valid_input:
            position = int(random.random()*9)
            if str(position) in new_board:
                valid_input = True
        change_board(new_board, position, symbols[turn])
        win, player = check_win(new_board)
        turn = 'player'
    
if player == 'player':
    print('You win!')
elif player == 'computer':
    print('You lose sorry bro :/')
else:
    print("It's a draw!")
print_board(new_board)
