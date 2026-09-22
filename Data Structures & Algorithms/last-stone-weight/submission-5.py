class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        arr=[]

        for i in stones:
            heapq.heappush(arr, -i)

        while len(arr)>1:
            a=heapq.heappop(arr)
            b=heapq.heappop(arr)
            a=a*-1
            b=b*-1
            if a==b:
                continue
            else:
                heapq.heappush(arr, -(a-b))
        
        if arr:
            return abs(heapq.heappop(arr))
        else:
            return 0

        