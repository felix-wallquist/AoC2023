nodes = []
with open("input.txt") as input:
    lines = input.readlines()
    instructions = lines[0].strip()
    for i in range(2, len(lines)):
        node = lines[i].strip().split(" ")[0]
        left = lines[i].strip().split("(")[1].split(",")[0]
        right = lines[i].strip().split(", ")[1][:-1]
        nodes.append([node, left, right])

steps = 0
current = 'AAA'
while current != 'ZZZ':
    for instruction in instructions:
        for j in range(len(nodes)):
            if nodes[j][0] == current:
                if instruction == 'L':
                    steps += 1
                    current = nodes[j][1]
                    break
                else:
                    steps += 1
                    current = nodes[j][2]
                    break
print(steps)
