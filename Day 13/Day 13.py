file = open('Advent-of-Code-2021\\Day 13\\Day 13 input.txt')

points = []
folds = []

for line in file:
    line = line.strip()

    if (line.find(',') != -1):
        pointparse = line.split(',')
        points.append([int(pointparse[0]),int(pointparse[1])])
    elif (line.find('=') != -1):
        foldparse = line.split('=')
        folds.append([foldparse[0][len(foldparse[0])-1], int(foldparse[1])])
    else:
        "Do nothing"

thisfold = folds[0]
newpoints = []
for point in points:
    if (thisfold[0] == 'x'):
        if (point[0] > thisfold[1]):
            checkpoint = [thisfold[1]-(point[0]-thisfold[1]),point[1]]
            if (checkpoint not in newpoints):
                newpoints.append(checkpoint)
        elif (point not in newpoints):
                newpoints.append(point)
        else:
            "Do Nothing"
        
    else:
        if (point[1] > thisfold[1]):
            checkpoint = [point[0],thisfold[1]-(point[1]-thisfold[1])]
            if (checkpoint not in newpoints):
                newpoints.append(checkpoint)
        elif (point not in newpoints):
                newpoints.append(point)
        else:
            "Do Nothing"

print(newpoints)
print(len(newpoints))