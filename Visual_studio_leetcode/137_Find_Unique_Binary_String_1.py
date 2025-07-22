class Solution(object):
    def findDifferentBinaryString(self, nums):
  
        str_set = {s for s in nums}

        def backtrack(i, cur):
            if i == len(nums):
                res = "".join(cur)
                return None if res in str_set else res
            
            res = backtrack(i + 1, cur)
            if res:
                return res
            
            cur[i] = "1"
            res = backtrack(i + 1, cur)
            if res:
                return res
            
        return backtrack(0, ["0" for s in nums])

nums = ["011","000","001"]
print(Solution().findDifferentBinaryString(nums))
# | Aspect               | Value                         |
# | -------------------- | ----------------------------- |
# | **Algorithm**        | Backtracking                  |
# | **Approach**         | Generate binary strings       |
# | **Technique**        | DFS, early stopping           |
# | **Time Complexity**  | `O(n * 2^n)`                  |
# | **Space Complexity** | `O(n + 2^n)`                  |
# | **Best Case**        | Early match, closer to `O(n)` |
# | **Worst Case**       | Explore full space            |


#                            i=0, cur=['0','0','0']
#                           /                     \
#             (keep '0') i=1              (set cur[0]='1') i=1
#             cur=['0','0','0']                cur=['1','0','0']
#              /        \                       /        \
#   (keep '0')       (set '1')        (keep '0')       (set '1')
# i=2 ['0','0','0'] ['0','1','0']    ['1','0','0']   ['1','1','0']
#    /     \           /    \          /   \           /   \
# ...      ...       ...   ...       ...   ...       ...   ...
# → i=3 → base case → join cur → check if in str_set
# → return if not in set
