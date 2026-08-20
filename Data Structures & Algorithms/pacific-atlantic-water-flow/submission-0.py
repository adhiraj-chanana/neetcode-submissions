class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows=len(heights)
        cols=len(heights[0])
        pacific=set()
        atlantic=set()
        def dfs(i,j, visit, prev):
            if i<0 or j<0 or i==rows or j==cols or heights[i][j]<prev or (i,j) in visit:
                return
            visit.add((i,j))
            dfs(i+1,j,visit,heights[i][j])
            dfs(i-1,j, visit, heights[i][j])
            dfs(i,j+1, visit, heights[i][j])
            dfs(i,j-1, visit, heights[i][j])
        for i in range(rows):
            dfs(i,0,pacific,0)
            dfs(i,cols-1,atlantic, 0)

        for i in range(cols):
            dfs(0,i,pacific,0)
            dfs(rows-1,i,atlantic,0)

        a=pacific & atlantic

        return list(a)
        

        

        



        


                



        
        

        