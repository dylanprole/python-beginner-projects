import string
import random

board_size = 10

def create_board(board_size):
    return ['?']*board_size*board_size

def create_mines(board_size, first_move):
    mine_board = [' ']*board_size*board_size
    mine_count = board_size
    while mine_count > 0:
        print(f'Mine number {mine_count}', end='; ')
        loc = int(random.random()*(len(mine_board)-0.01))
        print(f'New location = {loc}', end='; ')
        if mine_board[loc] != 'M' and loc != first_move:
            print('adding mine here....')
            mine_board[loc] = 'M'
            mine_count -= 1
    return mine_board

def create_mapping(board_size):
    '''
    board_size: (int): size of the board
    returns: (dict) Mapping for the coordinates to location in the board array
    '''
    mapping = {}
    letters = string.ascii_lowercase[:board_size]
    loc = 0
    for num in range(board_size):
        for letter in letters:
            mapping[letter+str(num)] = loc
            loc += 1
    return mapping

def calc_mine_numbers(mine_board, board_size):
    mine_count_board = mine_board[:]

    adjacent_regular = [-11, -10, -9, -1, 1, 9, 10, 11]
    adjacent_left_edge = [-10, -9, 1, 10, 11]
    adjacent_right_edge = [-11, -10, -1, 9, 10]
    adjacent_top_edge = [-1, 1, 9, 10, 11]
    adjacent_bottom_edge = [-11, -10, -9, -1, 1]
    adjacent_top_left = [1, 10, 11]
    adjacent_top_right = [-1, 9, 10]
    adjacent_bottom_left = [-10, -9, 1]
    adjacent_bottom_right = [-11, -10, -1]

    for loc in range(board_size*board_size):
        if loc == 0:
            adjacent = adjacent_top_left
        elif loc == board_size - 1:
            adjacent = adjacent_top_right
        elif loc == (board_size * board_size) - board_size:
            adjacent = adjacent_bottom_left
        elif loc == (board_size * board_size) - 1:
            adjacent = adjacent_bottom_right
        elif loc < board_size:
            adjacent = adjacent_top_edge
        elif loc % board_size == 0:
            adjacent = adjacent_left_edge
        elif (loc + 1) % board_size == 0:
            adjacent = adjacent_right_edge
        elif loc >= (board_size * board_size) - board_size:
            adjacent = adjacent_bottom_edge
        else:
            adjacent = adjacent_regular

        mine_count = 0
        if mine_count_board[loc] != 'M':
            for num in adjacent:
                if mine_count_board[loc + num] == 'M':
                    mine_count += 1
            mine_count_board[loc] = str(mine_count)

    return mine_count_board

def add_flag(board, mapping, pos):
    loc = mapping[pos]
    if board[loc] == '?':
        board[loc] = 'F'
    return board

def remove_flag(board, mapping, pos):
    loc = mapping[pos]
    if board[loc] == 'F':
        board[loc] = '?'
    return board

def adjacents(loc, board_size):
    adjacent_regular = [-11, -10, -9, -1, 1, 9, 10, 11]
    adjacent_left_edge = [-10, -9, 1, 10, 11]
    adjacent_right_edge = [-11, -10, -1, 9, 10]
    adjacent_top_edge = [-1, 1, 9, 10, 11]
    adjacent_bottom_edge = [-11, -10, -9, -1, 1]
    adjacent_top_left = [1, 10, 11]
    adjacent_top_right = [-1, 9, 10]
    adjacent_bottom_left = [-10, -9, 1]
    adjacent_bottom_right = [-11, -10, -1]

    if loc == 0:
        adjacent = adjacent_top_left
    elif loc == board_size - 1:
        adjacent = adjacent_top_right
    elif loc == (board_size * board_size) - board_size:
        adjacent = adjacent_bottom_left
    elif loc == (board_size * board_size) - 1:
        adjacent = adjacent_bottom_right
    elif loc < board_size:
        adjacent = adjacent_top_edge
    elif loc % board_size == 0:
        adjacent = adjacent_left_edge
    elif (loc + 1) % board_size == 0:
        adjacent = adjacent_right_edge
    elif loc >= (board_size * board_size) - board_size:
        adjacent = adjacent_bottom_edge
    else:
        adjacent = adjacent_regular
    
    return adjacent

