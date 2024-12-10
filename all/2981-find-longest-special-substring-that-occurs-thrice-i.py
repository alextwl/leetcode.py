'''
2024/12/10 daily challenge

brute force + counter approach
'''


import collections


class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)
        subcnt = collections.defaultdict(int)
        for i, c in enumerate(s):
            subcnt[c] += 1
            for j in range(i + 1, n):
                if s[j] == c:
                    subcnt[c * (j - i + 1)] += 1
                else:
                    break
        return max((len(k) for k, v in subcnt.items() if v >= 3), default=-1)

