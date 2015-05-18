import sys

# init board
board = [[0 for x in range(3)] for x in range(3)]

def transpose(l):
    return list(map(list, zip(*l)))

# fill board
for i in range(3):
    x = input()
    for j in range(3):
        board[i][j] = int(x[j])


tboard = transpose(board)

for i in range(3):
    if board[i] == [1,1,1]:
        print("Player 1 wins")
        sys.exit()
        break
    elif board[i] == [2,2,2]:
        print("Player 2 wins")
        sys.exit()
        break
    
    if tboard[i] == [1,1,1]:
        print("Player 1 wins")
        sys.exit()
        break
    elif tboard[i] == [2,2,2,]:
        print("Player 2 wins")
        sys.exit()
        break

# check diagonally


begin = board[0][0]
accum = True
for i in range(3):
    accum = accum and board[i][i] == begin

if accum and begin != 0:
    print("Player {} wins".format(begin))
    sys.exit()


begin = board[0][2]
accum = True
for i in range(3):
    accum = accum and board[i][2-i] == begin

if accum and begin != 0:
    print("Player {} wins".format(begin))
    sys.exit()

print("No winner")
