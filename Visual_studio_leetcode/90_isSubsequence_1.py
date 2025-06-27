class Solution(object):
    def isSubsequence(self, s, t):
  
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)   
     
s = "abc"
t = "ahbgdc"

sol = Solution()
print(sol.isSubsequence(s, t))    

# Time Complexity: O(n)
# where n is the length of string t (we scan it once).

# Space Complexity: O(1)
# No extra space is used, only pointers.

# Approach:
#   Two-Pointer Technique

# Algorithm Type:
#   Greedy Algorithm

# We greedily try to match characters of s in order within t, from left to right.

# Technique:
#   Linear Scan

#   Pointer Traversal

#   Character Matching