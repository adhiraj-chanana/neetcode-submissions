# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, x):
            if not node:
                return 0
            if node.val>=x:
                return 1+dfs(node.left, max(node.val, x))+dfs(node.right, max(node.val, x))
            else:
                return dfs(node.left, max(node.val, x))+dfs(node.right, max(node.val, x))
        
        return dfs(root, root.val)
        