# Problem: Unique Paths III - https://leetcode.com/problems/unique-paths-iii/

class Solution:
    def uniquePathsIII(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        total = 0
        start_r = start_c = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != -1:
                    total += 1
                if grid[i][j] == 1:
                    start_r, start_c = i, j
        
        self.paths = 0
        
        def dfs(r, c, visited_count):
            if not (0 <= r < m and 0 <= c < n) or grid[r][c] == -1:
                return
            if grid[r][c] == 2:
                if visited_count == total:
                    self.paths += 1
                return
            temp = grid[r][c]
            grid[r][c] = -1
            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                dfs(r + dr, c + dc, visited_count + 1)
            grid[r][c] = temp
        dfs(start_r, start_c, 1)
        
        return self.paths