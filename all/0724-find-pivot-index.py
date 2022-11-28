'''
leetcode 75 lv1 day 1

maintain the sum of left & right simutlaneously

time=O(n)
'''

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftsum, rightsum = 0, sum(nums)
        
        for i, val in enumerate(nums):
            rightsum -= val
            if leftsum == rightsum:
                return i
            leftsum += val
        
        return -1

