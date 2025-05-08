class Solution(object):
    def findMaxAverage(self, nums, k):
      
        window = sum(nums[:k])
        max_avg = window* 1.0 / k

        for i in range(k, len(nums)):
            window += nums[i] - nums[i - k]
            max_avg = max(max_avg, window * 1.0 / k)
        
        return max_avg


# Test
nums = [1, 12, -5, -6, 50, 3]
k = 4
            
sol = Solution()
print(sol.findMaxAverage(nums, k))

#  Sliding Window


# ⏱ Time Complexity: O(n)
# sum(nums[:k]) takes O(k) time.

# The loop from k to len(nums) takes O(n - k) time.

# So, total time = O(k + (n - k)) = O(n)

# 🧠 Space Complexity: O(1)
# You're using only a few variables (window, max_avg), regardless of the size of the input.

# No extra space proportional to input size.