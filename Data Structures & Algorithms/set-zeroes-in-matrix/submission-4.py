class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows=len(matrix)
        cols=len(matrix[0])
        def dfs(i,j):
            for y in range(rows):
                if matrix[y][j]==0:
                    continue
                matrix[y][j]='X'
            for y in range(cols):
                if matrix[i][y]==0:
                    continue
                matrix[i][y]='X'
            
        

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]==0:
                    dfs(i,j)
 
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]=='X':
                    matrix[i][j]=0
        
        
        


        
        