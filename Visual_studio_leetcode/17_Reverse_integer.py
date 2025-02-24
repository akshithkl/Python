class Solution:
    def reverse(self, x: int) -> int:
        isNegative = False
        if x < 0:
            isNegative = True
            x = -x
        
        s = str(x)
        reversedString = ''

        for i in reversed(range(len(s))):
            reversedString += s[i]
        
        reversedInt = int(reversedString)

        if isNegative:
             reversedInt = -reversedInt
        
        if  reversedInt < -2**31 or  reversedInt > 2**31 - 1:
            return 0
        
        return reversedInt

a = Solution()
B = a.reverse(-123)
print(B)