class Node:
    def __init__(self,val, next=None):
        self.val=val
        self.next=next
        

class MyLinkedList:

    def __init__(self):
        self.head=None
        self.tail=None
        self.l=0

    def get(self, index: int) -> int:
        if not self.head:
            return -1
        if index>=self.l:
            return -1
        c=0
        node=self.head
        while node:
            if c==index:
                return node.val
            c+=1
            node=node.next
       

        

    def addAtHead(self, val: int) -> None:

        if not self.head:
            self.head=self.tail=Node(val)
        else:
            curNode=Node(val, self.head)
            self.head=curNode
        self.l+=1
        

    def addAtTail(self, val: int) -> None:
        if not self.tail:
            self.head=self.tail=Node(val)
        else:
            curNode=Node(val)
            self.tail.next=curNode
            self.tail=curNode
        self.l+=1
        

    def addAtIndex(self, index: int, val: int) -> None:
        if not self.head:
            if index==0:
                self.addAtHead(val)
            else:
                return 
        if index==self.l:
            self.addAtTail(val)
            return
        
        if index>self.l:
            return
            
        node=self.head.next
        prev=self.head
       
        c=1
        while node:
            if c==index:
                curNode=Node(val)
                prev.next=curNode
                curNode.next=node
                self.l+=1
                return
            c+=1
            prev=node
            node=node.next
        
        node=self.head

        
        
        

    def deleteAtIndex(self, index: int) -> None:
        if index>=self.l:
            return  
        if index==0:
            self.head=self.head.next
            return
        c=0
        node=self.head
        while node:
            if c==index:
                prev.next=node.next
                if node==self.tail:
                    self.tail=prev
                self.l-=1
                return
            c+=1
            prev=node
            node=node.next


        
        



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)