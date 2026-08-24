class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        check=set(['1','2','3','4','5','6','7','8','9'])
        bounds=[3,6,9]
        for i in range(9):
            visited=set()
            for j in range(9):
                if board[i][j]=='.':
                    continue
                if board[i][j] not in check or board[i][j] in visited :
                    print('failing', board[i][j])
                    return False
                visited.add(board[i][j])
        for i in range(9):
            visited=set()
            for j in range(9):
                if board[j][i]=='.':
                    continue
                if board[j][i] not in check or board[j][i] in visited:
                    return False
                visited.add(board[j][i])
        # print('boxes')
        for i in bounds:
            for j in bounds:
                visited=set()
                for x in range(i-3,i):
                    
                    for y in range(j-3,j):
                        # print(x,y, board[x][y])
                        if board[x][y]=='.':
                            continue    
                        if board[x][y] not in check or board[x][y] in visited:
                            return False
                        visited.add(board[x][y])
                # print('box finished')

        return True


            

        

        

                



        