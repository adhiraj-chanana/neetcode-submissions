# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node=head
        for i in range(n-1):
            node=node.next
        bnode=head
        prev=head
        while node.next:
            node=node.next
            prev=bnode
            bnode=bnode.next
            #print(bnode.val, node.val, prev.val)
        if bnode==head:
            if not head.next:
                return None
            else:
                return head.next
        prev.next=bnode.next
        return head

        

        