'''
2025/10/02 daily challenge
'''


class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles

        while numBottles >= numExchange:
            numBottles -= numExchange - 1
            ans += 1  # drink
            numExchange += 1

        return ans


'''
math approach

learnt from official editorial 2:
https://leetcode.com/problems/water-bottles-ii/editorial/#approach-2-mathematics

t = max number of times exchanging empty bottles.

         t-1                                           (t - 1)
empty = sigma(numExchange + i) = t * numExchange + t * -------
         i=0                                              2

total = numBottles + t

empty <= total

empty - total <= 0

                      (t - 1)
t * numExchange + t * ------- - (numBottles + t) <= 0
                         2

t * 2 * numExchange + t * (t - 1) - 2 * numBottles - 2 * t <= 0

t * 2 * numExchange + t**2 - t - 2 * numBottles - 2 * t <= 0

t**2 + (2 * numExchange - 3) * t - 2 * numBottles <= 0

                     -b [+-] sqrt(b**2 - 4ac)
use ax**2 + bx + c = ------------------------ formula to solve for t.
                               2a
'''


import math


class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        # coefficients of quadratic formula
        a = 1                    # t**2
        b = 2 * numExchange - 3  # (2 * numExchange - 3) * t
        c = -(2 * numBottles)

        bsq_4ac = b ** 2 - 4 * a * c
        t = math.ceil((-b + bsq_4ac ** 0.5) / (2 * a))

        return numBottles + t - 1  # max i is (t - 1), see sigma param

