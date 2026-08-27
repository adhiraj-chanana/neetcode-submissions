class Solution:
    def maxDifference(self, s: str) -> int:
        a={chr(i):0 for i in range(97,123)}
        maxodd=0
        maxeven=len(s)
        for i in s:
            a[i]+=1
        
        for i in range(97,122):
            if a[chr(i)]%2==0 and a[chr(i)]!=0:
                maxeven=min(maxeven,a[chr(i)])
            else:
                maxodd=max(maxodd,a[chr(i)])
        return maxodd-maxeven
        