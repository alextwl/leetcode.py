'''
2026/07/10 daily challenge

sparse table (binary lifting) approach
'''


import math


class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        # sort nums with original index tracked
        arr = sorted(enumerate(nums), key=lambda x: x[1])
        # index mapping from nums to arr
        i2j = [None] * n
        for j, (i, _) in enumerate(arr):
            i2j[i] = j

        # build sparse table
        m = math.floor(math.log2(n)) + 1
        st = [[0] * m for _ in range(n)]  # n*m mat
        k = 0
        # gen first jump
        for i in range(n):
            k = max(k, i)
            while k + 1 < n and arr[k+1][1] - arr[k][1] <= maxDiff and arr[k+1][1] - arr[i][1] <= maxDiff:
                k += 1
            st[i][0] = k
        # binary lifting
        for j in range(1, m):
            for i in range(n):
                st[i][j] = st[st[i][j - 1]][j - 1]

        ans = [-1 for _ in range(len(queries))]
        for i, (u, v) in enumerate(queries):
            u, v = i2j[u], i2j[v]
            if u == v:
                ans[i] = 0
                continue
            if u > v:
                u, v = v, u

            # try to jump
            k = u
            move = 0
            for j in range(m - 1, -1, -1):
                if st[k][j] < v:
                    k = st[k][j]
                    move += (1 << j)
            if st[k][0] >= v:
                # v is reachable from u
                ans[i] = move + 1

        return ans

