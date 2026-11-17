class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        size=len(grid)

        pq=[[grid[0][0], 0, 0]]
        # mintime={}
        # for i in range(size):
        #     for j in range(size):
        #         mintime[(i,j)]=float('inf')

        
        directions=[[-1,0],[1,0], [0,-1], [0,1]]
        visited=set()
        # print(mintime)
        while pq:
            level, r, c= heapq.heappop(pq)
            # print(level, r,c)
            if r==c==size-1:
                return level
            for rr,cc in directions:
                nr,nc=r+rr, c+cc
                if nr<0 or nr==size or nc<0 or nc==size or (nr,nc) in visited:
                    continue
                else: 
                    visited.add((nr,nc))
                    l=max(level,grid[nr][nc])
                    heapq.heappush(pq,[l, nr,nc])
                    
        return -1
       





            

            
            

 


        