from typing import List
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        #Count servers in ROWs and COLUMNs
        serCol, serRow = [0]*n, [0]*m
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    serCol[i] += 1
                    serRow += 1
        ans = sum(x for x in serCol if x > 1)
        
        #Remove intersections of row and column in the grid.
        for i in range(m):
            if serRow[i] <= 1: continue
            else: ans += serRow[i]
            for j in range(n):
                if grid[i][j] == 1 and serCol[j] > 1: ans -= 1
        return ans
