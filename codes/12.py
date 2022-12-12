from math import floor
import heapq

with open("../inputs/12.txt") as f:
    lines = [[ord(char) - ord("a") + 1 for char in list(line.rstrip())] for line in f]

sx,sy = (0,0)
E = (0,0)
lowest = []
for i, l in enumerate(lines):
    for j, x in enumerate(l):
        if x == -13:
            sx, sy = i, j
            lowest.append(S)
        elif x == -27:
            E = (i,j)
        elif x == 1:
            lowest.append((i,j))

lines[sx][sy] = 1
lines[E[0]][E[1]] = ord("z") - ord("a") + 1

dirs = [(0,1), (0,-1), (1,0), (-1, 0)]
            
def dijkstra(G, s):
    lx = len(G)
    ly = len(G[0])
    razdalja = [[float("inf") for _ in range(ly)] for _ in range(lx)]
    razdalja[s[0]][s[1]] = 0
    predhodniki = {}
    R = [(0, s)]
    while R:
        p, (sx, sy) = heapq.heappop(R)
        if p == razdalja[sx][sy]:
            new_dirs = [(sx + dx, sy + dy) for dx, dy in dirs if (0 <= sx + dx < lx and 0 <= sy + dy < ly)]
            new_dirs = [(newx, newy) for newx, newy in new_dirs if (G[newx][newy] >= G[sx][sy] or G[newx][newy] - G[sx][sy] == -1)]
            for newx, newy in new_dirs:
                alt = razdalja[sx][sy] + 1
                if alt < razdalja[newx][newy]:
                    razdalja[newx][newy] = alt
                    predhodniki[(newx, newy)] = (sx, sy)
                    heapq.heappush(R, (alt, (newx, newy)))
    return razdalja #, predhodniki
        
distances = dijkstra(lines, E)
print(distances[sx][sy])
print(min([distances[lx][ly] for lx, ly in lowest]))


