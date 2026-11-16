class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r=0
        freq={}
        res=0
        while r<len(s):
            if s[r] in freq:
                freq[s[r]]+=1
            else:
                freq[s[r]]=1
            while l<r and freq[s[r]]>1:
                freq[s[l]]-=1
                l+=1
            res=max(r-l+1,res)
            r+=1
        return res
            
            




        