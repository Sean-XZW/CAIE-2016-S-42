board = [['E' for i in range(1, 9)]for j in range(1, 9)]
for i in range(0, 2):
    for j in range(0, 8):
        board[i][j] = 'B'

for i in range(6, 8):
    for j in range(0, 8):
        board[i][j] = 'W'

def ValidMoves(PieceColour, xCurrent, yCurrent):
    for i in range(xCurrent-1,0,-1):
        if xCurrent-1 == -1:
            print("Cannot move left")
        elif board[i][yCurrent] == "E":
            print("move left")
            print(i, yCurrent)
        if board[i][yCurrent] != 'E':
            if PieceColour == board[i][yCurrent]:
                print("cannot move left")
            else:
                print(i, yCurrent)

    for i in range(xCurrent, 8):
        if xCurrent == 8:
            print("cannot move right")
        elif board[i][yCurrent] == "E":
            print("move right")
            print(i, yCurrent)
        if board[i][yCurrent] != 'E':
            if PieceColour == board[i][yCurrent]:
                print("cannot move right")
            else:
                print(i, yCurrent)

