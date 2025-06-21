class Solution(object):
    def rob(self, nums):
        memo = {}

        def dp(i):
            if i >= len(nums):
                return 0
            if i in memo:
                return memo[i]

            # Option 1: Rob current house, then skip one
            rob = nums[i] + dp(i + 2)

            # Option 2: Skip current house
            skip = dp(i + 1)

            memo[i] = max(rob, skip)
            return memo[i]

        return dp(0)



nums = [2, 7, 9, 3, 1, 8]
sol = Solution()
print(sol.rob(nums))  # ✅ Output: 19


#  the answer is 19 becase
# Rob house 0 (2)

# Rob house 2 (9)

# Rob house 5 (8)

#  it jum 2 step or more very heighest value there but dont got one step


# | Attribute      | Description                                                           |
# | -------------- | --------------------------------------------------------------------- |
# | **Algorithm**  | **Dynamic Programming**                                               |
# | **Approach**   | **Top-Down (Recursion with Memoization)**                             |
# | **Technique**  | **DFS + Memoization**                                                 |
# | **Pattern**    | **Maximum Non-Adjacent Sum**                                          |
# | **Time**       | `O(n)` (each subproblem computed once)                                |
# | **Space**      | `O(n)` stack + memo dict                                              |
# | **Strengths**  | Easy to understand, follows problem logic directly                    |
# | **Weaknesses** | Uses more memory (call stack + memo), slower in Python for big inputs |
