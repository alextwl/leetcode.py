'''
leetcode 75 lv2 day 8
2023/08/08 daily challenge
2026/05/22 daily challenge

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


'''
2x binary search ver
'''


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums[0] > nums[-1]:
            # rotated sorted array found, find the pivot
            left, right = 0, len(nums) - 2
            pivot = None
            while(left <= right):
                mid = left + (right - left) // 2
                
                if nums[mid] > nums[mid+1]:
                    # pivot found
                    pivot = mid+1
                    break
                elif nums[0] > nums[mid+1]:
                    right = mid
                else:
                    left = mid + 1
            
            # split the nums by pivot and select which part to be searched.
            if target < nums[0]:
                left, right = pivot, len(nums) - 1
            else:
                left, right = 0, pivot-1
        else:
            # search the entire array
            left, right = 0, len(nums) - 1
        
        # time to search the target
        while(left <= right):
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                # target found
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        # not found
        return -1


'''
yet another two-pass binary search approach
'''


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        # determine the beginning of original array
        last_val = nums[-1]
        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > last_val:
                left = mid + 1
            else:
                right = mid

        # original array starts from nums[orig_head]
        orig_head = right

        # adjust the range to search for target
        if target <= last_val:
            left, right = orig_head, n - 1
        else:
            left, right = 0, orig_head - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        return right if nums[right] == target else -1

