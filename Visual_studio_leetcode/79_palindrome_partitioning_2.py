#  Bruteforce

class Solution(object):
    def partition(self, s):
        from itertools import product
        n = len(s)
        res = []

        # There are (n-1) places to cut between characters
        # Generate all binary masks of length (n-1)
        for cut_mask in product([0, 1], repeat=n-1):
            partition = []
            last = 0
            for i in range(n-1):
                if cut_mask[i]:  # cut here
                    partition.append(s[last:i+1])
                    last = i+1
            partition.append(s[last:])  # append last segment

            # Check if all parts are palindromes
            if all(self.isPalindrome(part) for part in partition):
                res.append(partition)
        return res

    def isPalindrome(self, s):
        return s == s[::-1]

sol = Solution()
print(sol.partition("aab"))


# | Metric                | Complexity           | Explanation                             |
# | --------------------- | -------------------- | --------------------------------------- |
# | **Time**              | `O(2^(n-1) * n)`     | `2^(n-1)` partitions, `O(n)` per check  |
# | **Palindrome check**  | `O(n)` per partition | Each substring is checked individually  |
# | **Space (result)**    | `O(n * 2^n)`         | Similar to optimized (stores all valid) |
# | **Space (temp vars)** | `O(n)`               | For partitions and substring building   |
