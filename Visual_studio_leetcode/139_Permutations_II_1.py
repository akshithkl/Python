class Solution(object):
    def permuteUnique(self, nums):

        res = []
        perm = []
        count = {n:0 for n in nums}
        for n in nums:
            count[n] += 1
        
        def dfs():
            if len(perm) == len(nums):
                res.append(perm.copy())
                return 
            
            for n in count:
                if count[n] > 0:
                    perm.append(n)

                    count[n] -= 1

                    dfs()

                    count[n] += 1
                    perm.pop()
            
        dfs()
        return res
s = Solution()
print(s.permuteUnique([1, 1, 2]))


# | Aspect               | Value                                       |
# | -------------------- | ------------------------------------------- |
# | **Algorithm**        | Backtracking with pruning                   |
# | **Approach**         | DFS + HashMap (count-based pruning)         |
# | **Time Complexity**  | O(n! × n) (or fewer with duplicates)        |
# | **Space Complexity** | O(n) auxiliary, O(n! × n) total with output |
