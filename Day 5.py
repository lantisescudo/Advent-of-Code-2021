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

for seg in lines:
    if (seg[0] == seg[1]):
        distance = max(seg[2],seg[3]) - min(seg[2],seg[3])+1
        start = min(seg[2],seg[3])
        x = seg[0]
        for index in range(distance):
            y = start+index
            positions[y][x] = positions[y][x] + 1
    else:
        distance = max(seg[0],seg[1]) - min(seg[0],seg[1])+1
        start = min(seg[0],seg[1])
        y = seg[2]
        for index in range(distance):
            x = start+index
            positions[y][x] = positions[y][x] + 1

count = 0

for row in positions:
    for column in row:
        if (column > 1):
            count = count+1

print(count)