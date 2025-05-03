from helpers import display_board, get_player_choice, check_for_winner

# Initialize the game state
spots = {1: '1', 2: '2', 3: '3', 4: "4", 5: '5', 6: '6',
         7: '7', 8: "8", 9: "9"}

game_running = True
turn_count = 0

# Let players choose their symbols
player1_symbol, player2_symbol = get_player_choice()

# Game loop
while game_running:
    # Clear the screen and display the board
    print("\n" * 100)
    display_board(spots)

    # Determine whose turn it is
    current_player = player1_symbol if turn_count % 2 == 0 else player2_symbol
    print(f"Player {1 if current_player == player1_symbol else 2} ({current_player})'s turn.")

    # Get player input for the spot
    choice = input("Which spot would you like to play? (1-9) or 'q' to quit: ")
    if choice.lower() == 'q':
        game_running = False
        break

    if choice.isdigit() and 1 <= int(choice) <= 9:
        spot = int(choice)
        if spots[spot] not in {'X', 'O'}:
            spots[spot] = current_player
            turn_count += 1
        else:
            print("That spot is already taken! Try again.")
    else:
        print("Invalid input, please choose a number between 1-9 or 'q' to quit.")

    # Check for a winner after each move
    if check_for_winner(spots):
        game_running = False
        display_board(spots)
        print(f"Player {1 if current_player == player1_symbol else 2} ({current_player}) wins!")
        break

    # If all spots are filled and there's no winner, declare a tie
    if turn_count == 9:
        game_running = False
        display_board(spots)
        print("It's a tie, no winner!")

# Thank the players for playing
print("Thank you for playing!")
