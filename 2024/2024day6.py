from aocd import data

# data = """....#.....
# .........#
# ..........
# ..#.......
# .......#..
# ..........
# .#..^.....
# ........#.
# #.........
# ......#..."""

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
            gx, gy = x, y
            row.append("visited")
        else:
            row.append(None)
    grid.append(row)

d = 0
visited = 1          
while True:
    dx, dy = DIRS[d]
    nx, ny = gx + dx, gy + dy
    if not (0 <= nx < len(grid) and 0 <= ny < len(grid[0])):
        break
    if grid[nx][ny] == "wall":
        d = (d + 1) % 4
        continue
    if grid[nx][ny] is None:
        grid[nx][ny] = "visited"
        visited += 1
    gx, gy = nx, ny
print(visited)