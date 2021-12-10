file = open('Day 10 input.txt','r')
#file = open('Advent-of-Code-2021\\Day 10 testin.txt','r')


illegal = [0,0,0,0]
completescores = []

for line in file:
    line = line.strip()
    illegalflag = False
    stack = []

    for char in line:
        if ((ord(char) == 40) or (ord(char) == 91) or (ord(char) == 123) or (ord(char) == 60)):
            stack.append(char)
            continue

        opener = stack.pop()

        if ((ord(opener) == 40) and (ord(char) == 41)):
            continue

        if ((ord(opener) == 91) and (ord(char) == 93)):
            continue

        if ((ord(opener) == 123) and (ord(char) == 125)):
            continue

        if ((ord(opener) == 60) and (ord(char) == 62)):
            continue

        if (ord(char) == 41):
            illegal[0] = illegal[0] + 1
            illegalflag = True
            break

        if (ord(char) == 93):
            illegal[1] = illegal[1] + 1
            illegalflag = True
            break

        if (ord(char) == 125):
            illegal[2] = illegal[2] + 1
            illegalflag = True
            break

        if (ord(char) == 62):
            illegal[3] = illegal[3] + 1
            illegalflag = True
            break
    
    if (illegalflag == True):
        continue

    completescore = 0
    while not (stack == []):
        item = stack.pop()
        completescore = completescore * 5

        if (ord(item) == 40):
            completescore = completescore + 1
            continue
        
        if (ord(item) == 91):
            completescore = completescore + 2
            continue

        if (ord(item) == 123):
            completescore = completescore + 3
            continue

        if (ord(item) == 60):
            completescore = completescore + 4
            continue
    
    completescores.append(completescore)
    
print(sorted(completescores)[len(completescores)//2])