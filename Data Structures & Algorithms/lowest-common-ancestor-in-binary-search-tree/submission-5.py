# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        lca=root

        while True:
            if lca.val==p.val or lca.val==q.val:
                return lca
            elif q.val<lca.val<p.val or p.val<lca.val<q.val:
                return lca
            else:
                if p.val<q.val<lca.val or q.val<p.val<lca.val:
                    lca=lca.left
                else:
                    lca=lca.right


        

        