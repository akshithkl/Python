class Solution:
    def decrypt(self, code, k):
        n = len(code)
        result = [0] * n


        for i in range(n):
            total = 0
            if k > 0:
                for j in range(1, k + 1):
                    total += code[(i + j) % n]
            elif k < 0:
                for j in range(1, -k + 1):
                    total += code[(i - j + n) % n]
            result[i] = total

        return result

print(Solution().decrypt([5,7,1,4], 0))

print(Solution().decrypt([5,7,1,4], 3))


# Time Complexity:
# Outer loop runs n times

# Inner loop runs |k| times
# ➡️ Total: O(n × |k|)

# ✅ Space Complexity:
# Output array of size n
# ➡️ Total: O(n)



# | Technique             | Description                                                |
# | --------------------- | ---------------------------------------------------------- |
# | **Brute-force loop**  | Each position is recomputed from scratch                   |
# | **Modulo arithmetic** | Handles wrapping in circular array                         |
# | **Conditional logic** | Separates logic for `k > 0`, `k < 0`, and `k == 0`         |
# | **No optimization**   | No reuse of previous window sums — i.e., no sliding window |

# | Aspect         | Value                                                 |
# | -------------- | ----------------------------------------------------- |
# | **Algorithm**  | Brute-force Circular Sum                              |
# | **Approach**   | Recalculate sum for each index using for-loops        |
# | **Techniques** | Modulo for circular wrap, conditional branching for k |
