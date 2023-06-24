board = []
for i in range(0, 9):
    x = input("Enter the move character: ")
    y = int(input("Enter the position: "))
    board.insert(y, x)


def wins():
# ROW WINS
    if(board[0] == board[1] and board[1] == board[2]):
        print("Winner is: ", board[0])
    elif(board[3] == board[4] and board[4] == board[5]):
        print("Winner is: ", board[3])
    elif(board[6] == board[7] and board[7] == board[8]):
        print("Winner is: ", board[6])

# COLUMN WINS
    if(board[0] == board[3] and board[3] == board[6]):
        print("Winner is: ", board[0])
    elif(board[1] == board[4] and board[4] == board[7]):
        print("Winner is: ", board[1])
    elif(board[2] == board[5] and board[5] == board[8]):
        print("Winner is: ", board[2])

# DIAGONAL WINS
    if(board[0] == board[4] and board[4] == board[8]):
        print("Winner is: ", board[0])
    elif(board[2] == board[4] and board[4] == board[6]):
        print("Winner is: ", board[2])
    else:
        print("Tie")

wins()