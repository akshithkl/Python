class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        
        dp[n] = 1  # Base case: empty string has 1 way to decode

        for i in range(n - 1, -1, -1):
            if s[i] != "0":
                dp[i] += dp[i + 1]
            
                if i + 1 < n and 10 <= int(s[i:i+2]) <= 26:
                    dp[i] += dp[i + 2]
        
        return dp[0]



s = "123"
print(Solution().numDecodings(s))


# | Aspect               | Value                         |
# | -------------------- | ----------------------------- |
# | **Problem Type**     | Decode Ways (Leetcode 91)     |
# | **Algorithm**        | Dynamic Programming           |
# | **Approach**         | Bottom-Up (Tabulation)        |
# | **Technique**        | Iterative DP on String        |
# | **Time Complexity**  | O(n)                          |
# | **Space Complexity** | O(n) → Can be reduced to O(1) |
