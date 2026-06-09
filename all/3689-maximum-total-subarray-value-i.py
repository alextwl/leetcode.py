'''
2026/06/09 daily challenge

greedy method approach

since a subarray could be chosen more than once,
just choose the same subarray with max values, k times.
'''


class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        return (max(nums) - min(nums)) * k

