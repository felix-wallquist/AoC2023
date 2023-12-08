import numpy as np

nodes = []
with open("input.txt") as input:
    lines = input.readlines()
    instructions = lines[0].strip()
    for i in range(2, len(lines)):
        node = lines[i].strip().split(" ")[0]
        left = lines[i].strip().split("(")[1].split(",")[0]
        right = lines[i].strip().split(", ")[1][:-1]
        nodes.append([node, left, right])

current = []
for node in nodes:
    if node[0][-1] == 'A':
        current.append(node[0])

steps_taken = []
for c in range(len(current)):
    steps = 0
    at_end = False
    while not at_end:
        for instruction in instructions:
            if at_end:
                break
            for i in range(len(nodes)):
                if nodes[i][0] == current[c]:
                    current[c] = nodes[i][1] if instruction == 'L' else nodes[i][2]
                    steps += 1
                    if current[c][-1] == 'Z':
                        at_end = True
                        steps_taken.append(steps)
                    break

lcm = np.lcm.reduce(steps_taken)
print(lcm)
