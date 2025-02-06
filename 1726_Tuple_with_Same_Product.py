from typing import List
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        # res stores frequency of occurrance of the product
        # of 2 elements of nums.
        res = {}
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                val = nums[i] * nums[j]
                if val not in res: res[val] = 1
                else: res[val] += 1
        ans = 0
        for key in res:
            if res[key] >= 2:
                #Permutation of 2 elements from n elements: n*(n-1)
                ans += 2*2*res[key]*(res[key] - 1)
        return ans
