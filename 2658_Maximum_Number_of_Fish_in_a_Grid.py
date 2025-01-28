from typing import List
from collections import deque
class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m, n, ans = len(grid), len(grid[0]), 0
        visited = [[False]*n for _ in range(m)]
        # Directs to adjacent cells
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        # Return total fish fisher can catch if starting at the cell.
        def in_grid(r, c) -> bool: return r >= 0 and r < m and c >= 0 and c < n
        def Try(startRow, startCol) -> int:
            totalFish = grid[startRow][startCol]
            dq = deque([(startRow, startCol)])
            while dq:
                curRow, curCol = dq.popleft()
                for dx, dy in directions:
                    nextRow, nextCol = curRow + dx, curCol + dy
                    if in_grid(nextRow, nextCol) and grid[nextRow][nextCol] > 0 and not visited[nextRow][nextCol]:
                        totalFish += grid[nextRow][nextCol]
                        visited[nextRow][nextCol] = True
                        dq.append((nextRow, nextCol))
            return totalFish
        for r in range(m):
            for c in range(n):
                if not visited[r][c] and grid[r][c] > 0: 
                    visited[r][c] = True
                    ans = max(ans, Try(r, c))         
        return ans