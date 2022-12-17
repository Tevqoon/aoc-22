from tqdm import tqdm
import re

with open("../inputs/15.txt") as f:
    lines = [[int(x) for x in re.findall(r'-?\d+', line)] for line in f]

sensors = sorted([(abs(x1 - x2) + abs(y1 - y2), x1, y1) for x1, y1, x2, y2 in lines], reverse=1)

merge = lambda a,b,c,d : (None, (min(a, c), max(b, d))) if a - 1 <= c <= b + 1 else ((a, b), (c, d))

def add_interval(intervals, new_i, index=0):
    if new_i[0] > new_i[1]: return
    while index < len(intervals):
        i1, new_i = merge(*sum(sorted([intervals.pop(index), new_i]), ()))
        if i1: index, _ = index + 1, intervals.insert(index, i1)
    intervals.append(new_i)
            
# Part 1
rowy = 2000000
firstint = []
for d, x1, y1 in sensors:
    add_interval(firstint, (x1 - (lr := d - abs(y1 - rowy)), x1 + lr))

print(sum([y - x + 1 for x, y in firstint]) - len({1 for _, _, _, y in lines if y == rowy}))
  
# Part 2
dmax = 4000000
for x, y in (([], y) for y in tqdm(range(dmax))):
    for d, x1, y1 in sensors:
        add_interval(x, (max(x1 - (lr := d - abs(y1 - y)), 0), min(x1 + lr, dmax)))
        if x == [(0, dmax)]: break
    else:
        print((x[0][1] + 1) * dmax + y)
        break
