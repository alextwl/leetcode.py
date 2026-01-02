'''
2026/01/02 daily challenge

set approach
'''


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        seen = set()
        for v in nums:
            if v in seen:
                return v
            seen.add(v)
        return -1  # undefined

