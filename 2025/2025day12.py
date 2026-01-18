from aocd import data
import re

shapes_txt, regions_txt = data.rsplit('\n\n', 1)

shapes = [
    tuple(
        tuple(
            char == "#"
            for char in line
        )
        for line in shape.split('\n')[1:]
    )
    for shape in shapes_txt.split('\n\n')
]

def rotate(shape, n):
    while n > 0:
        shape = tuple(
            tuple(
                shape[2 - j][i]
                for j in range(3)
            )
            for i in range(3)
        )
        n -= 1
    return shape

def flip(shape, flip):
    return tuple(reversed(shape)) if flip else shape

shape_rots = [
    { rotate(flip(shape, f), n) for n in range(4) for f in range(2) }
    for shape in shapes
]

def shape_to_str(shape):
    return '\n'.join(''.join('#' if val else '.' for val in row) for row in shape)


total = 0
for line in regions_txt.split('\n'):
    match = re.match(r"^(\d+)x(\d+): ((?:\d+ )*\d+)$", line)
    assert match is not None, line
    w, h, count = match.groups()
    w = int(w)
    h = int(h)
    count = list(map(int, count.split(' ')))

    c = 0
    for i, shape in enumerate(shapes):
        c += count[i] * sum(sum(row) for row in shape)

    if c > w * h:
        continue

    if (w // 3) * (h // 3) >= sum(count):
        total += 1
        continue
    
    print(w * h, c, (w // 3) * (h // 3), sum(count))

print(total)


print('\n\n\n'.join('\n\n'.join(map(shape_to_str, shape)) for shape in shape_rots))

