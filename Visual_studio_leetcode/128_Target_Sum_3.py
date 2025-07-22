class Solution(object):
    def findTargetSumWays(self, nums, target):
        def backtrack(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            
            # Try adding the current number
            add = backtrack(i + 1, total + nums[i])
            # Try subtracting the current number
            subtract = backtrack(i + 1, total - nums[i])
            
            return add + subtract

        return backtrack(0, 0)

# Example usage
nums = [1, 1, 1, 1, 1]
target = 3
print(Solution().findTargetSumWays(nums, target))  # Output: 5


# | Aspect               | Value                       |
# | -------------------- | --------------------------- |
# | **Algorithm**        | Recursive Backtracking      |
# | **Approach**         | Try all combinations of +/- |
# | **Technique**        | Brute-force recursion       |
# | **Time Complexity**  | O(2^n)                      |
# | **Space Complexity** | O(n) (due to recursion)     |
