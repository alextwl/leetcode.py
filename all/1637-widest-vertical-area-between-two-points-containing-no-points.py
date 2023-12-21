'''
2023/12/21 daily challenge

just find the maximum difference between each consecutive x-coordinates.
'''


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x_points = [x for x, _ in points]
        x_points.sort()
        
        max_width = 0
        prev = x_points[0]
        
        for x in x_points:
            diff = x - prev
            if diff and diff > max_width:
                max_width = diff
            prev = x

        return max_width

