# Problem: Game of Life - https://leetcode.com/problems/game-of-life/description/

class Solution:
    def gameOfLife(self, board):
        m, n = len(board), len(board[0])
        directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

        #apply rules using the encoding trick
        for i in range(m):
            for j in range(n):
                live_neighbors = 0
                
                #count live neighbors
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < m and 0 <= nj < n and abs(board[ni][nj]) == 1:
                        live_neighbors += 1
                
                #apply game rules
                if board[i][j] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[i][j] = -1  #alive to Dead
                elif board[i][j] == 0 and live_neighbors == 3:
                    board[i][j] = 2   #dead to Alive
        
        #convert encoding back to 0 or 1
        for i in range(m):
            for j in range(n):
                if board[i][j] > 0:
                    board[i][j] = 1
                else:
                    board[i][j] = 0
