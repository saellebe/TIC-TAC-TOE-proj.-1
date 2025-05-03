def draw_board(spots):
    board = (f"|{spots[1]}|{spots[2]}|{spots[3]}|\n"
             f"|{spots[4]}|{spots[5]}|{spots[6]}|\n"
             f"|{spots[7]}|{spots[8]}|{spots[9]}|")
    print(board)

def check_turn(turn):
    """This function alternates between 'X' and 'O' for player 1 and player 2."""
    if turn % 2 == 0:
        return 'X'  # Player 1 is 'X'
    else:
        return 'O'  # Player 2 is 'O'

def check_win(spots):
    """This function checks if there is a winner (horizontal, vertical, or diagonal)."""
    # Check Horizontal Wins
    if (spots[1] == spots[2] == spots[3]) \
            or (spots[4] == spots[5] == spots[6]) \
            or (spots[7] == spots[8] == spots[9]):
        return True
    # Check Vertical Wins
    elif (spots[1] == spots[4] == spots[7]) \
            or (spots[2] == spots[5] == spots[8]) \
            or (spots[3] == spots[6] == spots[9]):
        return True
    # Check Diagonal Wins
    elif (spots[1] == spots[5] == spots[9]) \
            or (spots[3] == spots[5] == spots[7]):
        return True
    return False
