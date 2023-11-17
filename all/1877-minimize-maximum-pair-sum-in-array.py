'''
2023/11/17 daily challenge

sorting approach

sort nums[] first, and then find the optimal pairs.
'''


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        half = len(nums) // 2
        return max(a + b for a, b in zip(nums[:half], reversed(nums[half:])))

