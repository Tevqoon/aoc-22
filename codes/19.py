import re
from frozendict import frozendict

def tonum(finds):
    if finds == []:
        return 0
    else:
        return int(finds[0].split(" ")[0])

def get_ingrs(line):
    return frozendict({ingr : tonum(re.findall(r"\d+ " + ingr, line)) for ingr in [r"ore", r"clay", r"obsidian"]})

def process(line):
    lst = line.split("Each")
    ore = get_ingrs(lst[1])
    clay = get_ingrs(lst[2])
    obsidian = get_ingrs(lst[3])
    geode = get_ingrs(lst[4])
    return {"ore" : ore, "clay" : clay, "obsidian" : obsidian, "geode" : geode}

with open("../inputs/19.txt") as f:
    lines = [process(line.rstrip()) for line in f]

sample = [process(line) for line in [
          "Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.",
          "Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian."
          ]]

blueprints = sample

def test(a, b):
    return 1 if a == b else 0

def simulate(blueprint, time,
             ore=0, clay=0, obsidian=0, geode=0,
             dore=1, dclay=0, dobsidian=0, dgeode=0):
    if time <= 0:
        return geode
    m = geode
    for build in ["ore", "clay", "obsidian", "geode"]:
        if 0 < blueprint[build]["ore"] > ore:
            continue
        elif 0 < blueprint[build]["clay"] > clay:
            continue
        elif 0 < blueprint[build]["obsidian"] > obsidian:
            continue
        else:
            m = max(m, simulate(blueprint, time - 1,
                                ore + dore, clay + dclay, obsidian + dobsidian, geode + dgeode,
                                dore + test(build, "ore"),
                                dclay + test(build, "clay"),
                                dobsidian + test(build, "obsidian"),
                                dgeode + test(build, "geode")
                                ))
    m = max(m, simulate(blueprint, time - 1,
                        ore + dore, clay + dclay, obsidian + dobsidian, geode + dgeode,
                        dore, dclay, dobsidian, dgeode))
    return m

simulate(blueprints[0], time=24)
