class Solution(object):
    def shortestBridge(self, grid):

        n = len(grid)
        visited = [[False for _ in range(n)] for _ in range(n)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = []

        # Step 1: DFS to find and mark the first island
        def dfs(x, y):
            if x < 0 or x >= n or y < 0 or y >= n:
                return
            if visited[x][y] or grid[x][y] == 0:
                return
            visited[x][y] = True
            queue.append((x, y))  # collect for BFS
            for dx, dy in directions:
                dfs(x + dx, y + dy)

        # Step 1: Find first island and mark it
        found = False
        for i in range(n):
            if found:
                break
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    found = True
                    break

        # Step 2: BFS from the first island to find second island
        steps = 0
        while queue:
            next_queue = []  # manual queue for next level
            for x, y in queue:
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                        if grid[nx][ny] == 1:
                            return steps
                        visited[nx][ny] = True
                        next_queue.append((nx, ny))
            queue = next_queue
            steps += 1
          

        return -1  # should never happen


grid = [[0,1],[1,0]]

print(Solution().shortestBridge(grid))

# grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]

# output




# | **Aspect**              | **Details**                                                               |
# | ----------------------- | ------------------------------------------------------------------------- |
# | **Problem Type**        | Graph traversal                                                           |
# | **Input**               | `n x n` binary grid (0: water, 1: land)                                   |
# | **Goal**                | Find minimum number of `0`s to flip to connect two islands                |
# | **Algorithm**           | - DFS (for island marking) <br> - BFS (for shortest path search)          |
# | **Approach**            | - Flood fill with DFS <br> - Multi-source BFS                             |
# | **Techniques Used**     | - DFS recursion <br> - Manual BFS queue (list) <br> - Visited matrix      |
# | **Time Complexity**     | `O(N^2)`                                                                  |
# | **Space Complexity**    | `O(N^2)`                                                                  |
# | **Why Time is O(N²)?**  | Every cell is visited at most once during DFS and once during BFS         |
# | **Why Space is O(N²)?** | - `visited` matrix: O(N²) <br> - BFS queue: O(N²) <br> - DFS stack: O(N²) |
# | **Output**              | Minimum number of `0`s to flip (integer)                                  |
# | **Edge Cases Handled**  | Assumes exactly 2 islands (guaranteed by problem constraints)             |

