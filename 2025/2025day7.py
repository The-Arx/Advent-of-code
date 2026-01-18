from aocd import data
from collections import Counter

data = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
..............."""

splitters = set()
for i, line in enumerate(data.split("\n")):
    for j, char in enumerate(line):
        if char == "S":
            start = (j, i)
        elif char == "^":
            splitters.add((j, i))

y = start[1] + 1
beams = Counter([start[0]])
hit = 0
while y < data.count('\n'):
    new_beams = Counter()
    for x, n in beams.items():
        if (x, y) in splitters:
            new_beams[x - 1] += n
            new_beams[x + 1] += n
            hit += 1
        else:
            new_beams[x] += n
    beams = new_beams
    print("".join("/\\" if (x, y) in splitters else f"{beams[x]:>2d}" if x in beams else "  " for x in range(data.index('\n'))))
    y += 1
print(hit, sum(beams.values()))