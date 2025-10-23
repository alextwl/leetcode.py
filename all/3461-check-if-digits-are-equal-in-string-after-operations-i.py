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

