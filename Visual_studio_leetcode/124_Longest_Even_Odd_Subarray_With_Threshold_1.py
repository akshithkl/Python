class Solution(object):
    def longestAlternatingSubarray(self, nums, threshold):
        max_len = 0
        i = 0

        while i < len(nums):
            if nums[i] % 2 == 0 and nums[i] <= threshold:
                j = i
                while j < len(nums) and nums[j] <= threshold and(j == i or nums[j] % 2 != nums[j - 1] % 2):
                    j += 1
                max_len = max(max_len, j - i)
                i = j  # skip to next potential start
            else:
                i += 1

        return max_len

nums = [3,2,5,4]
threshold = 5
print(Solution().longestAlternatingSubarray(nums, threshold ))

# Time: O(n) — we scan the list once.
# Space: O(1) — only variables used, no extra space.

# | Technique            | Description                                                               |
# | -------------------- | ------------------------------------------------------------------------- |
# | **Two Pointers**     | Used to define the window `[i, j]` and expand/shrink it as needed.        |
# | **Sliding Window**   | Simulates continuous checking of a subarray while maintaining conditions. |
# | **Modulo Operation** | To check **even** (`x % 2 == 0`) or **odd** (`x % 2 == 1`).               |
# | **Greedy Expansion** | Expand the window as long as all conditions are satisfied.                |
