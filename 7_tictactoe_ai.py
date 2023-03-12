# Tic Tac Toe (Unbeatable AI)
# Created by: Dylan Prole 
# Time taken: 90 minutes

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
            if board[i][j] == 'O':
                row_scores[0][i] += 1
            elif board[i][j] == 'X':
                row_scores[0][i] -= 1
    # col scores
    for j in range(3):
        for i in range(3):
            if board[i][j] == 'O':
                col_scores[0][j] += 1
            elif board[i][j] == 'X':
                col_scores[0][j] -= 1
    # dia scores
    for i in range(3):
        if board[i][i] == 'O':
            dia_scores[0][0] += 1
        elif board[i][i] == 'X':
            dia_scores[0][0] -= 1
        if board[2-i][i] == 'O':
            dia_scores[0][1] += 1
        elif board[2-i][i] == 'X':
            dia_scores[0][1] -= 1
    return row_scores, col_scores, dia_scores
    
def choose_pos(board):
    # Check if first turn
    new_board = True
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'O':
                new_board = False
                break
            elif board[i][j] == 'X':
                new_board = False
                break
    if new_board == True:
        return 1
    # Get current scores of board    
    row, col, dia = get_score(board)
    # Check if opponent has played first move in corner
    moves = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'O' or board[i][j] == 'X':
                moves += 1
    if moves == 1:
        if board[0][0] == 'X' or board[0][2] == 'X' or board[2][0] == 'X' or board[2][2] == 'X':
            return 5
    # If there are 2 of the same symbols in a streak, play in that streak
    if 2 in row[0]:
        for i in range(3): 
            if row[0][i] == 2:
                #get pos
                for pos in row[1][i]:
                    if pos in board:
                        return int(pos)
    if 2 in col[0]:
        for i in range(3):
            if col[0][i] == 2:
                #get pos
                for pos in col[1][i]:
                    if pos in board:
                        return int(pos)
    if 2 in dia[0]:
        for i in range(2):
            if dia[0][i] == 2:
                #get pos
                for pos in dia[1][i]:
                    if pos in board:
                        return int(pos)
    # If there are 2 player symbols in a streak, play to block
    if -2 in row[0]:
        for i in range(3): 
            if row[0][i] == -2:
                #get pos
                for pos in row[1][i]:
                    if pos in board:
                        return int(pos)
    if -2 in col[0]:
        for i in range(3):
            if col[0][i] == -2:
                #get pos
                for pos in col[1][i]:
                    if pos in board:
                        return int(pos)
    if -2 in dia[0]:
        for i in range(2):
            if dia[0][i] == -2:
                #get pos
                for pos in dia[1][i]:
                    if pos in board:
                        return int(pos)
    # Do a corner move if nothing else
    if '1' in board:
        return 1
    if '2' in board:
        if '3' in board:
            return 3
    elif '4' in board:
        if '7' in board:
            return 7
    elif '9' in board:
        return 9
    # Choose a random valid position otherwise
    valid_pos = False
    while not valid_pos:
        position = int(random.random()*9.99)
        if str(position) in board:
            valid_pos = True
            return position
        
symbols = {'player':'X', 'computer':'O'}
players = ['player', 'computer']
turn = players[int(random.random()*1.99)]

new_board = create_board()
win, player = check_win(new_board)

while not win:
    if check_draw(new_board):
        break
    
    if turn == 'player':
        print_board(new_board)
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
        position = choose_pos(new_board)
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
