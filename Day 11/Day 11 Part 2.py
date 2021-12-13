file = open('Advent-of-Code-2021\\Day 11\\Day 11 input.txt','r')
#file = open('Day 11 testin.txt','r')

board = []

def addaround(pair):
    x = pair[0]
    y = pair[1]
    listtoadd = []

    if not (x == 0):
        listtoadd.append([x-1,y])
        if not (y == 0):
            listtoadd.append([x-1,y-1])
        if not (y == len(board[x])-1):
            listtoadd.append([x-1,y+1])
    if not (x == len(board)-1):
        listtoadd.append([x+1,y])
        if not (y == 0):
            listtoadd.append([x+1,y-1])
        if not (y == len(board[x])-1):
            listtoadd.append([x+1,y+1])
    if not (y == 0):
        listtoadd.append([x,y-1])
    if not (y == len(board[x])-1):
        listtoadd.append([x,y+1])

    for newpair in listtoadd:
        board[newpair[0]][newpair[1]] = board[newpair[0]][newpair[1]] + 1
    
for line in file:
    newrow = []
    for char in line.strip():
        newrow.append(int(char))
    
    board.append(newrow)

allflash = False
step = 0
octocount = len(board[0]) * len(board)
while (allflash == False):
    step = step + 1
    flashcount = 0
    #increment everything
    for row in range(len(board)):
        for item in range(len(board[row])):
            board[row][item] = board[row][item] + 1

    #check for flashes
    flashlist = []
    newflash = True

    while (newflash == True):
        newflash = False
        for row in range(len(board)):
            for item in range(len(board[row])):
                if (board[row][item] > 9):
                    if ([row,item] not in flashlist):
                        flashlist.append([row,item])
                        newflash = True
                        addaround([row,item])
                        flashcount = flashcount +1

    #Reset flashers to 0
    for row in range(len(board)):
        for item in range(len(board[row])):
            if (board[row][item] > 9):
                board[row][item] = 0

    #Check for all flashes
    if (octocount == flashcount):
        allflash = True

print(step)