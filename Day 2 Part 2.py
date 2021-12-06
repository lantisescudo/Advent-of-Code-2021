file = open("Day 2 input.txt","r")
horiz = 0
depth = 0
aim = 0

for line in file:
    command = line.split()
    if(command[0] == "forward"):
        horiz = horiz+int(command[1])
        depth = depth+(int(command[1])*aim)
        print("Advancing ",int(command[1]))
    if command[0] == "up":
        aim = aim-int(command[1])
        print("Aiming->rise ",int(command[1]))
    if command[0] == "down":
        aim = aim+int(command[1])
        print("Aiming->dive ",int(command[1]))
    print("Horiz: ",horiz,", Depth: ",depth,", Aim:",aim,", Position: ",horiz*depth)