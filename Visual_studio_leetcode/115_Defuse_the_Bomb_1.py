class Solution(object):
    def decrypt(self, code, k):
    
        n = len(code)
        result = [0] * n

        if k == 0:
            return result

        # Initialize window sum
        window_sum = 0
        start = 1 if k > 0 else n + k
        end = k if k > 0 else n - 1

        # Build initial window sum
        for i in range(start, end + 1):
            window_sum += code[i % n]

        # Slide window across each position
        for i in range(n):
            result[i] = window_sum
            # Slide window: remove old, add new
            window_sum -= code[(start) % n]
            start += 1
            end += 1
            window_sum += code[(end) % n]

        return result

code = [5,7,1,4]
k = 3

print(Solution().decrypt(code, k))
# Time: O(n) — single pass to compute all values
# Space: O(n) — for the result array

# | Name                        | Description                                                                 |
# | --------------------------- | --------------------------------------------------------------------------- |
# | **Sliding Window**          | Avoids recomputation by using a running sum while moving the window forward |
# | **Modulo Arithmetic**       | Used to wrap around the array since it’s circular                           |
# | **Two-pointer (start/end)** | Used internally to keep track of window boundaries                          |
# | **Simultaneous Update**     | All elements are updated at the same time, not one after another            |

