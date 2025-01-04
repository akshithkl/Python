 
class Solution:
    def Simple_Palindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

a = Solution()

user_input = input("Type....Any words : ")

c = a.Simple_Palindrome(user_input )

print(f' The user input is "{user_input}" ,It is Palindrome = {c}')        
