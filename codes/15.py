from collections import defaultdict

def manhattan(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)

def process(line):
    lst = [int(x.replace(",", "").replace(":", "").split("=")[1]) for x in line.rstrip().split(" ") if x != x.split("=")[0]]
    x1, y1, x2, y2 = tuple(lst)
    return (x1, y1, x2, y2, manhattan((x1, y1), (x2, y2)))

with open("../inputs/15.txt") as f:
    lines = [process(line) for line in f]

sensors = [(x1, y1, d) for x1, y1, _, _, d in lines]
beacons = {(x2, y2)    for _, _, x2, y2, _ in lines}

def merge_intervals(i1, i2):
    a, b = i1
    c, d = i2
    if a - 1 <= c <= b + 1 or c - 1 <= a <= d + 1:
        return [(min(a, c), max(b,d))]
    elif b < c:
        return [(a, b), (c, d)]
    elif d < a:
        return [(c, d), (a, b)]

def add_interval(intervals, new_interval):
    if intervals == []:
        return [new_interval]
    new = merge_intervals(intervals[0], new_interval)
    if len(intervals) == 1:
        return new
    else:
        return new[:-1] + add_interval(intervals[1:], new[-1])

# Part 1
rowy = 2000000
firstint = []
for x1, y1, d in sensors:
    lr = d - abs(y1 - rowy) # if < 0, we have nothing left
    if lr > 0:
        firstint = add_interval(firstint, (x1 - lr, x1 + lr))

print(sum([y - x for x, y in firstint]))
  
        
# Part 2
dmax = 4000000        
rows = defaultdict(lambda: [])
for x1, y1, d in sensors:
    for y in range(max(y1 - d, 0), min(y1 + d + 1, dmax)):
        lr = abs(d - abs(y1 - y))
        rows[y] = add_interval(rows[y], (max(x1 - lr, 0), min(x1 + lr, dmax)))

for k, v in rows.items():
    if len(v) > 1:
        print((v[0][1] + 1) * 4000000 + k)
        break


