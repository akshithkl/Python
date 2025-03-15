class Solution:
    def sortedSquares(self, nums):
        return sorted(map(lambda x:x*x,nums))
    
a = Solution()

print(a.sortedSquares([-4,-1,0,3,10]))