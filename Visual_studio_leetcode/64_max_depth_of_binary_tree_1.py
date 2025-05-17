# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
            stack = [[root, 1]]
            res = 0 
            while stack:
                node, depth = stack.pop()

                if node:
                    res = max(res, depth)
                    stack.append([node.left, depth + 1])
                    stack.append([node.right, depth + 1])

            return res
        
# | Aspect       | Time Complexity | Space Complexity                                  |
# | ------------ | --------------- | ------------------------------------------------- |
# | `maxDepth()` | **O(n)**        | **O(n)** (worst case) or **O(log n)** (best case) |
