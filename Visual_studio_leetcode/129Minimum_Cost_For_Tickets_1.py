class Solution(object):
    def mincostTickets(self, days, costs):
        
        dp = {}
        n = len(days)

        for i in range(n - 1, -1, -1):  # iterate from end to start
            dp[i] = float("inf")
            for d, c in zip([1, 7, 30], costs):
                j = i
                while j < n and days[j] < days[i] + d:
                    j += 1
                dp[i] = min(dp[i], c + dp.get(j, 0))

        return dp[0]
    
days = [1,4,6,7,8,20]
costs = [2,7,15]
print(Solution().mincostTickets(days, costs))

# | Attribute            | Value / Explanation                           |
# | -------------------- | --------------------------------------------- |
# | **Algorithm**        | Dynamic Programming                           |
# | **Approach**         | Bottom-Up (Reverse iteration)                 |
# | **Technique**        | Tabulation using dictionary                   |
# | **Time Complexity**  | O(N)                                          |
# | **Space Complexity** | O(N)                                          |
# | **Optimized**        | Yes (no recursion stack used, pure iterative) |
#                  |


# | Index `i` | Travel Day | `days[i]` | Pass Options Tried                                    | Next `j` Index (First Not Covered) | Cost Expression           | `dp[i]` |
# | --------- | ---------- | --------- | ----------------------------------------------------- | ---------------------------------- | ------------------------- | ------- |
# | 5         | Last day   | 20        | 1-day → \[20], 7-day → \[20], 30-day → \[20]          | 6, 6, 6                            | min(2 + 0, 7 + 0, 15 + 0) | 2       |
# | 4         |            | 8         | 1-day → \[8], 7-day → \[8 to 14], 30-day → \[8 to 37] | 5, 6, 6                            | min(2 + 2, 7 + 0, 15 + 0) | 4       |
# | 3         |            | 7         | 1-day → \[7], 7-day → \[7 to 13], 30-day → \[7 to 36] | 4, 5, 6                            | min(2 + 4, 7 + 2, 15 + 0) | 6       |
# | 2         |            | 6         | 1-day → \[6], 7-day → \[6 to 12], 30-day → \[6 to 35] | 3, 5, 6                            | min(2 + 6, 7 + 2, 15 + 0) | 8       |
# | 1         |            | 4         | 1-day → \[4], 7-day → \[4 to 10], 30-day → \[4 to 33] | 2, 5, 6                            | min(2 + 8, 7 + 2, 15 + 0) | 9       |
# | 0         | First day  | 1         | 1-day → \[1], 7-day → \[1 to 7], 30-day → \[1 to 30]  | 1, 3, 6                            | min(2 + 9, 7 + 6, 15 + 0) | 11      |
