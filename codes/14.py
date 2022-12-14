from math import copysign

with open("../inputs/14.txt") as f:
    lines = [[tuple(map(int,pair.split(","))) for pair in line.rstrip().split(" -> ")] for line in f]

sample = [[(498,4), (498,6), (496,6)], [(503,4), (502,4), (502,9), (494,9)]]

sand1 = dict()
sand2 = dict()

def addt(t1, t2):
    return tuple(map(sum, zip(t1, t2)))

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
            sand1[point] = "#"
            sand2[point] = "#"

def drop1(point=(500,0)):
    if point[1] > 500:
        return False
    elif not(addt(point, (0, 1)) in sand1):
        return drop1(addt(point, (0, 1)))
    elif not(addt(point, (-1, 1)) in sand1):
        return drop1(addt(point, (-1, 1)))
    elif not(addt(point, (1, 1)) in sand1):
        return drop1(addt(point, (1,1)))
    else:
        sand1[point] = "o"
        return True

def drop2(point=(500,0)):
    if (500, 0) in sand2:
        return False
    elif point[1] == maxd + 1:
        sand2[point] = "o"
        return True
    elif not(addt(point, (0, 1)) in sand2):
        return drop2(addt(point, (0, 1)))
    elif not(addt(point, (-1, 1)) in sand2):
        return drop2(addt(point, (-1, 1)))
    elif not(addt(point, (1, 1)) in sand2):
        return drop2(addt(point, (1,1)))
    else:
        sand2[point] = "o"
        return True
    
while drop1():
    pass

while drop2():
    pass

print(list(sand1.values()).count("o"))
print(list(sand2.values()).count("o"))
        

