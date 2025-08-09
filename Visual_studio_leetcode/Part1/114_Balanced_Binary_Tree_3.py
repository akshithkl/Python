class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def height(self, node):
        if not node:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

    def isBalanced(self, root):
        if not root:
            return True

        left_height = self.height(root.left)
        right_height = self.height(root.right)

        if abs(left_height - right_height) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)

# -------------------------------
# Example usage for brute-force:
# -------------------------------
if __name__ == "__main__":
    # Balanced Tree
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    sol = Solution()
    print("Is the tree balanced?", sol.isBalanced(root))  # Output: True

    # Unbalanced Tree
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.left.left = TreeNode(3)

    print("Is the tree balanced?", sol.isBalanced(root2))  # Output: False


# Approach	    Time Complexity	        Space Complexity	Notes
# Brute Force	  O(n²)	                 O(h)	              Height recalculated many times
