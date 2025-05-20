class Solution:
    def solNqueens(self, n: int):
        res = []

        def is_valid(perm):
            for i in range(len(perm)):
                for j in range(i + 1, len(perm)):
                    # Check if queens are on the same diagonal
                    if abs(i - j) == abs(perm[i] - perm[j]):
                        return False
            return True

        def permute(arr, l, r):
            if l == r:
                if is_valid(arr):
                    board = []
                    for i in range(n):
                        row = ["." for _ in range(n)]
                        row[arr[i]] = "Q"
                        board.append("".join(row))
                    res.append(board)
            else:
                for i in range(l, r + 1):
                    arr[l], arr[i] = arr[i], arr[l]
                    permute(arr, l + 1, r)
                    arr[l], arr[i] = arr[i], arr[l]  # backtrack

        # Start with a list of columns [0, 1, 2, ..., n-1]
        permute(list(range(n)), 0, n - 1)

        return res


# Example usage:
n = 4
sol = Solution()
for solution in sol.solNqueens(n):
    for row in solution:
        print(row)
    print()


# | Metric           | Complexity      |
# | ---------------- | --------------- |
# | Time Complexity  | `O(n! · n²)`    |
# | Space Complexity | `O(S · n² + n)` |
