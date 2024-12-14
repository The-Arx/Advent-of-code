from aocd import data

# data = """190: 10 19
# 3267: 81 40 27
# 83: 17 5
# 156: 15 6
# 7290: 6 8 6 15
# 161011: 16 10 13
# 192: 17 8 14
# 21037: 9 7 18 13
# 292: 11 6 16 20"""

def test(goal, nums, i, val):
    if i >= len(nums):
        return val == goal
    if val * nums[i] <= goal:
        if test(goal, nums, i + 1, val * nums[i]):
            return True
    
    if val + nums[i] <= goal:
        if test(goal, nums, i + 1, val + nums[i]):
            return True
    
    concat = int(str(val) + str(nums[i]))
    if concat <= goal:
        return test(goal, nums, i + 1, concat)
    return False


count = 0
for i, line in data.split("\n"):
    goal, nums = line.split(": ")
    goal = int(goal)
    nums = list(map(int, nums.split()))
    if test(goal, nums, 1, nums[0]):
        count += goal
        
print(count)
    
