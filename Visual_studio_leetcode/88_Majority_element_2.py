class Solution(object):
    def majorityElement(self, nums):
        freq = {}
        majority_count = len(nums) // 2

        for n in nums:
            freq[n] = freq.get(n, 0) + 1
            if freq[n] > majority_count:
                return n

nums = [2, 2, 1, 1, 1, 2, 2]
sol = Solution()
print(sol.majorityElement(nums))


# ⏱️ Time & Space Complexity:
# Time Complexity: O(n)

# Space Complexity: O(n) (for the dictionary)