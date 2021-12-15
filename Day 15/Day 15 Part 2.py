import networkx as nx

file = open('Advent-of-Code-2021\\Day 15\\Day 15 input.txt','r')

bigarray = []
lcount = 0
for line in file:
    line = line.strip()
    linearray = []
    for char in line:
        linearray.append(int(char))
    bigarray.append(linearray)


fullmap = []
colwidth = len(bigarray[0])
for row in range(((len(bigarray))*5)):
    temprow = []
    for col in range(((colwidth)*5)):
        if ((row < len(bigarray)) and (col < len(bigarray[row]))):
            temprow.append(bigarray[row][col])
        elif (col < colwidth):
            val = fullmap[row-len(bigarray)][col]+1
            if (val == 10):
                val = 1
            temprow.append(val)
        else:
            val = temprow[col-colwidth]+1
            if (val == 10):
                val = 1
            temprow.append(val)
    fullmap.append(temprow)

biggraph = nx.DiGraph()
for row in range(len(fullmap)):
    for col in range(len(fullmap[row])):
        if not (row == 0):
            biggraph.add_edge((row,col),(row-1,col),weight=fullmap[row-1][col])
            biggraph.add_edge((row-1,col),(row,col),weight=fullmap[row][col])
        if not (row == len(fullmap)-1):
            biggraph.add_edge((row,col),(row+1,col),weight=fullmap[row+1][col])
            biggraph.add_edge((row+1,col),(row,col),weight=fullmap[row][col])
        if not (col == 0):
            biggraph.add_edge((row,col),(row,col-1),weight=fullmap[row][col-1])
            biggraph.add_edge((row,col-1),(row,col),weight=fullmap[row][col])
        if not (col == len(fullmap[row])-1):
            biggraph.add_edge((row,col),(row,col+1),weight=fullmap[row][col+1])
            biggraph.add_edge((row,col+1),(row,col),weight=fullmap[row][col])

len = nx.shortest_path_length(biggraph,source=(0,0),target=(len(fullmap)-1,len(fullmap[0])-1),weight='weight')
print (len)