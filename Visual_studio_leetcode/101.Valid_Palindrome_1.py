class Solution(object):
    def isPalindrome(self, s):
        def is_alphanumeric(c):
            return ('a' <= c <= 'z') or ('A' <= c <= 'Z') or ('0' <= c <= '9')
        
        def to_lower(c):
            if 'A' <= c <= 'Z':
                return chr(ord(c) + 32)
            return c

        left, right = 0, len(s) - 1

        while left < right:
            while left < right and not is_alphanumeric(s[left]):
                left += 1
            while left < right and not is_alphanumeric(s[right]):
                right -= 1

            if to_lower(s[left]) != to_lower(s[right]):
                return False

            left += 1
            right -= 1

        return True
    
s = "A man, a plan, a canal: Panama"

sol = Solution()
print(sol.isPalindrome(s))


# | Metric | Value           |
# | ------ | --------------- |
# | Time   | O(n)            |
# | Space  | O(1) (in-place) |


# | Aspect        | Details                              |
# | ------------- | ------------------------------------ |
# | **Technique** | Two Pointers                         |
# | **Approach**  | Skip non-alphanumeric, compare ends  |
# | **Pattern**   | Two-pointer string scan (left–right) |
