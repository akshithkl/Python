class Solution(object):
    def wordBreak(self, s, wordDict):

        wordSet = set(wordDict)
        memo = {}

        def dfs(i):
            if i == len(s):
                return True
            if i in memo:
                return memo[i]

            for j in range(i + 1, len(s) + 1):
                if s[i:j] in wordSet and dfs(j):
                    memo[i] = True
                    return True

            memo[i] = False
            return False

        return dfs(0)

s = "leetcode"
wordDict = ["leet","aeet", "code"]

print(Solution().wordBreak(s, wordDict))

# | **Aspect**           | **Value**                                                         |
# | -------------------- | ----------------------------------------------------------------- |
# | **Algorithm**        | Dynamic Programming                                               |
# | **Approach**         | Top-Down Recursion + Memoization                                  |
# | **Technique**        | DFS + Substring Matching                                          |
# | **Time Complexity**  | O(n \* m), where `n` is length of `s`, `m` is average word length |
# | **Space Complexity** | O(n) for recursion stack and memo                                 |
# | **Best Case**        | Early successful match and pruning                                |
# | **Worst Case**       | Try all substrings with no matches                                |


# dfs(0) → "leetcode"
# │
# ├─ Try s[0:1] = "l"   ❌ not in dict
# ├─ Try s[0:2] = "le"  ❌ not in dict
# ├─ Try s[0:3] = "lee" ❌ not in dict
# ├─ Try s[0:4] = "leet" ✅
# │   └─ dfs(4) → "code"
# │       ├─ Try s[4:5] = "c"     ❌
# │       ├─ Try s[4:6] = "co"    ❌
# │       ├─ Try s[4:7] = "cod"   ❌
# │       ├─ Try s[4:8] = "code"  ✅
# │       │   └─ dfs(8) → ""      ✅ → return True
# │       └─ dfs(4) = True        (memoized)
# └─ dfs(0) = True
