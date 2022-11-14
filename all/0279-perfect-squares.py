'''
dynamic programming approach

try to minimize the number of perfect squares that sum to n.
if n itself was already a perfect square, then the least number is 1.

since there's 1 <= n <= 10**4 constraint,
pre-calculating perfect squares <= 10**4 in advance is reasonable in order to speedup.
'''

SQUARES = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100,
            121, 144, 169, 196, 225, 256, 289, 324,
            361, 400, 441, 484, 529, 576, 625, 676,
            729, 784, 841, 900, 961, 1024, 1089,
            1156, 1225, 1296, 1369, 1444, 1521,
            1600, 1681, 1764, 1849, 1936, 2025,
            2116, 2209, 2304, 2401, 2500, 2601,
            2704, 2809, 2916, 3025, 3136, 3249,
            3364, 3481, 3600, 3721, 3844, 3969,
            4096, 4225, 4356, 4489, 4624, 4761,
            4900, 5041, 5184, 5329, 5476, 5625,
            5776, 5929, 6084, 6241, 6400, 6561,
            6724, 6889, 7056, 7225, 7396, 7569,
            7744, 7921, 8100, 8281, 8464, 8649,
            8836, 9025, 9216, 9409, 9604, 9801, 10000]


class Solution:
    def numSquares(self, n: int) -> int:
        '''
        dp[n] = the least number of perfect squares.
        '''
        dp = [0]
        for i in range(1, n+1):
            '''
            try to subtract all possible perfect squares <= i,
            find the minimum and plus 1.

            note: dp[-sq] == dp[i-sq]
            '''
            dp.append(min([dp[-sq] for sq in SQUARES if sq <= i]) + 1)

        return dp[-1]

