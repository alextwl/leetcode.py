'''
2024/06/17 daily challenge

binary search approach
'''

import math


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for a in range(math.isqrt(c) + 1):
            b = c - a * a
            left, right = 0, b
            while (left <= right):
                mid = (right - left) // 2 + left
                if (sq := mid * mid) == b:
                    # b**2 found
                    return True
                elif sq > b:
                    right = mid - 1
                else:
                    # sq < b
                    left = mid + 1

        return False

