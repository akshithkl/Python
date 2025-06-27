# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# ----------- Test Code Below --------------
if __name__ == "__main__":
    # Tree 1
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)

    # Tree 2
    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(3)

    sol = Solution()
    print(sol.isSameTree(p, q))  # Should print True


# ⏱️ Time Complexity: O(n)

# You visit each node once.

# n is the total number of nodes in either tree (whichever is smaller if unequal).

# 🧠 Space Complexity: 
#     O(h) in the best/average case, where h is the height of the tree (for recursion stack).

# In the worst case (skewed tree), h = n, so space complexity becomes O(n).

# In the best case (balanced tree), h = log n, so space becomes O(log n).