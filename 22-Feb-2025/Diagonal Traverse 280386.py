# Problem: Diagonal Traverse - https://leetcode.com/problems/diagonal-traverse/

class Solution(object):
    def findDiagonalOrder(self, mat):
        if not mat or not mat[0]:
            return []
        
        m, n = len(mat), len(mat[0])
        diagonals = {}
        
        for row in range(m):
            for col in range(n):
                diag_index = row + col
                if diag_index not in diagonals:
                    diagonals[diag_index] = []
                diagonals[diag_index].append(mat[row][col])
        
        result = []
        
        for key in range(m + n - 1):
            if key % 2 == 0:
                result.extend(reversed(diagonals[key]))
            else:
                result.extend(diagonals[key])  
        
        return result
