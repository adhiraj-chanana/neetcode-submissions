# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        a={}
        node=head
        c=0
        while node:
            a[c]=node
            node=node.next
            c+=1
        delete=c-n
        if delete==0:
            if c==1:
                return None
            else:
                return a[1]
        elif delete==c-1:
            a[delete-1].next=None
        else:
            a[delete-1].next=a[delete+1]
        return head





        