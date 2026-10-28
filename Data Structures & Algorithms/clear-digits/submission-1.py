class Solution:
    def clearDigits(self, s: str) -> str:
        stack=[]

        a='1234567890'

        for i in range(len(s)):
            if s[i] in a:
                stack.pop()
            else:
                stack.append(s[i])
        
        return ''.join(stack)



