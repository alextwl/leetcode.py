class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # do binary search
        left, right = 0, len(nums)-1
        
        while(left < right):
            mid = left + (right-left)//2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid
        
        # determine the position to insert in order
        return left + 1 if nums[left] < target else left
