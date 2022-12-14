from math import copysign

with open("../inputs/14.txt") as f:
    lines = [[tuple(map(int,pair.split(","))) for pair in line.rstrip().split(" -> ")] for line in f]
    
sand = set()

def draw(p1, p2):
    "Returns all the points between two points (assumed hor/vert line)"
    x1, y1 = p1
    x2, y2 = p2
    if x1 == x2:
        sign = int(copysign(1, y2 - y1))
        return [(x1, y) for y in range(y1, y2 + sign, sign)]
    elif y1 == y2:
        sign = int(copysign(1, x2 - x1))
        return [(x, y1) for x in range(x1, x2 + sign, sign)]

maxd = float("-inf")
for line in lines:
    for first, second in zip(line, line[1:]):
        for point in draw(first, second):
            maxd = max(maxd, point[1])
            sand.add(point)
maxd += 1
            
def drop1():
    p1, p2 = 500, 0
    while p2 < maxd:
        if not((p1, p2 + 1) in sand):
            p2 += 1
        elif not((p1 - 1, p2 + 1) in sand):
            p1 -= 1
            p2 += 1
        elif not((p1 + 1, p2 + 1) in sand):
            p1 += 1
            p2 += 1
        else:
            sand.add((p1, p2))
            return True
    return False

def drop2():
    p1, p2 = 500, 0
    while not((500, 0) in sand):
        if p2 == maxd:
            sand.add((p1, p2))
            return True
        elif not((p1, p2 + 1) in sand):
            p2 += 1
        elif not((p1 - 1, p2 + 1) in sand):
            p1 -= 1
            p2 += 1
        elif not((p1 + 1, p2 + 1) in sand):
            p1 += 1
            p2 += 1
        else:
            sand.add((p1, p2))
            return True
    return False

s = 0
while drop1():
    s += 1
    pass

print(s)

# The first sort of drop will always fill up first.
while drop2(): 
    s += 1
    pass

print(s)
        

