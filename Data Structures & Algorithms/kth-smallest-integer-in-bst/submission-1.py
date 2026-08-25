# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr=[]
        def in_order_traversal(node,arr):
            if not node:
                return
            
            in_order_traversal(node.left,arr)
            arr.append(node.val)
            in_order_traversal(node.right,arr)
        in_order_traversal(root,arr)
        
        return arr[k-1]
                
        




        