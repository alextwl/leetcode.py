'''
2024/02/15 daily challenge

sorting + prefix sum approach
'''


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)

        remain = sum(nums)  # sum(a1..ak-1) (without ak's length)

        # try to find a valid longest side
        for i, l in enumerate(nums):
            remain -= l
            if remain > l:
                break

        if i >= len(nums) - 2:
            # we need at least 3 sides to form a polygon
            return -1

        return remain + l

