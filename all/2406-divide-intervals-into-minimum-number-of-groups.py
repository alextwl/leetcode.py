'''
2024/10/12 daily challenge

min heap approach
'''


import heapq


class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))

        h = []
        max_overlap = 1

        for left, right in intervals:
            while h and h[0] < left:
                heapq.heappop(h)

            heapq.heappush(h, right)
            max_overlap = max(max_overlap, len(h))

        return max_overlap

