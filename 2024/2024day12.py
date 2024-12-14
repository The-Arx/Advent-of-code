from aocd import data

dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]

# data = """AAAA
# BBCD
# BBCC
# EEEC"""

# data = """RRRRIICCFF
# RRRRIICCCF
# VVRRRCCFFF
# VVRCCCJFFF
# VVVVCJJCFE
# VVIVCCJJEE
# VVIIICJJEE
# MIIIIIJJEE
# MIIISIJEEE
# MMMISSJEEE"""

grid = data.split("\n")
width = len(grid)
height = len(grid[0])

def get(x, y):
    if 0 <= x < width and 0 <= y < height:
        return grid[x][y]
    return None

seen = set()
def check(x, y):
    letter = grid[x][y]
    print(x, y, letter)
    positions = [(x, y)]
    seen.add((x, y))
    region = {(x, y)}
    perim = 0
    for pos in positions:
        for dx, dy in dirs:
            cx = pos[0] + dx
            cy = pos[1] + dy
            check = cx, cy
            if check in region:
                continue
            if get(cx, cy) == letter:
                positions.append(check)
                seen.add(check)
                region.add(check)
            else:
                perim += 1
    print(len(positions), perim)
    return len(positions) * perim

# def find_perimiter(start_x, start_y):
#     letter = grid[start_x][start_y]
#     perim = 0
#     d = 1
#     x = start_x
#     y = start_y
#     while True:
#         # print(x, y, d)
#         for i in range(0, 4):
#             test_d = (d + i - 1) % 4
#             dx, dy = dirs[test_d]
#             cx = x + dx
#             cy = y + dy
#             if get(cx, cy) == letter:
#                 perim += i
#                 x = cx
#                 y = cy
#                 d = test_d
#                 break
#         else:
#             if x == start_x and y == start_y:
#                 return 4
#             assert False
#         if x == start_x and y == start_y: # and d == 1:
#             return perim + (1 - d) % 4

count = 0
for y in range(height):
    for x in range(width):
        if (x, y) not in seen:
            count += check(x, y)# * find_perimiter(x, y)
            
print(count)
        