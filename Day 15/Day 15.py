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

biggraph = nx.DiGraph()
for row in range(len(bigarray)):
    for col in range(len(bigarray[row])):
        if not (row == 0):
            biggraph.add_edge((row,col),(row-1,col),weight=bigarray[row-1][col])
            biggraph.add_edge((row-1,col),(row,col),weight=bigarray[row][col])
        if not (row == len(bigarray)-1):
            biggraph.add_edge((row,col),(row+1,col),weight=bigarray[row+1][col])
            biggraph.add_edge((row+1,col),(row,col),weight=bigarray[row][col])
        if not (col == 0):
            biggraph.add_edge((row,col),(row,col-1),weight=bigarray[row][col-1])
            biggraph.add_edge((row,col-1),(row,col),weight=bigarray[row][col])
        if not (col == len(bigarray[row])-1):
            biggraph.add_edge((row,col),(row,col+1),weight=bigarray[row][col+1])
            biggraph.add_edge((row,col+1),(row,col),weight=bigarray[row][col])

len = nx.shortest_path_length(biggraph,source=(0,0),target=(len(bigarray)-1,len(bigarray[0])-1),weight='weight')
print (len)