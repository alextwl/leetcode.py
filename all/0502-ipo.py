'''
2023/02/23 daily challenge

greedy + heap approach
learnt from the official solution

use heap to manage available projects and import more projects
after more profits added to the capital w.
'''

from heapq import heappush, heappop


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = list(zip(capital, profits))
        projects.sort()

        q = []  # available projects with sufficient capital
        n = len(projects)
        next_prj = 0

        # do projects
        for _ in range(k):
            # import more projects to the queue
            for i in range(next_prj, n):
                if projects[i][0] > w:
                    break
                heappush(q, -projects[i][1]) # push (negatived) profit of a candidate
                next_prj += 1

            if not q:
                # no more projects can be done
                return w

            # pick one project to do with highest profit
            w -= heappop(q)  # aka w += profit, add profit to current capital

        return w

