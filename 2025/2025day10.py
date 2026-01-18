from aocd import data
from dataclasses import dataclass
import re
from itertools import chain, combinations
from scipy.optimize import milp, LinearConstraint

@dataclass
class Machine:
    lights: set[int]
    buttons: list[set[int]]
    joltage: tuple[int, ...]

    @staticmethod
    def from_line(line):
        lights = set(i for i, char in enumerate(re.search(r"\[([\.#]*)\]", line).groups()[0]) if char == '#')
        buttons = [
            set(map(int, match.groups()[0].split(',')))
            for match in re.finditer(r"\(([\d,]*)\)", line)
        ]
        joltage = tuple(map(int, re.search(r"\{([\d,]*)\}", line).groups()[0].split(',')))
        return Machine(lights, buttons, joltage)
    

machines = [Machine.from_line(line) for line in data.split('\n')]

presses = 0
for machine in machines:
    for buttons in chain(*(combinations(machine.buttons, i) for i in range(len(machine.buttons)))):
        lights: set[int] = set()
        for l in buttons:
            lights ^= l
        if lights == machine.lights:
            presses += len(buttons)
            break
    else:
        assert False, machine

print(presses)

presses = 0
for m in machines:
    res = milp(
        [1] * len(m.buttons),
        integrality=[1] * len(m.buttons),
        constraints=[
            LinearConstraint([
                1 if i in b else 0
                for b in m.buttons
            ], joltage, joltage)
            for i, joltage in enumerate(m.joltage)
        ],
    )
    presses += int(round(res.mip_dual_bound))

print(presses)

