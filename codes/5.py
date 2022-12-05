with open("../inputs/5.txt") as f:
    lines = [line.rstrip() for line in f]

sep = lines.index("")
table1 = [["D", "L", "V", "T", "M", "H", "F"],
         ["H", "Q", "G", "J", "C", "T", "N", "P"],
         ["R", "S", "D", "M", "P", "H"],
         ["L", "B", "V", "F"],
         ["N", "H", "G", "L", "Q"],
         ["W", "B", "D", "G", "R", "M", "P"],
         ["G", "M", "N", "R", "C", "H", "L", "Q"],
         ["C", "L", "W"],
         ["R", "D", "L", "Q", "J", "Z", "M", "T"]]
table2 = [["D", "L", "V", "T", "M", "H", "F"],
         ["H", "Q", "G", "J", "C", "T", "N", "P"],
         ["R", "S", "D", "M", "P", "H"],
         ["L", "B", "V", "F"],
         ["N", "H", "G", "L", "Q"],
         ["W", "B", "D", "G", "R", "M", "P"],
         ["G", "M", "N", "R", "C", "H", "L", "Q"],
         ["C", "L", "W"],
         ["R", "D", "L", "Q", "J", "Z", "M", "T"]]

instr = [(int(x) for x in l.split() if x.isnumeric()) for l in lines[sep + 1:]]

def move1(n, start, fin):
    for _ in range(n):
        table1[fin - 1].append(table1[start - 1].pop())

def move2(n, start, fin):
    table2[fin - 1].extend(table2[start - 1][-n:])
    table2[start - 1] = table2[start - 1][:-n]
        
for x,y,z in instr:
    move1(x,y,z)
    move2(x,y,z)
    
print("".join([l[-1] for l in table1]))
print("".join([l[-1] for l in table2]))
