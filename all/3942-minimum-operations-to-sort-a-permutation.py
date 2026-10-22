'''
2026/10/22 daily challenge

simulation approach

learnt from official editorial:
https://leetcode.com/problems/minimum-operations-to-sort-a-permutation/editorial/#approach-simulation

hint: a sortable array is either cyclically increasing/decreasing by operations
'''


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return 0

        start = nums.index(0)
        ascending = descending = True
        for i in range(1, n):
            v = nums[(start + i) % n]
            if v != i:
                ascending = False
            if v != n - i:
                descending = False
            if not ascending and not descending:
                return -1

        if ascending:
            return min(start, n - start + 2)
        # descending
        return min(n - start, start + 2)

