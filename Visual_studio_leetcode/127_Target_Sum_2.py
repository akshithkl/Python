class Solution(object):
    def findTargetSumWays(self, nums, target):
            total = sum(nums)
            
            # Edge case: If (total + target) is odd, no possible subset
            if (total + target) % 2 != 0 or abs(target) > total:
                return 0

            subset_sum = (total + target) // 2

            # DP array: dp[i] = number of ways to get sum i
            dp = [0] * (subset_sum + 1)
            dp[0] = 1  # There is one way to make sum 0 — choose nothing

            for num in nums:
                # Traverse backwards to avoid overwriting
                for s in range(subset_sum, num - 1, -1):
                    dp[s] += dp[s - num]

            return dp[subset_sum]

# Example
nums = [1, 1, 1, 1, 1]
target = 3
print(Solution().findTargetSumWays(nums, target))  # Output: 5



# | Complexity    | Notation                         | Explanation                         |
# | ------------- | -------------------------------- | ----------------------------------- |
# | **Time**      | $O(n \times S)$                  | $n$ elements × subset sum range $S$ |
# | **Space**     | $O(S)$                           | DP array size proportional to $S$   |
# | **Algorithm** | Dynamic Programming              | Bottom-up subset sum count approach |
# | **Technique** | 1D DP array, optimized for space | Avoids 2D DP by iterating backwards |
