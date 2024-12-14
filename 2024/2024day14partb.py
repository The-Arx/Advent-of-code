from aocd import data
import re
from time import sleep

width = 101
height = 103
robots = []
for line in data.split("\n"):
    x0, y0, vx, vy = map(int, re.match(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", line).groups())
    robots.append((x0, y0, vx, vy))
    
def print_frame(n):
    grid = [[0] * width for _ in range(height)]
    for x0, y0, vx, vy in robots:
        x = (x0 + n * vx) % width
        y = (y0 + n * vy) % height
    
        grid[y][x] += 1
    
    # return grid
    print(f"{n}\n" + "\n".join("".join("##" if val else "  " for val in row) for row in grid)+"\n", end="")
    
for i in range(66, width * height, width):
    # print(i)
    print_frame(i)
    sleep(.1)
    