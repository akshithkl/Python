class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cleaned = ""
        for char in s:
            if ('a' <= char <= 'z') or ('A' <= char <= 'Z') or ('0' <= char <= '9'):
                # Convert uppercase to lowercase manually
                if 'A' <= char <= 'Z':
                    char = chr(ord(char) + 32)
                cleaned += char

        reversed_str = ""
        for i in range(len(cleaned) - 1, -1, -1):
            reversed_str += cleaned[i]

        return cleaned == reversed_str

s = "A man, a plan, a canal: Panama"

sol = Solution()
print(sol.isPalindrome(s))

# | Metric | Value              |
# | ------ | ------------------ |
# | Time   | O(n)               |
# | Space  | O(n) (new strings) |


# | Step                | Method               |
# | ------------------- | -------------------- |
# | Clean string        | Character filtering  |
# | Manual lowercase    | ASCII manipulation   |
# | Reversal comparison | String reversal loop |
