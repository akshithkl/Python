class Solution(object):
    def rob(self, nums):
        
        rob1, rob2 = 0, 0

        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
    
nums = [2,7,9,3,1, 8]
    
sol = Solution()
print(sol.rob(nums))


# Dynamic programing Bottom-Up (Tabulation)

#  time complexity : O(n)
# space complexity : O(1)

#  the answer is 19 becase
# Rob house 0 (2)

# Rob house 2 (9)

# Rob house 5 (8)

#  it jum 2 step or more very heighest value there but dont got one step

# | Attribute      | Description                                        |
# | -------------- | -------------------------------------------------- |
# | **Algorithm**  | **Dynamic Programming**                            |
# | **Approach**   | **Bottom-Up (Tabulation)**                         |
# | **Technique**  | **Space-Optimized DP** using two variables         |
# | **Pattern**    | **Maximum Non-Adjacent Sum**                       |
# | **Time**       | `O(n)`                                             |
# | **Space**      | `O(1)`                                             |
# | **Strengths**  | Fast, clean, optimal space                         |
# | **Weaknesses** | No recursion insight; harder to trace step-by-step |
