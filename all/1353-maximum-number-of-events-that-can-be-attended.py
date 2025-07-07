'''
2025/07/07 daily challenge

greedy method + min heap approach

learnt from official editorial:
https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/editorial/#approach-greedy

iterate all possible days and queue events.
'''


import heapq


class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        last_day = max(endDay for _, endDay in events)
        events.sort()

        h = []
        attended = 0
        i = 0  # index of last event to be queued
        # iterate all days
        for curr_day in range(1, last_day + 1):
            # queue all possible events started on and before curr_day
            while i < n and events[i][0] <= curr_day:
                heapq.heappush(h, events[i][1])
                i += 1
            # pop all events ended prior to curr_day
            while h and h[0] < curr_day:
                heapq.heappop(h)
            # attend an event
            if h:
                heapq.heappop(h)
                attended += 1

        return attended

