# Problem: Toeplitz matrix - https://leetcode.com/problems/toeplitz-matrix/description/

class Solution:
    def isToeplitzMatrix(self, matrix):
        rows, cols = len(matrix), len(matrix[0])

        for i in range(rows - 1):
            for j in range(cols - 1):
                if matrix[i][j] != matrix[i + 1][j + 1]:
                    return False

        return True