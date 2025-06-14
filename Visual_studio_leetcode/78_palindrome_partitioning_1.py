# Dfs Backtracking
class Solution(object):
    def partition(self, s):
    
        res = []
        part = []

        def dfs(i):
            if i >= len(s):
                res.append(list(part))
                # res.append(part[:])
                return
            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    part.append(s[i:j+1])
                    dfs(j + 1)
                    part.pop()
        dfs(0)
        return res
    
    def isPalindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True

sol = Solution()
print(sol.partition("aab"))
# Output: [['a', 'a', 'b'], ['aa', 'b']]



# | Metric                     | Complexity   |
# | -------------------------- | ------------ |
# | **Time**                   | `O(2^n * n)` |
# | **Space (total)**          | `O(n * 2^n)` |
# | **Space (recursion only)** | `O(n)`       |


# dfs(0)
# ├── j = 0 → s[0:1] = "a" is palindrome
# │   ├── part = ["a"]
# │   └── dfs(1)
# │       ├── j = 1 → s[1:2] = "a" is palindrome
# │       │   ├── part = ["a", "a"]
# │       │   └── dfs(2)
# │       │       ├── j = 2 → s[2:3] = "b" is palindrome
# │       │       │   ├── part = ["a", "a", "b"]
# │       │       │   └── dfs(3) → end of string, append to `res`
# │       │       │       └── res = [["a", "a", "b"]]
# │       │       └── backtrack: part = ["a", "a"]
# │       └── backtrack: part = ["a"]
# │
# ├── j = 1 → s[0:2] = "aa" is palindrome
# │   ├── part = ["aa"]
# │   └── dfs(2)
# │       ├── j = 2 → s[2:3] = "b" is palindrome
# │       │   ├── part = ["aa", "b"]
# │       │   └── dfs(3) → end of string
# │       │       └── res = [["a", "a", "b"], ["aa", "b"]]
# │       └── backtrack: part = ["aa"]
# │
# └── j = 2 → s[0:3] = "aab" is NOT a palindrome → skip
