class MinStack:

    def __init__(self):
        self.minstack=[]
        self.stack=[]
        self.min=float('inf')
        

    def push(self, val: int) -> None:
        if val<self.min:
            self.min=val
        self.stack.append(val)
        self.minstack.append(self.min)

        

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.minstack.pop()
            if self.minstack:
                self.min=self.minstack[-1]
            else:
                self.min=float('inf')

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min

        
