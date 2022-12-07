"""
            [M] [S] [S]            
        [M] [N] [L] [T] [Q]        
[G]     [P] [C] [F] [G] [T]        
[B]     [J] [D] [P] [V] [F] [F]    
[D]     [D] [G] [C] [Z] [H] [B] [G]
[C] [G] [Q] [L] [N] [D] [M] [D] [Q]
[P] [V] [S] [S] [B] [B] [Z] [M] [C]
[R] [H] [N] [P] [J] [Q] [B] [C] [F]
 1   2   3   4   5   6   7   8   9 
 """

stacks = []
stacks.append([])
stacks.append(["G","B","D","C","P","R"])
stacks.append(["G","V","H"])
stacks.append(["M","P","J","D","Q","S","N"])
stacks.append(["M","N","C","D","G","L","S","P"])
stacks.append(["S","L","F","P","C","N","B","J"])
stacks.append(["S","T","G","V","Z","D","B","Q"])
stacks.append(["Q","T","F","H","M","Z","B"])
stacks.append(["F","B","D","M","C"])
stacks.append(["G","Q","C","F"])

data = []

f = open('5.txt')
line = f.readline()

while(line):
    nums = line.replace("move ","").replace("\n","").replace(" from ",",").replace(" to ",",")
    row = []
    for n in nums.split(','):
        row.append(int(n))
    data.append(row)
    line = f.readline()

for row in data:
    move = row[0]
    start = row[1]
    end = row[2]

    for i in range(0,move):
        stacks[end].insert(0,stacks[start][0])
        del stacks[start][0]


s = ""
del stacks[0]
for i in stacks:
    s += i[0]

print(f"1:{s}")

stacks = []
stacks.append([])
stacks.append(["G","B","D","C","P","R"])
stacks.append(["G","V","H"])
stacks.append(["M","P","J","D","Q","S","N"])
stacks.append(["M","N","C","D","G","L","S","P"])
stacks.append(["S","L","F","P","C","N","B","J"])
stacks.append(["S","T","G","V","Z","D","B","Q"])
stacks.append(["Q","T","F","H","M","Z","B"])
stacks.append(["F","B","D","M","C"])
stacks.append(["G","Q","C","F"])

for row in data:
    move = row[0]
    start = row[1]
    end = row[2]

    slicestack = stacks[start][0:move]
    stacks[end] = slicestack + stacks[end]
    stacks[start] = stacks[start][move:]


s = ""
del stacks[0]
for i in stacks:
    s += i[0]


print(f"2:{s}")