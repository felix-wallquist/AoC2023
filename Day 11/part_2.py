def transpose_grid(l):
    lt = []
    for i in range(len(l[0])):
        row = ""
        for item in l:
            row += item[i]
        lt.append(row)
    return lt


def expanded(grid):
    exp = []
    for r, row in enumerate(grid):
        if len(set(list(row))) == 1 and row[0] == '.':
            exp.append(r)
    return exp


def find_galaxies(grid):
    pos = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '#':
                pos.append((i, j))
    return pos


def shortest_path(fr, to, exp_rows, exp_cols):
    x = abs(to[1] - fr[1])
    y = abs(to[0] - fr[0])
    for exp_row in exp_rows:
        if exp_row in range(fr[0], to[0]):
            x += 999999
    for exp_col in exp_cols:
        if exp_col in range(min(fr[1], to[1]), max(fr[1], to[1])):
            y += 999999
    return x + y


def sum_shortest_paths(gals):
    exp_rows = expanded(grid)
    exp_cols = expanded(transpose_grid(grid))
    sum = 0
    for i in range(len(gals) - 1):
        for j in range(i+1, len(gals)):
            sum += shortest_path(gals[i], gals[j], exp_rows, exp_cols)
    return sum


grid = []
with open("input.txt") as file:
    for line in file:
        grid.append(line.strip())

galaxies = find_galaxies(grid)
print(sum_shortest_paths(galaxies))
