'''
2026/07/15 daily challenge

prefix sums + table lookup method approach
'''


import itertools
import math


SUM_ODDS = list(itertools.accumulate(range(1, 2001, 2), initial=0))
SUM_EVENS = list(itertools.accumulate(range(2, 2001, 2), initial=0))


class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        return math.gcd(SUM_ODDS[n], SUM_EVENS[n])


'''
euclidean algorithm approach

sum_odd = 1 + 3 + 5 + ... + (2*n + 1) = n**2
sum_even = 2 + 4 + 6 + ... + 2*n = n * (n + 1)
'''


class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)
        return gcd(n * n, n * (n + 1))


'''
pattern observation approach

for each pair of n:
sum_odds = [1, 4, 9, 16, 25, ...]
sum_evens = [2, 6, 12, 20, 30, ...]
gcd_ans = [1, 2, 3, 4, 5, ...]

gcd(n**2, n * (n + 1)) = n * gcd(n, n + 1) = n * 1 = n
because all (n, n+1) pairs are always coprime.
'''


class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        return n

