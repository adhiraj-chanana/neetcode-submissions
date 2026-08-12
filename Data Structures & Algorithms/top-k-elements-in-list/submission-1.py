class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c={}
        for i in nums:
            if i in c:
                c[i]+=1
            else:
                c[i]=1
       
        freq={i:[] for i in range(1,len(nums)+1)}
        for d in c:
            freq[c[d]].append(d)
        
        i=len(nums)
        a=0
        res=[]
        while i>0:
            if len(freq[i])>0:
                
                for b in freq[i]:
                    res.append(b)
                    if len(res)==k:
                        break
           
            if len(res)==k:
                break
            i-=1

        return res








        