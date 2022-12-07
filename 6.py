
f = open('6.txt')
data = f.read()

startSignal = 0
while len(set(data[startSignal:startSignal+4]))!=4:
    startSignal+=1

print(f"1:{startSignal+4}")

startSignal = 0
while len(set(data[startSignal:startSignal+14]))!=14:
    startSignal+=1

print(f"2:{startSignal+14}")