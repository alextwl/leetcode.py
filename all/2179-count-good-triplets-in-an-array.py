'''
2025/04/15 daily challenge

Binary Indexed Tree (Fenwick tree) approach

learnt from official editorial:
https://leetcode.com/problems/count-good-triplets-in-an-array/editorial/
'''


class BIT:
    def __init__(self, n):
        self.tree = [0] * (n + 1)
    
    def update(self, i, delta):
        i += 1
        # walk upward
        while i < len(self.tree):
            self.tree[i] += delta
            # move to next node by accumulating LSSB
            i += i & -i
    
    def query(self, i):
        ret = 0
        i += 1
        # walk downward
        while i > 0:
            ret += self.tree[i]
            # move to next node by removing LSSB
            i -= i & -i
        return ret


class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        pos2 = [0] * n  # pos2[v] = the index of v in nums2
        rev_map = [0] * n  # rev_map[index in nums2] = index of same value in nums1
        for i, v2 in enumerate(nums2):
            pos2[v2] = i
        for i, v1 in enumerate(nums1):
            rev_map[pos2[v1]] = i

        t = BIT(n)
        ans = 0
        for v in range(n):
            pos1 = rev_map[v]
            left = t.query(pos1)
            t.update(pos1, 1)
            right = (n - 1 - pos1) - (v - left)
            ans += left * right

        return ans

