with open("../inputs/18.txt") as f:
    lines = {tuple(map(lambda x : int(x), line.split(","))) for line in f}

maxx, maxy, maxz = [max(lines, key=lambda x: x[i])[i] for i in range(3)]
dirs = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]

def area(working):
    count = 0
    for x,y,z in working:
        tmp = 6
        for dx, dy, dz in dirs:
            tmp -= 1 if (x + dx, y + dy, z + dz) in working else 0
        count += tmp
    return count

count_all = area(lines)
print(count_all)

table = [[[(x,y,z) in lines for z in range(maxz + 1)] for y in range(maxy + 1)] for x in range(maxx + 1)]
Q = [(0,0,0)]
while Q:
    x,y,z = Q.pop()
    for dx, dy, dz in dirs:
        if (0 <= (nx := x + dx) <= maxx and
            0 <= (ny := y + dy) <= maxy and
            0 <= (nz := z + dz) <= maxz and
            not table[nx][ny][nz]):
            table[nx][ny][nz] = True
            Q.append((nx, ny, nz))

pockets = set()
for i, x in enumerate(table):
    for j, y in enumerate(x):
        for k, z in enumerate(y):
            if not z:
                pockets.add((i,j,k))

print(count_all - area(pockets))

