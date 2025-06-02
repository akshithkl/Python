# Back_Tracking
class Solution(object):
    def combinationSum(self, candidates, target):
        res = []
        
        def dfs(i, cur, total):
            if total == target:
                # res.append(list(cur))
                res.append(cur[:])
                return

            if i >= len(candidates) or total > target:
                return

            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            cur.pop()
            dfs(i+1, cur, total)
           
        dfs(0, [],0)
        return res

candidates = [2,3,6,7]
target = 7

sol = Solution()
print(sol.combinationSum(candidates, target))


# ✅ Time Complexity:
# O(2^T), where T = target

# In the worst case, every recursive call either includes a candidate (again) or skips to the next candidate.

# This gives a binary recursion tree, with a maximum depth proportional to the target (in the worst case, like [1,1,1,...] summing to target).

# So the number of possible combinations is exponential in target.

# 📦 Space Complexity:
# O(T) (for recursion stack)
# O(R × L) (for result list)

# Recursive stack can go as deep as target in the worst case ([1,1,1,...] up to target).

# Result list (res) stores all valid combinations:

# Let R be the number of valid combinations.

# Let L be the average length of each combination.