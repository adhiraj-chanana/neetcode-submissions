class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        size=len(grid)

        pq=[[grid[0][0], 0, 0]]
        mintime={}
        for i in range(size):
            for j in range(size):
                mintime[(i,j)]=float('inf')

        mintime[(0,0)]=grid[0][0]
        directions=[[-1,0],[1,0], [0,-1], [0,1]]
        visited=set()
        # print(mintime)
        while pq:
            level, r, c= heapq.heappop(pq)
            # print(level, r,c)
            visited.add((r,c))

            for rr,cc in directions:
                nr,nc=r+rr, c+cc
                if nr<0 or nr==size or nc<0 or nc==size or (nr,nc) in visited:
                    continue
                else: 
                    if nr==nc==size-1:
                        return min(mintime[(nr,nc)],max(mintime[(r,c)],grid[nr][nc]))
                    mintime[(nr,nc)]=min(mintime[(nr,nc)],max(mintime[(r,c)],grid[nr][nc]))
                    heapq.heappush(pq,[grid[nr][nc], nr,nc])
        
        
        if mintime[(size-1, size-1)]==float('inf'):
            return -1
        else:
            return mintime[(size-1, size-1)]





            

            
            

 


        