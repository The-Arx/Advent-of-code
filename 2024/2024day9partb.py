from aocd import data

# data = "2333133121414131402"

mem = []
is_file = True
files = []
gaps = [[] for _ in range(10)]
for char in data:
    size = int(char)
    if is_file:
        files.append((len(mem), size))
        for i in range(size):
            mem.append(True)
    else:
        if size != 0:
            gaps[size].append(len(mem))
        for i in range(size):
            mem.append(False)
    is_file = not is_file

# debug = [None] * 42
res = 0
for i in range(len(files) - 1, -1, -1):
    start, size = files[i]
    gap_size = None
    loc = float('inf')
    for j in range(size, 10):
        try:
            gap = gaps[j][0]
        except IndexError:
            continue
        if gap < loc:
            loc = gap
            gap_size = j
    if loc > start or gap_size is None:
        for j in range(start, start + size):
            # debug[j] = i
            res += j * i
        continue
    gaps[gap_size].pop(0)
    if gap_size != size:
        gaps[gap_size - size].append(loc + size)
        gaps[gap_size - size].sort()
    for j in range(start, start + size):
        mem[j] = False
    for j in range(loc, loc + size):
        # debug[j] = i
        res += j * i
        mem[j] = True
    
print(res)