from typing import List
from collections import deque
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # Create directed graph.
        graph = [[] for _ in range(numCourses)]
        for x, y in prerequisites:
            graph[x].append(y)
        

        # Using BFS finds path from ui -> vi in queries.
        def hasPath(startNode, endNode) -> bool:
            visited = set([startNode])
            dq = deque([startNode])
            while dq:
                curNode = dq.popleft()
                for neighbor in graph[curNode]:
                    if neighbor in visited: 
                        continue
                    visited.add(neighbor)
                    if neighbor == endNode: return True
                    dq.append(neighbor)
            return False
        
        ans = []
        for x, y in queries:
            ans.append(hasPath(x, y))
        return ans