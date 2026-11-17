class Solution:
    def longestPalindrome(self, s: str) -> str:

        def expand(l,r):
            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1
            return r-l+1,l+1,r-1

        res=0
        m=''
        for i in range(len(s)):
            t, l,r=expand(i,i)
            if t>res:
                res=t
                m=s[l:r+1]
            t, l,r=expand(i,i+1)
            if t>res:
                res=t
                m=s[l:r+1]

            

            
        
        return m




        