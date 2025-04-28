class Solution(object):
    def permute(self, nums):
    
        result = []

        if (len(nums) == 1):
            return [nums[:]]
        
        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)

            for perm in perms:
                perm.append(n)
            result.extend(perms)
            nums.append(n)
        return result
      
nums = [1,2,3]
sol = Solution() 
print(sol.permute(nums))

# Backtracking


# Start: [1,2,3]

# Pick 1 → Remaining [2,3]
#     Pick 2 → Remaining [3]
#         Pick 3 → Remaining []
#             => [3] → append 2 → [3,2] → append 1 → [3,2,1]
#     Pick 3 → Remaining [2]
#         Pick 2 → Remaining []
#             => [2] → append 3 → [2,3] → append 1 → [2,3,1]

# Pick 2 → Remaining [1,3]
#     Pick 1 → Remaining [3]
#         Pick 3 → Remaining []
#             => [3] → append 1 → [3,1] → append 2 → [3,1,2]
#     Pick 3 → Remaining [1]
#         Pick 1 → Remaining []
#             => [1] → append 3 → [1,3] → append 2 → [1,3,2]

# Pick 3 → Remaining [1,2]
#     Pick 1 → Remaining [2]
#         Pick 2 → Remaining []
#             => [2] → append 1 → [2,1] → append 3 → [2,1,3]
#     Pick 2 → Remaining [1]
#         Pick 1 → Remaining []
#             => [1] → append 2 → [1,2] → append 3 → [1,2,3]
