
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        n = len(s1)
        if len(s2) != n:
            return False
        if s1 == s2:
            return True

        # 3D DP: dp[i][j][l] = True if s1[i:i+l] is a scramble of s2[j:j+l]
        dp = [[[False] * (n + 1) for _ in range(n)] for _ in range(n)]

        # Length 1 substrings
        for i in range(n):
            for j in range(n):
                dp[i][j][1] = s1[i] == s2[j]

        # Length > 1 substrings
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                for j in range(n - length + 1):
                    for k in range(1, length):
                        if (dp[i][j][k] and dp[i + k][j + k][length - k]) or \
                           (dp[i][j + length - k][k] and dp[i + k][j][length - k]):
                            dp[i][j][length] = True
                            break

        return dp[0][0][n]

sol = Solution()

print(sol.isScramble("great", "rgeat"))   # ✅ True
print(sol.isScramble("abcde", "caebd"))   # ❌ False

# print(sol.isScramble("a", "a"))           # ✅ True
# print(sol.isScramble("abc", "bca"))       # ✅ True


#  Bottom-Up Summary
# Metric	Value
# Time Complexity	O(n⁴)
# Space Complexity	O(n³)
# Advantage	No recursion, less call stack pressure, often faster in real input cases
