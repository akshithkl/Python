class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def get_next(num):
            total = 0
            while num > 0:
                digit = num % 10
                total += digit * digit
                num //= 10
            return total
        
        seen = set()
        
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)
        
        return n == 1
n = 19
sol = Solution()
print(sol.isHappy(n))

# | Type                 | Value                                                         |
# | -------------------- | ------------------------------------------------------------- |
# | **Time Complexity**  | `O(log n)` digits per number × steps → bounded → **O(log n)** |
# | **Space Complexity** | **O(log n)** (for storing seen numbers in a set)              |
