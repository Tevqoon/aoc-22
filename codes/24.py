def process(line):
    return []

with open("../inputs/24.txt") as f:
    lines = {(x, y) for x, line in enumerate(f) for y, point in enumerate(line.rstrip()) if point == "#"}
