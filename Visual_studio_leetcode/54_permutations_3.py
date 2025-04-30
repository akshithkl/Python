class Solution:
    def permute(self, nums):
        ret = []
        sol = []
        n = len(nums)
        
        def backtrack():
            if len(sol) == n:
                ret.append(sol[:])
                return
            
            for num in nums:
                if num not in sol:
                    sol.append(num)
                    backtrack()
                    sol.pop()
            
        backtrack()
        return ret
    
 
nums = [1,2,3]
sol = Solution() 
print(sol.permute(nums))

# Backtracking
# cleaner, safer, and faster for larger inputs

# Start: sol = []

# Pick 1 → sol = [1]
#     Pick 2 → sol = [1,2]
#         Pick 3 → sol = [1,2,3] (length == n) → Add [1,2,3] to ret
#     Backtrack → sol = [1]
#     Pick 3 → sol = [1,3]
#         Pick 2 → sol = [1,3,2] → Add [1,3,2] to ret
#     Backtrack → sol = [1]

# Backtrack → sol = []

# Pick 2 → sol = [2]
#     Pick 1 → sol = [2,1]
#         Pick 3 → sol = [2,1,3] → Add [2,1,3] to ret
#     Backtrack → sol = [2]
#     Pick 3 → sol = [2,3]
#         Pick 1 → sol = [2,3,1] → Add [2,3,1] to ret
#     Backtrack → sol = [2]

# Backtrack → sol = []

# Pick 3 → sol = [3]
#     Pick 1 → sol = [3,1]
#         Pick 2 → sol = [3,1,2] → Add [3,1,2] to ret
#     Backtrack → sol = [3]
#     Pick 2 → sol = [3,2]
#         Pick 1 → sol = [3,2,1] → Add [3,2,1] to ret
#     Backtrack → sol = [3]

# Backtrack → sol = []
