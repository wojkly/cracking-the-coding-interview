def is_field_crossable(i, j, grid):
    return grid[i][j] != 'X'

def is_field_reachable(i, j, parents):
    return parents[i][j] is not None

def print_t(table):
    for row in table:
        print(row)

def get_path(parents):
    position = (len(parents) - 1, len(parents[0]) - 1)

    path = [position]

    while position != (0,0):
        position = parents[position[0]][position[1]]
        path.append(position)

    path.reverse()
    return path

def robot(grid: list[list[str]]):
    parents = [[None for j in range(len(grid[0]))] for i in range(len(grid))]

    parents[0][0] = (0,0)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if not is_field_crossable(i,j,grid):
                continue
            if not is_field_reachable(i,j,parents):
                continue

            if i + 1 < len(grid) and is_field_crossable(i + 1, j, grid):
                parents[i + 1][j] = (i, j)
            if j + 1 < len(grid[0]) and is_field_crossable(i,j + 1,grid):
                parents[i][j + 1] = (i,j)

    print_t(parents)

    path = get_path(parents)

    print(path)

grid1 = [
[  ' ', ' ', ' ', ' ', 'X', ' '],
[  ' ', ' ', 'X', ' ', 'X', ' '],
[  ' ', ' ', 'X', ' ', 'X', ' '],
[  ' ', ' ', 'X', ' ', ' ', ' '],
[  ' ', ' ', 'X', 'X', 'X', ' '],
[  ' ', ' ', ' ', ' ', 'X', ' ']
]

robot(grid1)
