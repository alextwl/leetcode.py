'''
2024/12/12 daily challenge

max heap approach
'''


import heapq


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        # build a max heap
        h = []
        for v in gifts:
            heapq.heappush(h, -v)
        # run ops k times
        for _ in range(k):
            v = -h[0]
            if v == 1:
                # shortcut: no need to go further because all elements are already 1.
                break
            heapq.heapreplace(h, -math.isqrt(v))
        return -sum(h)

