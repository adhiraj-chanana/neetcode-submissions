class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:

        freq={}
        for i in range(len(x)):
            if x[i] in freq:
                freq[x[i]]=max(freq[x[i]], y[i])
            else:
                freq[x[i]]=y[i]
        
        if len(freq)<3:
            return -1
        
        heap=[]
        for i in freq:
            heapq.heappush(heap, freq[i])
            if len(heap)>3:
                heapq.heappop(heap)
        return sum(heap)



        




        