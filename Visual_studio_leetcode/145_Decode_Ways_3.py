class Solution:
    def numDecodings(self, s: str) -> int:

        def dfs(i):
            # If reached end of string, it's a valid decoding
            if i == len(s):
                return 1
            
            # If current char is '0', invalid decode
            if s[i] == '0':
                return 0
            
            # Decode single digit
            res = dfs(i + 1)
            
            # Decode two digits if valid (between 10 and 26)
            if i + 1 < len(s) and 10 <= int(s[i:i+2]) <= 26:
                res += dfs(i + 2)
            
            return res
        
        return dfs(0)


s = "123"
print(Solution().numDecodings(s))



#  Brute Force Recursive Code (No Memoization)
 
#  | Complexity         | Value  | Reason                                         |
# | ------------------ | ------ | ---------------------------------------------- |
# | Time               | O(2^n) | Binary branching recursion without memoization |
# | Space (Call Stack) | O(n)   | Maximum depth of recursion stack               |
