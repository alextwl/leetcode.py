class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        numlen = len(nums)
        
        ptr = 0  # 
        for idx, n in enumerate(nums):
            if n != val:
                # replace nums[ptr] no matter whether ptr != idx or not.
                nums[ptr] = n
                ptr += 1
            else:
                # remove element
                numlen -= 1

        return numlen
