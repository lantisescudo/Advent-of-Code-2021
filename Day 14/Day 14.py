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
        conversions[pair[0]] = pair[1].strip()
        elements.add(pair[0][0])
        elements.add(pair[0][1])
        elements.add(pair[1].strip())

def expandpair(items):
    global conversions
    string = ''
    if (len(items) == 2):
        string = items[0] + conversions[items] + items[1]
    else:
        for index in range(len(items)-1):
            if (index == len(items)-1):
                "Do Nothing"
            else:
                pair = items[index]+items[index+1]
                string = string + items[index]
                string = string + conversions[pair]
                if (index == len(items)-2):
                    string = string + items[index+1]
    return(string)

def countstring(item):
    countdict = {}
    for char in item:
        if (char in countdict):
            countdict[char] = countdict[char] + 1
        else:
            countdict[char] = 1
    return(countdict)

for pair in conversions:
    expandsteps = 10
    expand = pair
    for i in range(expandsteps):
        expand = expandpair(expand)
    expansions[pair] = expand
    countsets[pair]=countstring(expand)

basecount = {}
for index in range(len(base)-1):
    pair = base[index]+base[index+1]
    for key in countsets[pair]:
        if (key in basecount):
            basecount[key] = basecount[key] + countsets[pair][key]
        else:
            basecount[key] = countsets[pair][key]
    #Decrement the count for the trailing character to avoid double counting with the first character of the next pair
    basecount[base[index+1]] = basecount[base[index+1]] - 1

#Re-increment for the final character
basecount[base[len(base)-1]] = basecount[base[len(base)-1]] + 1


print(basecount)
print(max(basecount.values())-min(basecount.values()))