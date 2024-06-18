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


'''
binary search approach
'''


class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        job_profit = sorted([d, p] for d, p in zip(difficulty, profit))

        # override profits of each job if there's an easier but more profitable job
        n = len(job_profit)
        max_profit = job_profit[0][1]
        for i in range(n):
            max_profit = job_profit[i][1] = max(max_profit, job_profit[i][1])

        # do binary search for each worker
        total_profit = 0
        for ability in worker:
            left, right = 0, n - 1

            # find the most difficult job the current worker can do.
            # the profit is already maximized.
            worker_profit = 0
            while(left <= right):
                mid = (right - left) // 2 + left
                if job_profit[mid][0] <= ability:
                    worker_profit = max(worker_profit, job_profit[mid][1])
                    left = mid + 1
                else:
                    right = mid - 1

            total_profit += worker_profit

        return total_profit

