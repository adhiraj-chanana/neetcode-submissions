class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        q=deque()
        unrotten=0
        visited=set()
        directions=[[0,1],[0,-1],[-1,0],[1,0]]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==2:
                    q.append((i,j))
                    visited.add((i,j))
                if grid[i][j]==1:
                    unrotten+=1
                
        if unrotten==0:
            return 0
        time=0
        while q:
            
            for _ in range(len(q)):
                r,c=q.popleft()
                if grid[r][c]==1:
                    unrotten-=1
                for dr, dc in directions:
                    nr,nc=dr+r,dc+c
                    if nr<0 or nc<0 or nr==rows or nc==cols or grid[nr][nc]!=1 or (nr,nc) in visited:
                        continue
                    else:
                        visited.add((nr,nc))
                        q.append((nr,nc))
            time+=1
        if unrotten==0:
            return time-1
        else:
            return -1





                    



        
        