from aocd import data

data = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

DIRS = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1),
]

grid = []
for x, line in enumerate(data.split("\n")):
    row = []
    for y, char in enumerate(line):
        if char == "#":
            row.append("wall")
        elif char == "^":
            start_x, start_y = x, y
            row.append("visited")
        else:
            row.append(None)
    grid.append(row)

def test():
    gx, gy = start_x, start_y
    d = 0       
    visited = set()
    while True:
        curr = (gx, gy, d)
        if curr in visited:
            return True
        visited.add(curr)
        dx, dy = DIRS[d]
        nx, ny = gx + dx, gy + dy
        if not (0 <= nx < len(grid) and 0 <= ny < len(grid[0])):
            return False
        if grid[nx][ny] == "wall":
            d = (d + 1) % 4
            continue
        gx, gy = nx, ny

count = 0
for x, row in enumerate(grid):
    for y, val in enumerate(row):
        if val is None:
            grid[x][y] = "wall"
            if test():
                count += 1
            grid[x][y] = None
print(count)
            