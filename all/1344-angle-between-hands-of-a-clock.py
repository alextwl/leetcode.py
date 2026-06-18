'''
2026/06/18 daily challenge

determine the position of hour & minute hands in the range of [0.0, 360.0),
and return smaller non-negative difference between them.
'''


class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hh_angle = (hour % 12) * 30.0 + minutes * 0.5
        mm_angle = minutes * 6.0

        d0 = hh_angle - mm_angle
        if d0 < 0.0:
            d0 += 360.0
        d1 = mm_angle - hh_angle
        if d1 < 0.0:
            d1 += 360.0

        return min(d0, d1)

