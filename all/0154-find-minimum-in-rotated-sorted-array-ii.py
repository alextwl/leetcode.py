'''
2026/05/16 daily challenge

binary search approach

similar to problem 153 with value duplication

worst case=O(n) if all elements were the same.
'''


class Solution:
    def findMin(self, nums: List[int]) -> int:
        last_val = nums[-1]

        left, right = 0, len(nums) - 1
        # bypass left if duplicate found
        while nums[left] == last_val and left < right:
            left += 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > last_val:
                # if it's bigger than nums[-1], the minimum is in the right side.
                left = mid + 1
            else:
                # let nums[right] always <= nums[-1].
                right = mid
        return nums[right]

