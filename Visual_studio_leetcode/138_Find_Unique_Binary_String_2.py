class Solution(object):
    def findDifferentBinaryString(self, nums):
        n = len(nums)
        res = []

        for i in range(n):
            # Flip the i-th bit of the i-th string
            if nums[i][i] == '0':
                res.append('1')
            else:
                res.append('0')

        return ''.join(res)


nums = ["011","000","001"]
print(Solution().findDifferentBinaryString(nums))

# | Aspect               | Value             |
# | -------------------- | ----------------- |
# | **Algorithm**        | Greedy / Diagonal |
# | **Approach**         | Cantor's diagonal |
# | **Time Complexity**  | `O(n)`            |
# | **Space Complexity** | `O(n)`            |
