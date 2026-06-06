'''
2026/06/06 daily challenge

prefix sum approach
'''


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        right_rev_sums = []
        prefix = 0
        for v in reversed(nums):
            right_rev_sums.append(prefix)
            prefix += v

        ans = []
        prefix = 0
        for v, right_sum in zip(nums, reversed(right_rev_sums)):
            ans.append(abs(prefix - right_sum))
            prefix += v

        return ans

