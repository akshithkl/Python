class Solution(object):
    def longestAlternatingSubarray(self, nums, threshold):
        n = len(nums)
        max_len = 0

        for i in range(n):
            # Must start with even number and be within threshold
            if nums[i] % 2 == 0 and nums[i] <= threshold:
                current_len = 1
                for j in range(i + 1, n):
                    if nums[j] > threshold:
                        break
                    if nums[j] % 2 == nums[j - 1] % 2:
                        break
                    current_len += 1
                max_len = max(max_len, current_len)

        return max_len


nums = [3,2,5,4]
threshold = 5
print(Solution().longestAlternatingSubarray(nums, threshold ))

# | Metric    | Value |
# | --------- | ----- |
# | **Time**  | O(n²) |
# | **Space** | O(1)  |


# | Technique                    | Description                                                                             |
# | ---------------------------- | --------------------------------------------------------------------------------------- |
# | 🔍 **Brute Force**           | Try all possible starting indices and simulate subarray construction manually.          |
# | ➡️ **Prefix Expansion**      | For each valid starting index, move forward to see how far a valid subarray can extend. |
# | 🔁 **Parity Check (modulo)** | Use `% 2` to check for **even vs odd** alternation.                                     |
# | ⚠️ **Early Break**           | Stop expansion **early** if any condition (threshold or parity) fails.                  |
# | 🧮 **Length Tracking**       | Keep track of `current_len` and update `max_len` as we find valid subarrays.            |
