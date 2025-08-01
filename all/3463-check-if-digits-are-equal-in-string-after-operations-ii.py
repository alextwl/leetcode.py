'''
brute-force build pascal's triangle reversely (TLE)
'''


import itertools


class Solution:
    def hasSameDigits(self, s: str) -> bool:
        curr = [0] * (len(s) - 1)
        for i, (a, b) in enumerate(itertools.pairwise(map(int, s))):
            curr[i] = (a + b) % 10
        
        prev = curr
        curr = [0] * (len(s) - 2)
        for i in range(len(curr), 1, -1):
            for j in range(i):
                curr[j] = (prev[j] + prev[j + 1]) % 10
            prev, curr = curr, prev

        return prev[0] == prev[1]


'''
binomial coefficients & combinatorial approach

learnt from @VehicleOfPuzzle's good explanation:
https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-ii/solutions/6458127/how-to-notice-that-it-s-pascal-s-triangle-and-compute-it-if-you-re-not-a-mathematician

use mod 2 & mod 5 because there's no multiplicative inverse mod 10 for even numbers & 5.
'''


INV = {1: 1, 3: 7, 7: 3, 9: 9}  # pairs of multiplicative inverse mod 10


def mul(a, b):
    return (a[0] + b[0], a[1] + b[1], (a[2] * b[2]) % 10)


def div(a, b):
    return (a[0] - b[0], a[1] - b[1], (a[2] * INV[b[2]]) % 10)


def solve(s, coe):
    return sum((a * b) % 10 for a, b in zip(map(int, s), coe)) % 10


# powers of 2 with a positive exponent end with 2, 4, 8, 6, 2, 4, 8, 6, ... ad infinitum.
TWOS = [2, 4, 8, 6]
# all positive exponents of powers of 5 ends with 5.
FIVES = [5]


def simplify(v2, v5, res):
    if v2:
        res = (res * TWOS[(v2 - 1) % 4])
    if v5:
        res = (res * 5) % 10  # == (res * FIVES[(v5 - 1) % len(FIVES)]) % 10
    return res


class Solution:
    def hasSameDigits(self, s: str) -> bool:
        n = len(s) - 2

        facts = [(0, 0, 1)]  # (v2, v5, res)
        while n >= len(facts):
            num = len(facts)
            v2 = 0
            while num % 2 == 0:
                num //= 2
                v2 += 1
            v5 = 0
            while num % 5 == 0:
                num //= 5
                v5 += 1
            facts.append(mul(facts[-1], (v2, v5, num)))

        pascals = []
        for k in range(n + 1):
            pascals.append(simplify(*div(div(facts[n], facts[k]), facts[n - k])))

        a = solve(s, pascals)
        b = solve(s[1:], pascals)

        return a == b

