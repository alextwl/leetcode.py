'''
check intersections for all coordinates.
'''

class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        overlap_x = min(rec1[2], rec2[2]) - max(rec1[0], rec2[0])  # min(x2) - max(x1)
        overlap_y = min(rec1[3], rec2[3]) - max(rec1[1], rec2[1])  # min(y2) - max(y1)
        return overlap_x > 0 and overlap_y > 0

