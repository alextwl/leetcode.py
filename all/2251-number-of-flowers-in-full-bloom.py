'''
2023/10/11 daily challenge

min heap approach
'''

import heapq


class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        flowers.sort()

        time_blossom = {}
        h = []  # the heap queue containing all flowers are in full bloom.

        # the index of next flower's full bloom time range to be proceeded
        i = 0
        for t in sorted(set(people)):
            while i < len(flowers) and flowers[i][0] <= t:
                # push the flower with its end time in full bloom
                heapq.heappush(h, flowers[i][1])
                i += 1

            # pop flowers faded
            while h and h[0] < t:
                heapq.heappop(h)

            time_blossom[t] = len(h)

        ans = [time_blossom[t] for t in people]

        return ans

