# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import make_empty_board


# Reminder to check all the tests

if __name__ == '__main__':
    board = make_empty_board()
    winner = None
    while winner == None:
        print("TODO: take a turn!")
        # TODO: Show the board to the user.
        print(board)
        # TODO: Input a move from the player.
        
        # TODO: Update the board.

        #check rows
        for row in board:
            if row[0]==row[1]==row[2]:
                output = row[0] + ' won'
            else:
                output = 'Draw'
        #check columns
        for i in range(3):
            if board[0][i]==board[1][i]==board[2][i]:
                output = board[0][i] + ' won'
            #check diagonals
            if board[0][0]==board[1][1]==board[2][2] or board[2][0]==board[1][1]==board[2][0]:
                output = board[1][1] + ' won'

        print(output)     #print the output

        # TODO: Update who's turn it is.
        winner = 'X'  # FIXME
