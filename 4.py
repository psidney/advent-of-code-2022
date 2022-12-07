data = []

f = open('4.txt')
line = f.readline()

while(line):
    pairA = line.replace('\n','').replace('-',',').split(',')
    pair = []
    for p in pairA:
        pair.append(int(p))
    data.append(pair)
    line = f.readline()

counter = 0
for pair in data:
    if (pair[0]>=pair[2] and pair[1]<=pair[3]) or (pair[2]>=pair[0] and pair[3]<=pair[1]):
        counter +=1

print(f"1: {counter}")

counter = 0
for pair in data:
    chairs = {}
    overlap = False
    for i in range(pair[0], pair[1]+1):
        chairs[i] = 1
    for i in range(pair[2], pair[3]+1):
        if i in chairs.keys():
            overlap = True
    if overlap == True:
        counter +=1
print(f"2: {counter}")