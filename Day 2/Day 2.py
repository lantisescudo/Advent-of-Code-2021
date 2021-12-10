file = open("Day 2 input.txt","r")
horiz = 0
depth = 0

for line in file:
    command = line.split()
    if(command[0] == "forward"):
        horiz = horiz+int(command[1])
        print("Advancing ",int(command[1]))
    if(command[0] == "back"):
        horiz = horiz-int(command[1])
        print("Retreating ",int(command[1]))
    if command[0] == "up":
        depth = depth-int(command[1])
        print("Rising ",int(command[1]))
    if command[0] == "down":
        depth = depth+int(command[1])
        print("Diving ",int(command[1]))
    print("Horiz: ",horiz,", Depth: ",depth,", Position: ",horiz*depth)