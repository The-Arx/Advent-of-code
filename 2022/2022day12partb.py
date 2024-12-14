from aocd import data
from collections import deque

grid = []
for x, line in enumerate(data.split("\n")):
    row = []
    for y, char in enumerate(line):
        if char == "E":
            end = (x, y)
            char = 'z'
        elif char == "S":
            char = 'a'
        row.append(ord(char) - ord('a'))
    grid.append(row)
    
width = len(grid)
height = len(grid[0])
    
dist = [[None] * height for _ in range(width)]
dist[end[0]][end[1]] = 0
queue = deque()
queue.append(end)

moves = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
]

while queue:
    x, y = queue.popleft()
    val = grid[x][y]
    d = dist[x][y]
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < width and 0 <= ny < height and dist[nx][ny] is None and grid[nx][ny] + 1 >= val:
            dist[nx][ny] = d + 1
            queue.append((nx, ny))
            if grid[nx][ny] == 0:
                print(d + 1)
            
            


            
        
    
    