from typing import List
from collections import deque
class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        def bfs(startNode: int, visitedNodes: set, reversedGraph: List[List[int]]):
            # Store nodes and its distance from start node.
            dq = deque([(startNode, 0)])
            max_distance = 0
            while dq:
                curNode, curDis = dq.popleft()
                # Visit neighbor nodes of current node.
                for neighbor in reversedGraph[curNode]:
                    if neighbor in visitedNodes:
                        continue
                    dq.append((neighbor, curDis + 1))
                max_distance = max(max_distance, curDis)
            return max_distance
        
        n = len(favorite) # number of people.
        reversedGraph = [[] for _ in range(n)]
        for person in range(n):
            reversedGraph[favorite[person]].append(person) # Points to its admirers
        
        twoCycle, longestCycle = 0, 0
        visited = [False] * n
        for person in range(n):
            if not visited[person]:
                distance, cur_person = 0, person
                # Key: person  Value: Distance from current person to person.
                visited_person = {}
                while True:
                    if visited[cur_person]:
                        break
                    visited[cur_person] = True
                    visited_person[cur_person] = distance
                    distance += 1
                    next_person = favorite[cur_person]
                    # Detect cycle.
                    if next_person in visited_person:
                        cycleLen = distance - visited_person[next_person]
                        longestCycle = max(longestCycle, cycleLen)
                        # Handle Case 2-Cycle.
                        if cycleLen == 2:
                            # Start Nodes are 2 heads of 2-cycle.
                            twoCycle += (
                                2
                                + bfs (
                                    cur_person, {cur_person, next_person}, reversedGraph
                                )
                                + bfs (
                                    next_person, {cur_person, next_person}, reversedGraph
                                )
                            )
                        break
                    cur_person = next_person
        return max(longestCycle, twoCycle)

                