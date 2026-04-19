'''
2026/04/20 daily challenge

find the first positions of two distinct colors,
and maximize the farthest pair of (i, j).

time=O(n)
'''


class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        # find the first seen two distinct colors
        seen_idx1 = 0
        seen_color1 = colors[0]
        for i, color in enumerate(colors):
            if color != seen_color1:
                seen_idx2 = i
                break
        else:
            return -1  # undefined

        # maximize the farthest pair
        ans = seen_idx2
        for i in range(seen_idx2, len(colors)):
            color = colors[i]
            if color != seen_color1:
                ans = max(ans, i - seen_idx1)
            else:
                ans = max(ans, i - seen_idx2)

        return ans

