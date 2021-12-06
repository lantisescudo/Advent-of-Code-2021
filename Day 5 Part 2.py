import re

file = open("Day 5 input.txt","r")
positions = [[0]*1000 for _ in range(1000)]
lines = []

pattern = re.compile("(\d+),(\d+) -> (\d+),(\d+)")

for line in file:
    match = pattern.match(line)
    x1 = int(match.group(1))
    y1 = int(match.group(2))
    x2 = int(match.group(3))
    y2 = int(match.group(4))

    if not((x1 != x2) & (y1 != y2)):
        lines.append([x1,x2,y1,y2])
    elif (abs(x1-x2) == abs(y1-y2)):
        lines.append([x1,x2,y1,y2])

for seg in lines:
    if (seg[0] == seg[1]):
        distance = max(seg[2],seg[3]) - min(seg[2],seg[3])+1
        start = min(seg[2],seg[3])
        x = seg[0]
        for index in range(distance):
            y = start+index
            positions[y][x] = positions[y][x] + 1
    elif (seg[2] == seg[3]):
        distance = max(seg[0],seg[1]) - min(seg[0],seg[1])+1
        start = min(seg[0],seg[1])
        y = seg[2]
        for index in range(distance):
            x = start+index
            positions[y][x] = positions[y][x] + 1
    else:
        maxX = max(seg[0],seg[1])
        if (seg[2]<seg[3]):
            dir = 1
        else:
            dir = -1
        
        step = 0
        if (seg[0] < seg[1]):
            currX = seg[0]
            startY = seg[2]
        else:
            currX = seg[1]
            startY = seg[3]
            dir = -dir

        while (currX <= maxX):
            currY = startY + (step*dir)
            positions[currY][currX] = positions[currY][currX] + 1
            currX = currX + 1
            step = step + 1


count = 0

for row in positions:
    for column in row:
        if (column > 1):
            count = count+1

print(count)