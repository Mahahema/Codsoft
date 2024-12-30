import numpy as np
import random
from time import sleep

def create_board():
    return np.zeros((3, 3), dtype=int)

def possibilities(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i, j] == 0]

def random_place(board, player):
    i, j = random.choice(possibilities(board))
    board[i, j] = player
    return board

def check_win(board, player):
    return any(np.all(board[i, :] == player) or np.all(board[:, i] == player) for i in range(3)) or \
           np.all(np.diagonal(board) == player) or np.all(np.diagonal(np.fliplr(board)) == player)

def play_game():
    board = create_board()
    winner = 0
    for counter in range(9):
        player = 1 if counter % 2 == 0 else 2
        board = random_place(board, player)
        print(f"Board after {counter+1} move:")
        print(board)
        sleep(1)
        if check_win(board, player):
            return player
    return -1  # Draw

print("Winner is:", play_game())

