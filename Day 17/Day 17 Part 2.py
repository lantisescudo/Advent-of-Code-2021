targetX = [143,177]
targetY = [-106,-71]
# targetX = [20,30]
# targetY = [-10,-5]

def step(X,Y,vX,vY):
    X = X + vX
    Y = Y + vY
    vY = vY - 1
    if (vX > 0):
        vX = vX - 1
    elif (vX < 0):
        vX = vX + 1
    return [X,Y,vX,vY]

hits = []

for vx in range(max(targetX)+1):
    for vy in range(-max(max(targetY),abs(min(targetY)))-1,max(max(targetY),abs(min(targetY)))+1):
        pos = [0,0,vx,vy]
        isHit = False
        isMiss = False
        maxY = 0
        while ((isHit == False) and (isMiss == False)):
            pos = step(pos[0],pos[1],pos[2],pos[3])
            if (pos[1] > maxY):
                maxY = pos[1]
            if ((pos[0] >= min(targetX)) and (pos[0] <= max(targetX)) and (pos[1] >= min(targetY)) and (pos[1] <= max(targetY))):
                isHit = True
            if (pos[1] < min(targetY)):
                isMiss = True
            if ((pos[0] > max(targetX)) and (pos[2] > 0)):
                isMiss = True
        
        if (isHit):
            hits.append([vx,vy,maxY])

absmax = 0
for h in hits:
    if (h[2] > absmax):
        absmax = h[2]

print(absmax)
print(len(hits))