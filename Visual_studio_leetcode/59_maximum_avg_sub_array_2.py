class Solution(object):
    def findMaxAverage(self, nums, k):

        window = sum(nums[0:k])
        window_max = window 
        
        for i in range(k, len(nums)):
            window = window + nums[i] - nums[i - k] 
            if window > window_max:
                window_max = window 

        print(k)
        print(window_max)
        
        return float(window_max) / k

# Test
nums = [1, 12, -5, -6, 50, 3]
k = 4
            
sol = Solution()
print(sol.findMaxAverage(nums, k))


# Sliding Window

# ⏱ Time Complexity: O(n)
# sum(nums[0:k]) is O(k)

# Loop runs (n - k) times, each step is O(1)

# So total time is O(n)

# 🧠 Space Complexity: O(1)
# Uses constant space (window, window_max)

