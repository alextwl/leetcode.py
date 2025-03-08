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


'''
k-length sliding window approach
'''


class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        it = iter(blocks)
        # build a k-length window
        w = 0  # number of white blocks to be recolored
        for _ in range(k):
            if next(it) == 'W':
                w += 1
        # b = k - w
        min_recolors = w

        # slide the window
        i = 0
        for c in it:
            if c == 'W':
                w += 1
            # else:
            #     b += 1
            if blocks[i] == 'W':
                w -= 1
            # else:
            #     b -= 1
            if w < min_recolors:
                min_recolors = w
            i += 1
        return min_recolors

