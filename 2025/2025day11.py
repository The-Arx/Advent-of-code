from aocd import data
from functools import cache

# data = """aaa: you hhh
# you: bbb ccc
# bbb: ddd eee
# ccc: ddd eee fff
# ddd: ggg
# eee: out
# fff: out
# ggg: out
# hhh: ccc fff iii
# iii: out"""

devices = {}
for line in data.split('\n'):
    name, outputs = line.split(": ")
    devices[name] = outputs.split(' ')

@cache
def ways_to_out(name):
    if name == "out":
        return 1
    ways = 0
    for out in devices[name]:
        ways += ways_to_out(out)
    return ways

print(ways_to_out("you"))

@cache
def part2(name, dac, fft):
    if name == "out":
        return 1 if dac and fft else 0
    if name == "dac":
        dac = True
    if name == "fft":
        fft = True
    ways = 0
    for out in devices[name]:
        ways += part2(out, dac, fft)
    return ways

print(part2('svr', False, False))
