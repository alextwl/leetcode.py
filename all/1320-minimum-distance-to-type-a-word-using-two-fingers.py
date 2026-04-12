'''
2026/04/12 daily challenge

dynamic programming + table lookup + space optimized approach

learnt from official editorial 2:
https://leetcode.com/problems/minimum-distance-to-type-a-word-using-two-fingers/editorial/#approach-2-dynamic-programming--space-optimization
'''


ASCII_A = ord('A')
COORD = [divmod(i, 6) for i in range(26)]
DIST = [[0] * 26 for _ in range(26)]


for i in range(26):
    x0, y0 = COORD[i]
    for j in range(i + 1, 26):
        x1, y1 = COORD[j]
        dist = abs(x0 - x1) + abs(y0 - y1)
        DIST[i][j] = dist
        DIST[j][i] = dist



class Solution:
    def minimumDistance(self, word: str) -> int:
        n = len(word)
        # no need to distinguish between left & right hands,
        # reduce dp[i][left/right hand][pos of other hand] to dp[i][pos of other hand]
        dp = [[0] * 26] + [[float('inf')] * 26 for _ in range(n - 1)]

        it = enumerate(word)
        prev = ord(next(it)[1]) - ASCII_A
        for i, c in it:
            curr = ord(c) - ASCII_A
            p2c_dist = DIST[prev][curr]
            for j in range(26):
                dp[i][j] = min(dp[i][j], dp[i - 1][j] + p2c_dist)
                if prev == j:
                    # repeat keystroke
                    for k, k2c_dist in enumerate(DIST[curr]):
                        dp[i][j] = min(dp[i][j], dp[i - 1][k] + k2c_dist)
            prev = curr

        return min(dp[n - 1])

