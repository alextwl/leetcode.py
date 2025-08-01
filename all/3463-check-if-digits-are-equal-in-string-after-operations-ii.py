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

