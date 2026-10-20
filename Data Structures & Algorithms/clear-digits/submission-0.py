class Solution:
    def clearDigits(self, s: str) -> str:
        
        stack=[]
        d="0123456789"
        for i in s:
            if i in d:
                stack.pop()
            else:
                stack.append(i)
        
        return ''.join(stack)
