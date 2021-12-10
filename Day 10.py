file = open('Day 10 testin.txt','r')
#file = open('Advent-of-Code-2021\\Day 10 testin.txt','r')


illegal = [0,0,0,0]

for line in file:
    line = line.strip()
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
            break

        if (ord(char) == 93):
            illegal[1] = illegal[1] + 1
            break

        if (ord(char) == 125):
            illegal[2] = illegal[2] + 1
            break

        if (ord(char) == 62):
            illegal[3] = illegal[3] + 1
            break

score = (illegal[0] * 3) + (illegal[1] * 57) + (illegal[2] * 1197) + (illegal[3] * 25137)
print(score)