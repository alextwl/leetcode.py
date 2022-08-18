class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        numsLen = len(nums)
        zeroCount = 0
        newIdx = 0
        
        for idx in range(numsLen):
            if nums[idx] != 0:
                nums[newIdx] = nums[idx]
                newIdx += 1
            else:
                zeroCount += 1
        
        # fill zeroes into the end of nums
        for idx in range(numsLen - zeroCount,numsLen):
            nums[idx] = 0
        
        return

