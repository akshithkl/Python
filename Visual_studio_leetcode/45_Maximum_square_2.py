# Brute Force Approac

class Solution(object):
    def maximalSquare(self, matrix):
        
        if not matrix or not matrix[0]: 
            return 0
        
        rows, cols = len(matrix), len(matrix[0])
        max_side = 0  # Store the max side length of a square

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == '1':  # Found a potential square
                    side_length = 1  # Minimum square size is 1x1
                    is_valid = True  # Flag to check if square is valid
                    
                    # Try increasing the square size
                    while (r + side_length < rows) and (c + side_length < cols) and is_valid:
                        # Check new row and column
                        for k in range(side_length + 1):
                            if matrix[r + side_length][c + k] != '1' or matrix[r + k][c + side_length] != '1':
                                is_valid = False
                                break
                        
                        if is_valid:
                            side_length += 1  # Increase square size
                    
                    max_side = max(max_side, side_length)  # Update max square side length

        return max_side * max_side  # Return area of the largest square



sol = Solution()
res = sol.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])
print(res)

# Time Complexity: 𝑂(𝑚2×𝑛2)O(m 2×n 2)
# Space Complexity: 𝑂(1)O(1)