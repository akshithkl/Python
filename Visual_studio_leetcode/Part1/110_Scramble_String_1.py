class Solution(object):
    def isScramble(self, s1, s2):

        memo = {}

        def dfs(x, y):
            if (x, y) in memo:
                return memo[(x, y)]

            if x == y:
                memo[(x, y)] = True
                return True

            if sorted(x) != sorted(y):
                memo[(x, y)] = False
                return False

            n = len(x)
            for i in range(1, n):
                # Case 1: No swap
                if dfs(x[:i], y[:i]) and dfs(x[i:], y[i:]):
                    memo[(x, y)] = True
                    return True
                # Case 2: Swap
                if dfs(x[:i], y[-i:]) and dfs(x[i:], y[:-i]):
                    memo[(x, y)] = True
                    return True

            memo[(x, y)] = False
            return False

        return dfs(s1, s2)


sol = Solution()

print(sol.isScramble("great", "rgeat"))   # ✅ True
print(sol.isScramble("abcde", "caebd"))   # ❌ False




# | Aspect               | Value                                         |
# | -------------------- | --------------------------------------------- |
# | **Algorithm**        | DFS + Memoization                             |
# | **Technique**        | Divide and Conquer, Dynamic Programming       |
# | **Approach**         | Recursively split + check swapped/non-swapped |
# | **Time Complexity**  | `O(n⁴)`                                       |
# | **Space Complexity** | `O(n³)`                                       |
