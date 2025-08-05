class Solution(object):
    def minCostClimbingStairs(self, cost):
        a, b = 0, 0
        
        for i in range(2, len(cost) + 1):
            a, b = b, min(b + cost[i - 1], a + cost[i - 2])
        return b
    
cost = [10, 15, 20, 25, 10]
print(Solution().minCostClimbingStairs(cost))


# cost = [1,100,1,1,1,100,1,1,100,1]
# print(Solution().minCostClimbingStairs(cost))  # Output: 15

    
# | Item                 | Value                                  |
# | -------------------- | -------------------------------------- |
# | **Algorithm**        | Dynamic Programming                    |
# | **Approach**         | Bottom-Up Tabulation                   |
# | **Technique**        | State Transition, Optimal Substructure |
# | **Time Complexity**  | O(n)                                   |
# | **Space Complexity** | O(1) (optimized)               |
