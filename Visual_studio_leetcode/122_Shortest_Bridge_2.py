from collections import deque
from typing import List

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        N = len(grid)
        direct = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def invalid(r, c):
            return r < 0 or c < 0 or r >= N or c >= N

        visit = set()

        # DFS to mark the first island and add its coordinates to 'visit'
        def dfs(r, c):
            if invalid(r, c) or not grid[r][c] or (r, c) in visit:
                return
            visit.add((r, c))
            for dr, dc in direct:
                dfs(r + dr, c + dc)

        # BFS to expand from first island to reach second island
        def bfs():
            res = 0
            q = deque(visit)
            while q:
                for i in range(len(q)):
                    r, c = q.popleft()
                    for dr, dc in direct:
                        curR, curC = r + dr, c + dc
                        if invalid(curR, curC) or (curR, curC) in visit:
                            continue
                        if grid[curR][curC] == 1:
                            return res
                        q.append((curR, curC))
                        visit.add((curR, curC))
                res += 1

        # Find first island using DFS
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 1:
                    dfs(r, c)
                    return bfs()

grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
print(Solution().shortestBridge(grid))

# This is Better
# output is

# [
#     [1, 1, 1, 1, 1],
#     [1, 0, 0, 0, 1],
#     [1, 1, 1, 0, 1],  # ← (2,1) changed from 0 → 1
#     [1, 0, 0, 0, 1],
#     [1, 1, 1, 1, 1]
# ]


# | Aspect           | Details                                                       |
# | ---------------- | ------------------------------------------------------------- |
# | Algorithm        | DFS + BFS                                                     |
# | Technique        | Graph traversal; marking island + shortest path BFS expansion |
# | Time Complexity  | O(N²)                                                         |
# | Space Complexity | O(N²)                                                         |
