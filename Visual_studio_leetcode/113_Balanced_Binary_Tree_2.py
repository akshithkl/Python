from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Function to build tree from level order input
def build_tree(level_order):
    if not level_order or level_order[0] is None:
        return None

    root = TreeNode(level_order[0])
    queue = deque([root])
    i = 1

    while queue and i < len(level_order):
        node = queue.popleft()

        # Left child
        if i < len(level_order) and level_order[i] is not None:
            node.left = TreeNode(level_order[i])
            queue.append(node.left)
        i += 1

        # Right child
        if i < len(level_order) and level_order[i] is not None:
            node.right = TreeNode(level_order[i])
            queue.append(node.right)
        i += 1

    return root

# Solution class with isBalanced function
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

input1 = [3, 9, 20, None, None, 15, 7]  # Balanced
input2 = [1, 2, None, 3]               # Unbalanced

tree1 = build_tree(input1)
tree2 = build_tree(input2)

sol = Solution()
print("Is the first tree balanced?", sol.isBalanced(tree1))  # Output: True
print("Is the second tree balanced?", sol.isBalanced(tree2)) # Output: False




# | Function       | Algorithm/Approach | Time Complexity | Space Complexity | Notes                       |
# | -------------- | ------------------ | --------------- | ---------------- | --------------------------- |

# | `build_tree()` | BFS with deque     | O(n)            | O(n)             | Efficient queue-based build |



# 2. build_tree() Function (Using deque and input like [3,9,20,None,...])
# This function builds a binary tree from level-order list input.

# 🔧 Algorithm/Technique Used
# BFS (Breadth-First Search) approach using a queue

# Processes the list left to right, linking children level by level

# ⏱️ Time Complexity
# O(n) — Each element in the input list is processed once

# n is the number of nodes (non-None values in the list)

# 🧠 Space Complexity
# O(n) — for the queue and for storing the tree nodes

