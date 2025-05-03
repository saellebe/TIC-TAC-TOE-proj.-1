from helpers import draw_board, check_turn, check_win

spots = {1: '1', 2: '2', 3: '3', 4: "4", 5: '5', 6: '6',
         7: '7', 8: "8", 9: "9"}

playing = True
complete = False
turn = 0
prev_turn = -1

while playing:
    # Reset the screen each turn
    print("\n" * 100)
    draw_board(spots)

    if prev_turn == turn:
        print("Invalid spot selected, please pick another spot.")

    prev_turn = turn
    print(f"Player {((turn % 2) + 1)}'s turn: Pick a spot (1-9) or press 'q' to quit.")

    # Input from player
    choice = input("Which spot do you want to play? (1-9): ")
    if choice.lower() == "q":
        playing = False
    # Check if choice is a valid number between 1-9
    elif choice.isdigit() and int(choice) in spots:
        # Check if spot has already been taken
        if spots[int(choice)] not in {"X", "O"}:
            # Valid move, update the board
            turn += 1
            spots[int(choice)] = check_turn(turn)
        else:
            print("That spot is already taken! Choose another.")
    else:
        print("Invalid input, please pick a number between 1 and 9 or 'q' to quit.")

    # Check if someone won the game
    if check_win(spots):
        playing, complete = False, True

    if turn >= 9:  # Maximum moves is 9 for a complete game
        playing = False

# Clear the screen and display the final board
print("\n" * 100)
draw_board(spots)

if complete:
    if check_turn(turn) == "X":
        print("Player 1 Wins!")
    else:
        print("Player 2 Wins!")
else:
    print("It's a tie, no winner!")

print("Thank you for playing!")

