'''
2023/10/09 daily challenge

binary search approach
'''


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        # find left bound
        target_left = target - 1
        left, right = 0, len(nums) - 1
        while(left < right):
            mid = left + ((right - left) >> 1)
            v = nums[mid]
            if v <= target_left:
                left = mid + 1
            else:
                right = mid - 1
        
        if nums[left] == target:
            left_bound = left
        elif (next_left := left + 1) < len(nums) and nums[next_left] == target:
            left_bound = next_left
        else:
            return [-1, -1]
        
        # find right bound
        target_right = target + 1
        right = len(nums) - 1
        while(left < right):
            mid = left + ((right - left) >> 1)
            v = nums[mid]
            if v >= target_right:
                right = mid - 1
            else:
                left = mid + 1

        if nums[left] == target:
            right_bound = left
        else:
            right_bound = left - 1

        return [left_bound, right_bound]

