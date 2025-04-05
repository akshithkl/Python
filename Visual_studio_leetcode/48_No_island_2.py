def num_islands_bruteforce(grid):
    def is_new_island(i, j):
        # Check if current cell is land and not touching previous lands
        return (
            grid[i][j] == '1' and
            (i == 0 or grid[i - 1][j] == '0') and
            (j == 0 or grid[i][j - 1] == '0')
        )

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if is_new_island(i, j):
                count += 1
    return count

grid = [
    ['1', '1', '0', '0', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '1', '0', '0'],
    ['0', '0', '0', '1', '1']
]


result = num_islands_bruteforce(grid)
print(result)  # Output should be 3
