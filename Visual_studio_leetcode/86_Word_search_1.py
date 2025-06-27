class Solution(object):
    def exist(self, board, word):
        rows = len(board)
        cols = len(board[0])                     
        path = set()  
                                                             
        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or r >= rows or c >= cols or word[i] != board[r][c] or (r, c) in path):               
                return True
            
            path.add((r, c))
            res = (
                   dfs(r+1, c, i+1) or
                   dfs(r-1, c, i+1) or
                   dfs(r, c+1, i+1) or
                   dfs(r, c-1, i+1))
            path.remove((r,c))
            return res
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0):  #Try to find the word starting from position (r, c)
                    return False
        return False

board = [["W","A","B","D"],
         ["S","A","B","C"],
         ["A","D","E","C"]]

word = "ABCCED"

sol = Solution()
print(sol.exist(board, word))

# board = [["W","A","B","C"],
#          ["S","F","D","C"],
#          ["A","D","D","E"]]



#         | Type             | Complexity         |
# | ---------------- | ------------------ |
# | Time Complexity  | **O(m × n × 4^L)** |
# | Space Complexity | **O(L)**           |


# Time Complexity:
# Let:

# m = number of rows (rows)

# n = number of columns (cols)

# L = length of the word (len(word))


# Space Complexity:
# Recursion depth = L (the length of the word).

# path set stores up to L positions.

# So, auxiliary space used = O(L).

# If you also consider the input board itself, space used is:

# O(L) (for recursion stack and path set)



