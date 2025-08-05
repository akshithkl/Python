class Solution(object):
    def shortestAlternatingPaths(self, n, redEdges, blueEdges):

        # Step 1: Create adjacency lists (normal dicts)
        red_graph = {}
        blue_graph = {}

        for i in range(n):
            red_graph[i] = []
            blue_graph[i] = []

        for u, v in redEdges:
            red_graph[u].append(v)

        for u, v in blueEdges:
            blue_graph[u].append(v)

        # Step 2: Initialize visited and answer
        answer = [-1] * n
        visited = [[False, False] for _ in range(n)]  # visited[node][color]

        # Step 3: Implement queue manually: [ [node, steps, last_color], ... ]
        queue = []
        queue.append([0, 0, -1])  # Start from node 0, steps 0, no last color

        front = 0  # pointer for queue front (to simulate deque)

        while front < len(queue):
            node, steps, last_color = queue[front]
            front += 1

            if answer[node] == -1:
                answer[node] = steps

            # If last color not red (0), take red edges next
            if last_color != 0:
                for nei in red_graph[node]:
                    if not visited[nei][0]:
                        visited[nei][0] = True
                        queue.append([nei, steps + 1, 0])

            # If last color not blue (1), take blue edges next
            if last_color != 1:
                for nei in blue_graph[node]:
                    if not visited[nei][1]:
                        visited[nei][1] = True
                        queue.append([nei, steps + 1, 1])

        return answer



n = 3
redEdges = [[0,1]]
blueEdges = [[1,2]]

# Output: [0,1,2]

sol = Solution()
print(sol.shortestAlternatingPaths( n, redEdges, blueEdges))



# | Component            | Description                                |
# | -------------------- | ------------------------------------------ |
# | **Algorithm**        | BFS with edge color tracking               |
# | **Approach**         | Level-order BFS with color alternation     |
# | **Technique**        | Graph traversal, visited state by color    |
# | **Time Complexity**  | `O(n + r + b)`                             |
# | **Space Complexity** | `O(n + r + b)`                             |
# | **Use Case**         | Shortest path with alternating constraints |
