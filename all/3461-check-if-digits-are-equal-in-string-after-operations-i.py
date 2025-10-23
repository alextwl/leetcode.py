'''
2025/10/23 daily challenge

small input version of problem 3463
'''


import itertools


class Solution:
    def hasSameDigits(self, s: str) -> bool:
        n = len(s)
        prev = list(map(int, s))
        for _ in range(n, 2, -1):
            curr = []
            for a, b in itertools.pairwise(prev):
                curr.append((a + b) % 10)
            prev = curr
        return prev[0] == prev[1]


'''
reversed Pascal's triangle approach

cauculate binomial coefficients by built-in combinatorial function
'''


import math


class Solution:
    def hasSameDigits(self, s: str) -> bool:
        n = len(s)
        d = list(map(int, s))

        '''
        build the last row's binomial coefficients:
         n-2
        C
         i
        '''
        full_coeff = [math.comb(n - 2, i) for i in range(n - 1)]
        # left = C[0] * d[0] + C[1] * d[1] + ... + C[-2] * d[-3] + C[-1] * d[-2]
        left = sum(coe * dig for coe, dig in zip(full_coeff, d[:-1])) % 10
        # right = C[0] * d[1] + C[1] * d[2] + ... + C[-2] * d[-2] + C[-1] * d[-1]
        right = sum(coe * dig for coe, dig in zip(full_coeff, d[1:])) % 10

        return left == right

