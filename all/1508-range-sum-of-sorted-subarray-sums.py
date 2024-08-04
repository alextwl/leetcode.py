'''
2024/08/04 daily challenge

exhaustive method approach
'''


class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sub_sums = []
        
        for i, a in enumerate(nums):
            prefix = 0
            for j in range(i, n):
                prefix += nums[j]
                sub_sums.append(prefix)
        
        sub_sums.sort()
        return sum(sub_sums[left-1:right]) % 1_000_000_007

