# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return
        node=head
        prev=None
        while node:
            if node.val==val:
                if not prev:
                    head=node.next        
                else:
                    prev.next=node.next       
            else:
                prev=node
            node=node.next
        return head

        