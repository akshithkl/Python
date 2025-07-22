class Solution(object):
    def findTargetSumWays(self, nums, target):
        
        dp = {}

        def backtrack(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            if (i, total) in dp:
                return dp[(i, total)]
            
            dp[(i, total)] = (backtrack(i+1, total + nums[i])
                              +
                              backtrack(i+1, total - nums[i]))
            return dp[(i, total)]            
        
        return backtrack(0, 0)

nums = [1,1,1,1,1]
target = 3
print(Solution().findTargetSumWays(nums, target))

# | Aspect               | Description                               |
# | -------------------- | ----------------------------------------- |
# | **Algorithm**        | Top-down Dynamic Programming (with memo)  |
# | **Approach**         | Backtracking + Memoization (Recursive DP) |
# | **Technique**        | DFS-style recursion + DP cache            |
# | **Time Complexity**  | `O(n * sum(nums))`                        |
# | **Space Complexity** | `O(n * sum(nums))`                        |


# (0, 0)
# ├── +1 → (1, 1)
# │   ├── +1 → (2, 2)
# │   │   ├── +1 → (3, 3)
# │   │   │   ├── +1 → (4, 4)
# │   │   │   │   ├── +1 → (5, 5) ❌
# │   │   │   │   └── -1 → (5, 3) ✅ +1
# │   │   │   └── -1 → (4, 2)
# │   │   │       ├── +1 → (5, 3) ✅ +1
# │   │   │       └── -1 → (5, 1) ❌
# │   │   └── -1 → (3, 1)
# │   │       ├── +1 → (4, 2) → Already computed
# │   │       └── -1 → (4, 0) ❌
# │   └── -1 → (2, 0)
# │       ├── +1 → (3, 1) → Already computed
# │       └── -1 → (3, -1)
# │           ├── +1 → (4, 0) ❌
# │           └── -1 → (4, -2) ❌
# └── -1 → (1, -1)
#     ├── +1 → ...
#     └── -1 → ...
