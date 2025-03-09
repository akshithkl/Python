class Solution:
    def sortedSquares(self, nums):
        new_nums = []
        
        for i, v in enumerate(nums):
            k = i
            val = v * v
            if not new_nums:
                new_nums.append(val)
            
            elif val < new_nums[i-1]:
                new_nums.append(val)
                for j in range(1,len(nums)):
                    if j >= 0:
                        new_nums[j-1], new_nums[k] =  new_nums[k], new_nums[j-1]
                        j -= 1
                
            
            else:
                new_nums.append(val)
                


        
       # new_nums.sort() 
       
        return new_nums             #sorted(new_nums) 

a = Solution()

print(a.sortedSquares([-4,-1,0,3,10]))