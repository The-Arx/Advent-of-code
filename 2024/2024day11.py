from aocd import data
from functools import cache

# data = "125 17"

@cache
def stones(val, depth):
    # print(val, depth)
    if depth == 0:
        return 1
    if val == 0:
        return stones(1, depth - 1)
    s = str(val)
    if len(s) % 2 == 0:
        return stones(int(s[:len(s) // 2]), depth - 1) + stones(int(s[len(s) // 2:]), depth - 1)
    return stones(val * 2024, depth - 1)

count = 0
for num in map(int, data.split()):
    count += stones(num, 25)
    
print(count)