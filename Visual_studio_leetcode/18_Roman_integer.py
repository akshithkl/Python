class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000,
            }
        
        result = 0

        for a, b in zip(s, s[1:]):
            if dict[a] < dict[b]:
                result -= dict[a]
            else:
                result += dict[a]
        
        return result + dict[s[-1]]
    
a = Solution()

b = a.romanToInt("IX")
print(b)

b = a.romanToInt("LVIII")
print(b)

b = a.romanToInt("MCMXCIV")
print(b)




# ⏱ Time Complexity:
# Iteration over string: The zip(s, s[1:]) operation iterates over n-1 adjacent pairs in the string s, where n is the length of the string.

# Time complexity of this iteration: O(n).

# Dictionary lookup: For each pair, a dictionary lookup is performed, which is O(1) for each lookup.

# Final operation: The final operation to add the value of the last character s[-1] is a constant-time operation: O(1).

# Thus, the total time complexity is:

# O(n) where n is the length of the input string s.

# 🧠 Space Complexity:
# Dictionary: The dictionary dict contains a constant number of keys (7 entries for Roman numeral characters).

# Space complexity: O(1).

# Result Variable: The result variable stores the cumulative sum, which is a constant amount of space.

# Space complexity: O(1).

# Input String: The space complexity of the input string s is O(n), but this is typically considered part of the input, so it's not counted as extra space used by the function.

# Thus, the total space complexity is:

# O(1), excluding the input space.


# ✅ Conclusion:
# Time Complexity: O(n), where n is the length of the input string s.

# Space Complexity: O(1), since we're using only a fixed amount of extra space regardless of input size.
