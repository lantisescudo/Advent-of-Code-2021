import re

file = open('Advent-of-Code-2021\\Day 14\\Day 14 input.txt','r')

base = ''
elements = set()
conversions = {}
expansions = {}
countsets = {}

for line in file:
    line = line.strip()
    if (len(line) == 0):
        "Do Nothing"
    elif (line.find('->')) == -1:
        base = line
    else:
        pair = re.split(' ->',line)
        conversions[pair[0]] = [pair[0][0]+pair[1].strip(),pair[1].strip()+pair[0][1]]

counts = {}
for index in range(len(base)-1):
    pair = base[index]+base[index+1]
    if pair in counts:
        counts[pair] = counts[pair] + 1
    else:
        counts[pair] = 1

for step in range(40):
    newcount = {}
    for pair in counts:
        for res in conversions[pair]:
            if res in newcount:
                newcount[res] = newcount[res] + counts[pair]
            else:
                newcount[res] = counts[pair]
    counts = newcount
    print(counts)

lettercount = {}
for pair in counts:
    if pair[0] in lettercount:
        lettercount[pair[0]] = lettercount[pair[0]] + counts[pair]
    else:
        lettercount[pair[0]] = counts[pair]

lettercount[base[len(base)-1]] = lettercount[base[len(base)-1]] + 1

print(lettercount)
print(max(lettercount.values())-min(lettercount.values()))