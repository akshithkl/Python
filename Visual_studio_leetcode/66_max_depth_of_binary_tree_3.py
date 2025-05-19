# Definition for a binary tree node
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Function to build the tree from a list (level-order)
def build_tree(values):
    if not values:
        return None

    root = TreeNode(values[0])
    queue = [root]  # Using a list as the queue
    i = 1

    while queue and i < len(values):
        node = queue.pop(0)  # Pop from the front of the list (queue operation)
        
        if values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)  # Add to the back of the list (queue operation)
        i += 1

        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)  # Add to the back of the list
        i += 1

    return root

# Solution class to find max depth
class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0

        queue = [root]  # Queue for BFS
        level = 0
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.pop(0)  # Pop the front of the list
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1

        return level

# Input
tree_list = [3, 9, 20, None, None, 15, 7]
root = build_tree(tree_list)

# Now call your function
sol = Solution()
print(sol.maxDepth(root))  # Output should be 3


# | **Operation**         | **Time Complexity** | **Space Complexity** |
# | --------------------- | ------------------- | -------------------- |
# | **Building the tree** | O(n)                | O(n)                 |
# | **Max depth (BFS)**   | O(n)                | O(n)                 |

