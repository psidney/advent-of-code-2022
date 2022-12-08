

f = open('8.txt')

data = []

line = f.readline()

while line:
    data.append(line.replace('\n',''))
    line = f.readline()

field = []

for line in data:
    temp = []
    for l in line:
        temp.append(int(l))
    field.append(temp)

count = 0
y = 0
tree_list = {}

for row in field:
    cursor = 0
    tallest_tree = -1
    while cursor<len(row):
        if row[cursor]>tallest_tree:
            tallest_tree = row[cursor]
            tree_list[str(cursor) + '_' + str(y)] = True
        cursor+=1
    cursor = len(row)-1
    tallest_tree = -1
    while cursor>=0:
        if row[cursor]>tallest_tree:
            tallest_tree = row[cursor]
            tree_list[str(cursor) + '_' + str(y)] = True
        cursor-=1
    y+=1

x = 0
while x<len(field[0]):
    cursor = 0
    tallest_tree = -1
    while cursor<len(field):
        if field[cursor][x] > tallest_tree:
            tallest_tree = field[cursor][x]
            tree_list[str(x) + '_' + str(cursor)] = True
        cursor +=1
    cursor = len(field)-1
    tallest_tree = -1
    while cursor>=0:
        if field[cursor][x] > tallest_tree:
            tallest_tree = field[cursor][x]
            tree_list[str(x) + '_' + str(cursor)] = True
        cursor -=1
    x+=1

print(f"1:{len(tree_list.keys())}")

#part 2

def calculate_score(x,y,field):
    left = 0
    right = 0
    down = 0
    up = 0
    if x == 0 or y == 0 or x == len(field[0])-1 or y==len(field)-1:
        return 0

    height = field[y][x]
    x2 = x+1
    right +=1
    while x2<len(field[0])-1 and field[y][x2]<height:
        x2 += 1
        right +=1
    y2 = y+1
    down +=1
    while y2<len(field)-1 and field[y2][x]<height:
        y2 += 1
        down +=1
    x2 = x-1
    left +=1
    while x2>0 and field[y][x2]<height:
        x2 -=1
        left +=1
    y2 = y-1
    up +=1
    while y2>0 and field[y2][x]<height:
        y2 -=1
        up+=1
    return left * right * up * down

y = 0
max_score = 0

while y<len(field):
    x = 0
    while x<len(field[0]):
        if calculate_score(x,y,field)>max_score:
            max_score = calculate_score(x,y,field)
        x+=1
    y+=1

print(f"2:{max_score}")