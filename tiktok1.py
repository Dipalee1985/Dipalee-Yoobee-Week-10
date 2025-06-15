import random


def create_board():
    return [[" " for _ in range(3)] for _ in range(3)]


def display_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True


def check_win(board, symbol):
    for row in board:
        if row.count(symbol) == 3:
            return True

    for col in range(3):
        if all(board[row][col] == symbol for row in range(3)):
            return True

    if all(board[i][i] == symbol for i in range(3)):
        return True
    if all(board[i][2 - i] == symbol for i in range(3)):
        return True

    return False


def player_turn(board, symbol):
    while True:
        try:
            pos = int(input(f"Player {symbol}, choose position (1-9): ")) - 1
            row, col = divmod(pos, 3)
            if 0 <= pos < 9 and board[row][col] == " ":
                board[row][col] = symbol
                break
            else:
                print("Cell is taken or out of range.")
        except ValueError:
            print("Invalid input. Enter a number 1-9.")


def computer_turn(board):
    print("Computer's turn (O)...")
    empty = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
    row, col = random.choice(empty)
    board[row][col] = "O"


def play_game():
    board = create_board()
    mode = input("Choose mode: 1. 2 Players  2. vs Computer: ").strip()

    if mode == "1":
        player1 = input("Enter name for Player 1 (X): ").strip() or "Player 1"
        player2 = input("Enter name for Player 2 (O): ").strip() or "Player 2"
    else:
        player1 = input("Enter your name (Player X): ").strip() or "Player 1"
        player2 = "Computer"

    current = "X"

    print("\n🎮 Tic Tac Toe - Start!")
    print("Use positions 1 to 9 like this:")
    print("1 | 2 | 3\n4 | 5 | 6\n7 | 8 | 9\n")

    while True:
        display_board(board)

        if mode == "1" or (mode == "2" and current == "X"):
            player_turn(board, current)
        else:
            computer_turn(board)

        if check_win(board, current):
            display_board(board)
            winner_name = player1 if current == "X" else player2
            print(f" {winner_name} wins!")
            break
        elif is_board_full(board):
            display_board(board)
            print("It's a tie!")
            break

        current = "O" if current == "X" else "X"


if __name__ == "__main__":
    play_game()
