import re


def num_from_index(s, i):
    result = re.finditer(r'\d+', s)
    for match in result:
        if i in range(match.span()[0], match.span()[1]):
            return match.group()
    return 0


sum = 0
with open("input.txt") as input:
    lines = input.readlines()
    for line_index in range(len(lines)):
        for i in range(len(lines[line_index])):
            symbol = lines[line_index][i]
            if symbol != '.' and symbol != '\n' and not symbol.isdigit():

                # Left
                if lines[line_index][i - 1].isdigit():
                    sum += int(num_from_index(lines[line_index], i - 1))

                # Right
                if lines[line_index][i + 1].isdigit():
                    sum += int(num_from_index(lines[line_index], i + 1))

                # Above
                if line_index > 0:
                    if not lines[line_index - 1][i].isdigit():

                        if lines[line_index - 1][i - 1].isdigit():
                            sum += int(num_from_index(lines[line_index - 1], i - 1))

                        if lines[line_index - 1][i + 1].isdigit():
                            sum += int(num_from_index(lines[line_index - 1], i + 1))

                    else:
                        sum += int(num_from_index(lines[line_index - 1], i))

                # Below
                if line_index < len(lines)-1:

                    if not lines[line_index + 1][i].isdigit():

                        if lines[line_index + 1][i - 1].isdigit():
                            sum += int(num_from_index(lines[line_index + 1], i - 1))

                        if lines[line_index + 1][i + 1].isdigit():
                            sum += int(num_from_index(lines[line_index + 1], i + 1))

                    else:
                        sum += int(num_from_index(lines[line_index + 1], i))
print(sum)
