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


'''
fermat's theorem approach

learnt from official solution 5:
https://leetcode.com/problems/sum-of-square-numbers/solution/

Ref.:
https://en.wikipedia.org/wiki/Fermat%27s_theorem_on_sums_of_two_squares
'''


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i = 2
        while (i * i <= c):
            count = 0
            if (c % i == 0):
                while (c % i == 0):
                    count += 1
                    c //= i
                # check if every prime of the form (4k + 3)
                # occurs an even number of times.
                if (i % 4 == 3 and count % 2 != 0):
                    # odd number of times
                    # a counterexample found, impossible to form a**2 + b**2
                    return False
            i += 1

        return c % 4 != 3

