'''
2024/06/18 daily challenge

min heap approach
'''

import heapq


class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        h = []  # min heap: (difficulty, profit) for each job
        for d, p in zip(difficulty, profit):
            heapq.heappush(h, (d, p))

        # the max profit of a job
        # since one job could be completed multiple times,
        # let all workers do their most profitable job.
        max_job_profit = 0

        total_profit = 0
        for ability in sorted(worker):
            while (h and h[0][0] <= ability):
                max_job_profit = max(max_job_profit, heapq.heappop(h)[1])

            total_profit += max_job_profit

        return total_profit

