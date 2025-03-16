class Solution:
    def sortedSquares(self, nums):
        for i in range(len(nums)):
            nums[i] = nums[i] * nums[i]
            
        nums.sort() 
       
        return nums              #sorted(new_nums) '''
        
a = Solution()

print(a.sortedSquares([-4,-1,0,3,10]))