class Solution(object):
    def minWindow(self, s, t):
        if t == "":
            return ""

        def count_chars(string):
            count = {}
            for c in string:
                count[c] = count.get(c, 0) + 1
            return count

        def contains_all(sub_count, t_count):
            for c in t_count:
                if c not in sub_count or sub_count[c] < t_count[c]:
                    return False
            return True

        t_count = count_chars(t)
        min_len = float('inf')
        result = ""

        for i in range(len(s)):
            for j in range(i, len(s)):
                substring = s[i:j+1]
                sub_count = count_chars(substring)
                if contains_all(sub_count, t_count):
                    if (j - i + 1) < min_len:
                        min_len = j - i + 1
                        result = substring

        return result
    
sol = Solution()
print(sol.minWindow("ADOBECODEBANC", "ABC"))  # Output: "BANC"



# brute force without using library

# ⏱️ Time and Space Complexity of Brute-Force:
# Time Complexity:

# There are O(n^2) substrings.

# For each substring, we count characters: O(n)

# And compare with target count: O(1) (since max 26–128 characters)

# So total = O(n^3) worst-case.

# Space Complexity:

# Character count dictionaries for each substring → O(n)

# So worst-case space = O(n)

