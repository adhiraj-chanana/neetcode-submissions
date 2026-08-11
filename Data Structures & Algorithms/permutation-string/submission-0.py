class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s2_map={chr(i):0 for i in range(97,123)}
        s1_map={chr(i):0 for i in range(97,123)}
        if len(s1)>len(s2):
            return False
        for i in s1:
            s1_map[i]+=1
        
        for i in range(len(s1)-1):
            s2_map[s2[i]]+=1
        l=0
        r=len(s1)-1
        while r<len(s2):
            s2_map[s2[r]]+=1
            if s1_map==s2_map:
                return True
            else:
                s2_map[s2[l]]-=1
                l+=1
                r+=1
        return False
                
                



        