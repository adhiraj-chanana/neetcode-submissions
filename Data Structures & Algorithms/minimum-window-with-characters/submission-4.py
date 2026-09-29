class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l=0
        r=0
        freqS={chr(i):0 for i in range(65,91)}
        freqT={chr(i):0 for i in range(65,91)}
        for i in range(97,123):
            freqS[chr(i)]=0
            freqT[chr(i)]=0

        def compareDicts():
            for i in freqT:
                if freqT[i]>freqS[i]:
                    return False
            return True


        for i in t:
            freqT[i]+=1
        result=""
        t=float('inf')
        for r in range(len(s)):
            c=s[r]
            freqS[c]+=1
            if compareDicts():
                while l<=r and freqS[s[l]]>freqT[s[l]]:
                    freqS[s[l]]-=1
                    l+=1
                if (r-l+1)<t:
                        result=s[l:r+1]
                        t=len(result)
                    
        
        return result





        