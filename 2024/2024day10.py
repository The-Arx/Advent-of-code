from aocd import data


DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
grid = []
for line in data.split("\n"):
    grid.append(list(map(int, line)))

width = len(grid)
height = len(grid[0])
scores = [[1 if val == 9 else 0 for j, val in enumerate(row)] for i, row in enumerate(grid)]
    
def check_grid(n):
    for x, row in enumerate(grid):
        for y, val in enumerate(row):
            if val != n:
                continue
            s = scores[x][y]
            for dx, dy in DIRS:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < width and 0 <= ny < height and grid[nx][ny] == n - 1:
                    scores[nx][ny] += s

for i in range(9, 0, -1):
    check_grid(i)
    
total = 0
for x, row in enumerate(grid):
    for y, val in enumerate(row):
        if val == 0:
            total += scores[x][y]
print(total)