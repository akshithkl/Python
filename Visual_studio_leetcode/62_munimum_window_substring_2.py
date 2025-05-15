class Solution(object):
    def minWindow(self, s, t):
        from collections import Counter

        if not s or not t:
            return ""

        countT = Counter(t)
        min_len = float("inf")
        res = ""

        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                window = s[i:j]
                windowCount = Counter(window)

                if all(windowCount[c] >= countT[c] for c in countT):
                    if (j - i) < min_len:
                        min_len = j - i
                        res = window

        return res


s ="ADOBECODEBANC"
t = "ABC"
sol = Solution()
print(sol.minWindow(s,t))


#  Bruteforce


# 🕒 Time Complexity: O(n^3)
# Outer loop: O(n)

# Inner loop: O(n)

# Counter(window) → O(n) in worst case

# Comparison with countT → O(k) (k = unique characters in t)

# So total worst-case: O(n^3)

# 📦 Space Complexity: O(n + k)
# windowCount: at most O(n)

# countT: O(k) where k = len(t)