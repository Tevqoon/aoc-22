from collections import defaultdict

def process(lines):
    return {(x, y) : True for x, line in enumerate(lines) for y, point in enumerate(line.rstrip()) if point == "#"}

with open("../inputs/23.txt") as f:
    lines = process(f)

sample = process("""....#..
..###.#
#...#.#
.#...##
#.###..
##.#.##
.#..#..""".split("\n"))

smaller = process(""".....
..##.
..#..
.....
..##.
.....""".split("\n"))

working = lines

# N = (-1, 0), S = (1, 0), E = (0, 1), W = (0, -1)
dir8 = [(x,y) for x in range(-1,2) for y in range(-1, 2) if (x,y) != (0,0)]
dir4 = [[(-1, 0), (-1,1), (-1,-1)],
        [(1,0), (1,1), (1,-1)],
        [(0,-1), (-1,-1), (1,-1)],
        [(0,1), (-1,1), (1,1)]]

def printer(board):
    for x in range(-5,10):
        for y in range(-10,20):
            if board.get((x,y)):
                print("#", end="")
            else:
                print(".", end="")
        print()
    print()

def move(board, dir4):
    propositions = defaultdict(lambda : [])
    new_board = dict()
    for x,y in board.keys():
        if len([1 for dx, dy in dir8 if board.get((x + dx, y + dy))]) > 0:
            for dirs in dir4:
                for dx, dy in dirs:
                    if board.get((x + dx, y + dy)):
                        break
                else:
                    dx, dy = dirs[0]
                    propositions[(x + dx, y + dy)].append((x,y))
                    break
            else:
                propositions[(x,y)].append((x,y))
        else:
            propositions[(x,y)].append((x,y))
    #print("Propositions: ", dict(propositions))
    for new, olds in propositions.items():
        if len(olds) == 1:
            new_board[new] = True
        else:
            for old in olds:
                new_board[old] = True
    #print("New board state: ", new_board.keys())
    return new_board, dir4[1:] + dir4[:1]

def boundaries(board):
    points = board.keys()
    minx = min(points, key=lambda x: x[0])[0]
    maxx = max(points, key=lambda x: x[0])[0]
    miny = min(points, key=lambda x: x[1])[1]
    maxy = max(points, key=lambda x: x[1])[1]
    return((minx, miny), (maxx, maxy))

one = working.copy()
onedirs = dir4.copy()
for _ in range(10):
    one, onedirs = move(one, onedirs)
    #printer(working)

(minx, miny), (maxx, maxy) = boundaries(one)
print((maxx - minx + 1) * (maxy - miny + 1) - len(one))

two = working.copy()
prev = dict()
twodirs = dir4.copy()
index = 0
while prev != two:
    if index % 1000 == 0:
        print(index)
    prev = two
    two, twodirs = move(two, twodirs)
    index += 1
print(index)
