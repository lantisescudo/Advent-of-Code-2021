file = open('Advent-of-Code-2021\\Day 12\Day 12 input.txt','r')

caves = []
pairs = []

for line in file:
    currpair = line.strip().split('-')
    if (currpair not in pairs):
        pairs.append(currpair)
    
    for p in currpair:
        if (p not in caves):
            caves.append(p)

#Build dictionary
cavedict = {}
for edge in pairs:
    if (edge[0] not in cavedict):
        cavedict[edge[0]] = [edge[1]]
    else:
        if (edge[1] not in cavedict[edge[0]]):
            cavedict[edge[0]].append(edge[1])
    
    if (edge[1] not in cavedict):
        cavedict[edge[1]] = [edge[0]]
    else:
        if (edge[0] not in cavedict[edge[1]]):
            cavedict[edge[1]].append(edge[0])

paths = []
badpaths = []
for node in cavedict["start"]:
    paths.append(["false","start",node])

stillsearching = True

while (stillsearching == True):
    stillsearching = False
    newpaths = []
    for p in paths:
        if (p[len(p)-1] == "end"):
            newpaths.append(p)
            continue

        for node in cavedict[p[len(p)-1]]:
            addpath = p.copy()
            addpath.append(node)
            addthis = True

            if (addpath in badpaths):
                addthis = False
            elif (addpath in newpaths):
                addthis = False
            else:
                if (ord(node[0]) > 96):
                    if (node == "end"):
                        "Do Nothing"
                    elif (node == "start"):
                        badpaths.append(addpath)
                        addthis = False
                    elif ((node in p) and (addpath[0] == "false")):
                        addpath[0] = "true"
                    elif (node in p):
                        badpaths.append(addpath)
                        addthis = False
                    else:
                        "Do Nothing"

            if (addthis == False):
                "Do nothing"
            else:
                newpaths.append(addpath)
                stillsearching = True
    paths = newpaths

goodpaths = 0
for item in paths:
    if (item[len(item)-1] == "end"):
        goodpaths = goodpaths + 1

print(goodpaths)