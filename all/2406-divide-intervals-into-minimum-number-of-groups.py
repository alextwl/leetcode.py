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


'''
prefix sum approach
'''


class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        events = []  # (time, 1 for left and -1 for right+1)
        for left, right in intervals:
            events.append((left, 1))
            events.append((right + 1, -1))  # note the right is inclusive, so subtract the count at the next time point.
        events.sort()

        prefix_sum = 0
        max_sum = 1  # at least 1 group present
        for _, v in events:
            prefix_sum += v
            max_sum = max(max_sum, prefix_sum)

        return max_sum


'''
line sweep approach
'''


import collections


class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        freq = collections.defaultdict(int)

        for left, right in intervals:
            freq[left] += 1
            freq[right + 1] -= 1

        running_sum = 0
        max_overlap = 1
        for t in sorted(freq.keys()):
            running_sum += freq[t]
            max_overlap = max(max_overlap, running_sum)

        return max_overlap

