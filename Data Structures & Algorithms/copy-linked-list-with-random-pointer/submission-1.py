"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return
        newNode=None
        node=head
        prev=None
        map={}
        while node:
            newNode=Node(node.val)
            if prev:
                prev.next=newNode
            
            prev=newNode
            map[node]=newNode
            node=node.next
        node=head
        while node:
            if not node.random:
                map[node].random=None
            else:
                map[node].random=map[node.random]
            node=node.next
        return map[head]





        