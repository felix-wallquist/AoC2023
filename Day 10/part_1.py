adj_map = {
    'r': ['-', 'J', '7'],
    'l': ['-', 'F', 'L'],
    'u': ['|', 'F', '7'],
    'd': ['|', 'J', 'L']
}


def find_s(grid):
    for r, row in enumerate(grid):
        if 'S' in row:
            return r, grid[r].index('S')


def find_s_symbol(grid, path):
    path1 = path[0]
    path2 = path[1]

    if grid[path1[0]][path1[1]] in adj_map['r']:
        if grid[path2[0]][path2[1]] in adj_map['d']:
            return 'F'
        if grid[path2[0]][path2[1]] in adj_map['l']:
            return '-'
        if grid[path2[0]][path2[1]] in adj_map['u']:
            return 'L'

    if grid[path1[0]][path1[1]] in adj_map['l']:
        if grid[path2[0]][path2[1]] in adj_map['d']:
            return '7'
        if grid[path2[0]][path2[1]] in adj_map['r']:
            return '-'
        if grid[path2[0]][path2[1]] in adj_map['u']:
            return 'J'

    if grid[path1[0]][path1[1]] in adj_map['u']:
        if grid[path2[0]][path2[1]] in adj_map['d']:
            return '|'
        if grid[path2[0]][path2[1]] in adj_map['l']:
            return 'J'
        if grid[path2[0]][path2[1]] in adj_map['r']:
            return 'L'

    if grid[path1[0]][path1[1]] in adj_map['d']:
        if grid[path2[0]][path2[1]] in adj_map['u']:
            return '|'
        if grid[path2[0]][path2[1]] in adj_map['l']:
            return '7'
        if grid[path2[0]][path2[1]] in adj_map['r']:
            return 'F'


def find_s_adj(grid, point):
    adj = []
    if point[1] < len(grid[0]) - 1 and grid[point[0]][point[1] + 1] in adj_map['r']:
        adj.append((point[0], point[1] + 1))

    if point[1] > 0 and grid[point[0]][point[1] - 1] in adj_map['l']:
        adj.append((point[0], point[1] - 1))

    if point[0] < len(grid) - 1 and grid[point[0] + 1][point[1]] in adj_map['d']:
        adj.append((point[0] + 1, point[1]))

    if point[0] > 0 and grid[point[0] - 1][point[1]] in adj_map['u']:
        adj.append((point[0] - 1, point[1]))

    return adj


def find_adj(grid, point, prev):
    current = grid[point[0]][point[1]]
    previous = grid[prev[0]][prev[1]]
    if current == 'L':
        # north
        if prev[1] > point[1]:
            return point[0] - 1, point[1]
        # east
        else:
            return point[0], point[1] + 1
    if current == '|':
        # south
        if prev[0] < point[0]:
            return point[0] + 1, point[1]
        # north
        else:
            return point[0] - 1, point[1]
    if current == '-':
        # east
        if prev[1] < point[1]:
            return point[0], point[1] + 1
        # west
        else:
            return point[0], point[1] - 1
    if current == 'F':
        # east
        if prev[0] > point[0]:
            return point[0], point[1] + 1
        # south
        else:
            return point[0] + 1, point[1]
    if current == '7':
        # south
        if prev[1] < point[1]:
            return point[0] + 1, point[1]
        # west
        else:
            return point[0], point[1] - 1
    if current == 'J':
        # north
        if prev[1] < point[1]:
            return point[0] - 1, point[1]
        # west
        else:
            return point[0], point[1] - 1


def find_loop(grid, p):
    path1 = find_s_adj(grid, p)[0]
    prev1 = p
    start = p
    loop = [start]

    while path1 != start:
        loop.append(path1)
        temp1 = find_adj(grid, path1, prev1)
        prev1 = path1
        path1 = temp1
    return loop


grid = []
with open("input.txt") as file:
    for line in file:
        grid.append(line.strip())


s = find_s(grid)
loop = find_loop(grid, s)
print(int(((len(loop)+1)/2)))
