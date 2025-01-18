from typing import List
import heapq
class Solution: 
    #Base on DIJSKTRA's Algorithm.
    def minCost(self, grid: List[List[int]]) -> int:
        num_rows, num_cols = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        # Min-heap ordered by cost. Each element is (cost, row, col)
        pq = [(0, 0, 0)]  # Using list as heap, elements are tuples.

        # minCost stores the min cost to move from [0][0] to [i][j].
        minCost = [[float("inf")] * num_cols for _ in range(num_rows)]
        minCost[0][0] = 0

        while pq:
            cost, row, col = heapq.heappop(pq)
            # Move to neighbor cells of current cells.
            for d, (dx, dy) in enumerate(directions):
                new_row, new_col = row + dx, col + dy
                # Check if next position is in grid.
                if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
                    new_cost = cost + (d != grid[row][col]-1)
                    # Update minCost.
                    if minCost[new_row][new_col] > new_cost:
                        minCost[new_row][new_col] = new_cost
                        heapq.heappush(pq, (new_cost, new_row, new_col))
                        
        return minCost[num_rows-1][num_cols-1]