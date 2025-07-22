class Solution:
    def subsets(self, nums):
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # Decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # Decision to exclude nums[i]
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res
nums = [1, 2, 3]

print(Solution().subsets(nums))


# | Aspect          | Value        | Reason                                              |
# | --------------- | ------------ | --------------------------------------------------- |
# | **Time**        | `O(2^n)`     | Each element has 2 choices: include or exclude      |
# | **Space**       | `O(n)`       | Call stack + subset list                            |
# | **Output Size** | `O(2^n * n)` | Up to `2^n` subsets, each of size `n` in worst case |

