class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]
        
        res = []
        for i in range(len(nums)):
            # Take current number and fix it at first position
            curr = nums[i]
            remaining = nums[:i] + nums[i+1:]  # remove the chosen element
            # Get all permutations of the remaining
            for p in self.permute(remaining):
                res.append([curr] + p)  # Add current number in front
        return res

# Example usage
nums = [1, 2, 3]
print(Solution().permute(nums))



# permute([1,2,3])
#     fix 1 → permute([2,3])
#         fix 2 → permute([3])
#             return [ [3] ]
#             => [2] + [3] = [2,3]
#         fix 3 → permute([2])
#             return [ [2] ]
#             => [3] + [2] = [3,2]
#         => combine: [ [2,3], [3,2] ]
#         => add 1 at front:
#             [1,2,3], [1,3,2]

#     fix 2 → permute([1,3])
#         fix 1 → permute([3])
#             return [ [3] ]
#             => [1] + [3] = [1,3]
#         fix 3 → permute([1])
#             return [ [1] ]
#             => [3] + [1] = [3,1]
#         => combine: [ [1,3], [3,1] ]
#         => add 2 at front:
#             [2,1,3], [2,3,1]

#     fix 3 → permute([1,2])
#         fix 1 → permute([2])
#             return [ [2] ]
#             => [1] + [2] = [1,2]
#         fix 2 → permute([1])
#             return [ [1] ]
#             => [2] + [1] = [2,1]
#         => combine: [ [1,2], [2,1] ]
#         => add 3 at front:
#             [3,1,2], [3,2,1]
