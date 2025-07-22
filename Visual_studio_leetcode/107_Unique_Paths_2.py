class Solution(object):
    def uniquePaths(self, m, n):
        def dfs(i, j):
            if i == m - 1 and j == n - 1:
                return 1
            if i >= m or j >= n:
                return 0
            return dfs(i + 1, j) + dfs(i, j + 1)
        
        return dfs(0, 0)

m = 3
n = 7

sol = Solution()
print(sol.uniquePaths(m, n))


# 💻 Code (Brute Force Recursion):
    
# | Metric               | Value                        |
# | -------------------- | ---------------------------- |
# | **Time Complexity**  | Exponential → **O(2^(m+n))** |
# | **Space Complexity** | Stack space → **O(m + n)**   |
