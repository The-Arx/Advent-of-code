from aocd import data
import re

t = 0
for res in re.finditer(r"mul\((\d+),(\d+)\)", data):
    t += int(res[1]) * int(res[2])
print(t)

while True:
    try:
        start = data.index("don't()")
    except ValueError:
        break
    try:
        end = data.index('do()', start + 7)
    except ValueError:
        data = data[:start]
        break
    data = data[:start] + data[end:]
    
t = 0
for res in re.finditer(r"mul\((\d+),(\d+)\)", data):
    t += int(res[1]) * int(res[2])
print(t)