class Solution(object):
    def isPowerOfThree(self, n):
        if n <= 0:
            return False
        while n % 3 == 0:
            n //= 3
        return n == 1

n  = 27 
sol = Solution()
print(sol.isPowerOfThree(n))

# | Complexity | Value       |
# | ---------- | ----------- |
# | **Time**   | `O(log₃ n)` |
# | **Space**  | `O(1)`      |


# | Category      | Detail                           |
# | ------------- | -------------------------------- |
# | **Algorithm** | Simple Math / Factor Check       |
# | **Approach**  | Iterative                        |
# | **Technique** | Division Loop / Greedy Reduction |
# | **Time**      | `O(log₃ n)`                      |
# | **Space**     | `O(1)`                           |

