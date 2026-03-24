import numpy as np 

board = np.zeros((3,3),dtype=int)

print(board)

def print_board(b):
    Symbols = {0 : "", 1 : "X" , -1: "O"}
    for r in range(3):
        row = "  | ".join(Symbols[val] for val in b[r])
        print(" "+ row)
        if r<2:
            print("---+---+---")
    print()

def check_winner(b):
    if 3 in np.sum(b,axis=1) or 3 in np.sum(b,axis=0):
        return "X"
    if -3 in np.sum(b,axis=1) or -3 in np.sum(b,axis=0):
        return "O"
    
    if np.trace(b) == 3 or np.trace(np.fliplr(b)) == 3:
        return "X"

    if np.trace(b) == -3 or np.trace(np.fliplr(b) == -3):
        return "O"
    
    if not 0 in b :
        return "DRAW"
    
    return None

currnt = 1
print("----------WELCOME TO TIC TAC TOE-----------")
print_board(board)

while True :
    if currnt ==  1:
        player = "X"

    else :
        player = "O"


    try :
        row = int(input(player + "- Enter row(0,1,2)"))
        col = int(input(player + "- Enter column (0,1,2)"))
    except ValueError:
        print("Please enter number only \n")
        continue

    if row <0 or row >2 or col <0 or col>2:
        print("row and column mush be between 0 and 2")

    if board[row,col]!= 0:
        print("cell is already taken")

    board[row,col] = currnt
    print_board(board)
    
    result = check_winner(board)

    if result is not None:
        if result ==  "DRAW":
            print("oHHH shit! draw ho gyaa ")

        else:
            print(result,"wins")

        break
    if currnt == 1:
        currnt = -1
    else:
        currnt =1