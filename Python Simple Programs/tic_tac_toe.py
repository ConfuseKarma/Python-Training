# This code creates a simple Tic-Tac-Toe game ("Jogo da velha" in portuguese) using python.
# Using the terminal to set up the board and setting who'll be "X" and "O", through columns and lines.

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board, player):
    # Verifica linhas, colunas e diagonais
    for row in board:
        if all(s == player for s in row):
            return True
    for col in range(3):
        if all(row[col] == player for row in board):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def is_full(board):
    return all(all(cell != " " for cell in row) for row in board)


def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = input("Escolha X ou O: ").upper()
    while player not in ["X", "O"]:
        player = input("Escolha inválida. Escolha X ou O: ").upper()

    current_player = player
    while True:
        print_board(board)
        try:
            row, col = map(int, input(f"Jogador {
                           current_player}, escolha a linha e a coluna (0, 1 ou 2) separadas por espaço: ").split())
            if board[row][col] != " ":
                print("Posição já ocupada. Tente novamente.")
                continue
        except (ValueError, IndexError):
            print("Entrada inválida. Tente novamente.")
            continue

        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"Jogador {current_player} venceu!")
            break

        if is_full(board):
            print_board(board)
            print("Empate!")
            break

        current_player = "O" if current_player == "X" else "X"


tic_tac_toe()
