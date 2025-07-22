from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def goodNodes(self, root):
 
        def dfs(node, MaxVal):
            if not node:
                return 0

            res = 1 if node.val >= MaxVal else 0
            MaxVal = max(node.val, MaxVal)
            res += dfs(node.left, MaxVal)
            res += dfs(node.right, MaxVal)
            return res

        return dfs(root, root.val)

# Helper function to build binary tree from level-order list
def build_tree(level_order):
    if not level_order:
        return None

    root = TreeNode(level_order[0])
    queue = deque([root])
    i = 1

    while queue and i < len(level_order):
        current = queue.popleft()
        if level_order[i] is not None:
            current.left = TreeNode(level_order[i])
            queue.append(current.left)
        i += 1

        if i < len(level_order) and level_order[i] is not None:
            current.right = TreeNode(level_order[i])
            queue.append(current.right)
        i += 1

    return root

if __name__ == "__main__":
    # LeetCode-style input
    level_order = [3, 1, 4, 3, None, 1, 5]
    root = build_tree(level_order)

    sol = Solution()
    result = sol.goodNodes(root)
    print("Number of good nodes:", result)


    """
        Count the number of "good" nodes in a binary tree.

        | Aspect               | Value                                        |
        | -------------------- | -------------------------------------------- |
        | **Algorithm**        | DFS (Depth-First Search)                     |
        | **Approach**         | Recursive Tree Traversal                     |
        | **Technique**        | Top-Down DFS with state propagation (MaxVal) |
        | **Time Complexity**  | O(n), where n is the number of nodes         |
        | **Space Complexity** | O(h), where h is the height of the tree      |
     """