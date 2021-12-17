file = open('Advent-of-Code-2021\\Day 16\\Day 16 input.txt','r')

string = file.readline().strip()

dict = {'0':'0000','1':'0001','2': '0010','3': '0011','4': '0100','5': '0101','6': '0110','7': '0111','8': '1000','9': '1001','A': '1010','B': '1011','C': '1100','D': '1101','E': '1110','F': '1111'}

opstring = ''
oppos = 0
bitpos = 0
evalstack = []

def parse_packet():
    global opstring
    global oppos
    global string
    global bitpos
    packetdone = False

    while packetdone == False:
        if (len(opstring) < 3):
            opstring = opstring + dict[string[oppos]]
            oppos = oppos + 1
        version = int(opstring[0:3],base=2)
        opstring = opstring[3:]
        bitpos = bitpos + 3
        # print("Version:",version)
        
        if (len(opstring) < 3):
            opstring = opstring + dict[string[oppos]]
            oppos = oppos + 1
        typeid = int(opstring[0:3],base=2)
        opstring = opstring[3:]
        bitpos = bitpos + 3
        # print("Type:",typeid)
        
        if (typeid == 4):
            num = ''
            numcomplete = False
            while numcomplete == False:
                while (len(opstring) < 5):
                    opstring = opstring + dict[string[oppos]]
                    oppos = oppos + 1
                numadd = opstring[0:5]
                if (numadd[0] == '0'):
                    numcomplete = True
                num = num + numadd[1:]
                opstring = opstring[5:]
                bitpos = bitpos + 5
            value = int(num,base=2)
            # print("Value:",value)
            packetdone = True
        else:
            if (len(opstring) < 1):
                opstring = opstring + dict[string[oppos]]
                oppos = oppos + 1
            lengthid = opstring[0]
            opstring = opstring[1:]
            bitpos = bitpos + 1
            subpackets = []
            if (lengthid == '0'):
                while (len(opstring) < 15):
                    opstring = opstring + dict[string[oppos]]
                    oppos = oppos + 1
                bitlength = int(opstring[0:15],base=2)
                opstring = opstring[15:]
                bitpos = bitpos + 15
                startpos = bitpos
                while (bitpos < (startpos + bitlength)):
                    subpackets.append(parse_packet())
                packetdone = True
            else:
                while (len(opstring)< 11):
                    opstring = opstring + dict[string[oppos]]
                    oppos = oppos + 1
                numpackets = int(opstring[0:11],base=2)
                opstring = opstring[11:]
                bitpos = bitpos + 11
                for p in range(numpackets):
                    subpackets.append(parse_packet())
                packetdone = True
    
    if (typeid == 4):
        return [version,typeid,value]
    else:
        return [version,typeid,subpackets]

def eval_packet(packet):
    type = packet[1]
    value = 0
    match type:
        case 0:
            value = 0
            for p in packet[2]:
                value += eval_packet(p)
        
        case 1:
            value = 1
            for p in packet[2]:
                value *= eval_packet(p)
        
        case 2:
            list = []
            for p in packet[2]:
                list.append(eval_packet(p))
            value = min(list)
        
        case 3:
            list = []
            for p in packet[2]:
                list.append(eval_packet(p))
            value = max(list)
        
        case 4:
            value = packet[2]

        case 5:
            if ((eval_packet(packet[2][0])) > (eval_packet(packet[2][1]))):
                value = 1
            else:
                value = 0

        case 6:
            if ((eval_packet(packet[2][0])) < (eval_packet(packet[2][1]))):
                value = 1
            else:
                value = 0

        case 7:
            if ((eval_packet(packet[2][0])) == (eval_packet(packet[2][1]))):
                value = 1
            else:
                value = 0
    
    return value

packets = parse_packet()
# print(packets)
execval = eval_packet(packets)
print(execval)

