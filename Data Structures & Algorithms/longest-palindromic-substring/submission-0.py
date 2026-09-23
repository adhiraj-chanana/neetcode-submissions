class Solution:
    def longestPalindrome(self, s: str) -> str:
        result=""
        def expand(l,r,result):
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l)+1>len(result):
                    result=s[l:r+1]
                l-=1
                r+=1
            return result
        for i in range(len(s)):
            result=expand(i,i,result)
            result=expand(i,i+1,result)
        
        return result



        
        