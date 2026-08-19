class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        r=0
        maxres=0
        maxchar=0
        freq={chr(i):0 for i in range(65,91)}
        while r<len(s):
            freq[s[r]]+=1
            maxchar=max(maxchar, freq[s[r]])
            while (r-l+1)-maxchar>k:
                freq[s[l]]-=1
                l+=1
            maxres=max(maxres, r-l+1)
            r+=1
        
        return maxres





        