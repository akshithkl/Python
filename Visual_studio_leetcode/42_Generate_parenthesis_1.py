class Solution(object):
    def generateParenthesis(self, n):
        stack = []
        res = [] 

        def backtrack(open_pth, closed_pth):
            if open_pth == closed_pth == n:
                res.append("".join(stack))
                return
            
            if open_pth < n:
                stack.append("(")
                backtrack(open_pth + 1, closed_pth)
                stack.pop()
            
            if closed_pth < open_pth:
                stack.append(")")
                backtrack(open_pth, closed_pth + 1)
                stack.pop()
        
        backtrack(0, 0)
        return res

a = Solution()
print(a.generateParenthesis(3))