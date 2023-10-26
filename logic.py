# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.


def make_empty_board():
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]


def get_winner(board):
    """Determines the winner of the given board.
    Returns 'X', 'O', or None."""
     #check rows
    for row in board:
        if row[0]==row[1]==row[2]:
            output = row[0]
        else:
            output = None
    #check columns
    for i in range(3):
        if board[0][i]==board[1][i]==board[2][i]:
            output = board[0][i]
        #check diagonals
        if board[0][0]==board[1][1]==board[2][2] or board[2][0]==board[1][1]==board[2][0]:
            output = board[1][1]
    return output  # FIXME


def other_player(player):
    """Given the character for a player, returns the other player."""
    if player == "X":
        return "O"
    elif player == "O":
        return "X"
