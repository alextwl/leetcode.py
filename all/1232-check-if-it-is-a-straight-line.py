'''
2023/06/05 daily challenge

geometry approach
'''

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        def get_slope(x1, y1, x2, y2):
            # a perpendicular's slope is undefined. (delta x = 0)
            if (dx := x2 - x1) == 0:
                return None
            dy = y2 - y1
            return dy / dx

        it = iter(coordinates)
        # get the first coordinate
        first = next(it)
        # get the first 2 coordinates' slope.
        slope = get_slope(*first, *next(it))
        # compare the slope with remaining coordinates.
        for coord in it:
            if get_slope(*first, *coord) != slope:
                return False
        # these points make a straight line in the XY plane.
        return True

