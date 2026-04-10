'''
consider only the maximum & minimum,
try to minimize their's difference.
'''


class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        diff = max(nums) - min(nums)
        if diff <= k * 2:
            return 0
        return diff - k * 2

