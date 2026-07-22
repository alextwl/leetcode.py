'''
2026/07/22 daily challenge

binary search + segment tree approach

learnt from official editorial 1:
https://leetcode.com/problems/maximize-active-section-with-trade-ii/editorial/#approach-1-binary-search--segment-tree
'''


import bisect
import itertools


class SegTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.arr = arr
        self.seg = [0] * (self.n << 2)
        if self.n:
            self.build(1, 0, self.n - 1)

    def build(self, p, left, right):
        if left == right:
            self.seg[p] = self.arr[left]
            return

        mid = (left + right) >> 1
        self.build(p << 1, left, mid)
        self.build(p << 1 | 1, mid + 1, right)
        self.seg[p] = max(self.seg[p << 1], self.seg[p << 1 | 1])
        return

    def query(self, left, right):
        if left > right:
            return 0

        def _query(p, l, r):
            if left <= l and r <= right:
                return self.seg[p]
            mid = (l + r) >> 1
            ret = 0
            if left <= mid:
                ret = _query(p << 1, l, mid)
            if right > mid:
                ret = max(ret, _query(p << 1 | 1, mid + 1, r))
            return ret

        return _query(1, 0, self.n -1)


class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)

        zero_blocks = []
        block_left = []
        block_right = []
        i = 0
        while i < n:
            start = i
            while i < n and s[i] == s[start]:
                i += 1
            if s[start] == '0':
                zero_blocks.append(i - start)
                block_left.append(start)
                block_right.append(i - 1)

        m = len(zero_blocks)
        ctr_one = s.count('1')
        if m < 2:
            # no valid trade could be performed
            return [ctr_one] * len(queries)

        tmp_sum = [z0 + z1 for z0, z1 in itertools.pairwise(zero_blocks)]
        tree = SegTree(tmp_sum)

        ans = []
        for l, r in queries:
            i = bisect.bisect_left(block_right, l)
            j = bisect.bisect_right(block_left, r) - 1

            if i > m - 1 or j < 0 or i >= j:
                # zero blocks < 2, no valid trade in the given query
                ans.append(ctr_one)
                continue

            # leftmost zero block's length within the query
            first_len = block_right[i] - max(block_left[i], l) + 1
            # rightmost zero block's length within the query
            last_len = min(block_right[j], r) - block_left[j] + 1

            if i + 1 == j:
                # only one valid trade (only 2 consecutive zero blocks)
                ans.append(ctr_one + first_len + last_len)
                continue
            
            v1 = first_len + zero_blocks[i + 1]
            v2 = zero_blocks[j - 1] + last_len
            v3 = tree.query(i + 1, j - 2)
            best_gain = max(v1, v2, v3)
            ans.append(ctr_one + best_gain)

        return ans

