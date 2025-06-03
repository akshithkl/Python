
class Solution(object):
    def combinationSum(self, candidates, target):
        self.res = []
        self.helper(candidates, target, [], 0)
        return self.res

    def helper(self, candidates, target, path, index):
        current_sum = self.sum_list(path)
        if current_sum == target:
            self.res.append(path[:])
            return
        if current_sum > target:
            return

        for i in range(index, len(candidates)):
            path.append(candidates[i])
            self.helper(candidates, target, path, i)  # use same index again (unlimited usage)
            path.pop()

    def sum_list(self, lst):
        total = 0
        for num in lst:
            total += num
        return total

candidates = [2,3,6,7]
target = 7

sol = Solution()
print(sol.combinationSum(candidates, target))

# 🕒 Time Complexity (Brute-force):
# Time: Exponential → O(2^T) where T = target

# Space: Also exponential (due to recursion + result storage)


