'''
2023/05/28 daily challenge

dynamic programming approach

learnt from
https://leetcode.com/problems/minimum-cost-to-cut-a-stick/solutions/3569897/python-java-c-simple-solution-easy-to-understand/
'''

class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        cuts = [0] + cuts + [n]

        '''
        dp[i][j] = the minimum cost to cut between [cuts[i], cuts[j]]
        '''
        m = len(cuts)
        dp = [[0] * m for _ in range(m)]

        '''
        segs = the count of continuous segments to be cut
        we iterate it from the minimum count 2 because
        2 segments can be cut into one segment and one segment.
        '''
        for segs in range(2, m):
            for i in range(m - segs):
                j = i + segs
                dp[i][j] = float('inf')
                ij_length = cuts[j] - cuts[i]
                # try to do each cut within [cuts[i], cuts[j]]
                for k in range(i+1, j):
                    '''
                    cuts[k] is a cut between [cuts[i], cuts[j]]

                    dp[i][j] is a minimized cost of segment consists of
                    2 smaller segments dp[i][k] & dp[k][j].
                    when these 2 small segments form a new segment,
                    the new segment's cost (ij_length) is accumulated.
                    '''
                    dp[i][j] = min(dp[i][j],
                                   dp[i][k] + dp[k][j] + ij_length)

        # the minimized cost of the entire stick as a segment is the answer.
        return dp[0][-1]

