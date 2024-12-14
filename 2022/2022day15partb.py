from aocd import data
import re

# data = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
# Sensor at x=9, y=16: closest beacon is at x=10, y=16
# Sensor at x=13, y=2: closest beacon is at x=15, y=3
# Sensor at x=12, y=14: closest beacon is at x=10, y=16
# Sensor at x=10, y=20: closest beacon is at x=10, y=16
# Sensor at x=14, y=17: closest beacon is at x=10, y=16
# Sensor at x=8, y=7: closest beacon is at x=2, y=10
# Sensor at x=2, y=0: closest beacon is at x=2, y=10
# Sensor at x=0, y=11: closest beacon is at x=2, y=10
# Sensor at x=20, y=14: closest beacon is at x=25, y=17
# Sensor at x=17, y=20: closest beacon is at x=21, y=22
# Sensor at x=16, y=7: closest beacon is at x=15, y=3
# Sensor at x=14, y=3: closest beacon is at x=15, y=3
# Sensor at x=20, y=1: closest beacon is at x=15, y=3"""

regions = []
for line in data.split("\n"):
    sx, sy, bx, by = map(int,re.match(r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)", line).groups())
    dist = abs(sx - bx) + abs(sy - by)
    regions.append((sx, sy, dist))
    
chunks = []
res = None
for row_y in range(0, 4000001):
# for row_y in range(0, 21):
    chunks.clear()
    for x, y, dist in regions:
        y_diff = abs(row_y - y)
        if y_diff > dist:
            continue
        start = x - dist + y_diff
        end = x + dist - y_diff
        chunks.append((start, end))
    chunks.sort()
    if chunks[0][0] > 0:
        print(f"Empty region from x=0 to x={chunks[0][0] - 1} at y={row_y}")
        res = 0, row_y
    max_x = 0
    for start, end in chunks:
        if start > max_x + 1:
            print(f"Empty region from x={max_x + 1} to x={start - 1} at y={row_y}")
            res = max_x + 1, row_y
        max_x = max(max_x, end)
    if max_x < 4000000:
        print(f"Empty region from x={max_x + 1} to x=4000000 at y={row_y}")
        res = 4000000, row_y
    # if max_x < 20:
    #     print(f"Empty region from x={max_x + 1} to x=20 at y={row_y}")
    #     res = 20, row_y
    
print(res[0] * 4000000 + res[1])
    