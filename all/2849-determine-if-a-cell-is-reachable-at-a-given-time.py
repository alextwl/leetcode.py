'''
2023/11/08 daily challenge

Chebyshev distance approach

https://en.wikipedia.org/wiki/Chebyshev_distance
'''


class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if sx == fx and sy == fy:
            # corner case: beginning & destination is the same cell.
            # we cannot reach the destination if there's only 1 step and
            # it's impossible to move back to the same cell.
            return t != 1

        # Chebyshev distance
        dChess = max(abs(sx - fx), abs(sy - fy))

        return dChess <= t

