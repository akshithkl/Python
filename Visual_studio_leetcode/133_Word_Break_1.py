class Solution(object):
    def wordBreak(self, s, wordDict):
  
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                
                if dp[i]:
                    break
            
        return dp[0]

s = "leetcode"
wordDict = ["leet","code"]

print(Solution().wordBreak(s, wordDict))

# Time Complexity	O(n * k * m)
# Space Complexity	O(n)

# | **Aspect**           | **Value**                                  |
# | -------------------- | ------------------------------------------ |
# | **Algorithm**        | Dynamic Programming                        |
# | **Approach**         | Bottom-Up Tabulation                       |
# | **Technique**        | String Matching + Early Termination        |
# | **Best Case**        | Early match in `wordDict` (fast `break`)   |
# | **Worst Case**       | All combinations checked (no early breaks) |


# | Index (i) | Substring `s[i:]` | Matched Word | `dp[i + len(word)]` | `dp[i]` |
# | --------- | ----------------- | ------------ | ------------------- | ------- |
# | 7         | `"e"`             | ❌            |                     | False   |
# | 6         | `"de"`            | ❌            |                     | False   |
# | 5         | `"ode"`           | ❌            |                     | False   |
# | 4         | `"code"`          | ✅ `"code"`   | `dp[8] = True`      | True    |
# | 3         | `"tcode"`         | ❌            |                     | False   |
# | 2         | `"etcode"`        | ❌            |                     | False   |
# | 1         | `"eetcode"`       | ❌            |                     | False   |
# | 0         | `"leetcode"`      | ✅ `"leet"`   | `dp[4] = True`      | True    |
