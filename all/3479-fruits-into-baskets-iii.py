'''
2025/08/06 daily challenge

segment tree + binary search approach

learnt from official editorial 2:
https://leetcode.com/problems/fruits-into-baskets-iii/editorial/#approach-2-segment-tree--binary-search
'''


class SegmentTree:
    def __init__(self, baskets):
        self.n = len(baskets)
        size = 2 << (self.n - 1).bit_length()
        self.seg = [0] * size
        self._build(baskets, 1, 0, self.n - 1)
    
    def _maintain(self, o):
        # update max capacity from subtrees
        self.seg[o] = max(self.seg[o * 2], self.seg[o * 2 + 1])
    
    def _build(self, a, o, left, right):
        if left == right:
            self.seg[o] = a[left]
            return
        mid = (left + right) // 2
        # build [left, mid] & [mid+1, right] subtrees
        self._build(a, o * 2, left, mid)
        self._build(a, o * 2 + 1, mid + 1, right)
        # update current node
        self._maintain(o)
    
    def find_1st_and_update(self, o, left, right, x):
        # binary search x
        if self.seg[o] < x:
            return -1
        if left == right:
            # valid basket found
            self.seg[o] = -1
            return left
        mid = (left + right) // 2
        i = self.find_1st_and_update(o * 2, left, mid, x)
        if i == -1:
            i = self.find_1st_and_update(o * 2 + 1, mid + 1, right, x)
        self._maintain(o)
        return i


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        m = len(baskets)
        tree = SegmentTree(baskets)
        unplaced = 0
        for v in fruits:
            if tree.find_1st_and_update(1, 0, m-1, v) == -1:
                unplaced += 1
        return unplaced

