from aocd import data
from collections import defaultdict

# lines = data.split("\n")
# nums = list(map(int, lines[0].split()))
# mul = [op == '*' for op in lines[-1].split()]

# for line in lines[1:-1]:
#     for i, n in enumerate(map(int, line.split())):
#         if mul[i]:
#             nums[i] *= n
#         else:
#             nums[i] += n

# print(sum(nums))

# data = """123 328  51 64 
#  45 64  387 23 
#   6 98  215 314
# *   +   *   +  """

lines = data.split("\n")
mul = [op == '*' for op in lines[-1].split()]
nums = [defaultdict(str) for op in mul]

for line in lines[0:-1]:
    space = True
    i = 0
    for j, char in enumerate(line):
        if char == " ":
            if not space:
                space = True
                i += 1
            continue
        space = False
        nums[i][j] += char
    assert i - space == len(mul) - 1

total = 0
for i, op in enumerate(mul):
    print(nums[i])
    num = 1 if op else 0
    for n in map(int, nums[i].values()):
        num = num * n if op else num + n
    print(op, num)
    total += num

print(total)