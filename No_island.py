class Solution:
    def numIslands(self, grid):
        if len(grid) == 0:
            return 0
        
        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.mark_island(grid, i, j, len(grid), len(grid[0]))
                    count += 1
        
        return count

    def mark_island(self, grid, i, j, m, n):
        if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] != '1':
            return
        
        grid[i][j] = '2'  # Mark the cell as visited
        # Recursively mark the connected land
        self.mark_island(grid, i, j + 1, m, n)  # right
        self.mark_island(grid, i, j - 1, m, n)  # left
        self.mark_island(grid, i + 1, j, m, n)  # down
        self.mark_island(grid, i - 1, j, m, n)  # up


# Example usage
grid = [
    ['1', '1', '0', '0', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '1', '0', '0'],
    ['0', '0', '0', '1', '1']
]

solution = Solution()
result = solution.numIslands(grid)
print(result)  # Output should be 3
