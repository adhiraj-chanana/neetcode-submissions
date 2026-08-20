class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows=len(grid)
        cols=len(grid[0])
        q=deque()
        directions=[[-1,0],[1,0],[0,1], [0,-1]]
        visited=set()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==0:
                    q.append([i,j,0])
        
        while q:
            for _ in range(len(q)):
                r,c,d=q.popleft()
                grid[r][c]=min(grid[r][c], d+1)
                for nr,nc in directions:
                    rr,cc=r+nr,c+nc
                    if rr<0 or rr==rows or cc<0 or cc==cols or grid[rr][cc]==-1 or (rr,cc) in visited:
                        continue
                    else:
                        q.append([rr,cc,grid[r][c]])
                        visited.add((rr,cc))
        
        

                    


                






        