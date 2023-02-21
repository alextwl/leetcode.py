'''
2023/02/21 daily challenge

binary search approach
'''

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums) - 1
        left, right = 0, n

        while(left <= right):
            mid = left + (right-left)//2
            # align to even index
            mid = mid - (mid & 1)

            if mid > 0 and nums[mid] == nums[mid-1]:
                right = mid - 2
            elif mid < n and nums[mid] == nums[mid+1]:
                left = mid + 2
            else:
                # the answer always appears at an even index due to its characteristic.
                # because prior to the answer there are two or elements which are all pairs.
                return nums[mid]
        
        # undefined behavior: the problem guarantees there's one element which appears exactly once.
        return -1

