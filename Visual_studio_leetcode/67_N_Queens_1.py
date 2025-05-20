#  BackTracking
class Solution:
    def solNqueens(self, n: int):
        
        col = set()
        PostivDiago = set()
        NegDiago = set()
        
        res = []
        board = [["."]*n for i in range(n)]
        
        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                if c in col or (r + c) in PostivDiago or (r - c) in NegDiago:
                    continue
                
                col.add(c)
                PostivDiago.add(r + c)
                NegDiago.add(r - c)
                board[r][c] = "Q"
                
                backtrack(r + 1)
                
                
                col.remove(c)
                PostivDiago.remove(r + c)
                NegDiago.remove(r - c)
                board[r][c] = "."
        backtrack(0)
        return res
                
            
n = 4
sol = Solution()
print(sol.solNqueens(n))


# o/p
#  1.posibble                         2.posibble   
# [['.Q..', '...Q', 'Q...', '..Q.'], ['..Q.', 'Q...', '...Q', '.Q..']]

# | Metric           | Complexity   |
# | ---------------- | ------------ |
# | Time Complexity  | O(N! + S·N²) |
# | Space Complexity | O(S·N²)      |



# ✅ Time Complexity: O(N!)
# The N-Queens problem involves placing one queen in each row such that no two queens attack each other.

# At each row, you try placing the queen in any of the N columns, but due to constraints (no two queens can be in the same column or diagonal), you prune many branches.

# In the worst case, for the first row you try N positions, for the second row you try N - 1 (approx) positions, and so on.

# So the time complexity is: 𝑂(𝑁×(𝑁−1)×(𝑁−2)…1)=𝑂(𝑁!)O(N×(N−1)×(N−2)…1)=O(N!)
# Additionally, for each valid configuration, you're creating a copy of the board using:


# copy = ["".join(row) for row in board]
# This copying takes O(N^2) time for each solution, and there can be multiple such solutions (though the number is ≤ N!).

# So final time complexity (in worst case):O(𝑁!+𝑆⋅𝑁2)O(N!+S⋅N 2)
# Where S is the number of valid solutions.

# ✅ Space Complexity: O(N^2)
# You use:

# A board of size N x N: O(N²)

# Three sets (col, PostivDiago, NegDiago): each of size at most N: O(N)

# The recursion stack depth can go up to N (since you go one row deeper at each recursive call): O(N)

# The result list res, which stores all valid boards. Each board is of size N x N, and there can be up to O(N!) solutions (e.g., N = 8 has 92 solutions). So total space for results = O(S·N²)

# So final space complexity: 𝑂(𝑁2+𝑆⋅𝑁2)=𝑂(𝑆⋅𝑁2)O(N 2+S⋅N 2)=O(S⋅N 2)
