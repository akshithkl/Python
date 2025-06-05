class Solution(object):
    def addOperators(self, num, target):
        result = []

        def backtrack(index, path, evaluated, multed):
            if index == len(num):
                if evaluated == target:
                    result.append(path)
                return

            for i in range(index, len(num)):
               
                if i != index and num[index] == '0':
                    break

                current_str = num[index:i+1]
                current = int(current_str)

                if index == 0:
                   
                    backtrack(i+1, current_str, current, current)
                else:
                    backtrack(i+1, path + "+" + current_str, evaluated + current, current)

                    backtrack(i+1, path + "-" + current_str, evaluated - current, -current)
                    backtrack(i+1, path + "*" + current_str,
                              evaluated - multed + multed * current,
                              multed * current)

        backtrack(0, "", 0, 0)
        return result


s = Solution()
print(s.addOperators("123", 6))       # ["1+2+3", "1*2*3"]
# print(s.addOperators("232", 8))       # ["2*3+2", "2+3*2"]
# print(s.addOperators("105", 5))       # ["1*0+5","10-5"]
# print(s.addOperators("00", 0))        # ["0+0", "0-0", "0*0"]
# print(s.addOperators("3456237490", 9191))  # []


#  Back tracking

# ✅ Time Complexity: O(4ⁿ)
# In the worst case, for a string of length n, at each digit, we can either:

# split or not split (which gives 2ⁿ ways),

# and for each split part (number), we try 3 operators: +, -, *.

# So total combinations: 3^(n−1) or 4ⁿ (since some parts may skip operators due to leading zero constraints).

# Thus, the time complexity is exponential in the number of digits.

# Worst-case upper bound: O(4ⁿ)
# But often less due to:

# Skipping invalid numbers with leading zeros (like "05").

# Pruning branches that can't possibly reach the target.

# ✅ Space Complexity: O(n)
# The maximum depth of the recursion stack is O(n) (the length of the input num).

# At each step, we build strings (path), which take up O(n) space per call.

# So the space complexity is O(n) (excluding output).

# ✅ Output Space: O(k * n)
# Where:

# k = number of valid expressions found,

# n = average length of each expression.

# This is additional and depends on how many valid expressions match the target.

# Summary:
# Aspect	Complexity
# Time Complexity	O(4ⁿ)
# Space Complexity	O(n)
# Output Size	O(k * n)
