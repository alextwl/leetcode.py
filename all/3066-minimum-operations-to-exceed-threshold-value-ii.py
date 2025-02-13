'''
2025/02/13 daily challenge

min heap approach
'''


import heapq


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        min_excess = 1_000_000_001
        h = []
        for v in nums:
            if v < k:
                heapq.heappush(h, v)
            else:
                min_excess = min(min_excess, v)

        # push at most one num which is greater than or equal to k.
        if min_excess < 1_000_000_001:
            heapq.heappush(h, min_excess)

        steps = 0
        while len(h) >= 2 and h[0] < k:
            x = heapq.heappop(h)
            heapq.heapreplace(h, x * 2 + h[0])
            steps += 1

        return steps

