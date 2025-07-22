class Solution:
    def numDecodings(self, s: str) -> int:

        dp = {len(s): 1}

        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0

            res = dfs(i + 1)
            if i + 1 < len(s) and 10 <= int(s[i:i+2]) <= 26:
                res += dfs(i + 2)

            dp[i] = res
            return res

        return dfs(0)

s = "123"
print(Solution().numDecodings(s))


# | Aspect               | Value                        |
# | -------------------- | ---------------------------- |
# | **Problem Type**     | Decode Ways (Leetcode 91)    |
# | **Algorithm**        | Dynamic Programming          |
# | **Approach**         | Top-Down (DFS + Memoization) |
# | **Technique**        | Recursion, Memoization       |
# | **Time Complexity**  | O(n)                         |
# | **Space Complexity** | O(n)                         |


#           []
#          /   \
#      ['1']   ['12']
#      /   \       \
# ['1','2'] ['1','23'] ['12','3']
#     /
# ['1','2','3']
