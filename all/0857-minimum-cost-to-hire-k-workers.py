'''
2024/05/11 daily challenge

max heap approach

learnt from official solution:
https://leetcode.com/problems/minimum-cost-to-hire-k-workers/solution/
'''

import heapq


class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        # note the wage is the minimum wage of each worker.
        # quality[i]/quality[j] == wage_paid[i]/wage_paid[j]
        # quality[i]/sum(quality) == the wage ratio for worker i.
        n = len(quality)
        min_cost = float('inf')

        # wage/quality ratio in ascending order
        wq_ratio = [(w/q, q) for w, q in zip(wage, quality)]
        wq_ratio.sort()

        # max heap for highest quality values
        h = []

        total_quality = 0
        for ratio, q in wq_ratio:
            # the ratio is the highest wage-to-quality ratio until now,
            # we use it to compute the cost of current worker group.
            #
            # always pick the current worker.
            heapq.heappush(h, -q)
            total_quality += q

            # remove highest quality if the number of selected workers exceeded k
            if len(h) > k:
                # the value to be popped is negative, equivalent to remove it from total_quality.
                total_quality += heapq.heappop(h)

            # exact k workers selected, calculate the cost
            if len(h) == k:
                min_cost = min(min_cost, total_quality * ratio)

        return min_cost

