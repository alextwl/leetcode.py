class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        origLen = len(nums)
        newLen = 0
        prev = None
        
        for i, val in enumerate(nums):
            if val != prev:
                nums[newLen] = val
                newLen += 1
                prev = val
        #for i in range(newLen, origLen):
        #    nums.pop()
        return newLen
