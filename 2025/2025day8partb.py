from aocd import data

# data = """162,817,812
# 57,618,57
# 906,360,560
# 592,479,940
# 352,342,300
# 466,668,158
# 542,29,236
# 431,825,988
# 739,650,466
# 52,470,668
# 216,146,977
# 819,987,18
# 117,168,530
# 805,96,715
# 346,949,466
# 970,615,88
# 941,993,340
# 862,61,35
# 984,92,344
# 425,690,689"""

boxes = [tuple(map(int, line.split(','))) for line in data.split("\n")]


def dist(b1, b2):
    return (b1[0] - b2[0]) ** 2 + (b1[1] - b2[1]) ** 2 + (b1[2] - b2[2]) ** 2

pairs = [(b1, boxes[j]) for i, b1 in enumerate(boxes) for j in range(0, i)]

pairs.sort(key=lambda p: dist(p[0], p[1]))

connections = { b: set([b]) for b in boxes }
circuits = { id(c) for c in connections.values() }

for b1, b2 in pairs:
    c1 = connections[b1]
    c2 = connections[b2]
    if c1 is c2:
        continue
    c1.update(c2)
    for box in c2:
        connections[box] = c1
    circuits.remove(id(c2))
    if len(circuits) == 1:
        print(b1[0] * b2[0])
        break





