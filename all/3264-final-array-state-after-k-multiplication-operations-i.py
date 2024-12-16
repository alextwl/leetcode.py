'''
2024/12/16 daily challenge

min heap approach
'''

import heapq


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        if multiplier == 1:
            return nums
        h = []  # (v, i)
        for i, v in enumerate(nums):
            heapq.heappush(h, (v, i))
        for _ in range(k):
            v, i = h[0]
            v *= multiplier
            nums[i] = v
            heapq.heapreplace(h, (v, i))
        return nums

