class Solution:
    def subsets(self, nums):
        n = len(nums)
        res = []
        total = 1 << n  # 2^n subsets

        for mask in range(total):
            subset = []
            for i in range(n):
                if mask & (1 << i):  # if i-th bit is 1, include nums[i]
                    subset.append(nums[i])
            res.append(subset)

        return res
nums = [1, 2, 3]

print(Solution().subsets(nums))

# Bruteforce

# | Type                | Complexity           |
# | ------------------- | -------------------- |
# | **Time**            | `O(2^n * n)`         |
# | **Space (output)**  | `O(2^n * n)`         |
# | **Auxiliary Space** | `O(n)` per iteration |
