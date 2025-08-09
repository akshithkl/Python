class Solution:
    def decrypt(self, code, k):
        n = len(code)
        result = [0] * n


        for i in range(n):
            if k > 0:
                for j in range(i + 1, i + 1 + k):
                    result[i] += code[ j % n]
            elif k < 0:
                for j in range(i - 1, i - 1 - abs(k), - 1):
                    result[i] += code[j]

        return result

code = [5,7,1,4]
k = 3

print(Solution().decrypt(code, k))

code = [5,7,1,4]
k = -3

print(Solution().decrypt(code, k))


# Time Complexity:
# Outer loop runs n times
# Inner loop runs |k| times
# ➡️ Total: O(n × |k|)

# ✅ Space Complexity:
# Output array of size n
# ➡️ Total: O(n)

# | Technique             | Description                                                      |
# | --------------------- | ---------------------------------------------------------------- |
# | **Brute-force loop**  | Each index is recomputed from scratch using inner for-loops     |
# | **Modulo arithmetic** | Used to wrap forward index (k > 0) within bounds of array        |
# | **Negative indexing** | Uses Python’s support for negative indices for k < 0             |
# | **Conditional logic** | Separates forward and backward sum logic based on sign of `k`    |
# | **No optimization**   | Does not use sliding window or prefix sums to reduce computation |

# | Aspect         | Value                                                             |
# | -------------- | ----------------------------------------------------------------- |
# | **Algorithm**  | Brute-force Circular Sum                                          |
# | **Approach**   | Use index-based loop to sum previous or next `k` elements         |
# | **Techniques** | Modulo for forward circular wrap; native negative indexing for back |

