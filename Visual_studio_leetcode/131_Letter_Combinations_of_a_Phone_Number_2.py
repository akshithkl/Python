class Solution(object):
    def letterCombinations(self, digits):
        digitToChar = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        if not digits:
            return []
        
        # Generate all possible strings of length len(digits) from a–z
        result = []
        charset = "abcdefghijklmnopqrstuvwxyz"
        
        def generate_all(current):
            if len(current) == len(digits):
                # Check if current matches the digit mapping
                for i in range(len(digits)):
                    if current[i] not in digitToChar[digits[i]]:
                        return  # invalid
                result.append(current)
                return
            
            for c in charset:
                generate_all(current + c)
        
        generate_all("")
        return result

digits = "23"
print(Solution().letterCombinations(digits))

# | Aspect               | Value                                                             |
# | -------------------- | ----------------------------------------------------------------- |
# | **Algorithm**        | Brute-force generation + filtering                                |
# | **Approach**         | Full permutation generation from `'a'` to `'z'`                   |
# | **Technique**        | Generate all strings of length `n`, filter based on digit mapping |
# | **Time Complexity**  | $O(26^n \cdot n)$                                                 |
# | **Space Complexity** | $O(26^n)$ (for storing all valid/invalid combinations)            |
# | **Best Case**        | $O(26^n)$, still exponential, no early pruning like backtracking  |
