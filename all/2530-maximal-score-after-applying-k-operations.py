'''
2024/10/14 daily challenge

max heap approach
'''


import heapq


class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heapq.heapify(h := [-v for v in nums])

        score = 0
        for _ in range(k):
            v = -h[0]
            score += v
            heapq.heapreplace(h, -((v + 2) // 3))

        return score

