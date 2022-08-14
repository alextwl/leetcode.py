class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # sort and compare by pair
        nums.sort()
        
        numlen = len(nums)
        ptr = 0
        while(ptr < numlen):
            if ptr + 1 >= numlen:
                return nums[ptr]
            
            if nums[ptr] == nums[ptr+1]:
                ptr += 2
            else:
                return nums[ptr]
