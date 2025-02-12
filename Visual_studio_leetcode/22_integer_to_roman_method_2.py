class Solution:
    def intToRoman(self, num: int) -> str:
        roman = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"),
            (1, "I")
        ]
        
        result = []
        for val, symb in roman:
            count, num = divmod(num, val)  # Efficient division & modulus
            result.append(symb * count)  # Append multiple symbols at once
        
        return "".join(result)  # Efficient string concatenation

# Example Usage
sol = Solution()
print(sol.intToRoman(1994))  # Output: "MCMXCIV"
print(sol.intToRoman(58))    # Output: "LVIII"
print(sol.intToRoman(9))     # Output: "IX"


'''Why is This O(1)?
Fixed number of iterations:

The loop runs at most 13 times (since there are only 13 unique Roman numeral values).
This does not depend on num, making it O(1) in terms of complexity.
Using divmod() for Efficient Computation:

Instead of repeated subtraction (while num >= val), divmod(num, val) directly computes how many times val fits into num in a single operation.
List Append & String Join:

Using a list (result.append(symb * count)) is more efficient than string concatenation (+=), which creates new string objects each time.
"".join(result) is fast in Python.
Final Complexity Analysis
The loop runs at most 13 iterations.
Each operation inside the loop (divmod(), append(), join()) is constant time.
Overall, the solution runs in O(1) time complexity. 

'''




