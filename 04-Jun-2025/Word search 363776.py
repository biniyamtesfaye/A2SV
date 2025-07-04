# Problem: Word search - https://leetcode.com/problems/word-search/

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        if not word:
            return True
        
        for i in range(len(board)): 
            for j in range(len(board[0])): 
                if self.dfs(board, word, i, j): 
                    return True
        return False   
        
    
    def dfs(self, board, word, i, j):
        if board[i][j] == word[0]: 
            if not word[1:]:
                return True
        
            board[i][j] = " " 
        
            if i > 0 and self.dfs(board, word[1:], i - 1, j): 
                return True
            if i < len(board) - 1 and self.dfs(board, word[1:], i + 1, j): 
                return True
            if j > 0 and self.dfs(board, word[1:], i, j - 1): 
                return True
            if j < len(board[0]) - 1 and self.dfs(board, word[1:], i, j + 1): 
                return True
        
            board[i][j] = word[0]
            return False
        else:
            return False