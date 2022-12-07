f = open('2.txt')

data = []
line = f.readline()

while(line):
    lineData = line.replace('\n','').split(" ")
    data.append(lineData[0] + "_" + lineData[1])
    line = f.readline()

scoreA = 0
scoreB = 0
winTable = { 'A_X': 0, 'A_Y':2, 'A_Z': 1,
             'B_X': 1, 'B_Y':0, 'B_Z': 2,
             'C_X': 2, 'C_Y':1, 'C_Z': 0}

loseTable2= {'A':3,'B':1,'C':2}
tieTable2 = {'A':1,'B':2,'C':3}
winTable2 = {'A':2,'B':3,'C':1}
for battle in data:
    winner = winTable[battle]
    if battle[0] == 'A':
        scoreA+=1
    elif battle[0] == 'B':
        scoreA+=2
    elif battle[0] == 'C':
        scoreA+=3
    if battle[2] == 'X':
        scoreB+=1
    elif battle[2] == 'Y':
        scoreB+=2
    elif battle[2] == 'Z':
        scoreB+=3
    if winner==0:
        scoreA += 3
        scoreB += 3
    elif winner==1:
        scoreA+=6
    elif winner==2:
        scoreB+=6

print(f"1: {scoreA} / {scoreB}")

scoreA = 0
scoreB = 0
for battle in data:
    if battle[2] == 'X':
        scoreB+= loseTable2[battle[0]]
        scoreA+= tieTable2[battle[0]]
        scoreA+=6
    elif battle[2] == 'Y':
        scoreB+= tieTable2[battle[0]]
        scoreA+= tieTable2[battle[0]]
        scoreA+=3
        scoreB+=3
    elif battle[2] == 'Z':
        scoreB+= winTable2[battle[0]]
        scoreA+= tieTable2[battle[0]]
        scoreA+=0
        scoreB+=6


print(f"2: {scoreA} / {scoreB}")