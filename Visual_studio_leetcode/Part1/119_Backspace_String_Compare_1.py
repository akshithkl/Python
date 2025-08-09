class Solution(object):
    def backspaceCompare(self, s, t):

        def process(string):
            stack = []
            for char in string:
                if char == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(char)
            return stack
        
        return process(s) == process(t)

s = "ab#c"
t = "ad#c"   
sol = Solution()
print(sol.backspaceCompare(s, t))
    
    

# | **Aspect**            | **Details**                                                               |
# | --------------------- | ------------------------------------------------------------------------- |
# | **Algorithm**         | Stack Simulation                                                          |
# | **Approach**          | Simulate typing in a text editor using a stack                            |
# | **Technique**         | - Stack-based traversal  <br> - String processing <br> - Simulation       |
# | **Time Complexity**   | O(n + m), where `n` = len(s), `m` = len(t)                                |
# | **Space Complexity**  | O(n + m) for storing the processed characters in stacks                   |
# | **Optimized Version** | Two Pointer Technique (from end to start, skipping backspaced characters) |
# | **Optimized Space**   | O(1) — no extra stack, just counters and pointers                         |

