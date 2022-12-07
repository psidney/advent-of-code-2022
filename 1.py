

f = open('1.txt')

data = []
line = f.readline()

while(line):
    if line == "\n":
        data.append(0)
    else:
        data.append(int(line))
    line = f.readline()

totals = []
i = 0
running = 0
while i<len(data):
    if data[i] == 0:
        totals.append(running)
        running = 0
    else:
        running += data[i]
    i+=1

totals.sort(reverse=True)
print(f"1: {max(totals)}")
print(f"2: {sum(totals[0:3])}")
