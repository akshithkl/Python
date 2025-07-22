class Solution(object):
    def permuteUnique(self, nums):
        res = []
        
        def backtrack(start):
            if start == len(nums):
                res.append(nums[:])  # Make a copy of current permutation
                return
            
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]  # Swap
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]  # Swap back (backtrack)
        
        backtrack(0)

        # Remove duplicates using a set of tuples
        unique = set()
        final_result = []
        for perm in res:
            t = tuple(perm)
            if t not in unique:
                unique.add(t)
                final_result.append(perm)
        
        return final_result

s = Solution()
print(s.permuteUnique([1, 1, 2]))


# | Type        | Complexity    | Reason                                                |
# | ----------- | ------------- | ----------------------------------------------------- |
# | Time        | **O(n! × n)** | Generates `n!` permutations, filters duplicates       |
# | Space (res) | **O(n! × n)** | Stores all permutations (with and without duplicates) |
# | Space (set) | **O(n! × n)** | Set for removing duplicates                           |
