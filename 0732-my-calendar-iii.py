'''
2022/10/07 daily challenge

learnt from official solution

sweep-line algorithm

it's difficult to understand the description of the problem,
the actual goal is to find the max k events of intersections.
'''

from collections import defaultdict


class MyCalendarThree:

    def __init__(self):
        '''
        official imports 3rd-party sortedcontainers.SortedDict
        which sorts the dict at assignment is much faster
        than sorted(self.diff.keys()).
        '''
        self.diff = defaultdict(lambda:0)

    def book(self, start: int, end: int) -> int:
        self.diff[start] += 1
        self.diff[end] -= 1

        '''
        scan the diff array and record max k
        '''
        diffsum = 0
        kmax = 0
        
        for t in sorted(self.diff.keys()):
            diffsum += self.diff[t]
            kmax = max(kmax, diffsum)
        
        return kmax

