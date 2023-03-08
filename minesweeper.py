import string
import random

board_size = 5

def create_board(board_size):
    return ['?']*board_size*board_size

def create_mines(board_size):
    mine_board = [' ']*board_size*board_size
    mine_count = board_size
    while mine_count > 0:
        print(f'Mine number {mine_count}', end='; ')
        loc = int(random.random()*(len(mine_board)-0.01))
        print(f'New location = {loc}', end='; ')
        if mine_board[loc] != 'M':
            print('adding mine here....')
            mine_board[loc] = 'M'
            mine_count -= 1
    return mine_board

def print_board(board, board_size):
    letters = string.ascii_lowercase[:board_size]
    print('   | ', end='')
    for c in letters:
        print(c, end=' | ')
    print()
    print('---' + '----'*board_size + '-')
    for i in range(board_size):
        print(' ', end='')
        print(i, end=' | ')
        for j in range(board_size):
            print(board[board_size*i + j], end=' | ')
        print()
        print('---' + '----'*board_size + '-')
        
new_board = create_board(board_size)
print(new_board)
new_mines = create_mines(board_size)
print(new_mines)
