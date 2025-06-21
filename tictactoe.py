# Tic Tac Toe - Terminal Game

# Initialize the board
board = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"]
]

# Function to print the board
def print_board(board):
    for i in range(len(board)):
        print(" | ".join(board[i]))
        if i < len(board) - 1:
            print("---------")

# Function to check if a player has won
def check_winner(board, player):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] == player:
            return True

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

# Function to check for draw
def is_draw(board):
    for row in board:
        for cell in row:
            if cell not in ["X", "O"]:
                return False
    return True

# Game loop
current_player = "X"

while True:
    print_board(board)
    move = input(f"\nPlayer {current_player}, enter your move (1–9): ")

    if not move.isdigit() or not (1 <= int(move) <= 9):
        print("Invalid input! Please enter a number from 1 to 9.")
        continue

    move = int(move)
    row = (move - 1) // 3
    col = (move - 1) % 3

    if board[row][col] in ["X", "O"]:
        print("That cell is already taken. Please choose another one.")
        continue

    board[row][col] = current_player

    if check_winner(board, current_player):
        print_board(board)
        print(f"\nPlayer {current_player} wins!")
        break

    if is_draw(board):
        print_board(board)
        print("\nIt's a draw!")
        break

    # Switch player
    current_player = "O" if current_player == "X" else "X"

