'''
find recursive pattern instead of simulation.
'''


class Solution:
    def lastRemaining(self, n: int) -> int:
        curr = 1
        step = 1
        arrow = 1  # 1: left to right, 0: right to left

        while n > 1:
            if arrow or n & 1:
                # the current number is going to be eliminated,
                # need to step forward
                curr += step
            step <<= 1
            n >>= 1
            arrow ^= 1
        return curr

