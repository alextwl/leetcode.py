'''
2026/10/16 daily challenge

Segment Tree (Binary Indexed Tree) approach

learnt from official editorial:
https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-ii/editorial/#approach-binary-indexed-tree
'''


import collections


class SegTree2:
    def __init__(self, n):
        self.n = n
        self.t1 = collections.defaultdict(int)
        self.t2 = collections.defaultdict(int)
    
    def _add(self, i, delta):
        i += 1
        raw_i = i
        while i <= self.n:
            self.t1[i] += delta
            self.t2[i] += (raw_i - 1) * delta
            i += i & -i

    def add(self, left, right, delta):
        self._add(left, delta)
        self._add(right + 1, -delta)

    def _query(self, i):
        i += 1
        i = min(i, self.n)
        raw_i = i
        ret = 0
        while i > 0:
            ret += raw_i * self.t1[i] - self.t2[i]
            i -= i & -i
        return ret
    
    def query(self, left, right):
        return self._query(right) - self._query(left - 1)


class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        tree = SegTree2(n + 10)
        seen = dict()
        ans = curr = 0
        for i, v in enumerate(nums):
            j = seen.get(v, -1) + 1
            curr = (curr + tree.query(j, i) * 2 + i - j + 1) % 1_000_000_007
            ans = (ans + curr) % 1_000_000_007
            tree.add(j, i, 1)
            seen[v] = i
        return ans

