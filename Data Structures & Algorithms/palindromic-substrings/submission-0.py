class Solution:
    def countSubstrings(self, s: str) -> int:
        result=0
        def expand(l,r,result):
            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1
                result+=1
            return result



        for i in range(len(s)):
            result=expand(i,i,result)
            result=expand(i,i+1,result)
        
        return result


