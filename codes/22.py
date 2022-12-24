import re

with open("../inputs/22.txt") as f:
    lines = [line.rstrip() for line in f]

mapa = dict()

sample = ["        ...#    ",
          "        .#..    ",
          "        #...    ",
          "        ....    ",
          "...#.......#    ",
          "........#...    ",
          "..#....#....    ",
          "..........#.    ",
          "        ...#....",
          "        .....#..",
          "        .#......",
          "        ......#.",
          "\n",
          "10R5L5R10L4R5L5"]

working = lines

instructions = [int(instr) if instr.isnumeric() else instr for instr in re.findall(r"\d+|[A-Z]", working[-1])]

indexesx = [[] for _ in range(len(working[:-2]))]
indexesy = [[] for _ in range(len(working[0]))]

for x, l in enumerate(working[:-2]):
    for y, p in enumerate(l):
        if p != " ":
            indexesx[x].append(y)
            indexesy[y].append(x)
            mapa[(x,y)] = p

indexesx = [(line[0], line[-1]) for line in indexesx]
indexesy = [(line[0], line[-1]) for line in indexesy]

rotations = {"L": ((0, -1), (1, 0)), "R": ((0, 1), (-1, 0))}

def scalar(row, col):
    return row[0] * col[0] + row[1] * col[1]

def rotate(direction, rotation):
    return (scalar(rotations[rotation][0], direction), scalar(rotations[rotation][1], direction))

def move1(point, direction):
    x, y = point
    dx, dy = direction
    if dx:
        minx, maxx = indexesy[y]
        newx = minx + ((x + dx - minx) % (maxx - minx + 1))
        if mapa[(newx, y)] == ".":
            return (newx, y)
        else:
            return point
    elif dy:
        miny, maxy = indexesx[x]
        newy = miny + ((y + dy - miny) % (maxy - miny + 1))
        if mapa[(x, newy)] == ".":
            return (x, newy)
        else:
            return point

# def move(start, direction, instructions):
#     if instructions == []:
#         return start, direction
#     elif instructions[0] in ["R", "L"]:
#         return move(start, rotate(direction, instructions[0]), instructions[1:])
#     elif instructions[0] == 0:
#         return move(start, direction, instructions[1:])
#     else:
#         instructions[0] -= 1
#         return move(move1(start, direction), direction, instructions)
        

#(x, y), (dx, dy) = move((0, indexesx[0][0]), (0, 1), instr)

x, y = 0, indexesx[0][0]
dx, dy = (0, 1)
while instructions:
    if instructions[0] in ["R", "L"]:
        dx, dy = rotate((dx, dy), instructions[0])
        instructions.pop(0)
    elif instructions[0] == 0:
        instructions.pop(0)
    else:
        instructions[0] -= 1
        x, y = move1((x,y), (dx, dy))
    
x += 1 # row
y += 1 # col
dirvaluesy = [0, 0, 2]
dirvaluesx = [0, 1, 3]
print(1000 * x + 4 * y + dirvaluesy[dy] + dirvaluesx[dx])
