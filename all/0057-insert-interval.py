'''
2023/01/16 daily challenge
2024/03/17 daily challenge

binary search approach (refined ver)
'''


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newStart, newEnd = newInterval
        
        # binary search
        left, right = 0, len(intervals) - 1
        
        # let right index pointing a position which is left to the newInterval.
        while (left <= right):
            mid = left + (right - left) // 2
            mid_val = intervals[mid]
            
            if mid_val[1] < newStart:
                left = mid + 1
            else:
                right = mid - 1

        # the last interval which is not overlapped in the left slice
        prefix_end_idx = right
        # merge middle slice
        for i in range(prefix_end_idx + 1, len(intervals)):
            if newEnd < intervals[i][0]:
                break
            
            newStart = min(newStart, intervals[i][0])
            newEnd = max(newEnd, intervals[i][1])
        else:
            # the new interval overlaps the end of intervals
            i = len(intervals)

        return intervals[:prefix_end_idx+1] + [[newStart, newEnd]] + intervals[i:]

