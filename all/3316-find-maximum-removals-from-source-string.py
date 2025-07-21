'''
dynamic programming approach (knapsack problem)

convert the problem to "the minimal operations we cannot perform removals",
the difference between that and the total of target indices is the answer.

runtime=3864ms beats 5.19%
'''


class Solution:
    def maxRemovals(self, source: str, pattern: str, targetIndices: List[int]) -> int:
        n = len(source)
        m = len(pattern)
        dp = [[-1] * m for _ in range(n)]
        # convert targetIndices to boolean array mapped to source.
        flag = [False] * n
        for i in targetIndices:
            flag[i] = True
        
        def minOps(i, j):
            # the minimal operations that we cannot perform removals from source
            if j == m:
                # all pattern matched
                return 0
            if i == n:
                # source exhausted
                return float('inf')
            
            if dp[i][j] >= 0:
                return dp[i][j]
            
            # two options: to do & not to do
            do = minOps(i + 1, j)
            dont = float('inf')
            if source[i] == pattern[j]:
                nextpat = minOps(i + 1, j + 1)
                if nextpat != float('inf'):
                    # if flag[i] is true then we can remove source[i]
                    dont = flag[i] + nextpat
            ret = min(do, dont)
            dp[i][j] = ret
            return ret

        rev = minOps(0, 0)
        return len(targetIndices) - (0 if rev == float('inf') else rev)

