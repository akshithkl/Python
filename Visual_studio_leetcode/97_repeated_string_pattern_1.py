class Solution(object):
    def repeatedSubstringPattern(self, s):
 
        n = len(s)

        for l in range(1, n // 2 + 1):
            if n % l == 0:
                match = True
                # Check if repeating s[0:l] forms the full string
                for i in range(l, n):
                    if s[i] != s[i % l]:
                        match = False
                        break
                if match:
                    return True
        return False

s = "abab"
sol = Solution()
print(sol.repeatedSubstringPattern(s))

# Time Complexity:
# Worst-case O(n^2) (when checking all factors and comparing character by character)

# Space Complexity: O(1)


#| **Aspect**             | **Details**                                                                  |
# | ---------------------- | ---------------------------------------------------------------------------- |
# | **Problem**            | Check if string `s` is formed by repeating a substring                       |
# | **Algorithm Type**     | Brute-force with optimization                                                |
# | **Main Technique**     | Pattern matching using modulo indexing (`s[i] == s[i % l]`)                  |
# | **Approach**           | Try all substring lengths `l` from `1` to `n // 2` and check match           |
# | **Loop Condition**     | Only check when `len(s) % l == 0` (substring must divide full length evenly) |
# | **Simulation Style**   | Character-by-character comparison without constructing new strings           |
# | **Optimization**       | Early exit when match found                                                  |
# | **Time Complexity**    | Worst-case `O(n²)`                                                           |
# | **Space Complexity**   | `O(1)` (no extra space used)                                                 |
# | **Used for**           | String pattern detection / substring repetition problems                     |
# | **Alternative Method** | KMP Algorithm (O(n)) or `(s + s)[1:-1]` trick (O(n))                         |
