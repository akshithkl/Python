class Solution(object):
    def wordPattern(self, pattern, s):
    
        words = s.split()
        
        # Lengths must match
        if len(pattern) != len(words):
            return False
        
        char_to_word = {}
        word_to_char = {}
        
        for c, w in zip(pattern, words):
            # Check character -> word mapping
            if c in char_to_word:
                if char_to_word[c] != w:
                    return False
            else:
                char_to_word[c] = w
            
            # Check word -> character mapping
            if w in word_to_char:
                if word_to_char[w] != c:
                    return False
            else:
                word_to_char[w] = c
                
        return True

pattern = "abba"
s = "dog cat cat dog"

print(Solution().wordPattern(pattern, s))

# | Aspect               | Value                                 |
# | -------------------- | ------------------------------------- |
# | **Algorithm**        | Hashing                               |
# | **Approach**         | One-pass mapping                      |
# | **Technique**        | Dictionary for bijection check        |
# | **Time Complexity**  | `O(n)` where `n = len(s.split())`     |
# | **Space Complexity** | `O(k)` where `k = unique words/chars` |
