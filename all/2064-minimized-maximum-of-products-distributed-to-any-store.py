'''
2024/11/14 daily challenge

greedy method + max heap approach

splitting the product with largest ratio of its quantity to the amount of assigned stores
is always optimal.

Runtime: 4490 ms, faster than 10.86% of Python3 online submissions
'''


import heapq
import math


class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        h = []  # (ratio of quantity to assigned store, quantity, assigned store)
        for q in quantities:
            # init with assigning each type of product to single store
            heapq.heappush(h, (-q, q, 1))
        
        # fill remaining stores by evenly splitting a type of product with largest ratio
        for _ in range(n - len(quantities)):
            _, q, p = h[0]
            p += 1  # add one more store
            heapq.heapreplace(h, (-(q/p), q, p))
        
        return math.ceil(-h[0][0])

