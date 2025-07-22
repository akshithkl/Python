class Solution(object):
    def shortestBridge(self, grid):
        n = len(grid)
        island1 = []
        island2 = []

        visited = [[False for _ in range(n)] for _ in range(n)]

        def dfs(x, y, island):
            if x < 0 or x >= n or y < 0 or y >= n:
                return
            if visited[x][y] or grid[x][y] == 0:
                return
            visited[x][y] = True
            island.append((x, y))
            dfs(x + 1, y, island)
            dfs(x - 1, y, island)
            dfs(x, y + 1, island)
            dfs(x, y - 1, island)

        # Step 1: Find both islands and store their coordinates
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    island = []
                    dfs(i, j, island)
                    if not island1:
                        island1 = island
                    else:
                        island2 = island

        # Step 2: Brute force check all pairs from both islands
        min_dist = float('inf')
        for x1, y1 in island1:
            for x2, y2 in island2:
                dist = abs(x1 - x2) + abs(y1 - y2) - 1
                min_dist = min(min_dist, dist)

        return min_dist

# Example usage
grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
print(Solution().shortestBridge(grid))


# Time: O(n^4)

# DFS to collect both islands: O(n^2)

# Comparing all pairs: O(n^2 * n^2) → worst case.

# Space: O(n^2) for visited and storing island coordinates.

# ✅ When to Use Brute Force?
# Use brute force for:

# Understanding logic

# Small grid sizes

# Initial implementation before optimizing

# Let me know if you want to visualize this on an example!