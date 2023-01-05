'''
2023/01/05 daily challenge

interval overlapping approach
'''

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # sort by xStart first.
        points.sort()

        # set initial shot position to xEnd of the first point.
        arrows = 1
        currEnd = points[0][1]

        for start, end in points:
            if currEnd >= start:
                '''
                overlap found, try to adjust currEnd to a more suitable coordinate
                where most points overlap.
                '''
                currEnd = min(currEnd, end)  # try to move left
            else:
                '''
                the current position of arrow cannot overlap the previous balloon.
                we need to shoot a new arrow.
                '''
                arrows += 1
                currEnd = end

        return arrows

