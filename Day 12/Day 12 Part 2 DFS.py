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

pathcount = 0
pathlist = []

def dfs(path):
    global pathcount
    global cavedict
    for node in cavedict[path[len(path)-1]]:
        p = path.copy()
        if (node == 'end'):
            pathcount += 1
            pathlist.append(p+[node])
            continue
        if (node == 'start'):
            continue
        if ((ord(node[0]) > 96) and (node in p)):
            if (p[0] == True):
                continue
            else:
                p[0] = True
                dfs(p+[node])
        else:
            dfs(p+[node])

dfs([False,'start'])
# for p in pathlist:
#     print(p)
print(pathcount)


