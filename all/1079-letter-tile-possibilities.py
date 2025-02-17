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


'''
permutations & combinatorics approach

learnt from official editorial 3:
https://leetcode.com/problems/letter-tile-possibilities/editorial/#approach-3-permutations-and-combinations
'''


import collections
import math


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        # remaining and selected: the frequency of alphabets
        remaining = list(collections.Counter(tiles).values())
        selected = [0] * len(remaining)

        def dfs(i):
            # i: the index of remaining/selected to be proceeded
            # count permutations of selected chars
            perms = 1
            for freq in selected:
                if freq:
                    perms *= math.factorial(freq)
            # the formula of sequence counts from
            # selected chars with frequencies n1, n2, n3, ...
            #
            #     (n1 + n2 + n3 + ...)!
            #    -----------------------
            #     (n1)!*(n2)!*(n3)!*...
            #
            ret = math.factorial(sum(selected)) // perms

            # backtracking
            for j in range(i, len(remaining)):
                if remaining[j]:
                    selected[j] += 1
                    remaining[j] -= 1
                    ret += dfs(j)
                    selected[j] -= 1
                    remaining[j] += 1
            return ret
        return dfs(0) - 1  # excluding empty string

