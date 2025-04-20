# Problem: Minesweeper - https://leetcode.com/problems/minesweeper/

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        directions = [[1,0], [1,1], [0,1], [-1,1], [-1,0], [-1,-1], [0,-1], [1,-1]]

        def count_bomb_neighbor(row, col):
            counter = 0
            for i_row, i_col in directions:
                if 0<=row+i_row<len(board) and 0<=col+i_col<len(board[0]) and board[row+i_row][col+i_col] == 'M':
                    counter+=1
            return counter

        def search_neighbor(row, col):
            for i_row, i_col in directions:
                if 0<=row+i_row<len(board) and 0<=col+i_col<len(board[0]) and board[row+i_row][col+i_col] == 'E':
                    helper(row+i_row, col+i_col)  


        def helper(row, col):
            if board[row][col] == 'M':
                board[row][col] = 'X'

            elif board[row][col] == 'E':
                counter = count_bomb_neighbor(row, col)
                if counter:
                    board[row][col] = str(counter)
                else:
                    board[row][col] = 'B'
                    search_neighbor(row, col)       
        helper(click[0], click[1])
        return board