class Solution(object):
    def minimumTotal(self, triangle):
        dp = [0] * (len(triangle) + 1)
        for row in triangle[::-1]:
            for i, n in enumerate(row):
                dp[i] = n + min(dp[i], dp[i+1])
        return dp[0]

triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]

sol = Solution()
result = sol.minimumTotal(triangle)
print(result)


# Dynamic programing

# | Metric           | Value |
# | ---------------- | ----- |
# | Time Complexity  | O(n²) |
# | Space Complexity | O(n)  |

# ⏰ Time Complexity: O(n^2)
# Let n be the number of rows in the triangle.

# The total number of elements in a triangle with n rows is:1+2+3+⋯+𝑛=𝑛(𝑛+1)21+2+3+⋯+n = 2n(n+1) / 2
# ​
 
# The outer loop iterates through all rows (n rows).

# The inner loop iterates through each element in the row (up to n elements in the bottom row).

# Thus, the total number of operations is proportional to the number of elements in the triangle:
# O(n²)

# 💾 Space Complexity: O(n)
# The dp list is of size n+1 (where n is the number of rows).

# No extra 2D matrix is used—just a 1D array for space optimization.

# Hence, space complexity is: O(n)

