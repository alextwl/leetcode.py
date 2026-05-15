'''
2026/05/15 daily challenge

binary search approach
'''


class Solution:
    def findMin(self, nums: List[int]) -> int:
        last_val = nums[-1]

        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > last_val:
                # if it's bigger than nums[-1], the minimum is in the right side.
                left = mid + 1
            else:
                # let nums[right] always <= nums[-1].
                right = mid
        return nums[right]

