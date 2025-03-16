'''
2025/03/16 daily challenge

binary search approach
'''


class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def validate(minutes):
            repaired = 0
            for r in ranks:
                repaired += int((minutes / r) ** 0.5)
                if repaired >= cars:
                    return True
            return False
        
        l, r = 0, max(ranks) * 1_000_000_000_000
        while l <= r:
            mid = (l + r) // 2
            if validate(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l


'''
min heap approach

pick workers with the smallest cost of time.
'''


import collections
import heapq


class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        h = [(r, r, 1, v) for r, v in collections.Counter(ranks).items()]  # (time for next repair, rank, next car, freq)
        heapq.heapify(h)

        while cars > 0:
            t, r, cnt, f = h[0]
            cars -= f  # there're f workers with the same rank, fixing f cars simutaneously.
            cnt += 1
            heapq.heapreplace(h, (r * cnt * cnt, r, cnt, f))
        return t  # total time costed by the last group of workers is the ans

