class Solution(object):
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(string):
            stack = []
            for char in string:
                if char != '#':
                    stack.append(char)
                elif stack:
                    stack.pop()
            return stack

        return build(s) == build(t)

s = "ab#c"
t = "ad#c"   
sol = Solution()
print(sol.backspaceCompare(s, t))  # Output: True


# | **Metric**           | **Value**                  |
# | -------------------- | -------------------------- |
# | **Time Complexity**  | O(n + m)                   |
# | **Space Complexity** | O(n + m) (for both stacks) |


# | **Aspect**     | **Details**                        |
# | -------------- | ---------------------------------- |
# | **Approach**   | Brute-force using stack            |
# | **Technique**  | Simulation, Stack-based processing |
# | **Algorithm**  | Stack Simulation                   |
# | **Complexity** | Time: O(n + m), Space: O(n + m)    |
