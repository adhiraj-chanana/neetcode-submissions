# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class NodeWrapper:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val


class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        arr=[]
        cur=None
        head=None
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(arr, NodeWrapper(lists[i]))

       
        
        while arr:
            v=heapq.heappop(arr)
            temp=v.node
           
            if not head:
                head=temp
                cur=head
            else:
                cur.next=temp
                cur=cur.next
            if temp.next:
                heapq.heappush(arr, NodeWrapper(temp.next))
            

            
        return head