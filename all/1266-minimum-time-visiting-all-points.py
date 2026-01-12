'''
2023/12/03 daily challenge
2026/01/12 daily challenge

custom coordinate distance approach

the distance between A and B is the max difference of x-coord or y-coord.
'''


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        def secondDistance(x1, y1, x2, y2):
            '''
            calculate the distance like Manhattan but following the rules.
            '''
            dx, dy = abs(x1 - x2), abs(y1 - y2)
            return max(dx, dy)
        
        sec = 0
        it = iter(points)
        prev = next(it)
        for curr in it:
            sec += secondDistance(*prev, *curr)
            prev = curr

        return sec


'''
oneliner ver
'''


import itertools


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        return sum(max(abs(x0 - x1), abs(y0 - y1)) for (x0, y0), (x1, y1) in itertools.pairwise(points))

