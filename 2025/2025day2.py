from aocd import data

part_1 = 0
part_2 = 0
for r in data.split(','):
    start, end = map(int, r.split('-'))
    for n in range(start, end + 1):
        s = str(n)
        if s[:len(s)//2] == s[len(s)//2:]:
            part_1 += n
        for i in range(1, len(s) // 2 + 1):
            if s == s[:i] * (len(s) // i):
                part_2 += n
                break
print(part_1, part_2)