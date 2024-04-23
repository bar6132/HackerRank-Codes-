def numCells(grid):
    n, m = len(grid), len(grid[0])
    count = 0

    for i in range(n):
        for j in range(m):
            if isDominant(grid, i, j, n, m):
                count += 1

    return count

def isDominant(grid, i, j, n, m):
    if i > 0 and grid[i-1][j] >= grid[i][j]:
        return False
    if i < n-1 and grid[i+1][j] >= grid[i][j]:
        return False
    if j > 0 and grid[i][j-1] >= grid[i][j]:
        return False
    if j < m-1 and grid[i][j+1] >= grid[i][j]:
        return False
    if i > 0 and j > 0 and grid[i-1][j-1] >= grid[i][j]:
        return False
    if i > 0 and j < m-1 and grid[i-1][j+1] >= grid[i][j]:
        return False
    if i < n-1 and j > 0 and grid[i+1][j-1] >= grid[i][j]:
        return False
    if i < n-1 and j < m-1 and grid[i+1][j+1] >= grid[i][j]:
        return False
    return True