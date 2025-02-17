'''
2025/02/17 daily challenge

backtracking approach
'''


import collections
import functools


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        n = len(tiles)
        tilecount = collections.Counter(tiles)
        ans = 0

        @functools.cache
        def dfs(s):
            if s:
                nonlocal ans
                ans += 1
            if len(s) == n:
                return
            
            for c, k in tilecount.items():
                if not k:
                    continue
                tilecount[c] -= 1
                dfs(s + c)
                tilecount[c] += 1
            return

        dfs("")
        return ans

