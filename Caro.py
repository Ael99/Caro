num_of_line = 6
#board initialize
board = [[' ' for i in range(num_of_line)] for j in range(num_of_line)]

def print_board():
#print first line
    print('----' * len(board) + '-')
#print board with random format
    for row in range(len(board)):
        row_str = ''
        for col in range(len(board)):
            row_str += '| ' + board[row][col] + ' '
        print(row_str + '|')
        print('----' * len(board) + '-') 

def get_user_input():
    row = int(input('Choose the row for your next move (0-' + str(len(board) - 1) + '): '))
    col = int(input('Choose the column for your next move (0-' + str(len(board) - 1) + '): '))
    while not check_valid_move(row, col):
        print('Invalid move, try again !!!')
        row = int(input('Choose the row for your next move (0-' + str(len(board) - 1) + '): '))
        col = int(input('Choose the column for your next move (0-' + str(len(board) - 1) + '): '))
    
    return row, col

def check_valid_move(row, col):
        result = True
        if row < 0 or row >= len(board):
            result = False
        elif col < 0 or col >= len(board):
            result = False
        elif board[row][col] != ' ':
            result = False
        
        return result

def is_finished():    
    result = ''
    move_left = 0
    #win condition check
    #row
    for row in range(len(board)):
        for col in range(len(board) - 4):
            if board[row][col] != ' ' and board[row][col] == board[row][col+1] and board[row][col+1] == board[row][col+2] and board[row][col+2] == board[row][col+3] and board[row][col+3] == board[row][col+4]:
                result = board[row][col]
    #col
    for row in range(len(board) - 4):
        for col in range(len(board)):
            if board[row][col] != ' ' and board[row][col] == board[row+1][col] and board[row+1][col] == board[row+2][col] and board[row+2][col] == board[row+3][col] and board[row+3][col] == board[row+4][col]:
                result = board[row][col]
    #down vertical
    for row in range(len(board) - 4):
        for col in range(len(board) - 4):
            if board[row][col] != ' ' and board[row][col] == board[row+1][col+1] and board[row+1][col+1] == board[row+2][col+2] and board[row+2][col+2] == board[row+3][col+3] and board[row+3][col+3] == board[row+4][col+4]:
                result = board[row][col]
    #up vertical
    for row in range(4, len(board)):
        for col in range(len(board) - 4):
            if board[row][col] != ' ' and board[row][col] == board[row-1][col+1] and board[row-1][col+1] == board[row-2][col+2] and board[row-2][col+2] == board[row-3][col+3] and board[row-3][col+3] == board[row-4][col+4]:
                result = board[row][col]
    #full board check
    for row in range(len(board)):
        for col in range(len(board)):   
            if board[row][col] == ' ':
                move_left += 1
                break
    if move_left == 0:
        result = 'Draw'    
    return result

def start_game():
    result = is_finished()
    while result == '':
        print('Player 1 turn (X): ')
        row, col = get_user_input()
        board[row][col] = 'X'
        result = is_finished()
        print_board()
        
        while result == '':
            print('Player 2 turn (O): ')
            row, col = get_user_input()
            board[row][col] = 'O'
            result = is_finished()
            print_board()
            break
    if result == 'Draw':
        print('Draw game !')
    elif result == 'X':
        print('Player 1 wins !')
    elif result == 'O':
        print('Player 2 wins !')
                
start_game()
 