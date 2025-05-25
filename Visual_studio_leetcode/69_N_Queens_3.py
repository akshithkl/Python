class Solution:
    def solNqueens(self, n: int):
        # Variables to hold results and current state
        res = []
        board = [["."] * n for _ in range(n)]
        col = set()
        pos_diag = set()  # r + c
        neg_diag = set()  # r - c

        # Use an explicit stack to simulate recursion
        stack = [(0, col.copy(), pos_diag.copy(), neg_diag.copy(), [row[:] for row in board])]

        while stack:
            r, c_set, p_set, n_set, b = stack.pop()

            if r == n:
                res.append(["".join(row) for row in b])
                continue

            for c in range(n):
                if c in c_set or (r + c) in p_set or (r - c) in n_set:
                    continue

                # Copy current state
                new_col = c_set.copy()
                new_pos_diag = p_set.copy()
                new_neg_diag = n_set.copy()
                new_board = [row[:] for row in b]

                # Place queen
                new_col.add(c)
                new_pos_diag.add(r + c)
                new_neg_diag.add(r - c)
                new_board[r][c] = "Q"

                # Move to next row
                stack.append((r + 1, new_col, new_pos_diag, new_neg_diag, new_board))

        return res


# Test
sol = Solution()
print(sol.solNqueens(4))
