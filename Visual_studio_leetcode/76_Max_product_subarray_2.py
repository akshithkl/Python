class Solution(object):
    def maxProduct(self, nums):
        max_product = float('-inf')
        
        for i in range(len(nums)):
            product = 1
            for j in range(i, len(nums)):
                product *= nums[j]              # Calculate product from i to j
                max_product = max(max_product, product)  # Update result
                
        return max_product


nums = [2,3,-2,4]
sol = Solution()
print(sol.maxProduct(nums))

nums = [-2,0,-1]
sol = Solution()
print(sol.maxProduct(nums))


# 📊 Time and Space Complexity:
# Time: O(n²) — nested loop over all subarrays

# Space: O(1) — constant extra space used