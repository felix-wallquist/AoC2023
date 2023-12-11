def transpose_grid(l):
    lt = []
    for i in range(len(l[0])):
        row = ""
        for item in l:
            row += item[i]
        lt.append(row)
    return lt


def expand_rows(grid):
    expanded = []
    for row in grid:
        if len(set(list(row))) == 1 and row[0] == '.':
            expanded.append(row)
        expanded.append(row)
    return expanded


def expand_grid(grid):
    grid = expand_rows(grid)
    grid = transpose_grid(grid)
    grid = expand_rows(grid)
    return transpose_grid(grid)


def find_galaxies(grid):
    pos = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '#':
                pos.append((i, j))
    return pos


def shortest_path(fr, to):
    return abs(to[0] - fr[0]) + abs(to[1] - fr[1])


def sum_shortest_paths(gals):
    sum = 0
    for i in range(len(gals) - 1):
        for j in range(i+1, len(gals)):
            sum += shortest_path(gals[i], gals[j])
    return sum


grid = []
with open("input.txt") as file:
    for line in file:
        grid.append(line.strip())

grid = expand_grid(grid)
galaxies = find_galaxies(grid)
print(sum_shortest_paths(galaxies))
