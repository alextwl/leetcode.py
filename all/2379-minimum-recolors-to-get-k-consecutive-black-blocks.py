'''
2025/03/08 daily challenge

dynamic programming approach (DFS+cache recursive ver)
'''


import functools


class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)

        @functools.cache
        def dfs(i, b):
            # i: index of blocks to be proceeded
            # b: length of current consecutive black blocks
            while i < n and blocks[i] == 'B':
                i += 1
                b += 1
            if b >= k:
                return 0
            if i == n:
                return -1

            recolor = dfs(i + 1, b + 1)
            skip = dfs(i + 1, 0)
            if recolor != -1:
                recolor += 1

            if recolor != -1 and skip != -1:
                return min(recolor, skip)
            elif skip != -1:
                return skip
            return recolor
        return dfs(0, 0)

