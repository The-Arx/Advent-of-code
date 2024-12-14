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

target_y = 2000000
# target_y = 10
min_x = float('inf')
max_x = float('-inf')
chunks = []
beacons = []
for line in data.split("\n"):
    sx, sy, bx, by = map(int,re.match(r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)", line).groups())
    if by == target_y:
        beacons.append(bx)
    dist = abs(sx - bx) + abs(sy - by)
    y_diff = abs(target_y - sy)
    if y_diff > dist:
        continue
    start = sx - dist + y_diff
    end = sx + dist - y_diff
    chunks.append((start, end))
    min_x = min(min_x, start)
    max_x = max(max_x, end)
    
row = [False] * (max_x - min_x + 1)
for start, end in chunks:
    for x in range(start, end + 1):
        row[x] = True
        
for x in beacons:
    row[x] = False
        
print(sum(1 for val in row if val))
# 4424279 too high

found_x = row.index(False)
assert found_x != -1
if found_x > max_x:
    found_x -= len(row)
print(target_y + found_x * 4000000)