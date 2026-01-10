'''
top-down dynamic programming approach (recursion ver)

similar to problem 712.
'''


import functools


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        @functools.cache
        def dp(i, j):
            if i == m and j == n:
                return 0
            if i == m:
                return 1 + dp(i, j + 1)
            if j == n:
                return 1 + dp(i + 1, j)
            
            if word1[i] == word2[j]:
                return dp(i + 1, j + 1)
            # delete both or either word1[i] and word2[j]
            return min(1 + dp(i + 1, j), 1 + dp(i, j + 1), 2 + dp(i + 1, j + 1))

        return dp(0, 0)

