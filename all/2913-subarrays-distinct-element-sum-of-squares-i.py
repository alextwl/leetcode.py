'''
2026/10/15 daily challenge

set + brute force approach
'''


class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            dset = set()
            for j in range(i, n):
                dset.add(nums[j])
                ans += len(dset) ** 2
        return ans

