'''
binary search lv1 day 1

two pointer approach
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        
        while (left <= right):
            mid = left + (right-left)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        # target not found
        return -1

