class Solution(object):
    def reverseString(self, s):
    
        left, right = 0, len(s) - 1
        while left < right:
            # Swap the characters
            s[left], s[right] = s[right], s[left]
            # Move pointers
            left += 1
            right -= 1
      
s = ["h", "e", "l", "l", "o"]
Solution().reverseString(s)
print(s)  # → ['o', 'l', 'l', 'e', 'h']



# | Aspect        | Description                   |
# | ------------- | ----------------------------- |
# | **Algorithm** | Two-Pointer                   |
# | **Approach**  | In-Place Swapping             |
# | **Technique** | Two-Pointer, In-Place, Greedy |
# | **Time**      | O(n)                          |
# | **Space**     | O(1) (no extra memory used)   |
