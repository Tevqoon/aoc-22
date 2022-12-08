with open("../inputs/8.txt") as f:
    lines = [list(map(int, list(line.rstrip()))) for line in f]

test = [
    [3,0,3,7,3],
    [2,5,5,1,2],
    [6,5,3,3,2],
    [3,3,5,4,9],
    [3,5,3,9,0]
]

def count_visible(trees):
    l = len(trees)
    count = 0
    for y, line in enumerate(trees):
        for x, tree in enumerate(line):
            if y == 0 or x == 0 or x == l - 1 or y == l -1:
                count += 1
            else:
                flag1, flag2, flag3, flag4 = True, True, True, True
                for i in range(x + 1, l):
                    if trees[y][i] >= tree:
                        flag1 = False
                for i in range(y + 1, l):
                    if trees[i][x] >= tree:
                        flag2 = False
                for i in range(0, x):
                    if trees[y][i] >= tree:
                        flag3 = False
                for i in range(0, y):
                    if trees[i][x] >= tree:
                        flag4 = False
                if flag1 or flag2 or flag3 or flag4:
                    #print((y,x,tree))
                    count += 1
    return count

def scenic_score(trees):
    l = len(trees)
    scores = [[0 for _ in range(l)] for _ in range(l)]
    for y, line in enumerate(trees):
        for x, tree in enumerate(line):
            count1, count2, count3, count4 = 0,0,0,0
            # Up
            for i in range(y - 1, -1, -1):
                if trees[i][x] < tree:
                    count1 += 1
                if trees[i][x] >= tree:
                    count1 += 1
                    break
            # Left
            for i in range(x - 1, -1, -1):
                if trees[y][i] < tree:
                    count2 += 1
                if trees[y][i] >= tree:
                    count2 += 1
                    break
            # Down
            for i in range(y + 1, l):
                if trees[i][x] < tree:
                    count3 += 1
                if trees[i][x] >= tree:
                    count3 += 1
                    break
            # Right
            for i in range(x + 1, l):
                if trees[y][i] < tree:
                    count4 += 1
                if trees[y][i] >= tree:
                    count4 += 1
                    break
            scores[y][x] = count1 * count2 * count3 * count4
    return max(map(max, scores))
    #return scores
                
print(count_visible(lines))
print(scenic_score(lines))
