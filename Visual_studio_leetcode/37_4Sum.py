class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        n=len(nums)
        res=[]
        for i in range(n-3):
            if nums[i]+nums[i+1]+nums[i+2]+nums[i+3]>target:
                break
            if i>0 and nums[i]==nums[i-1]:
                continue
            if nums[i]+nums[n-1]+nums[n-2]+nums[n-3]<target:
                continue
            for j in range(i+1,n-2):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                l,r=j+1,n-1
                while l<r:
                    total = nums[i]+nums[j]+nums[l]+nums[r]
                    if total == target:
                        res.append([nums[i],nums[j],nums[l],nums[r]])
                        l+=1
                        r-=1
                        while l<r and nums[l]==nums[l-1]:
                            l+=1
                        while l<r and nums[r]==nums[r+1]:
                            r-=1
                    elif total<target:
                        l+=1
                    else:
                        r-=1
        return res

a = Solution()
 
result = a.fourSum([1,0,-1,0,-2,2], 0)
print(result) 

result = a.fourSum([2,2,2,2,2], 8)
print(result) 