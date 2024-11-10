# Definition of TreeNode (as above)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = []
        depth = 1
        queue.append((root, depth))
        while queue:
            curr, d = queue.pop(0)
            if curr.left is None and curr.right is None:
                return d
            if curr.left:
                queue.append((curr.left, d+1))
            if curr.right:
                queue.append((curr.right, d+1))
        return depth

# Sample tree for testing
if __name__ == "__main__":
    # Constructing a sample binary tree
    #      1
    #     / \
    #    2   3
    #   /
    #  4
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)

    # Create Solution object
    solution = Solution()
    # Output minimum depth
    print("Minimum Depth of Tree:", solution.minDepth(root))

