from aocd import data
from json import loads
from functools import cmp_to_key

def compare(left, right):
    if isinstance(left, int) and isinstance(right, list):
        left = [left]
    elif isinstance(right, int) and isinstance(left, list):
        right = [right]
    if isinstance(left, int):
        if left > right:
            return 1
        if right > left:
            return -1
        return 0
    for l, r in zip(left, right):
        res = compare(l, r)
        if res:
            return res
    return compare(len(left), len(right))

# data = """[1,1,3,1,1]
# [1,1,5,1,1]

# [[1],[2,3,4]]
# [[1],4]

# [9]
# [[8,7,6]]

# [[4,4],4,4]
# [[4,4],4,4,4]

# [7,7,7,7]
# [7,7,7]

# []
# [3]

# [[[]]]
# [[]]

# [1,[2,[3,[4,[5,6,7]]]],8,9]
# [1,[2,[3,[4,[5,6,0]]]],8,9]"""

data_list = list(map(loads, data.replace("\n\n", "\n").split("\n")))

dividers = [
    [[2]],
    [[6]],
]

for d in dividers:
    data_list.append(d)
    
data_list.sort(key=cmp_to_key(compare))

res = 1
for d in dividers:
    res *= data_list.index(d) + 1
        
print(res)