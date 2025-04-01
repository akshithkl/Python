class Solution(object):
    def pivotIndex(self, nums):
        total = sum(nums) # O(n)
        left_sum = 0

        for i in range(len(nums)):
            right_sum = total - nums[i] - left_sum
            if left_sum == right_sum:
                return i
            left_sum += nums[i]
        
        return -1

nums = [1,7,3,6,5,6]
sol = Solution()
result = sol.pivotIndex(nums)
print(result)

nums = [1,2,3]
sol = Solution()
result = sol.pivotIndex(nums)
print(result)

nums = [2,1,-1]
sol = Solution()
result = sol.pivotIndex(nums)
print(result)

nums = [2]
sol = Solution()
result = sol.pivotIndex(nums)
print(result)