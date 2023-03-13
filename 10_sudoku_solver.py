# Sudoku solver
# Created by: Dylan Prole 
# Time taken:  2 hours

def cells():
    '''
    returns: (dict) All cells and their corrosponding indexes
    '''
    cells = {}
    for cell_num in range(9):
        cells[f'cell_{cell_num}'] = []
        for i in range(3):
            for j in range(3):
                cells[f'cell_{cell_num}'].append((27*(cell_num//3)) + (3*(cell_num%3)) + (9*i) + j)
    return cells

def rows():
    '''
    returns: (dict) All rows and their corrosponding indexes
    '''
    rows = {}
    for row_num in range(9):
        rows[f'row_{row_num}'] = []
        for i in range(9):
            rows[f'row_{row_num}'].append((9*row_num) + i)
    return rows

def cols():
    '''
    returns: (dict) All cols and their corrosponding indexes
    '''
    cols = {}
    for col_num in range(9):
        cols[f'col_{col_num}'] = []
        for i in range(9):
            cols[f'col_{col_num}'].append(col_num + 9*i)
    return cols

def is_duplicates(L):
    '''
    L (list): Input list to check for duplicates
    returns: (bool) True or False
    '''
    unique = []
    duplicates = False
    for value in L:
        if value not in unique and value != ' ':
            unique.append(value)
        elif value in unique and value != ' ':
            duplicates = True
    return duplicates

def create_sudoku(sudoku_string):
    '''
    sudoku_string (string): Input string for easily entering values
    returns: (list) Array of sudoku values
    '''
    sudoku = []
    for value in sudoku_string:
        if value == '-':
            sudoku.append(' ')
        else:
            sudoku.append(value)
    return sudoku

def display_board(board):
    '''
    prints: Sudoku board visualised
    '''
    cell = 0
    for i in range(9):
        print()
        if i == 0:
            print('-'*41)
        elif i % 3 == 0:
            print('-'*41)
        print('-'*41)
        print('|| ', end='')
        for j in range(9):
            print(board[9*i + j], end='')
            cell += 1
            if (9*i + j + 1) % 3 == 0:
                print(' || ', end='')
            else:
                print(' | ', end='')
    print()
    print('-'*41)
    print('-'*41)

def valid_cells(board):
    valid = True
    cell_dict = cells()
    for cell in cell_dict:
        cell_values = []
        cell_indexes = cell_dict[cell]
        for index in cell_indexes:
            cell_values.append(board[index])
        if is_duplicates(cell_values):
            valid =  False
    return valid

def valid_rows(board):
    valid = True
    row_dict = rows()
    for row in row_dict:
        row_values = []
        row_indexes = row_dict[row]
        for index in row_indexes:
            row_values.append(board[index])
        if is_duplicates(row_values):
            valid =  False
    return valid

def valid_cols(board):
    valid = True
    col_dict = cols()
    for col in col_dict:
        col_values = []
        col_indexes = col_dict[col]
        for index in col_indexes:
            col_values.append(board[index])
        if is_duplicates(col_values):
            valid =  False
    return valid

def valid_board(board):
    return valid_cells(board) and valid_rows(board) and valid_cols(board)

def find_empty_pos(board, pos):
    for index in range(len(board)):
        if(board[index]== ' '):
                pos[0] = index
                return True
    return False

def solve_sudoku(board):
    pos = [0]

    if not find_empty_pos(board, pos):
        return True
    
    index = pos[0]

    for num in range(1, 10):

        copied_board = board.copy()
        copied_board[index] = str(num)

        if(valid_board(copied_board)):

            board[index]= str(num)

            if solve_sudoku(board):
                return True
            
            board[index] = ' '
              
    return False

easy_sudoku =   '16-9-472---257---3--7--18--4--719---------------825--9--43--5--3---489---281-7-64'
easy_solution = '163984725892576413547231896456719238289463157731825649674392581315648972928157364'

new_sudoku =    '8----------36------7--9-2---5---7-------457-----1---3---1----68--85---1--9----4--' 

new_board = create_sudoku(easy_sudoku)
solve_sudoku(new_board)
display_board(new_board) 
# solution = create_sudoku(easy_solution)
# if new_board == solution:
#     print('This is the correct solution!')
# else:
#     print('This is not the correct solution :(')