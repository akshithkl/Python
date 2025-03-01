# Mock function to simulate the API
def isBadVersion(version: int) -> bool:
    bad_version = 4  # Assume version 4 is the first bad version
    return version >= bad_version

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 1  
        end = n

        while start < end:
            mid = (start + end) // 2

            if isBadVersion(mid):  # Now this function is defined
                end = mid
            else:
                start = mid + 1
        
        return start

# Test the function
solution = Solution()
n = 10   # Assume 10 versions exist
print(solution.firstBadVersion(n))  # Output: 4

