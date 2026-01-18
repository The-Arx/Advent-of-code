from aocd import data

grid = [[char == '@' for char in line] for line in data.split('\n')]
w = len(grid)
h = len(grid[0])

dirs = [(x, y) for x in range(-1, 2) for y in range(-1, 2) if x or y]

def get_val(x, y):
    if x < 0 or y < 0 or x >= w or y >= h:
        return False
    return grid[x][y]

part1 = 0
for x, row in enumerate(grid):
    for y, val in enumerate(row):
        if not val:
            continue
        touching = 0
        for dx, dy in dirs:
            if get_val(x + dx, y + dy):
                touching += 1
        if touching < 4:
            part1 += 1
print(part1)

part2 = 0
changed = None
while changed != 0:
    changed = 0
    new_grid = [[False] * h for _ in range(w)]
    for x, row in enumerate(grid):
        for y, val in enumerate(row):
            if not val:
                continue
            touching = 0
            for dx, dy in dirs:
                if get_val(x + dx, y + dy):
                    touching += 1
            if touching < 4:
                changed += 1
            else:
                new_grid[x][y] = True
    grid = new_grid
    part2 += changed
print(part2)


