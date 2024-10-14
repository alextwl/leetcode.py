'''
2024/10/14 daily challenge

max heap approach
'''


import heapq


class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        h = []
        for v in nums:
            heapq.heappush(h, -v)

        score = 0
        for _ in range(k):
            v = -heapq.heappop(h)
            score += v
            heapq.heappush(h, -((v + 2) // 3))  # ceiling
        return score

