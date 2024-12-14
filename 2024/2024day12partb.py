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
ids = [[None] * height for _ in range(width)]

def get(x, y):
    if 0 <= x < width and 0 <= y < height:
        return grid[x][y]
    return None

areas = []
next_id = 0
def check(x, y):
    global next_id
    aid = next_id
    next_id += 1
    letter = grid[x][y]
    print(x, y, letter, aid)
    ids[x][y] = aid
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
                ids[cx][cy] = aid
                positions.append(check)
                seen.add(check)
                region.add(check)
            else:
                perim += 1
    print(len(positions), perim)
    areas.append(len(positions))
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
seen = set()
for y in range(height):
    for x in range(width):
        if (x, y) not in seen:
            check(x, y)# * find_perimiter(x, y)
        

sides = [0] * len(areas)
for x in range(-1, width):
    left = None
    right = None
    for y in range(height):
        if 0 <= x:
            id1 = ids[x][y]
        else:
            id1 = None
        if x + 1 < width:
            id2 = ids[x + 1][y]
        else:
            id2 = None
        if id1 == id2:
            if left is not None:
                sides[left] += 1
            if right is not None:
                sides[right] += 1
            left = None
            right = None
        else:
            if id1 != left:
                if left is not None:
                    sides[left] += 1
                left = id1
            if id2 != right:
                if right is not None:
                    sides[right] += 1
                right = id2
    if left is not None:
        sides[left] += 1
    if right is not None:
        sides[right] += 1


for y in range(-1, height):
    left = None
    right = None
    for x in range(width):
        if 0 <= y:
            id1 = ids[x][y]
        else:
            id1 = None
        if y + 1 < height:
            id2 = ids[x][y + 1]
        else:
            id2 = None
        if id1 == id2:
            if left is not None:
                sides[left] += 1
            if right is not None:
                sides[right] += 1
            left = None
            right = None
        else:
            if id1 != left:
                if left is not None:
                    sides[left] += 1
                left = id1
            if id2 != right:
                if right is not None:
                    sides[right] += 1
                right = id2
    if left is not None:
        sides[left] += 1
    if right is not None:
        sides[right] += 1

count = 0
for a, s in zip(areas, sides):
    count += a * s
print(count)