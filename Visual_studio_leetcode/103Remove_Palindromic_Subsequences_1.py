class Solution(object):
    def removePalindromeSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        def is_palindrome(s):
            left = 0
            right = len(s) - 1
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        if len(s) == 0:
            return 0
        if is_palindrome(s):
            return 1
        return 2

s = "abb"  
sol = Solution()
print(sol.removePalindromeSub(s))

# | Item          | Details                                                      |
# | ------------- | ------------------------------------------------------------ |
# | **Algorithm** | Greedy                                                       |
# | **Approach**  | 2-pointer palindrome check + optimal character group removal |
# | **Technique** | Manual string comparison (no built-in reversal)              |
# | **Time**      | O(n)                                                         |
# | **Space**     | O(1) (only variables `left` and `right`)                     |
