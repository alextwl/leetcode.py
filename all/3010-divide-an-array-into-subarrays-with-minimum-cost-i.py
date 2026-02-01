'''
2026/02/01 daily challenge

sum up the first element and two smallest elements in nums[1:].
'''


class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        min1 = min2 = 51
        for i in range(1, len(nums)):
            if nums[i] < min1:
                min1, min2 = nums[i], min1
            elif nums[i] < min2:
                min2 = nums[i]
        return nums[0] + min1 + min2

