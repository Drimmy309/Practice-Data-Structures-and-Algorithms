from collections import deque
from typing import List
class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m = len(isWater)
        n = len(isWater[0])

        height = [[-1]*n for _ in range(m)]
        dq = deque()

        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    dq.append((i, j))
                    height[i][j] = 0
        # Directions to adjacent cells. 
        adj = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        while dq:
            i, j = dq.popleft()
            for dx, dy in adj:
                _i = i + dx
                _j = j + dy
                if _i < 0 or _i == m or _j < 0 or _j == n or height[_i][_j] != -1:
                    continue
                
                height[_i][_j] = height[i][j] + 1
                dq.append((_i, _j))

        return height