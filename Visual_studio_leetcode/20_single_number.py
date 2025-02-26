class Solution:
    def singleNumber(self, nums):
        res = 0 
        for i in nums:
            res = i ^ res
        return res
        
a = Solution()
final = a.singleNumber([4,1,4,8,2,1,2])

print(final)