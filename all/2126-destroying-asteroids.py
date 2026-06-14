'''
2026/05/31 daily challenge

min heap approach
'''


import heapq


class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        h = []
        for a in asteroids:
            if mass >= a:
                mass += a
            else:
                # cannot destroy, push to the heap and check later
                heapq.heappush(h, a)
            # try again
            while h and mass >= h[0]:
                mass += heapq.heappop(h)

        return not h

