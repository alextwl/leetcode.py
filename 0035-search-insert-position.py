class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # do binary search
        start = 0
        end = len(nums)
        
        while(start < end):
            middle = (start + end) // 2
            if target > nums[middle]:
                start = middle + 1
            else:
                end = middle
        
        return start