def propogate_clearing(board, mine_numbers):
    adjacent_regular = [-11, -10, -9, -1, 1, 9, 10, 11]
    adjacent_left_edge = [-10, -9, 1, 10, 11]
    adjacent_right_edge = [-11, -10, -1, 9, 10]
    adjacent_top_edge = [-1, 1, 9, 10, 11]
    adjacent_bottom_edge = [-11, -10, -9, -1, 1]
    adjacent_top_left = [1, 10, 11]
    adjacent_top_right = [-1, 9, 10]
    adjacent_bottom_left = [-10, -9, 1]
    adjacent_bottom_right = [-11, -10, -1]

    cleared = False
    while not cleared:
        print('Checking cells to propogate....')
        cleared = True
        for loc in range(len(board)):
            print(f'Cell {loc} is a {board[loc]} on main board, and has a {mine_numbers[loc]} for mine number.')
            if board[loc] == ' ' and mine_numbers[loc] == '0':
                print('Identified cell to propogate outwards...')
                if loc == 0:
                    adjacent = adjacent_top_left
                elif loc == board_size - 1:
                    adjacent = adjacent_top_right
                elif loc == (board_size * board_size) - board_size:
                    adjacent = adjacent_bottom_left
                elif loc == (board_size * board_size) - 1:
                    adjacent = adjacent_bottom_right
                elif loc < board_size:
                    adjacent = adjacent_top_edge
                elif loc % board_size == 0:
                    adjacent = adjacent_left_edge
                elif (loc + 1) % board_size == 0:
                    adjacent = adjacent_right_edge
                elif loc >= (board_size * board_size) - board_size:
                    adjacent = adjacent_bottom_edge
                else:
                    adjacent = adjacent_regular

                for num in adjacent:
                    print('Checking adjacent cells.....')
                    if board[loc + num] == '?' and mine_numbers[loc + num] != 'M':
                        print(f'Adjacent cell {loc + num} is a {board[loc + num]} on main board, and has a {mine_numbers[loc + num]} for mine number.')
                        print('Clearing....')
                        if mine_numbers[loc + num] == '0':
                            board[loc + num] = ' '
                        else:
                            board[loc + num] = mine_numbers[loc + num]
                        cleared = False
            print('-----------')
    return board

def clear_space(board, mine_numbers, mapping, pos):
    loc = mapping[pos]
    # Reveal number below space
    if mine_numbers[loc] == 'M':
        board[loc] = 'X'
        return False, board
    elif mine_numbers[loc] == '0':
        board[loc] = ' '
    else:
        board[loc] = mine_numbers[loc]

    # Propogate clearing
    board = propogate_clearing(board, mine_numbers)

    return True, board

def print_board(board, board_size):
    letters = string.ascii_lowercase[:board_size]
    print('   || ', end='')
    for c in letters:
        print(c, end=' | ')
    print()
    print('----' + '----'*board_size + '-')
    for i in range(board_size):
        print(' ', end='')
        print(i, end=' || ')
        for j in range(board_size):
            print(board[board_size*i + j], end=' | ')
        print()
        print('----' + '----'*board_size + '-')



new_mapping = create_mapping(board_size)        
new_board = create_board(board_size)
print_board(new_board, board_size)
print()
new_mines = create_mines(board_size, 0)
print_board(new_mines, board_size)
print()
new_mine_numbers = calc_mine_numbers(new_mines, board_size)
print_board(new_mine_numbers, board_size)
print()
safe, new_board = clear_space(new_board, new_mine_numbers, new_mapping, 'b0')
print_board(new_board, board_size)
if not safe:
    print('You lose :(')