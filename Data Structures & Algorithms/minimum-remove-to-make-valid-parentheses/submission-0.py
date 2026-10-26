class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        stack=[]
        to_remove=[]
        for i,ch in enumerate(s):
            if ch=='(':
                stack.append(i)
            elif ch==')':
                if stack:
                    stack.pop()
                else:
                    to_remove.append(i)
        print(stack)
        print(to_remove)
        if stack:
            for i in range(len(stack)):
                a=stack.pop()
                s=s[:a]+s[a+1:]
                
        if to_remove:
            for i in range(len(to_remove)):
                a=to_remove.pop()
                s=s[:a]+s[a+1:]

                
        
        return s
        
        

                    




