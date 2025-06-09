class Solution(object):
    def isInterleave(self, s1, s2, s3):

        if len(s1) + len(s2) != len(s3):
            return False

        dp = [False] * (len(s2) + 1)
        dp[0] = True

        for j in range(1, len(s2) + 1):
            dp[j] = dp[j-1] and s2[j-1] == s3[j-1]

        for i in range(1, len(s1) + 1):
            dp[0] = dp[0] and s1[i-1] == s3[i-1]
            for j in range(1, len(s2) + 1):
                dp[j] = (dp[j] and s1[i-1] == s3[i+j-1]) or (dp[j-1] and s2[j-1] == s3[i+j-1])

        return dp[len(s2)]

s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"

sol = Solution()
print(sol.isInterleave(s1, s2, s3))

s1 = "aabcc"
s2 ="dbbca"
s3 = "aadbbbaccc"

sol = Solution()
print(sol.isInterleave(s1, s2, s3))


# ⏱️ Time and Space Complexity
# Time: O(m × n)

# Space: O(n) ← reduced from O(m × n)

