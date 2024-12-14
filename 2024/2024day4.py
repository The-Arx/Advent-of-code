from aocd import data

lines = data.split("\n")
width = len(lines)
height = len(lines[0])

moves = [
    (0, 0),
    (1, 0),
    (-1, 0),
    (0, 1),
    (1, 1),
    (-1, 1),
    (0, -1),
    (1, -1),
    (-1, -1),
]

goal = 'XMAS'
count = 0
for x in range(width):
    for y in range(height):
        for dx, dy in moves:
            text = ""
            nx, ny = x, y
            for _ in range(len(goal)):
                if not (0 <= nx < width and 0 <= ny < height):
                    break
                text += lines[nx][ny]
                nx += dx
                ny += dy
            # print(text)
            if text == goal:
                count += 1
print(count)

def test(s):
    return s == "MAS" or s == "SAM"
count = 0
for x in range(1, width - 1):
    for y in range(1, height - 1):
        m1 = m2 = ""
        for i in range(-1, 2):
            m1 += lines[x - i][y - i]
            m2 += lines[x + i][y - i]
        if test(m1) and test(m2):
            count += 1
print(count)