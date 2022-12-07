

data = []

f = open('3.txt')
line = f.readline()

while(line):
    data.append(line.replace('\n',''))
    line = f.readline()

letters = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

found = []
for pack in data:
    items = {}
    left = pack[0:(len(pack)//2)]
    right = pack[(len(pack)//2):]
    i = 0
    foundFlag = False
    while i<len(left) and foundFlag == False:
        j = 0
        while j<len(right) and foundFlag == False:
            if left[i]==right[j]:
                found.append(left[i])
                foundFlag = True
            j+=1
        i+=1

score = 0
for letter in found:
    score += letters.find(letter)

print(f"Answer 1: {score}")

d = 0

badges = []
while d<len(data):
    groupA = [data[d], data[d+1], data[d+2]]
    foundFlag = False
    i = 0
    while i<len(groupA[0]) and foundFlag == False:
        j = 0
        while j<len(groupA[1]) and foundFlag == False:
            k = 0
            while k<len(groupA[2]) and foundFlag == False:
                if groupA[0][i] == groupA[1][j] and groupA[0][i] == groupA[2][k]:
                    badges.append(groupA[0][i])
                    foundFlag = True
                k+=1
            j+=1
        i+=1
    d += 3

score = 0
for badge in badges:
    score += letters.find(badge)

print(f"Answer 2: {score}")