'''
2023/01/28 daily challenge

Sorted set approach

learnt from official solution 1
'''

import bisect


class SummaryRanges:

    def __init__(self):
        self.values = []  # keep it sorted & no duplication (as a set) manually

    def addNum(self, value: int) -> None:
        '''
        keep the input stream sorted when adding it.
        '''
        i = bisect.bisect_left(self.values, value)
        # if it's not existed, insert it by order
        if i == len(self.values) or self.values[i] != value:
            self.values.insert(i, value)

    def getIntervals(self) -> List[List[int]]:
        if not self.values:
            return []
        
        intervals = []
        left = right = -1
        for val in self.values:
            if left < 0:
                # reset the initial interval to the first value
                left = right = val
            elif val == right + 1:
                '''
                if the upcoming value is consecutive from the last right value,
                we can continue the current interval.
                '''
                right = val
            else:
                '''
                the upcoming value is not consecutive for the current interval.
                we can output (close) the current interval
                and reset the range for the next interval.
                '''
                intervals.append([left, right])
                left = right = val
        # output the last interval
        intervals.append([left, right])

        return intervals

