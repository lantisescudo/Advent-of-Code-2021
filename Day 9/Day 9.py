file = open('Day 9 input.txt','r')
linemap = []
sumlows = 0

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
            sumlows = sumlows + currval+1
            print("Row:",row,", Col:",char,", Rolling Sum:",sumlows)