class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s)==1:
            return True
        for i in range(len(s)):
            if i==0:
                a=s[i+1:]
            elif i==len(s)-1:
                a=s[:i] 
            else:
                a=s[:i]+s[i+1:]
            if a==a[::-1]:
                return True 
        return False
        