from aocd import data

mem = []
is_file = True
file_id = 0
files = 0
for char in data:
    size = int(char)
    if is_file:
        files += size
        for i in range(size):
            mem.append(file_id)
        file_id += 1
    else:
        for i in range(size):
            mem.append(None)
    is_file = not is_file

prev_empty = -1
while len(mem) > files:
    val = mem.pop()
    if val is None:
        continue
    i = mem.index(None, prev_empty + 1)
    mem[i] = val
    prev_empty = i
        
    
res = 0
for i, val in enumerate(mem):
    res += i * val
print(res)