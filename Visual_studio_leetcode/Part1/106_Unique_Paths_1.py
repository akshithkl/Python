class Solution(object):
    def uniquePaths(self, m, n):
        row  = [1] * n

        for i in range(m-1):
            newRow = [1] * n
            for j in range(n-2, -1, -1):
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow
        return row[0]

m = 3
n = 7

sol = Solution()
print(sol.uniquePaths(3, 7))

# | Feature              | Value                                     |
# | -------------------- | ----------------------------------------- |
# | **Algorithm**        | Dynamic Programming                       |
# | **Technique**        | Bottom-Up Tabulation + Space Optimization |
# | **Time Complexity**  | O(m × n)                                  |
# | **Space Complexity** | O(n)                                      |

# 📖 Explanation:
# In a 3x7 grid, the robot must make:

# 2 moves down

# 6 moves right

# Total moves = 8
# Choose any 2 of those 8 moves to be "down" (or 6 to be "right"):


# Unique Paths=( 8 / 2 ​ )=28
