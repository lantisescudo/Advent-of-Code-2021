file = open("Day 3 input.txt","r")
count = 0
ones = [0,0,0,0,0,0,0,0,0,0,0,0]
gamma = [0,0,0,0,0,0,0,0,0,0,0,0]
epsilon = [0,0,0,0,0,0,0,0,0,0,0,0]
outgamma = 0
outepsilon = 0
power = 0

for line in file:
    count = count + 1
    for char in range(len(line)):
        if line[char] == '1':
            ones[char] = ones[char]+1

for index in range(len(ones)):
    if ones[index] > (count/2):
        gamma[index] = 1
        epsilon[index] = 0
    else:
        gamma[index] = 0
        epsilon[index] = 1

outgamma = int(''.join(map(str,gamma)),base=2)
outepsilon = int(''.join(map(str,epsilon)),base=2)

# for index in range(len(gamma)):
#     outgamma = outgamma + (gamma[-1-index] * (2^index))
#     outepsilon = outepsilon + (epsilon[-1-index] * (2^index))

power = outgamma*outepsilon
print(gamma)
print(epsilon)
print(outgamma)
print(outepsilon)
print(power)