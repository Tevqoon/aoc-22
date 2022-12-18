from itertools import product

with open("../inputs/18.txt") as f:
    lines = {tuple(map(lambda x : int(x), line.split(","))) for line in f}

maxx = max(lines, key=lambda x: x[0])[0]
maxy = max(lines, key=lambda x: x[1])[1]
maxz = max(lines, key=lambda x: x[2])[2]

dirs = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]

def area(working):
    count = 0
    for x,y,z in working:
        tmp = 6
        for dx, dy, dz in dirs:
            if (x + dx, y + dy, z + dz) in working:
                tmp -= 1
        count += tmp
    return count

count_all = area(lines)
print(count_all)

table = [[[(x,y,z) in lines for z in range(maxz + 1)] for y in range(maxy + 1)] for x in range(maxx + 1)]
Q = [(0,0,0)]
while Q:
    x,y,z = Q.pop()
    if 0 <= x <= maxx and 0 <= y <= maxy and 0 <= z <= maxz and not table[x][y][z]:
        table[x][y][z] = True
        for dx, dy, dz in dirs:
            if (0 <= x + dx <= maxx and 0 <= y + dy <= maxy and 0 <= z + dz <= maxz and
                not table[x + dx][y + dy][z + dz]):
                Q.append((x + dx, y + dy, z + dz))

pockets = set()
for i, x in enumerate(table):
    for j, y in enumerate(x):
        for k, z in enumerate(y):
            if not z:
                pockets.add((i,j,k))

print(count_all - area(pockets))
