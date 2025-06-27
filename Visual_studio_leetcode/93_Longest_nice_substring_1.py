class Solution(object):
    def longestNiceSubstring(self, s):
        if len(s) < 2:
            return ""

        charset = set(s)
        for i, ch in enumerate(s):
            if ch.swapcase() not in charset:
                left = self.longestNiceSubstring(s[:i])
                right = self.longestNiceSubstring(s[i+1:])
                return left if len(left) >= len(right) else right

        return s


s = "aAbBcCdD"        # Output: "aAbBcCdD"
    
sol = Solution()
print(sol.longestNiceSubstring(s))

s = "YazaAay"         # Output: "aAa"   
sol = Solution()
print(sol.longestNiceSubstring(s))


# | Aspect    | Complexity |
# | --------- | ---------- |
# | **Time**  | O(n²)      |
# | **Space** | O(n)       |

# Time Complexity: O(n²)
# At each level of recursion, we may split the string around a character and recurse on two substrings.

# In the worst case, the split happens one character at a time (like quicksort with worst pivot), creating O(n) recursive calls.

# Each call creates a new substring of size up to O(n), and constructing set(s) takes O(n) time.

# Thus, the total time is bounded by:

# T(n) = T(k) + T(n-k-1) + O(n) \Rightarrow O(n^2)
# ]

# 📦 Space Complexity: O(n)
# Recursive call stack: Can go up to depth O(n) in the worst case.

# Set used in each call takes O(n) space.

# Substring creation (s[:i], s[i+1:]) also takes O(n) space overall (not reused).

# So, the total auxiliary space is O(n) (stack + set + substring).

