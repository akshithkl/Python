def minCostClimbingStairs(cost):
    def dfs(i):
        if i >= len(cost):
            return 0  # Reached top
        return cost[i] + min(dfs(i + 1), dfs(i + 2))
    
    return min(dfs(0), dfs(1))

cost = [10, 15, 20]

print(minCostClimbingStairs(cost))

# Recursive Brute Force (Without Memoization)

# | Type      | Complexity                                                                               |
# | --------- | ---------------------------------------------------------------------------------------- |
# | **Time**  | **O(2ⁿ)** — Exponential! Because from each step, we branch into two new recursive calls. |
# | **Space** | **O(n)** — due to the recursion call stack (worst case depth is `n`).                    |
