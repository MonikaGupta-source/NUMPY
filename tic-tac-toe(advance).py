# import numpy as np
# import random

# board = np.zeros((3, 3), dtype=int)


# def print_board(b):
#     symbols = {0: " ", 1: "X", -1: "O"}
#     for i in range(3):
#         row = " | ".join((symbols[val] for val in b[i]))
#         print(" " + row)
#         if i < 2:
#             print("---+---+---")
#     print()


# def check_win(player):
#     for i in range(3):
#         if np.all(board[i, :] == player):
#             return True

#     for i in range(3):
#         if np.all(board[:, i] == player):
#             return True
        
#     if np.all(np.diag(board) == player) or np.all(np.diag(np.fliplr(board)) == player):
#         return True

#     return False


# def computer_move():
#     empty_spot = []
#     for i in range(3):
#         for j in range(3):
#             if board[i, j] == 0:
#                 empty_spot.append((i, j))

#     if empty_spot:
#         return random.choice(empty_spot)
#     return None


# def is_full():
#     for i in range(3):
#         for j in range(3):
#             if board[i, j] == 0:
#                 return False
#     return True  

# def game_play():
#     print("-------WELCOME TO THE TIC-TAC-TOE--------")
#     print("X is you and O is computer")
#     print("Enter row(0-2) column(0-2) like: 0 0")

#     current_player = 'X'
#     while True:
#         print_board(board)
#         if current_player == "X":
#             try:
#                 row, col = map(int, input("Your turn (row col): ").split())
               
#                 if 0 <= row <= 2 and 0 <= col <= 2 and board[row, col] == 0:
#                     board[row, col] = 1 
#                 else:
#                     print("Invalid move! Try again.")
#                     continue
#             except:
#                 print("Enter numbers like: 0 1")
#                 continue

#         else:
#             print("Computer thinking...")
#             move = computer_move()  
#             if move is not None:
#                 row, col = move
#                 board[row, col] = -1  
#                 print(f"Computer picked: row {row}, col {col}")

#         if check_win(1):
#             print_board(board)
#             print("YOU WIN!")
#             break
#         elif check_win(-1):
#             print_board(board)
#             print("COMPUTER WINS!")
#             break
#         elif is_full():
#             print_board(board)
#             print("It's a DRAW!")
#             break

#         current_player = 'O' if current_player == 'X' else 'X'


# game_play()









        


