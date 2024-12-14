from aocd import data
from math import inf

def fill_line(x1, y1, x2, y2):
    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            orig_grid[(x1, y)] = '#'
    elif y1 == y2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            orig_grid[(x, y1)] = '#'
    else:
        assert False


orig_grid = {}

min_y = inf
max_y = -inf
min_x = inf
max_x = -inf
for line in data.split("\n"):
    prev = None
    for point in line.split(" -> "):
        x, y = map(int, point.split(","))
        min_y = min(min_y, y)
        max_y = max(max_y, y)
        min_x = min(min_x, x)
        max_x = max(max_x, x)
        if prev is not None:
            fill_line(*prev, x, y)
        prev = x, y
 
grid = dict(orig_grid)
sand = 0
while y <= max_y:
    x, y = 500, 0
    while y <= max_y:
        if (x, y) not in grid:
            pass
        elif (x - 1, y) not in grid:
            x -= 1
        elif (x + 1, y) not in grid:
            x += 1
        else:
            y -= 1
            grid[(x, y)] = 'o'
            sand += 1
            break
        y += 1
        
print(sand)


grid = dict(orig_grid)
sand = 0
while (500, 0) not in grid:
    x, y = 500, 0
    while True:
        y += 1
        if y == max_y + 2:
            y -= 1
            grid[(x, y)] = 'o'
            sand += 1
            break
        
        if (x, y) not in grid:
            pass
        elif (x - 1, y) not in grid:
            x -= 1
        elif (x + 1, y) not in grid:
            x += 1
        else:
            y -= 1
            grid[(x, y)] = 'o'
            sand += 1
            break
        
print(sand)
            