file = open("Day 8 input.txt","r")

count = [0]*10

for line in file:
    outdigits = line.split("|")[1]
    for digit in outdigits.split():
        count[len(digit)] = count[len(digit)]+1

print(count)
print(count[2]+count[4]+count[3]+count[7])