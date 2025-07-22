from collections import deque, defaultdict

class Solution(object):
    def shortestAlternatingPaths(self, n, redEdges, blueEdges):
 
        # Step 1: Build the graph
        red_graph = defaultdict(list)
        blue_graph = defaultdict(list)

        for u, v in redEdges:
            red_graph[u].append(v)
        for u, v in blueEdges:
            blue_graph[u].append(v)

        # Step 2: Initialize answer and visited tracking
        answer = [-1] * n
        visited = [[False, False] for _ in range(n)]  # visited[node][color]

        # Step 3: BFS queue -> (node, steps, last_color)
        queue = deque()
        queue.append((0, 0, -1))  # Start with node 0, 0 steps, no previous color

        while queue:
            node, steps, last_color = queue.popleft()

            if answer[node] == -1:
                answer[node] = steps

            # If last color was not red, explore red edges
            if last_color != 0:
                for neighbor in red_graph[node]:
                    if not visited[neighbor][0]:
                        visited[neighbor][0] = True
                        queue.append((neighbor, steps + 1, 0))

            # If last color was not blue, explore blue edges
            if last_color != 1:
                for neighbor in blue_graph[node]:
                    if not visited[neighbor][1]:
                        visited[neighbor][1] = True
                        queue.append((neighbor, steps + 1, 1))

        return answer  

n = 3
redEdges = [[0,1]]
blueEdges = [[2,1]]


sol = Solution()
print(sol.shortestAlternatingPaths( n, redEdges, blueEdges))

n = 3
redEdges = [[0,1]]
blueEdges = [[1,2]]

# Output: [0,1,2]

sol = Solution()
print(sol.shortestAlternatingPaths( n, redEdges, blueEdges))



#         | Aspect               | Value                           |
# | -------------------- | ------------------------------- |
# | **Algorithm**        | BFS with color tracking         |
# | **Technique**        | Level-wise BFS + visited matrix |
# | **Time Complexity**  | `O(n + r + b)`                  |
# | **Space Complexity** | `O(n + r + b)`                  |
# | **Best for**         | Shortest path with constraints  |
