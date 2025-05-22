def min_path_sum(grid):
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])

    for c in range(1, cols):
        grid[0][c] += grid[0][c - 1]

    for r in range(1, rows):
        grid[r][0] += grid[r - 1][0]

    for r in range(1, rows):
        for c in range(1, cols):
            grid[r][c] += min(grid[r - 1][c], grid[r][c - 1])

    return grid[-1][-1]
