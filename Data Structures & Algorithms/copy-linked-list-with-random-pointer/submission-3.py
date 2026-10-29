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
        map={}

        node=head
        prev=None
        while node:
            map[node]=Node(node.val)
            if not prev:
                prev=node
            else:
                map[prev].next=map[node]
                prev=node
            node=node.next
        
        node=head
        while node:
            if node.random:
                map[node].random=map[node.random]
            node=node.next
        
        return map[head]

        