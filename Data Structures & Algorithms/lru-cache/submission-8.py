class Node:
    def __init__(self, key:int , value: int, next=None, prev=None):
        self.key=key
        self.value=value
        self.next=next
        self.prev=prev 

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.size=0
        self.cache={}
        self.head=None
        self.tail=None


    def get(self, key: int) -> int:
        if key in self.cache:
            if self.head.key==key:
                return self.cache[key].value
            else:
                self.remove(self.cache[key])
                self.add(self.cache[key])
                return self.cache[key].value
            
        else:
            return -1
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
         
            self.cache[key].value=value
            self.remove(self.cache[key])
            self.add(self.cache[key])
        else:
            if self.capacity==self.size:
                del self.cache[self.tail.key] 
                self.remove(self.tail)
            newNode=Node(key, value)
            self.cache[key]=newNode
            self.add(newNode)
           
    



    
    def remove(self,node):

        if node==self.head and node==self.tail:
            self.head=None
            self.tail=None
        elif node is self.head:
            node.next.prev=None
            self.head=node.next
        elif node is self.tail:
            node.prev.next=None
            self.tail=node.prev
        else:
            node.prev.next=node.next
            node.next.prev=node.prev
        self.size-=1
    
    def add(self, node):
        if not self.head:
            self.tail=node
            self.head=node
        else:
            self.head.prev=node
            node.next=self.head
            node.prev=None
            self.head=node
        self.size+=1
        
    
        

        
        
