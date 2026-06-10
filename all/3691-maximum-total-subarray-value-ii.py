'''
2026/06/10 daily challenge

Range Minimum Query (RMQ) Sparse table + max heap approach

learnt from official editorial 1:
https://leetcode.com/problems/maximum-total-subarray-value-ii/editorial/#approach-1-sparse-table--max-heap
'''


import heapq


class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        log_n = n.bit_length()

        # sparse tables
        stmax = [[0] * log_n for _ in range(n)]
        stmin = [[0] * log_n for _ in range(n)]
        for i, v in enumerate(nums):
            stmax[i][0] = v
            stmin[i][0] = v
        for j in range(1, log_n):
            step = 1 << (j - 1)
            for i in range(n - (1 << j) + 1):
                stmax[i][j] = max(stmax[i][j - 1], stmax[i + step][j - 1])
                stmin[i][j] = min(stmin[i][j - 1], stmin[i + step][j - 1])

        def query_max(l, r):
            j = (r - l + 1).bit_length() - 1
            return max(stmax[l][j], stmax[r - (1 << j) + 1][j])

        def query_min(l, r):
            j = (r - l + 1).bit_length() - 1
            return min(stmin[l][j], stmin[r - (1 << j) + 1][j])

        # max heap: (-subarray_val, left, right)
        h = [(-(query_max(l, n - 1) - query_min(l, n - 1)), l, n - 1) for l in range(n)]
        heapq.heapify(h)

        ans = 0
        for _ in range(k):
            neg_val, l, r = heapq.heappop(h)
            ans -= neg_val
            if r > l:
                # push prev element (l, r - 1)
                heapq.heappush(h, (-(query_max(l, r - 1) - query_min(l, r - 1)), l, r - 1))

        return ans

