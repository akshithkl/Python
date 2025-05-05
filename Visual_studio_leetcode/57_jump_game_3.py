class Solution(object):
    def canJump(self, nums):
        def can_reach(position):
            if position == len(nums) - 1:
                return True  # reached the last index

            furthest_jump = min(position + nums[position], len(nums) - 1)

            for next_position in range(position + 1, furthest_jump + 1):
                if can_reach(next_position):
                    return True

            return False

        return can_reach(0)


sol = Solution()

nums = [2,3,1,1,4]

print(sol.canJump(nums))



# nums = [3,2,1,0,4]
# print(sol.canJump(nums))

#  Time Complexity: Worst case: Exponential — O(2^n)
# (because at each position you might branch into many possible jumps)

#  Space Complexity: O(n) — due to recursion stack (maximum n function calls on the call stack)

