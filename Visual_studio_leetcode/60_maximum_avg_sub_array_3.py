class Solution(object):
    def findMaxAverage(self, nums, k):
     
        max_avg = float('-inf')

        for i in range(len(nums) - k + 1):
            current_sum = sum(nums[i:i+k])
            current_avg = current_sum * 1.0 / k
            if current_avg > max_avg:
                max_avg = current_avg

        return max_avg

# Test
nums = [1, 12, -5, -6, 50, 3]
k = 4

sol = Solution()
print(sol.findMaxAverage(nums, k))

# Bruteforce

# 📈 Time Complexity:
# O(n * k) — because for each of the n − k + 1 subarrays, you're summing k elements.

# 🧠 Space Complexity:
# O(1) — constant space used.