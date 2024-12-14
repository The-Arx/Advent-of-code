from aocd import data

def get_directions():
    while True:
        for char in data:
            if char == "<":
                yield -1
            else:
                yield 1
                
dirs = get_directions()

blocks = [
    [
        [1],
        [1],
        [1],
        [1],
    ],
    [
        [0, 1, 0],
        [1, 1, 1],
        [0, 1, 0],
    ],
    
]