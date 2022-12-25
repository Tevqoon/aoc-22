from collections import defaultdict

with open("../inputs/23.txt") as f:
    lines = {(x, y) for x, line in enumerate(f) for y, point in enumerate(line.rstrip()) if point == "#"}

# N = (-1, 0), S = (1, 0), E = (0, 1), W = (0, -1)
dir8 = [(x,y) for x in range(-1,2) for y in range(-1, 2) if (x,y) != (0,0)]
dir4 = [[(-1, 0), (-1, 1), (-1,-1)],
        [(1 , 0), (1 , 1), (1 ,-1)],
        [(0 ,-1), (-1,-1), (1 ,-1)],
        [(0 , 1), (-1, 1), (1 , 1)]]
index = 0

def move(board):
    global dir4, index
    index += 1
    propositions = defaultdict(lambda : [])
    for x,y in board:
        if len([1 for dx, dy in dir8 if (x + dx, y + dy) in board]) > 0:
            for dirs in dir4:
                for dx, dy in dirs:
                    if (x + dx, y + dy) in board:
                        break
                else:
                    dx, dy = dirs[0]
                    propositions[(x + dx, y + dy)].append((x,y))
                    break
    change = False
    for new, olds in propositions.items():
        if (old := olds.pop()) and not olds:
            change = True
            board.add(new)
            board.remove(old)
    dir4 = dir4[1:] + dir4[:1]
    return change

def area(board):
    mins, maxs = [], []
    for i in range(2):
        mins.append(min(board, key=lambda x: x[i])[i])
        maxs.append(max(board, key=lambda x: x[i])[i])
    return (maxs[0] - mins[0] + 1) * (maxs[1] - mins[1] + 1)

while move(lines):
    if index == 10:
        print(area(lines) - len(lines))
print(index)
