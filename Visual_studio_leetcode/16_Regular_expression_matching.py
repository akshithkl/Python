class Solution:        
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}  # Memoization dictionary

        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if j == len(p):  
                return i == len(s)  # True if both strings are exhausted

            first_match = i < len(s) and (p[j] == s[i] or p[j] == '.')

            if j + 1 < len(p) and p[j + 1] == '*':
                # Either skip the '*' pattern or use it if the first character matches
                memo[(i, j)] = dp(i, j + 2) or (first_match and dp(i + 1, j))
            else:
                memo[(i, j)] = first_match and dp(i + 1, j + 1)

            return memo[(i, j)]

        return dp(0, 0)

# Creating an instance of the Solution class
a = Solution()

# Correct function call with both arguments
b = a.isMatch("aa", "a*")  
print(b)  # Output: True
