# 1. Name:
#      Zed Walted
# 2. Assignment Name:
#      Lab 01: Tic-Tac-Toe
# 3. Assignment Description:
#      Play the game of Tic-Tac-Toe
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part for me was figuring out where to start, it was one of the most complex programs I've attempted to code and I just got lost
#       trying to find a starting point to base the beginning of my code around.
# 5. How long did it take for you to complete the assignment?
#      In total this program took me about 3 hours to complete.

import json

# The characters used in the Tic-Tac-Too board.
# These are constants and therefore should never have to change.
X = 'X'
O = 'O'
BLANK = ' '

# A blank Tic-Tac-Toe board. We should not need to change this board;
# it is only used to reset the board to blank. This should be the format
# of the code in the JSON file.
blank_board = {  
            "board": [
                BLANK, BLANK, BLANK,
                BLANK, BLANK, BLANK,
                BLANK, BLANK, BLANK ]
        }


def read_board(filename):
    '''Read the previously existing board from the file if it exists.'''
    try:
        with open(f'{filename}') as file:
            save_board = file.read()
            board = json.loads(save_board)
            return board
    except:
        return blank_board['board']

def save_board(filename, board):
    '''Save the current game to a file.'''
    with open(f'{filename}', 'w') as convert_file:
        convert_file.write(json.dumps(board))
    convert_file.close()
    print(f'Your game was saved under {filename} filename.')

def display_board(board):
    '''Display a Tic-Tac-Toe board on the screen in a user-friendly way.'''
    # Put display code here.
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")
    return board

def is_x_turn(board, player1):
    '''Determine whose turn it is.'''
    if player1 == True:
        return True
    else:
        return False

def play_game(board):
    '''Play the game of Tic-Tac-Toe.'''
    filename = ''
    player1 = True
    game = False
    while game == False:
        display_board(board)
        number = input('')
        if number == 'q':
            filename = input('What filename would you like to save your game under? ')
            save_board(filename, board)
            break
        if is_x_turn(board, player1) == True:
            board[int(number)-1] = X
            player1 = False
        else:
            board[int(number)-1] = O
            player1 = True
        game = game_done(board, True)
        if game == True:
            display_board(board)
    return False

def game_done(board, message=False):
    '''Determine if the game is finished.
       Note that this function is provided as-is.
       You do not need to edit it in any way.
       If message == True, then we display a message to the user.
       Otherwise, no message is displayed. '''

    # Game is finished if someone has completed a row.
    for row in range(3):
        if board[row * 3] != BLANK and board[row * 3] == board[row * 3 + 1] == board[row * 3 + 2]:
            if message:
                print("The game was won by", board[row * 3])
            return True

    # Game is finished if someone has completed a column.
    for col in range(3):
        if board[col] != BLANK and board[col] == board[3 + col] == board[6 + col]:
            if message:
                print("The game was won by", board[col])
            return True

    # Game is finished if someone has a diagonal.
    if board[4] != BLANK and (board[0] == board[4] == board[8] or
                              board[2] == board[4] == board[6]):
        if message:
            print("The game was won by", board[4])
        return True

    # Game is finished if all the squares are filled.
    tie = True
    for square in board:
        if square == BLANK:
            tie = False
    if tie:
        if message:
            print("The game is a tie!")
        return True


    return False

# The file read code, game loop code, and file close code goes here.
def main():
    save = input('Do you have a previous save?(y/n) . ')
    if save == 'y':
        filename = input('What is the filename? ')
        board = read_board(filename)
    elif save == 'n':
        board = blank_board['board']
    # These user-instructions are provided and do not need to be changed.
    print("Enter 'q' to suspend your game. Otherwise, enter a number from 1 to 9")
    print("where the following numbers correspond to the locations on the grid:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 \n")
    print("The current board is:")
    play_game(board)


main()