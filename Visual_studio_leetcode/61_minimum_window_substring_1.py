class Solution(object):
    def minWindow(self, s, t):
        
        if t == "":
            return ""
        countT = {}  # count Table in t
        window = {}  # window of the s 

        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        have = 0             # size of the s
        need = len(countT)   # size of the t
        res = [-1, -1]       # start index and end index of the result window
        resLen = float("infinity")  # lenght of the result window
        l = 0  # left pointer


        for r in range(len(s)):    # r is right pointer  =  s[l] s[l+1] ... s[r]

            c = s[r]      
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)

                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res 
        return s[l : r+1] if resLen != float("infinity") else ""  
    
       
s = "ADOBECODEBANC"
t = "ABC"
sol = Solution()
print(sol.minWindow(s,t))

# sliding window
     

# ✅ Time Complexity: O(|s| + |t|)
# Let |s| = length of string s, and |t| = length of string t.

# Breakdown:

# Building countT dictionary:

# Takes O(|t|) time.

# Sliding window loop over s:

# Each character in s is visited at most twice — once by r (right pointer) and once by l (left pointer).

# So total operations = O(2 * |s|) = O(|s|).

# Total = O(|s| + |t|)

# ✅ Space Complexity: O(|s| + |t|)
# countT stores counts of characters in t → up to O(|t|) space.

# window stores counts of characters in current window of s → worst case O(|s|) if all characters are unique.