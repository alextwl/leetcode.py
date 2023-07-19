'''
2023/07/19 daily challenge

greedy algorithm for scheduling approach

always keep the interval with an earlier endtime and
we can maximize the number of non-overlapping intervals.
(== minimize the removal of overlapped intervals)

learnt from the official solution
https://leetcode.com/problems/non-overlapping-intervals/solution/
'''


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort by endtime
        intervals.sort(key=lambda t:t[1])

        last_endtime = float('-inf')
        removals = 0

        for start, end in intervals:
            if start >= last_endtime:
                # case 1: the interval can be scheduled because
                # its start time is equal or next to the last interval's endtime.
                last_endtime = end
            else:
                # start < last_endtime
                # case 2: it overlaps the last interval, we need to remove it.
                removals += 1

        return removals

