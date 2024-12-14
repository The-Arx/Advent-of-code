from aocd import data
from collections import defaultdict
from fractions import Fraction

# data = """............
# ........0...
# .....0......
# .......0....
# ....0.......
# ......A.....
# ............
# ............
# ........A...
# .........A..
# ............
# ............"""

antennas = defaultdict(list)
lines = data.split("\n")
width = len(lines)
height = len(lines[0])
for x, line in enumerate(lines):
    for y, char in enumerate(line):
        if char != ".":
            antennas[char].append((x, y))
            
antinodes = set()

for positions in antennas.values():
    for i, pos1 in enumerate(positions):
        x1, y1 = pos1
        for j, pos2 in enumerate(positions):
            if i == j:
                continue
            x2, y2 = pos2
            dx, dy = x1 - x2, y1 - y2
            ax, ay = x1 + dx, y1 + dy
            if 0 <= ax < width and 0 <= ay < height:
                antinodes.add((ax, ay))
                
print(len(antinodes))

antinodes = set()

for positions in antennas.values():
    for i, pos1 in enumerate(positions):
        x1, y1 = pos1
        for j in range(i + 1, len(positions)):
            x2, y2 = positions[j]
            dx, dy = x1 - x2, y1 - y2
            slope = Fraction(dx, dy)
            ax, ay = x1, y1
            while 0 <= ax < width and 0 <= ay < height:
                antinodes.add((ax, ay))
                ax += slope.numerator
                ay += slope.denominator
            ax, ay = x1, y1
            while 0 <= ax < width and 0 <= ay < height:
                antinodes.add((ax, ay))
                ax -= slope.numerator
                ay -= slope.denominator
                
print(len(antinodes))
            
            