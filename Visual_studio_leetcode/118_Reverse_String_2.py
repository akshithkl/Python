def reverseString(s):
    # Create a new list to store reversed characters
    reversed_s = []
    for i in range(len(s) - 1, -1, -1):
        reversed_s.append(s[i])
    
    # Copy back to original list (to simulate in-place)
    for i in range(len(s)):
        s[i] = reversed_s[i]


s = ["h", "e", "l", "l", "o"]
reverseString(s)
print(s)  # → ['o', 'l', 'l', 'e', 'h']


# | Metric               | Value                              |
# | -------------------- | ---------------------------------- |
# | **Algorithm**        | Brute Force                        |
# | **Technique**        | Reverse Traversal with Extra Space |
# | **Time Complexity**  | O(n)                               |
# | **Space Complexity** | O(n)                               |
# | **In-place?**        | ❌ No                              |
# | **Stable?**          | ✅ Yes                             |
