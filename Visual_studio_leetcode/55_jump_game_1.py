class Solution(object):
    def canJump(self, nums):
      
        goal = len(nums) - 1

        for i in range(len(nums) -1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return True if goal == 0 else False


sol = Solution()

nums = [2,3,1,1,4]

print(sol.canJump(nums))

nums = [3,2,1,0,4]
print(sol.canJump(nums))

# nums = [1] * 9999 + [0]
# print(sol.canJump(nums))

 # Time Complexity: O(n)
 # Space Complexity: O(1)
 
#  reverse Greedy