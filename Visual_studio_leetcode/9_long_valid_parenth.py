class Solution:
    @staticmethod
    def longestValidParentheses(s):
        left = 0
        right = 0
        max_length = 0

        # Left to right scan
        for x in s:
            if x == '(':
                left += 1
            else:
                right += 1
            
            if left == right:
                max_length = max(max_length, left + right)
            elif right > left:
                left = right = 0

        left = right = 0

        # Right to left scan
        for x in reversed(s):
            if x == '(':
                left += 1
            else:
                right += 1
            
            if left == right:
                max_length = max(max_length, left + right)
            elif left > right:
                left = right = 0
        
        return max_length



s = input("Enter the string: ").strip()
t
if set(s) - {'(', ')'}:
    print("Please enter a valid string containing only '(' and ')'.")
else:

    result = Solution.longestValidParentheses(s)
    print("The length of the longest valid parentheses substring is:", result)
