class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i]*=-1

        heapq.heapify(stones)

        while len(stones)>1:
            a=heapq.heappop(stones)
            b=heapq.heappop(stones)
            a*=-1
            b*=-1
            if a==b:
                continue
            else:
                heapq.heappush(stones,b-a)
        
        if len(stones)==1:
            return -1*stones[0]
        else:
            return 0

        