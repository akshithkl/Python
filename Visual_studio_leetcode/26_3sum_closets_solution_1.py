

class Solution:
    def threeSumClosest(self, nums, target) :
        nums.sort()
        closest_sum = float('inf')
        
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                    
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    return current_sum  # Exact match
        
        return closest_sum


nums = [-1,2,1,-4]

a = Solution()
print(a.threeSumClosest(nums, target=1))