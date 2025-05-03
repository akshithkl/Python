class Solution(object):
    def canJump(self, nums):
        maxReach = 0

        for i in range(len(nums)):
            if i > maxReach:
                return False  # Can't reach this position
            maxReach = max(maxReach, i + nums[i])  # Update farthest reachable index

        return True


sol = Solution()

nums = [2,3,1,1,4]

print(sol.canJump(nums))

nums = [3,2,1,0,4]
print(sol.canJump(nums))

# nums = [1] * 9999 + [0]
# print(sol.canJump(nums))

#  forward greedy

# ⏱️ Time Complexity:
# O(n) — One pass through the array.

# 📦 Space Complexity:
# O(1) — Only one variable maxReach used.

#  Forward Greedy is generally better in practice because:

# It can exit early if you hit an unreachable index.

# It's intuitive when solving "How far can I go?"