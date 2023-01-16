'''
2023/01/16 daily challenge

binary search + merge slices approach
'''

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        n = len(intervals)
        newStart, newEnd = newInterval
        # find left bound by start interval
        left, right = 0, n-1
        while(left <= right):
            mid = (left+right) // 2
            if (midStart := intervals[mid][0]) > newStart:
                right = mid - 1
            elif midStart < newStart:
                left = mid + 1
            else:
                left = mid
                break
        # check if previous interval was overlapped and adjust the position
        leftBound = left
        if leftBound > 0 and intervals[leftBound-1][1] >= newStart:
            leftBound -= 1
        # if the insertion point is already the leftmost terminal
        # and the first interval is not overlapped, just insert it and return.
        if leftBound == 0 and intervals[0][0] > newEnd:
            intervals.insert(0, newInterval)
            return intervals
        # if the insertion point is already the rightmost terminal, just append it.
        if leftBound == n:
            intervals.append(newInterval)
            return intervals

        # time to merge slices
        rightBound = leftBound
        for i in range(leftBound, n):
            iStart, iEnd = intervals[i]
            # check if it's overlapped
            if (min(iEnd, newEnd) - max(iStart, newStart)) >= 0:
                rightBound = i+1  # intervals[i] is to be merged
                newStart = min(newStart, iStart)
                newEnd = max(newEnd, iEnd)
            else:
                break

        return intervals[:leftBound] + [[newStart, newEnd]] + intervals[rightBound:]

