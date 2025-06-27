class Solution(object):
    def maxRotateFunction(self, nums):
        n = len(nums)
        total_sum = sum(nums)
        f = sum(i * num for i, num in enumerate(nums))
        max_value = f

        for i in range(1, n):
            f += total_sum - n * nums[-i]
            max_value = max(max_value, f)

        return max_value

nums = [4,3,2,6]
sol = Solution()
print(sol.maxRotateFunction(nums))

#  Dynamic Bottom up

# ⏱️ Time Complexity
# sum(nums) → O(n)

# sum(i * num for i, num in enumerate(nums)) → O(n)

# Loop from 1 to n-1 → O(n)

# So,
# Time Complexiy=𝑂(𝑛)
# Time Complexity= 
# O(n)
# ​
 
# 📦 Space Complexity
# We use only a constant number of variables: n, total_sum, f, max_value

# No additional data structures are created.So,

# Space Complexity=𝑂(1)
# Space Complexity= O(1)
# ​
 
"""
Formula :
       F(k)=F(k-1)+total_sum-n⋅nums[n-k]
       
Input: nums = [4,3,2,6]
Output: 26
Explanation:
F(0) = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 0 + 3 + 4 + 18 = 25
F(1) = (0 * 6) + (1 * 4) + (2 * 3) + (3 * 2) = 0 + 4 + 6 + 6 = 16
F(2) = (0 * 2) + (1 * 6) + (2 * 4) + (3 * 3) = 0 + 6 + 8 + 9 = 23
F(3) = (0 * 3) + (1 * 2) + (2 * 6) + (3 * 4) = 0 + 2 + 12 + 12 = 26
So the maximum value of F(0), F(1), F(2), F(3) is F(3) = 26.
"""

