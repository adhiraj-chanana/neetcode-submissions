class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        x1,y1=0,0
        arr=[]

        for x2,y2 in points:
            d=(((x1 - x2)**2 + (y1 - y2)**2)**(0.5))
            heapq.heappush(arr,[d,x2,y2])
        l=[]
        for i in range(k):
            a=heapq.heappop(arr)
            l.append(a[1:])
        return l





        