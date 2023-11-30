from collections import defaultdict

with open("../inputs/17.txt") as f:
    instr = [list(line) for line in f][0]


sample = list(">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>")

working = sample
lw = len(working)

blocks = [
    [[1, 1, 1, 1]],
    
    [[0, 1, 0],
     [1, 1, 1],
     [0, 1, 0]],
    
    [[0, 0, 1],
     [0, 0, 1],
     [1, 1, 1]],

    [[1],
     [1],
     [1],
     [1]],
    
    [[1, 1],
     [1, 1]]
]
lb = len(blocks)

step = 0
highest = 0
well = defaultdict(lambda : [0] * 7)
well[-1] = [1] * 7

def covering(l1, l2):
    for x in map(lambda x, y : x and y, l1, l2):
        if x:
            return True
    else:
        return False

def ormap(l1, l2):
    return list(map(lambda x, y : x or y, l1, l2))

def moveright(padded):
    edge = [line[-1] for line in padded]
    for e in edge:
        if e:
            return padded
    return [line[-1:] + line[:-1] for line in padded]
            
def moveleft(padded):
    edge = [line[0] for line in padded]
    for e in edge:
        if e:
            return padded
    return [line[1:] + line[:1] for line in padded]

def drop(block):
    global step
    global highest
    global well
    h = len(block)
    l = len(block[0])
    padded = [[0] * 2 + line + [0] * (7 - l - 2) for line in block]

    y = highest + 3
    while True:
        #print("step", working[step % lw])
        if working[step % lw] == ">":
            padded = moveright(padded)
        elif working[step % lw] == "<":
            padded = moveleft(padded)
        step += 1
            
        if covering(padded[-1], well[y - 1]):
            for offset, line in enumerate(reversed(padded)):
                well[y + offset] = ormap(line, well[y + offset])
            break
        else:
            y -= 1
            
    highest = y + h
    print(highest)

def printer():
    for i in range(highest, -1, -1):
        print(well[i])
    
drop(blocks[0])
drop(blocks[1])
drop(blocks[2])
printer()
#print(well)
#drop(blocks[1])
#print(well)

#for i in range(2022):
#    drop(blocks[i % lb])
#
#print(highest)    
