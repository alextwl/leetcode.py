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


'''
2024/11/14 daily challenge

binary search approach

just binary search **the answer** and validate it.
'''


import math


class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def validate(x):
            if x < 1:
                return False

            # validate if products could be distributed
            # when the maximum quantity of a store was x.
            empty_stores = n

            for v in quantities:
                if v > x:
                    empty_stores -= math.ceil(v / x)
                else:
                    empty_stores -= 1

                if empty_stores < 0:
                    return False

            return True

        # binary search the maximum quantity x for a store
        left, right = 0, max(quantities)
        while left < right:
            middle = (left + right) // 2
            if validate(middle):
                # note the middle value is valid, so we shrink the right boundary
                # but we also need to include it (not to right=middle-1) because
                # the middle may also be the minimized answer.
                right = middle
            else:
                # the middle value is too small, need to increase.
                left = middle + 1

        return left

