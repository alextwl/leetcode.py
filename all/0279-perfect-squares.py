'''
dynamic programming approach

try to minimize the number of perfect squares that sum to n.
if n itself was already a perfect square, then the least number is 1.

since there's 1 <= n <= 10**4 constraint,
pre-calculating perfect squares <= 10**4 in advance is reasonable in order to speedup.
'''

SQUARES = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100,
            121, 144, 169, 196, 225, 256, 289, 324,
            361, 400, 441, 484, 529, 576, 625, 676,
            729, 784, 841, 900, 961, 1024, 1089,
            1156, 1225, 1296, 1369, 1444, 1521,
            1600, 1681, 1764, 1849, 1936, 2025,
            2116, 2209, 2304, 2401, 2500, 2601,
            2704, 2809, 2916, 3025, 3136, 3249,
            3364, 3481, 3600, 3721, 3844, 3969,
            4096, 4225, 4356, 4489, 4624, 4761,
            4900, 5041, 5184, 5329, 5476, 5625,
            5776, 5929, 6084, 6241, 6400, 6561,
            6724, 6889, 7056, 7225, 7396, 7569,
            7744, 7921, 8100, 8281, 8464, 8649,
            8836, 9025, 9216, 9409, 9604, 9801, 10000]


class Solution:
    def numSquares(self, n: int) -> int:
        '''
        dp[n] = the least number of perfect squares.
        '''
        dp = [0]
        for i in range(1, n+1):
            '''
            try to subtract all possible perfect squares <= i,
            find the minimum and plus 1.

            note: dp[-sq] == dp[i-sq]
            '''
            dp.append(min([dp[-sq] for sq in SQUARES if sq <= i]) + 1)

        return dp[-1]


'''
2022/11/22 daily challenge

math approach

learnt from
https://leetcode.com/problems/perfect-squares/discuss/71488/Summary-of-4-different-solutions-(BFS-DP-static-DP-and-mathematics)
'''

import math


class Solution:
    def numSquares(self, n: int) -> int:
        '''
        according to Lagrange's four-square theorem:
        https://en.wikipedia.org/wiki/Lagrange%27s_four-square_theorem
        
        `every` natural number p can be represented as the sum of 4 integer (a0~a3) squares.
        p = a0**2 + a1**2 + a2**2 + a3**3
        
        also referring to Legendre's three-square theorem:
        https://en.wikipedia.org/wiki/Legendre%27s_three-square_theorem
        
        a natural number n may be represented as:
        n = x**2 + y**2 + z**2
        
        if and only if n is not of the form
        n = 4**a * (8*b + 7) with non-negative integer a & b.
        
        so, if n couldn't be represented as a perfect square, a two-square, or a three-square,
        we can comfortably say n can be represented as a four-square
        and the least number of perfect square numbers is 4.
        '''
        # python >= 3.8: fast nearest integer square root by Newton's iteration.
        isSquare = lambda n: n == math.isqrt(n)**2
        
        if isSquare(n):
            # n is already a perfect square.
            return 1

        '''
        check if n could fit in x**2 + y**2 (two-square)

        note: two-square check may be done after four-square check with n evenly divided by 4 (n >>= 2)
        as the original solution by davidtan1890 & zhukov.

        See "Computing sum of squares when the factorization is not known"
        explanation by Dario Alejandro Alpern
        https://www.alpertron.com.ar/4SQUARES.HTM

        s = a**2 + b**2 + c**2 + d**2
        n = (4**r) * s = (2**r * a)**2 + (2**r * b)**2 + (2**r * c)**2 + (2**r * d)**2
       
        where some variables can be equal to zero.
        '''
        for i in range(1, math.isqrt(n) + 1):
            if isSquare(n - i**2):
                # n can be represented as a two-square
                return 2

        '''
        check if it's an exception from Legendre's three-square by
        n = 4**a * (8*b + 7)
        '''
        while((n & 3) == 0):
            n >>= 2
        if (n & 7) == 7:
            # the least number is Lagrange's four-square.
            return 4
        
        '''
        now we can comfortably say n can be represented as a three-square.

        n is neither a perfect square and a two-square sum,
        but is a Legendre's three-square sum.
        '''
        return 3

