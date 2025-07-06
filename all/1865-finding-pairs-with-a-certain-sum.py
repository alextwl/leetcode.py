'''
2025/07/06 daily challenge

counter approach

hash nums2 and brute force nums1[i] + nums2[j] == tot pairs
'''


import collections


class FindSumPairs:
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.ctr = collections.Counter(nums2)

    def add(self, index: int, val: int) -> None:
        old_val = self.nums2[index]
        new_val = old_val + val
        self.ctr[old_val] -= 1
        self.ctr[new_val] += 1
        self.nums2[index] = new_val

    def count(self, tot: int) -> int:
        ans = 0
        for opnd1 in self.nums1:
            if opnd1 < tot:
                ans += self.ctr.get(tot - opnd1, 0)
        return ans

