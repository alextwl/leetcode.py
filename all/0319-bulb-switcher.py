'''
2023/04/27 daily challenge

learnt from
https://leetcode.com/problems/bulb-switcher/solutions/3459024/python-java-c-simple-solution-one-line/

note when n >= 3 >= i, for the i-th round, we toggle every i bulb (e.g. i-th, 2i-th, 3i-th, ...)
and by observing the values, a bulb i will be on at the end if and only if i is a perfect square.
'''

import math


class Solution:
    def bulbSwitch(self, n: int) -> int:
        return math.isqrt(n)

