class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:

        freq={}
        for i in range(len(x)):
            if x[i] in freq:
                freq[x[i]]=max(freq[x[i]], y[i])
            else:
                freq[x[i]]=y[i]
        print(freq)
        
        if len(freq)<3:
            return -1
        
        heap=[]
        for i in freq:
            heapq.heappush(heap, -freq[i])
        s=0
        for i in range(3):
            s+=abs(heapq.heappop(heap))
        return s



        




        