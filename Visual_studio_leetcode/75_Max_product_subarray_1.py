class Solution(object):
    def maxProduct(self, nums):
       
        res = max(nums)
        curMin, curMax = 1, 1

        for n in nums:
            if n == 0:
                curMin, curMax = 1, 1
                continue
            temp = curMax * n
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(temp, n * curMin, n)
            res = max(res, curMax)
        return res

nums = [2,3,-2,4]
sol = Solution()
print(sol.maxProduct(nums))

nums = [-2,0,-1]
sol = Solution()
print(sol.maxProduct(nums))

# Time Complexity: O(n) – Single pass through the array

# Space Complexity: O(1) – Only constant extra variables used

# | Feature            | Present in Your Code       |
# | ------------------ | -------------------------- |
# | Iterative solution | ✅ Yes                      |
# | Builds from base   | ✅ Yes (`curMin`, `curMax`) |
# | No recursion       | ✅ Yes                      |
# | No memo/dictionary | ✅ Yes                      |
