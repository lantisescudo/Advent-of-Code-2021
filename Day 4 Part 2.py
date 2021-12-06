calllist = [69,88,67,56,53,97,46,29,37,51,3,93,92,78,41,22,45,66,13,82,2,7,52,40,18,70,32,95,89,64,84,68,83,26,43,0,61,36,57,34,80,39,6,63,72,98,21,54,23,28,65,16,76,11,20,33,96,4,10,25,30,19,90,24,55,91,15,8,71,99,58,14,60,48,44,17,47,85,74,87,86,27,42,38,81,79,94,73,12,5,77,35,9,62,50,31,49,59,75,1]
boards = []
currboard = []

wincall = None
winboard = None
flagboard = None
boardwins = []

file = open("Day 4 boards.txt","r")
count = 0

for line in file:
    count = count + 1
    if ((count%6) == 0):
        boards.append(currboard)
        currboard = []
    else:
        currboard.append(line.split())

boards.append(currboard)

def markboards(call):
    for board in range(len(boards)):
        for row in range(len(boards[board])):
            for item in range(len(boards[board][row])):
                if (boards[board][row][item] != 'x'):
                    if (int(boards[board][row][item]) == int(call) ):
                        boards[board][row][item] = 'x'

def checkboard(board):
    winner = True
    exit = False

    for row in board:
        for item in row:
            if (item != 'x'):
                winner = False
        if (winner == True):
            exit = True
            break
        else:
            winner = True
    
    if (exit == True):
        return True
    
    winner = True
    for col in range(5):
        for row in board:
            if (row[col] != "x"):
                winner = False
        if (winner == True):
            exit = True
            break
        else:
            winner = True
    
    if (exit == True):
        return True
    else:
        return False

def countwins():
    count = 0
    lastboard = None
    for board in range(len(boardwins)):
        if (boardwins[board] == False):
            count = count + 1
            lastboard = board
    
    return [count,lastboard]


for board in range(len(boards)):
    boardwins.append(False)


for call in calllist:
    markboards(call)
    for board in range(len(boards)):
        if (boardwins[board] == False):
            if (checkboard(boards[board])):
                boardwins[board] = True
                wincount = countwins()
                if (wincount[0] == 1):
                    flagboard = wincount[1]
                if (wincount[0] == 0):
                    winboard = boards[flagboard]
                    wincall = call
    if (wincall != None):
        break

winsum = 0

for row in winboard:
    for item in row:
        if (item != 'x'):
            winsum = winsum + int(item)

print(wincall)
print(winboard)
print(winsum)
print(wincall*winsum)