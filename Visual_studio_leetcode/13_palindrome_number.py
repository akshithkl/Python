 
class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False
        revers_num = 0
        y = x

        while x > 0:
            reminder = x % 10
            revers_num = revers_num * 10 + reminder
            x = x // 10

        if y == revers_num:
            return True
        else:
            return False
        
final = Solution()

print(final.isPalindrome(12321))