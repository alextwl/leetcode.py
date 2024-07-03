'''
2024/07/03 daily challenge

sorting + greedy method approach
'''


class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0

        nums.sort()
        
        # remove at most 3 elements from either smallest or largest 3 numbers
        # and minimize the absolute difference from those combinations.
        return min(abs(nums[i] - nums[i-4]) for i in range(4))

