from collections import deque
from typing import List
class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        if len(nums) == 1: return nums
        sortedNums = sorted(nums)
        groupNum = {}# Classify numbers into groups
        Group = {}# Group[i] contains numbers classified with the ith group.
        cnt = 0 #Index of group

        # Specific Case for 0 index.
        groupNum[sortedNums[0]] = cnt 
        Group[0] = deque([sortedNums[0]])
        if sortedNums[1] - sortedNums[0] > limit:
            cnt += 1 
            
        # Processing Classify
        for i in range(1, len(sortedNums)):
            if sortedNums[i] - sortedNums[i-1] <= limit: 
                groupNum[sortedNums[i]] = cnt 
                Group[cnt].append(sortedNums[i])  
            else:
                cnt += 1
                groupNum[sortedNums[i]] = cnt
                Group[cnt] = deque([sortedNums[i]])
        
        # Assign numbers to nums
        for i in range(len(nums)):
            nums[i] = Group[groupNum[nums[i]]].popleft()
        return nums

