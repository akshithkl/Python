# Brute Force Code (O(n²))

class Solution(object):
    def pivotIndex(self, nums):
        for i in range(len(nums)):  
            left_sum = sum(nums[:i])    # O(n)
            right_sum = sum(nums[i+1:]) # O(n)
            
            if left_sum == right_sum:
                return i
        return -1

nums = [1,7,3,6,5,6]
sol = Solution()
result = sol.pivotIndex(nums)
print(result)  # Output: 3
