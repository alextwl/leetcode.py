'''
2025/05/04 daily challenge

counter approach
'''


import collections


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        ans = 0
        ctr = collections.defaultdict(int)

        for a, b in dominoes:
            if a > b:
                a, b = b, a
            key = (a, b)
            ans += ctr[key]
            ctr[key] += 1

        return ans

