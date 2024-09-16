'''
2024/09/16 daily challenge

sorting approach

convert time points to minutes and sort it.
'''


import itertools


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = [int(t[:2]) * 60 + int(t[3:]) for t in timePoints]
        minutes.sort()
        
        min_diff = min(t1 - t0 for t0, t1 in itertools.pairwise(minutes))
        # min_diff vs the last point ~ the first point
        min_diff = min(min_diff, 1440 - minutes[-1] + minutes[0])
        return min_diff

