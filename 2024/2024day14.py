from aocd import data
import re


width = 101
height = 103
quadrants = [[0, 0], [0, 0]]
for line in data.split("\n"):
    x0, y0, vx, vy = map(int, re.match(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", line).groups())
    x = (x0 + 100 * vx) % width
    y = (y0 + 100 * vy) % height
    if x == width // 2 and width % 2 == 1 or y == height // 2 and height % 2 == 1:
        continue
    quadrants[x < width // 2][y < height // 2] += 1
    
print(quadrants[0][0] * quadrants[0][1] * quadrants[1][0] * quadrants[1][1])
    