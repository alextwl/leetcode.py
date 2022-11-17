'''
2022/11/17 daily challenge

union area = area(A+B) - overlap

since the problem has defined the coordinates of the corners,
the coordinate name with '2' suffix in the same rectangle is
always greater than the name with '1' suffix. (e.g. ax2 > ax1)
'''

class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        # calculate the area of rectangles
        area_a = (ax2-ax1) * (ay2-ay1)
        area_b = (bx2-bx1) * (by2-by1)
        
        # calculate the overlaps
        overlap_x = min(ax2, bx2) - max(ax1, bx1)
        overlap_y = min(ay2, by2) - max(ay1, by1)
        if overlap_x > 0 and overlap_y > 0:
            area_overlap = overlap_x * overlap_y
        else:
            # these rectangles are not overlapped.
            area_overlap = 0
        
        return area_a + area_b - area_overlap

