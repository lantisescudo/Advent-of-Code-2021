file = open('Day 9 input.txt','r')

linemap = []
lowspotlist = []
basins = []

for line in file:
    linemap.append(line.strip())

for row in range(len(linemap)):
    for char in range(len(linemap[row])):
        lowspot = True
        currval = int(linemap[row][char])
        
        #Check Verticals
        if (row == 0):
            if (currval >= int(linemap[row+1][char])):
                lowspot = False
                continue
        elif (row == (len(linemap)-1)):
            if (currval >= int(linemap[row-1][char])):
                lowspot = False
                continue
        else:
            if ((currval >= int(linemap[row+1][char]) or (currval >= int(linemap[row-1][char])))):
                lowspot = False
                continue
        
        #Check Horizontals
        if (char == 0):
            if (currval >= int(linemap[row][char+1])):
                lowspot = False
                continue
        elif (char == (len(linemap[row])-1)):
            if (currval >= int(linemap[row][char-1])):
                lowspot = False
                continue
        else:
            if ((currval >= int(linemap[row][char+1]) or (currval >= int(linemap[row][char-1])))):
                lowspot = False
                continue

        if (lowspot == True):
            lowspotlist.append([row,char])

for point in lowspotlist:
    currbasin = [point]
    index = 0
    while (index < len(currbasin)):
        x = currbasin[index][0]
        y = currbasin[index][1]

        #Above
        if (x == 0 or (int(linemap[x-1][y]) == 9)):
            "Do Nothing"
        else:
            addpoint = True
            for point in currbasin:
                if ((point[0] == (x-1)) and (point[1] == y)):
                    addpoint = False
                    break
            if (addpoint == True):
                currbasin.append([x-1,y])
        
        #Below
        if (x == (len(linemap)-1) or (int(linemap[x+1][y]) == 9)):
            "Do Nothing"
        else:
            addpoint = True
            for point in currbasin:
                if ((point[0] == (x+1)) and (point[1] == y)):
                    addpoint = False
                    break
            if (addpoint == True):
                currbasin.append([x+1,y])

        #Left
        if (y == 0 or (int(linemap[x][y-1]) == 9)):
            "Do Nothing"
        else:
            addpoint = True
            for point in currbasin:
                if ((point[0] == (x)) and (point[1] == (y-1))):
                    addpoint = False
                    break
            if (addpoint == True):
                currbasin.append([x,y-1])

        #Right
        if (y == (len(linemap[x])-1) or (int(linemap[x][y+1]) == 9)):
            "Do Nothing"
        else:
            addpoint = True
            for point in currbasin:
                if ((point[0] == x) and (point[1] == (y+1))):
                    addpoint = False
                    break
            if (addpoint == True):
                currbasin.append([x,y+1])

        index = index + 1

    basins.append(len(currbasin))

basins = sorted(basins)
print(basins[len(basins)-1]*basins[len(basins)-2]*basins[len(basins)-3])