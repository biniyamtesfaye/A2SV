# Problem: Maximum Sum of an Hourglass - https://leetcode.com/problems/maximum-sum-of-an-hourglass/

class Solution(object):
    def isBound(self, r, c, rows, cols):
        return 0 <= r < rows and 0 <= c < cols
    def isHourglass(self, r, c, rows, cols):
        return 1 <= r < rows -1 and 1 <= c < cols - 1
    
    def maxSum(self, grid):
        directions = {
            (-1, -1), (-1,0), (-1, 1),(1,-1),(1,0),(1,1),(0,0)
            }
        rows, cols = len(grid), len(grid[0])
        max_sum = float('-inf')
        for r in range(rows):
            for c in range(cols):
                if self.isHourglass(r, c,rows,cols):
                    hourglass = [
                        grid[r + dx][c + dy]
                        for dx, dy in directions
                        if self.isBound(r + dx, c + dy, rows, cols)
                    ]
                    hourglass_sum = sum(hourglass)

                    max_sum = max(max_sum, hourglass_sum)

        return max_sum

        