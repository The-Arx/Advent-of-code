from aocd import data
from itertools import combinations
import math

# data = """7,1
# 11,1
# 11,7
# 9,7
# 9,5
# 2,5
# 2,3
# 7,3"""

dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

tiles = [tuple(map(int, line.split(','))) for line in data.split('\n')]

# print(
#     max((
#         ((abs(t1[0] - t2[0]) + 1)
#         * (abs(t1[1] - t2[1]) + 1), t1, t2)
#         for t1, t2 in combinations(tiles, 2)
#     ))
# )

x_positions = sorted(set(x for x, y in tiles))
x_map = {x: i for i, x in enumerate(x_positions)}
y_positions = sorted(set(y for x, y in tiles))
y_map = {y: i for i, y in enumerate(y_positions)}

grid: list[list[int | None]] = [[None] * len(y_positions) for i in range(len(x_positions))]

def sign(n):
    return 0 if n == 0 else -1 if n < 0 else 1
x_p, y_p = tiles[-1]
prev = x_map[x_p], y_map[y_p]
for x_p, y_p in tiles:
    x = x_map[x_p]
    y = y_map[y_p]
    grid[x][y] = 2
    dx = sign(x - prev[0])
    dy = sign(y - prev[1])
    if dx == 0:
        cx = x
        for cy in range(prev[1] + dy, y, dy):
            grid[cx][cy] = 1
    else:
        assert dy == 0
        cy = y
        for cx in range(prev[0] + dx, x, dx):
            grid[cx][cy] = 1
    prev = x, y

queue = [(100, 50)]
grid[100][50] = 0
i = 0
while i < len(queue):
    x, y = queue[i]
    for dx, dy in dirs:
        if 0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[0]) and grid[x + dx][y + dy] is None:
            grid[x + dx][y + dy] = 0
            queue.append((x + dx, y + dy))
    i += 1


print('\n'.join(''.join({None: '.', 2: '#', 1: 'O', 0: 'o'}[val] for val in row) for row in grid))

empty_tiles_by_row = []
for row in grid:
    curr_row = []
    empty = 0
    curr_row.append(0)
    for val in row:
        if val is None:
            empty += 1
        curr_row.append(empty)
    empty_tiles_by_row.append(curr_row)

empty_tiles = [[] for i in range(len(grid))]
for y in range(len(grid[0])):
    empty = 0
    for x, row in enumerate(grid):
        empty += empty_tiles_by_row[x][y]
        empty_tiles[x].append(empty)
empty_tiles.insert(0, [0] * len(empty_tiles_by_row[0]))

print(empty_tiles)

max_a = 0
for t1, t2 in combinations(tiles, 2):
    x1, x2 = x_map[t1[0]], x_map[t2[0]]
    y1, y2 = y_map[t1[1]], y_map[t2[1]]
    sy = min(y1, y2)
    by = max(y1, y2)
    sx = min(x1, x2)
    bx = max(x1, x2)
    for i in range(sx, bx + 1):
        for j in range(sy, by + 1):
            if grid[i][j] is None:
                break
        else:
            continue
        break
    else:
        area = (abs(t1[0] - t2[0]) + 1) * (abs(t1[1] - t2[1]) + 1)
        max_a = max(max_a, area)
print(max_a)


