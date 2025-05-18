'''
2025/05/18 daily challenge

bitmask + dynamic programming approach

learnt from official editorial:
https://leetcode.com/problems/painting-a-grid-with-three-different-colors/editorial/
'''


import collections


class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        mask_colors = dict()
        for mask in range(3 ** m):
            colors = []
            val = mask
            for i in range(m):
                val, rem = divmod(val, 3)
                colors.append(rem)
            if any(colors[i] == colors[i+1] for i in range(m - 1)):
                continue
            mask_colors[mask] = colors
        
        adj = collections.defaultdict(list)
        for mask1, color1 in mask_colors.items():
            for mask2, color2 in mask_colors.items():
                if not any(a == b for a, b in zip(color1, color2)):
                    adj[mask1].append(mask2)

        f = [int(mask in mask_colors) for mask in range(3**m)]
        g = [0] * (3 ** m)
        for i in range(1, n):
            for mask2 in mask_colors.keys():
                curr = 0
                for mask1 in adj[mask2]:
                    curr = (curr + f[mask1]) % 1_000_000_007
                g[mask2] = curr
            f, g = g, f

        return sum(f) % 1_000_000_007

