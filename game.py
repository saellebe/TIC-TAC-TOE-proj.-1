def display_board(spots):
    """Display the Tic-Tac-Toe board."""
    board = f"""
    {spots[1]} | {spots[2]} | {spots[3]}
    ---------
    {spots[4]} | {spots[5]} | {spots[6]}
    ---------
    {spots[7]} | {spots[8]} | {spots[9]}
    """
    print(board)


def get_player_choice():
    """Allow players to choose their symbols."""
    while True:
        player1_symbol = input("Player 1, choose your symbol (X or O): ").upper()
        if player1_symbol in ['X', 'O']:
            player2_symbol = 'O' if player1_symbol == 'X' else 'X'
            return player1_symbol, player2_symbol
        else:
            print("Invalid choice, please choose either 'X' or 'O'.")


def check_for_winner(spots):
    """Check if there's a winner."""
    # Check horizontal, vertical, and diagonal lines
    winning_combinations = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],  # Horizontal
        [1, 4, 7], [2, 5, 8], [3, 6, 9],  # Vertical
        [1, 5, 9], [3, 5, 7]  # Diagonal
    ]

    for combo in winning_combinations:
        if spots[combo[0]] == spots[combo[1]] == spots[combo[2]] and spots[combo[0]] in {'X', 'O'}:
            return True
    return False
