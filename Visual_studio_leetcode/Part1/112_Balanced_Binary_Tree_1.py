# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root):
        def check(node):
            if not node:
                return 0

            left = check(node.left)
            if left == -1: return -1

            right = check(node.right)
            if right == -1: return -1

            if abs(left - right) > 1:
                return -1

            return 1 + max(left, right)

        return check(root) != -1

# ----------------------------
# Example Usage
# ----------------------------


    # Example: Balanced Tree
    #     3
    #    / \
    #   9  20
    #      / \
    #     15  7
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
   
sol = Solution()
print("Is the tree balanced?", sol.isBalanced(root))  # Output: True

    # Example: Unbalanced Tree
    #     1
    #    /
    #   2
    #  /
    # 3
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.left.left = TreeNode(3)

print("Is the tree balanced?", sol.isBalanced(root2))  # Output: False
    
    
    
    # | Property           | Value                                                   |
# | ------------------ | ------------------------------------------------------- |
# | ✅ Time Complexity  | O(n)                                                    |
# | ✅ Space Complexity | O(h)                                                    |
# | ✅ Algorithm        | DFS, Postorder Traversal                                |
# | ✅ Techniques Used  | Recursion, Early Termination, Bottom-Up Height Checking |

# | Concept                     | Usage in Code                                              |
# | --------------------------- | ---------------------------------------------------------- |
# | ✅ **Recursion**             | To traverse tree and compute height                        |
# | ✅ **Postorder DFS**         | Compute left & right subtree heights before current node   |
# | ✅ **Early Stopping**        | If imbalance is detected, return `-1` immediately          |
# | ✅ **Bottom-Up Approach**    | Height and balance info is calculated from children → root |
# | ✅ **Sentinel Value (`-1`)** | Used to signal imbalance up the recursive stack            |
