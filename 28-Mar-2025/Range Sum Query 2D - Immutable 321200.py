# Problem: Range Sum Query 2D - Immutable - https://leetcode.com/problems/range-sum-query-2d-immutable/

prefix = []

class NumMatrix:
    
    def __init__(self, matrix: List[List[int]]):
        self.prefix = matrix
        n, m = len(matrix), len(matrix[0])
        for i in range(n):
            for j in range(1, m):
                self.prefix[i][j] += self.prefix[i][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = 0
        for i in range(row1, row2+1):
            ans += (self.prefix[i][col2] - (self.prefix[i][col1-1] if col1 != 0 else 0))
        return ans