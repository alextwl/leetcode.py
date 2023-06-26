'''
2023/06/26 daily challenge

min heap approach
'''

from heapq import heappush, heappop, heapify


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        ans = 0
        
        # initial break the tie sessions
        session = 0
        left = candidates
        right = n - 1 - candidates
        if left <= right:
            h1, h2 = [], []
            for v in costs[:candidates]:
                heappush(h1, v)
            for v in costs[-candidates:]:
                heappush(h2, v)

            # time to hire k workers
            for session in range(k):
                if left > right:
                    break

                # note for the same lowest cost of workers,
                # we always choose h1 because the smallest index first.
                if h1[0] <= h2[0]:
                    ans += heappop(h1)
                    heappush(h1, costs[left])
                    left += 1
                else:
                    ans += heappop(h2)
                    heappush(h2, costs[right])
                    right -= 1
            else:
                # enough workers hired
                return ans
            
            # combine the left & right heaps into one, and continue remaining session
            for v in h2:
                heappush(h1, v)
            h = h1
        else:
            # no need to break the tie, heapify the costs
            h = costs
            heapify(h)

        # proceed remaining sessions to hire
        for _ in range(session, k):
            ans += heappop(h)

        return ans

