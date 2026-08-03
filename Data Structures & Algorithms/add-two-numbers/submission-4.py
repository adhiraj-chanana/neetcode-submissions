# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node1=l1
        node2=l2
        c=0
        prev=None
        newHead=None
        while node1 or node2:
            if not node2 and node1:
                s=node1.val+c
            elif not node1 and node2:
                s=node2.val+c
            else:
                s=node1.val+node2.val+c
            c=0
            if s>9:
                c=1
                d=s%10
                curNode=ListNode(s%10)
            else:
                curNode=ListNode(s)
            if not prev:
                newHead=curNode
            else:
                prev.next=curNode
            prev=curNode
            if node1:
                node1=node1.next
            if node2:
                node2=node2.next
        if c==1:
            curNode.next=ListNode(c)
        return newHead



        
        