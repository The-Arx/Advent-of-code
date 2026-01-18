from aocd import data

def max_joltage(line, n):
    if len(line) == 0 or n == 0:
        return "", n
    d = max(line)
    n -= 1
    i = line.index(d)
    j1, n = max_joltage(line[i + 1:], n)
    j2, n = max_joltage(line[:i], n)
    return j2 + str(d) + j1, n

j1 = 0
j2 = 0
for line in data.split('\n'):
    line = list(map(int, line))
    j1 += int(max_joltage(line, 2)[0])
    j2 += int(max_joltage(line, 12)[0])




print(j1, j2)