# Guess the number (computer)
# Created by: Dylan Prole 
# Time taken: 3 hours

import string
import random

board_size = 10

def create_board(board_size):
    return ['-']*board_size*board_size

def create_mines(board_size, first_move):
    mine_board = [' ']*board_size*board_size
    mine_count = (board_size*board_size)//8
    adjacent = get_adjacent(first_move, board_size)
    illegal_mine_loc = [first_move]
    for num in adjacent:
        illegal_mine_loc.append(first_move+num)
    while mine_count > 0:
        print(f'Mine number {mine_count}', end='; ')
        loc = int(random.random()*(len(mine_board)-0.01))
        print(f'New location = {loc}', end='; ')
        if mine_board[loc] != 'M' and loc not in illegal_mine_loc:
            print('adding mine here....')
            mine_board[loc] = 'M'
            mine_count -= 1
        else:
            print()
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

    for loc in range(len(mine_board)):
        print(f'Counting adjacent mines at location {loc}...')
        adjacent = get_adjacent(loc, board_size)
        mine_count = 0
        if mine_count_board[loc] != 'M':
            for num in adjacent:
                print(f'Checking adjacent cell {loc + num}...', end='')
                if mine_count_board[loc + num] == 'M':
                    mine_count += 1
                    print('mine found!!!')
                else:
                    print()
            mine_count_board[loc] = str(mine_count)
        print()

    return mine_count_board

def add_flag(board, mapping, pos):
    loc = mapping[pos]
    if board[loc] == '-':
        board[loc] = 'F'
    return board

def remove_flag(board, mapping, pos):
    loc = mapping[pos]
    if board[loc] == 'F':
        board[loc] = '-'
    return board

def get_adjacent(loc, board_size):
    adjacent_regular = [-(board_size + 1), -board_size, -(board_size - 1), -1, 1, (board_size - 1), board_size, (board_size + 1)]
    adjacent_left_edge = [-board_size, -(board_size - 1), 1, board_size, (board_size + 1)]
    adjacent_right_edge = [-(board_size + 1), -board_size, -1, (board_size - 1), board_size]
    adjacent_top_edge = [-1, 1, (board_size - 1), board_size, (board_size + 1)]
    adjacent_bottom_edge = [-(board_size + 1), -board_size, -(board_size - 1), -1, 1]
    adjacent_top_left = [1, board_size, (board_size + 1)]
    adjacent_top_right = [-1, (board_size - 1), board_size]
    adjacent_bottom_left = [-board_size, -(board_size - 1), 1]
    adjacent_bottom_right = [-(board_size + 1), -board_size, -1]

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

def propogate_clearing(board, mine_numbers, board_size):
    cleared = False
    while not cleared:
        #print('Checking cells to propogate....')
        cleared = True
        for loc in range(len(board)):
            #print(f'Cell {loc} is a {board[loc]} on main board, and has a {mine_numbers[loc]} for mine number.')
            if board[loc] == ' ' and mine_numbers[loc] == '0':
                #print('Identified cell to propogate outwards...')
                adjacent = get_adjacent(loc, board_size)
                for num in adjacent:
                    #print('Checking adjacent cells.....')
                    if board[loc + num] == '-' and mine_numbers[loc + num] != 'M':
                        #print(f'Adjacent cell {loc + num} is a {board[loc + num]} on main board, and has a {mine_numbers[loc + num]} for mine number.')
                        #print('Clearing....')
                        if mine_numbers[loc + num] == '0':
                            board[loc + num] = ' '
                        else:
                            board[loc + num] = mine_numbers[loc + num]
                        cleared = False
            #print('-----------')
    return board

def clear_space(board, mine_numbers, mapping, pos, board_size):
    loc = mapping[pos]
    if board[loc] == '-':
        # Reveal number below space
        if mine_numbers[loc] == 'M':
            board[loc] = 'X'
            return True, board
        elif mine_numbers[loc] == '0':
            board[loc] = ' '
        else:
            board[loc] = mine_numbers[loc]

        # Propogate clearing
        board = propogate_clearing(board, mine_numbers, board_size)

    return False, board

def print_board(board, board_size):
    print()
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

def check_win(board, mine_numbers):
    win = True
    for loc in range(len(board)):
        if board[loc] == '-' and mine_numbers[loc] != 'M':
            win = False
    return win

def valid_first_move(mapping):
    valid_move = False
    while not valid_move:
        pos = input('Please enter a coordinate for your first move: ')
        if pos in mapping:
            loc = mapping[pos]
            valid_move = True
    return pos, loc

def valid_move(mapping):
    options = {'af':'add a flag', 'rf':'remove a flag', 'cs':'clear a space'}
    valid_option = False
    while not valid_option:
        player_choice = input('Add flag (af), remove flag (rf), or clear space (cs): ')
        if player_choice in options:
            valid_option = True
    
    valid_move = False
    while not valid_move:
        pos = input(f'Where would you like to {options[player_choice]}?: ')
        if pos in mapping:
            loc = mapping[pos]
            valid_move = True
    
    return player_choice, pos

if __name__ == '__main__':
    lose, win = False, False
    # Create new board and board mapping for coordinates
    new_board = create_board(board_size)
    new_mapping = create_mapping(board_size)        
    # Print the initial board
    print_board(new_board, board_size)
    # Get a vlid first move from player and remove this space
    first_pos, first_loc = valid_first_move(new_mapping)
    new_mines = create_mines(board_size, first_loc)
    new_mine_numbers = calc_mine_numbers(new_mines, board_size)
    lose, new_board = clear_space(new_board, new_mine_numbers, new_mapping, first_pos, board_size)
    win = check_win(new_board, new_mine_numbers)

    while not (lose or win):
        print_board(new_board, board_size)
        player_choice, player_pos = valid_move(new_mapping)
        if player_choice == 'af':
            new_board = add_flag(new_board, new_mapping, player_pos)
        elif player_choice == 'cf':
            new_board = remove_flag(new_board, new_mapping, player_pos)
        elif player_choice == 'cs':
            lose, new_board = clear_space(new_board, new_mine_numbers, new_mapping, player_pos, board_size)
        win = check_win(new_board, new_mine_numbers)
    
    if win:
        print_board(new_board, board_size)
        print('You won!')
    elif lose:
        print_board(new_board, board_size)
        print('You lose :(')
