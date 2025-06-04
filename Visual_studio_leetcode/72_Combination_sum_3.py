class Solution(object):
    def combinationSum(self, candidates, target):
        res = []
        stack = [(0, [], 0)]  # (index, current_combination, current_sum)

        while stack:
            i, cur, total = stack.pop()

            if total == target:
                res.append(cur)
                continue
            if i >= len(candidates) or total > target:
                continue

            # include candidates[i]
            stack.append((i, cur + [candidates[i]], total + candidates[i]))
            # exclude candidates[i]
            stack.append((i + 1, cur, total))

        return res


candidates = [2,3,6,7]
target = 7

sol = Solution()
print(sol.combinationSum(candidates, target))

#  this is not preferable