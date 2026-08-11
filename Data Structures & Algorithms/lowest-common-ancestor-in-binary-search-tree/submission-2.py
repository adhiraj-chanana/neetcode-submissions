# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.left==q or p.right==q:
            return p
        if q.left==p or q.right==p:
            return q
        if not root:
            return None
        while True:
            if root==p or root==q:
                return root
            elif (p.val<root.val and q.val>root.val) or (p.val>root.val and q.val<root.val):
                return root
            elif p.val<root.val and q.val<root.val:
                root=root.left
            else:
                root=root.right
        return None



        