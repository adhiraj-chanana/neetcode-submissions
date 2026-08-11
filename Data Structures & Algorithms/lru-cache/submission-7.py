class Node:
    def __init__(self,key,val,n=None,p=None):
        self.key=key
        self.val=val
        self.next=n
        self.prev=p


class LRUCache:

    def __init__(self, capacity: int):
        self.head=None
        self.tail=None
        self.capacity=capacity
        self.map={}
        self.count=0


        

    def get(self, key: int) -> int:
        ##print("gettomg", key)
        if key in self.map:
            if key==self.tail:
                return self.map[key].val
            else:
                self.remove_node(self.map[key])
                self.add_tail(self.map[key])
                return self.map[key].val
        else:
            return -1
            


    def put(self, key: int, value: int) -> None:
        ##print(key,value)
        if key in self.map:
            self.map[key].val=value
            if self.map[key]==self.tail:
                return
            self.remove_node(self.map[key])
            self.add_tail(self.map[key])
        else:
            if self.capacity==self.count:
                del self.map[self.head.key]
                self.remove_node(self.head)
                self.count-=1
            node=Node(key,value)
            self.add_tail(node)
            self.count+=1
            self.map[key]=node


        

    
    def add_tail(self, node: Node):
        if not self.tail:
            self.tail=node
            self.head=node
        else:   
            self.tail.next=node
            node.prev=self.tail
            node.next=None
            self.tail=node
    
    def remove_node(self,node: Node):
        if node==self.head and node==self.tail:
            self.head=None
            self.tail=None
        elif node==self.head:
            self.head=node.next
            self.head.prev=None
        elif node==self.tail:
            return 
        else:
            node.prev.next=node.next
            node.next.prev=node.prev
    



