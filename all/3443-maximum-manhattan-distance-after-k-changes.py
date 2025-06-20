'''
2025/06/20 daily challenge

brute force approach

always re-calculate the Manhattan distance with
max k modifications applied every step.
'''


class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        get_distance = lambda d1, d2, t: abs(d1 - d2) + t * 2
        max_dist = 0
        ctr = {'N': 0, 'S': 0, 'E': 0, 'W': 0}
        for c in s:
            ctr[c] += 1
            x = min(ctr['N'], ctr['S'], k)  # avail chars to be modified on x-axis
            y = min(ctr['E'], ctr['W'], k - x)  # avail chars to be modified on y-axis
            max_dist = max(max_dist,
                           get_distance(ctr['N'], ctr['S'], x) + \
                           get_distance(ctr['E'], ctr['W'], y))
        return max_dist

