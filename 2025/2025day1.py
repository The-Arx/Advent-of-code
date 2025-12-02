from aocd import data

num = 50
part1 = 0
part2 = 0
for line in data.split('\n'):
    d = -1 if line[0] == 'L' else 1
    n = int(line[1:])

    if num == 0 and d == -1:
        part2 -= 1
    
    num += n * d
    part2 += abs(num // 100)
    num %= 100

    if num == 0 and d == -1:
        part2 += 1
        
    if num == 0:
        part1 += 1
    

print(part1, part2)
