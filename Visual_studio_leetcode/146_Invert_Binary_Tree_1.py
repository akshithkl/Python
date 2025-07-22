from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Function to invert the tree
class Solution:
    def invertTree(self, root):
        if not root:
            return None

        # Swap left and right
        root.left, root.right = root.right, root.left

        # Recursively invert children
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

# Helper function to build a binary tree from list
def build_tree_from_list(values):
    if not values:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        current = queue.popleft()
        if values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1

        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1

    return root

# Helper function to print tree level-order (for testing)
def print_level_order(root):
    if not root:
        print([])
        return

    queue = deque([root])
    result = []

    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # Remove trailing None values for clean output
    while result and result[-1] is None:
        result.pop()

    print(result)

# Input
input_list = [4, 2, 7, 1, 3, 6, 9]
root = build_tree_from_list(input_list)

# Solution
sol = Solution()
inverted_root = sol.invertTree(root)

# Output
print("Inverted tree (level-order):")
print_level_order(inverted_root)
