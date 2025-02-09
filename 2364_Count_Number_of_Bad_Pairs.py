class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        ans = 0
        diff = {}

        for pos in range(len(nums)):
            pairVal = pos - nums[pos]

            # Check if value of the pair occurs or not.
            # If not, return 0.
            good_pair = diff.get(pairVal, 0)

            # Total number of bad pairs at this position.
            # Equal to total pairs - good pairs.  
            ans += pos - good_pair

            diff[pairVal] = good_pair + 1 # Update numbers of good pair.
        return ans