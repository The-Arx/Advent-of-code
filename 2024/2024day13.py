from aocd import data
import re
import numpy as np

# data = """Button A: X+94, Y+34
# Button B: X+22, Y+67
# Prize: X=8400, Y=5400

# Button A: X+26, Y+66
# Button B: X+67, Y+21
# Prize: X=12748, Y=12176

# Button A: X+17, Y+86
# Button B: X+84, Y+37
# Prize: X=7870, Y=6450

# Button A: X+69, Y+23
# Button B: X+27, Y+71
# Prize: X=18641, Y=10279"""


tokens = 0
for machine in data.split("\n\n"):
    x1, y1, x2, y2, x, y = map(int, re.match(r"""Button A: X\+(\d+), Y\+(\d+)
Button B: X\+(\d+), Y\+(\d+)
Prize: X=(\d+), Y=(\d+)""", machine).groups())
    mat = np.array([
        [x1, x2],
        [y1, y2],
    ])
    target = np.array([x, y])
    res = np.linalg.solve(mat, target)
    res = [np.round(v, 10) for v in res]
    # print(res)
    if all(v.is_integer() for v in res):
        # print(res[0] * 3 + res[1])
        tokens += res[0] * 3 + res[1]
    
print(tokens)

tokens = 0
for machine in data.split("\n\n"):
    x1, y1, x2, y2, x, y = map(int, re.match(r"""Button A: X\+(\d+), Y\+(\d+)
Button B: X\+(\d+), Y\+(\d+)
Prize: X=(\d+), Y=(\d+)""", machine).groups())
    mat = np.array([
        [x1, x2],
        [y1, y2],
    ])
    target = np.array([x, y]) + 10000000000000
    res = np.linalg.solve(mat, target)
    res = np.array([np.round(v, 3) for v in res])
    print(res)
    if all(v.is_integer() for v in res):
        assert (mat @ res.astype('int') == target).all()
        print(res[0] * 3 + res[1])
        tokens += res[0] * 3 + res[1]
    
print(tokens)