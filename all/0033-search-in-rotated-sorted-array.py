'''
leetcode 75 lv2 day 8

binary search + pivot approach
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find the minimum value's index as a pivot
        pivot = 0
        if nums[0] > nums[-1]:
            for i in range(1, len(nums)):
                if nums[i-1] > nums[i]:
                    pivot = i
                    break
        
        left, right = 0, len(nums) - 1
        while(left <= right):
            mid = (left+right) // 2
            i = mid + pivot
            if i >= len(nums):
                i -= len(nums)
            if nums[i] > target:
                right = mid - 1
            elif nums[i] < target:
                left = mid + 1
            else:
                # target hit
                return i

        # target not found
        return -1

