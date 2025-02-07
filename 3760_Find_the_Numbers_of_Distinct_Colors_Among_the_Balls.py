from collections import defaultdict
from typing import List
class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        colors = defaultdict(int)
        cnt = 0
        res = {}
        ans = []
        for num, color in queries:
            if num not in res:
                res[num] = color
                # If the color is painted the first time.
                if colors[color] == 0:
                    cnt += 1
            else:
                colors[res[num]] -= 1 # Erase color of the num_th ball.
                if colors[res[num]] == 0: 
                    cnt -= 1
                res[num] = color
                if colors[color] == 0:
                    cnt += 1
            # Update total numbers of the color.
            colors[color] += 1
            ans.append(cnt)
        return ans