file = open('Day 8 input.txt',"r")

totalsum = 0

for line in file:
    signals = line.split("|")[0].split()
    outdigits = line.split("|")[1].split()
    transcription = [0]*10
    fives = []
    sixes = []

    for digit in signals:
        if (len(digit) == 2):
            transcription[1] = sorted(digit)
            continue

        if (len(digit) == 3):
            transcription[7] = sorted(digit)
            continue
        
        if (len(digit) == 4):
            transcription[4] = sorted(digit)
            continue

        # 2, 3, 5
        if (len(digit) == 5):
            fives.append(sorted(digit))
            continue

        # 0, 6, 9
        if (len(digit) == 6):
            sixes.append(sorted(digit))
            continue

        if (len(digit) == 7):
            transcription[8] = sorted(digit)
            continue

    #Find 3 and 6
    for item in fives:
        notThree = False
        for char in transcription[1]:
            if not (char in item):
                notThree = True
        if (notThree == False):
            transcription[3] = item
            break
    
    for item in sixes:
        isSix = False
        for char in transcription[7]:
            if not (char in item):
                isSix = True
        if (isSix == True):
            transcription[6] = item
            break
    
    #Find 0 and 9
    for item in sixes:
        isZero = False
        if (item == transcription[6]):
            continue
        for char in transcription[3]:
            if not (char in item):
                transcription[0] = item
                isZero = True
        if (isZero == False):
            transcription[9] = item

    #Find 2 and 5
    for item in fives:
        isTwo = False
        if (item == transcription[3]):
            continue
        for char in item:
            if not (char in transcription[6]):
                transcription[2] = item
                isTwo = True
        if (isTwo == False):
            transcription[5] = item

    #Parse output number
    outnum = 0
    outnum = outnum + transcription.index(sorted(outdigits[0]))*1000
    outnum = outnum + transcription.index(sorted(outdigits[1]))*100
    outnum = outnum + transcription.index(sorted(outdigits[2]))*10
    outnum = outnum + transcription.index(sorted(outdigits[3]))
    totalsum = totalsum + outnum
    print("Round number:",outnum,", Running Total:",totalsum)