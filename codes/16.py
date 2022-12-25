from tqdm import tqdm
from collections import defaultdict
from itertools import chain, combinations

def process(line):
    words = line.replace(";", "").replace(",", "").replace("=", " ").split(" ")
    return words[1], int(words[5]), tuple(words[10:])

with open("../inputs/16.txt") as f:
    lines = [process(line.rstrip()) for line in f]

graph = dict()
for x, i, rest in lines:
    graph[x] = (i, rest)

nonnil = frozenset({(x, i) for x, i, _ in lines if i != 0})

dist = defaultdict(lambda : float("+inf"))
for start, (_, targets) in graph.items():
    dist[(start, start)] = 0
    for target in targets:
        dist[(start, target)] = 1
for k in graph.keys():
    for i in graph.keys():
        for j in graph.keys():
            if dist[(i,j)] > (new := dist[(i,k)] + dist[(k,j)]):
                dist[(i,j)] = new

def dfs1(start="AA", time_left=30, score=0, to_open=nonnil):
    if time_left <= 0 or to_open == set():
        return score
    m = score
    for option, flow in to_open:
        next_time = time_left - dist[(start,option)] - 1
        m = max(m, dfs1(option, next_time, score + flow * next_time, to_open - {(option, flow)}))
    return m

print(dfs1())

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return list(map(frozenset, list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))))

vals = dict()
powers = powerset(nonnil)
for set1 in tqdm(powers):
    vals[set1] = dfs1(time_left=26, to_open=set1)

m = 0
for set1 in tqdm(powers):
    set2 = nonnil - set1
    m = max(m, vals[set1] + vals[set2])
print(m)
