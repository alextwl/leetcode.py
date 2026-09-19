'''
2026/09/19 daily challenge

geometry approach

learnt from official editorial 2:
https://leetcode.com/problems/circle-and-rectangle-overlapping/editorial/?envType=daily-question&envId=2026-09-19#approach-2-minimum-distance-from-the-circles-center-to-the-rectangle

find the minimum distance from circle's center to boundaries of the rectangle,
and test if it's smaller than the radius or not.
'''


class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        dist = 0  # square of the minimum distance
        if xCenter < x1 or xCenter > x2:
            # center of the circle is in the left/right side of the rectangle boundaries
            dist += min((x1 - xCenter) ** 2, (x2 - xCenter) ** 2)
        if yCenter < y1 or yCenter > y2:
             # center of the circle is upper/lower than the rectangle boundaries
            dist += min((y1 - yCenter) ** 2, (y2 - yCenter) ** 2)
        return dist <= radius ** 2

