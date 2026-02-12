'''
2026/02/12 daily challenge

brute force + counter approach
'''


import collections


class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        ans = 1

        for i in range(n):
            ctr = collections.Counter(s[i:i+ans])
            for j in range(i + ans, n):
                ctr[s[j]] += 1
                if len(set(ctr.values())) == 1:
                    ans = max(ans, j - i + 1)

        return ans

