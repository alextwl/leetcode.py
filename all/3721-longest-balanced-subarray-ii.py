'''
2026/02/11 daily challenge

prefix sum + segment tree approach

learnt from official editorial:
https://leetcode.com/problems/longest-balanced-subarray-ii/editorial/#approach-prefix-sum--segment-tree

large input version of problem 3719.
'''


import collections


class Tag:
    # tag struct for lazy propagation
    def __init__(self):
        self.to_add = 0
    
    def add(self, other):
        self.to_add += other.to_add
        return self

    def has_tag(self):
        return self.to_add != 0
    
    def clear(self):
        self.to_add = 0


class Node:
    def __init__(self):
        self.min_val = 0
        self.max_val = 0
        self.tag = Tag()


class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [Node() for _ in range(self.n * 4 + 1)]
        self._build(data, 1, self.n, 1)
    
    def add(self, l, r, val):
        tag = Tag()
        tag.to_add = val
        self._update(l, r, tag, 1, self.n, 1)
    
    def find_last(self, start, val):
        if start > self.n:
            return -1
        return self._find(start, self.n, val, 1, self.n, 1)
    
    def _apply_tag(self, i, tag):
        tree = self.tree[i]
        tree.min_val += tag.to_add
        tree.max_val += tag.to_add
        tree.tag.add(tag)
    
    def _push_down(self, i):
        tree = self.tree[i]
        if tree.tag.has_tag():
            tag = Tag()
            tag.to_add = tree.tag.to_add
            self._apply_tag(i << 1, tag)
            self._apply_tag((i << 1) | 1, tag)
            tree.tag.clear()
    
    def _push_up(self, i):
        self.tree[i].min_val = min(self.tree[i << 1].min_val,
                                   self.tree[(i << 1) | 1].min_val)
        self.tree[i].max_val = max(self.tree[i << 1].max_val,
                                   self.tree[(i << 1) | 1].max_val)
    
    def _build(self, data, l, r, i):
        if l == r:
            self.tree[i].min_val = data[l - 1]
            self.tree[i].max_val = data[l - 1]
        else:
            mid = l + ((r - l) >> 1)
            self._build(data, l, mid, i << 1)
            self._build(data, mid + 1, r, (i << 1) | 1)
            self._push_up(i)
    
    def _update(self, target_l, target_r, tag, l, r, i):
        if target_l <= l and r <= target_r:
            self._apply_tag(i, tag)
        else:
            self._push_down(i)
            mid = l + ((r - l) >> 1)
            if target_l <= mid:
                self._update(target_l, target_r, tag, l, mid, i << 1)
            if target_r > mid:
                self._update(target_l, target_r, tag, mid + 1, r, (i << 1) | 1)
            self._push_up(i)
    
    def _find(self, target_l, target_r, val, l, r, i):
        if self.tree[i].min_val > val or self.tree[i].max_val < val:
            return -1
        
        if l == r:
            return l
        
        self._push_down(i)
        mid = l + ((r - l) >> 1)
        if target_r >= mid + 1:
            ret = self._find(target_l, target_r, val, mid + 1, r, (i << 1) | 1)
            if ret != -1:
                return ret
        if l <= target_r and mid >= target_l:
            return self._find(target_l, target_r, val, l, mid, i << 1)
        
        return -1


def sign(x):
    return 1 if x % 2 == 0 else -1


class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        occ_v2q = collections.defaultdict(collections.deque)

        max_len = 0
        it = enumerate(nums)
        v = next(it)[1]  # nums[0]
        pfx = [0] * n
        pfx[0] = sign(v)
        occ_v2q[v].append(1)

        for i, v in it:
            pfx[i] = pfx[i - 1]
            occ = occ_v2q[v]
            if not occ:
                pfx[i] += sign(v)
            occ.append(i + 1)
        
        seg = SegmentTree(pfx)
        for i, v in enumerate(nums):
            max_len = max(max_len, seg.find_last(i + max_len, 0) - i)
            next_pos = n + 1
            occ_v2q[v].popleft()
            if occ_v2q[v]:
                next_pos = occ_v2q[v][0]
            seg.add(i + 1, next_pos - 1, -sign(v))
        
        return max_len

