class Solution(object):
    def mincostTickets(self, days, costs):
        n = len(days)
        memo = {}

        def dfs(i):
            if i >= n:
                return 0

            if i in memo:
                return memo[i]

            # Option 1: 1-day pass
            cost1 = costs[0]
            j = i
            while j < n and days[j] < days[i] + 1:
                j += 1
            total1 = cost1 + dfs(j)

            # Option 2: 7-day pass
            cost7 = costs[1]
            j = i
            while j < n and days[j] < days[i] + 7:
                j += 1
            total7 = cost7 + dfs(j)

            # Option 3: 30-day pass
            cost30 = costs[2]
            j = i
            while j < n and days[j] < days[i] + 30:
                j += 1
            total30 = cost30 + dfs(j)

            memo[i] = min(total1, total7, total30)
            return memo[i]

        return dfs(0)

days = [1,4,6,7,8,20]
costs = [2,7,15]
print(Solution().mincostTickets(days, costs))



# | Component                 | Value                                    |
# | ------------------------- | ---------------------------------------- |
# | **Approach**              | Top-Down DP with Memoization             |
# | **Algorithmic Technique** | DP + Greedy choices (brute-force + memo) |
# | **Time Complexity**       | O(n)                                     |
# | **Space Complexity**      | O(n)                                     |
