'''
2025/07/12 daily challenge

dynamic programming (memorization) + state machine approach

learnt from official editorial:
https://leetcode.com/problems/the-earliest-and-latest-rounds-where-players-compete/editorial/#approach-analyze-fundamentally-different-standing-situations--memoized-search

need to consider all the combination of positions for both f & s on the left/right or in the middle.
'''


import functools


class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        @functools.cache
        def dp(n, f, s):
            fs = f + s
            if fs == n + 1:
                return (1, 1)
            
            if fs > n + 1:
                # flip arrangement
                return dp(n, n + 1 - s, n + 1 - f)
            
            earliest, latest = float('inf'), float('-inf')
            half = (n + 1) // 2
            if s <= half:
                # 2nd player on the left or in the middle
                for i in range(f):
                    for j in range(s - f):
                        x, y = dp(half, i + 1, i + j + 2)
                        earliest, latest = min(earliest, x), max(latest, y)
            else:
                # 2nd player on the right
                prime = n + 1 - s
                mid = (n - 2 * prime + 1) // 2
                for i in range(f):
                    for j in range(prime - f):
                        x, y = dp(half, i + 1, i + j + mid + 2)
                        earliest, latest = min(earliest, x), max(latest, y)
            return (earliest + 1, latest + 1)
        
        if firstPlayer > secondPlayer:
            firstPlayer, secondPlayer = secondPlayer, firstPlayer

        earliest, latest = dp(n, firstPlayer, secondPlayer)
        dp.cache_clear()  # clear for the next testcase
        return [earliest, latest]

