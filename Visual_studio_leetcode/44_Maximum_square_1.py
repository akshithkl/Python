class Solution(object):
    def maximalSquare(self, matrix):
       
        if not matrix or not matrix[0]: 
            return 0
        
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]  
        max_side = 0  
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == '1':
                    dp[r+1][c+1] = min(dp[r][c], dp[r+1][c], dp[r][c+1]) + 1  
                    max_side = max(max_side, dp[r+1][c+1])  
                
        return max_side * max_side 
    
sol = Solution()
res = sol.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])
print(res)


#  Time Complexity: 𝑂(𝑚×𝑛)O(m×n)

#  Space Complexity: 𝑂(𝑚×𝑛)O(m×n)
# A full dp table of size (m+1) × (n+1) is used