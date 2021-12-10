file = open("Day 3 input.txt","r")
list = []
co2 = 0
oxygen = 0
lifesupport = 0
globindex = 0

def countinglist(itemlist):
    itemcount = 0
    itemones = [0,0,0,0,0,0,0,0,0,0,0,0]
    morecommon = [0,0,0,0,0,0,0,0,0,0,0,0]
    lesscommon = [0,0,0,0,0,0,0,0,0,0,0,0]

    for item in itemlist:
        itemcount = itemcount + 1
        for char in range(len(item)):
            if item[char] == '1':
                itemones[char] = itemones[char]+1
        
        for index in range(len(itemones)):
            if itemones[index] >= (itemcount/2):
                morecommon[index] = 1
                lesscommon[index] = 0
            else:
                morecommon[index] = 0
                lesscommon[index] = 1

    return [morecommon,lesscommon]


for line in file:
    list.append(line)

filterlist = list.copy()

while len(filterlist)>1:
    copylist = []
    countreturn = countinglist(filterlist)
    gamma = countreturn[0]
    epsilon = countreturn[1]
    for item in filterlist:
        if (int(gamma[globindex]) == int(item[globindex])):
            copylist.append(item)
    
    filterlist = copylist.copy()
    print(len(filterlist))
    globindex = globindex+1

oxygen = filterlist[0]

globindex = 0
filterlist = list.copy()

while len(filterlist)>1:
    copylist = []
    countreturn = countinglist(filterlist)
    gamma = countreturn[0]
    epsilon = countreturn[1]
    for item in filterlist:
        if (int(epsilon[globindex]) == int(item[globindex])):
            copylist.append(item)
    
    filterlist = copylist.copy()
    globindex = globindex+1

co2 = filterlist[0]
lifesupport = int(co2,base=2)*int(oxygen,base=2)
print(co2)
print(int(co2,base=2))
print(oxygen)
print(int(oxygen,base=2))
print(lifesupport)