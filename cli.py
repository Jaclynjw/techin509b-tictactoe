# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import make_empty_board, get_winner, other_player


# Reminder to check all the tests

if __name__ == '__main__':
    board = make_empty_board()
    winner = None
    sign = 'X'
    while winner == None:
        print("TODO: take a turn!")
        # TODO: Show the board to the user.
        print(board)
        # TODO: Input a move from the player.
        pos_x, pos_y = input("Enter a position(x,y), split with space: ").split()
        # TODO: Update the board.
        board[int(pos_x)][int(pos_y)] = sign
        winner = get_winner(board)
        # TODO: Update who's turn it is.
        if not winner:
            sign = other_player(sign)
    print(winner)
