'''
2026/09/22 daily challenge

segment tree approach

learnt from official editorial:
https://leetcode.com/problems/find-x-value-of-array-ii/editorial/#approach-segment-tree
'''


class SegTree:
    def __init__(self, nums, k):
        n = len(nums)
        size = 2 << n.bit_length()

        self.k = k
        self.tree = [[0] * (k + 1) for _ in range(size)]
        self.build(nums, 1, 0, n - 1)
    
    def make_leaf(self, o, v):
        info_arr = [0] * (self.k + 1)
        rem = v % self.k
        info_arr[rem] = 1
        info_arr[self.k] = rem
        self.tree[o] = info_arr
    
    def merge_prefix(self, lefts, rights):
        pfx = [0] * (self.k + 1)
        prod_left = lefts[self.k]
        prod_right = rights[self.k]

        pfx[self.k] = (prod_left * prod_right) % self.k
        # only within left interval
        for x in range(self.k):
            pfx[x] = lefts[x]
        # within left interval + prefix of right interval
        for x in range(self.k):
            pfx[(prod_left * x) % self.k] += rights[x]

        return pfx

    def maintain(self, o):
        self.tree[o] = self.merge_prefix(self.tree[o * 2], self.tree[o * 2 + 1])

    def build(self, nums, o, l, r):
        if l == r:
            self.make_leaf(o, nums[l])
            return

        mid = (l + r) >> 1
        self.build(nums, o * 2, l, mid)
        self.build(nums, o * 2 + 1, mid + 1, r)
        self.maintain(o)

    def update(self, o, l, r, i, v):
        if l == r:
            self.make_leaf(o, v)
            return
        
        mid = (l + r) >> 1
        if i <= mid:
            self.update(o * 2, l, mid, i, v)
        else:
            self.update(o * 2 + 1, mid + 1, r, i, v)
        self.maintain(o)

    def query(self, o, l0, r0, l1, r1):
        if l1 <= l0 and r0 <= r1:
            return self.tree[o]
        
        mid = (l0 + r0) >> 1
        if r1 <= mid:
            return self.query(o * 2, l0, mid, l1, r1)
        if l1 > mid:
            return self.query(o * 2 + 1, mid + 1, r0, l1, r1)

        left = self.query(o * 2, l0, mid, l1, r1)
        right = self.query(o * 2 + 1, mid + 1, r0, l1, r1)
        return self.merge_prefix(left, right)


class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        seg = SegTree(nums, k)

        ans = []
        for index, value, start, x in queries:
            seg.update(1, 0, n - 1, index, value)
            pfx = seg.query(1, 0, n - 1, start, n - 1)
            ans.append(pfx[x])
        return ans

