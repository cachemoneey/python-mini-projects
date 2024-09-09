import random
import time

# Function to print the Tic Tac Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


# Function to check if a player has won
def check_win(board, player):
    # Check rows
    for row in board:
        if all([cell == player for cell in row]):
            return True
    # Check columns
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    # Check diagonals
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False


# Function to check if the board is full (draw)
def is_full(board):
    return all([cell != " " for row in board for cell in row])


# Function for the computer to make a random move
def computer_move(board):
    empty_cells = [(row, col) for row in range(3) for col in range(3) if board[row][col] == " "]
    chosen_move = random.choice(empty_cells)
    time.sleep(5) # Add a 5 second delay here
    return chosen_move

# Main game function
def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]

    # Determine human and computer players
    human_player = input("Choose your symbol (X or O): ")
    computer_player = "X" if human_player == "O" else "O"

    turn = 0

    # Game loop
    while True:
        print_board(board)
        player = players[turn]

        # Handle human and computer turns
        if player == human_player:
            row = int(input(f"Player {player}, enter row (0, 1, 2): "))
            col = int(input(f"Player {player}, enter column (0, 1, 2): "))
        else:
            print(f"Computer ({computer_player}) is making a move...")
            row, col = computer_move(board)

        # Validate and update the board
        if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
            board[row][col] = player
            if check_win(board, player):
                print_board(board)
                if player == human_player:
                    print(f"Player {player} wins!")
                else:
                    print("Computer wins!")
                break
            elif is_full(board):
                print_board(board)
                print("It's a draw!")
                break
            else:
                turn = 1 - turn
        else:
            print("Invalid move. Try again.")


if __name__ == "__main__":
    main()




