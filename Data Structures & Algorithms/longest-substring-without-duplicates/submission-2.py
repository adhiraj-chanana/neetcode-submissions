class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r=0
        freq=set()
        res=0
        while r<len(s):
            if s[r] not in freq:
                freq.add(s[r])
                res=max(res,r-l+1)
            else:
                while l<r and s[l]!=s[r]:
                    freq.remove(s[l])
                    l+=1
                l+=1
            r+=1
        return res
            
            


        