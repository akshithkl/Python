class Solution(object):
    def minSubArrayLen(self, target, nums):
        l = 0
        total = 0
        res = float("inf")

        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                res = min(r - l + 1, res)
                total -= nums[l]
                l += 1
        return 0 if res == float("inf") else res
nums = [2,3,1,2,4,3]
target = 7

sol = Solution()
print(sol.minSubArrayLen(target, nums))

# ⏱️ Time Complexity: O(n)

# The right pointer r goes from 0 to n-1, so it runs n times.

# The left pointer l also only moves forward and never backward.

# Therefore, in total, both pointers traverse the array once, making the overall complexity O(n).

# 🧠 Space Complexity: O(1)

# No extra space is used apart from a few variables (l, r, total, res).

# The input list nums is not modified or duplicated.
   
    

