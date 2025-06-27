class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        res = float("inf")

        for i in range(n):
            total = 0
            for j in range(i, n):
                total += nums[j]
                if total >= target:
                    res = min(res, j - i + 1)
                    break  # Stop early since adding more will only increase the length

        return 0 if res == float("inf") else res


nums = [2,3,1,2,4,3]
target = 7

sol = Solution()
print(sol.minSubArrayLen(target, nums))


# ⏱️ Time Complexity:
# Outer loop runs n times.

# Inner loop runs up to n times (in the worst case).

# So the total is O(n²).

# 🧠 Space Complexity:
# Only uses constant space → O(1)