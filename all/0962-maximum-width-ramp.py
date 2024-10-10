'''
2024/10/10 daily challenge

iterate each width (TLE)
'''


class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        
        for width in range(n - 1, 0, -1):
            for left in range(0, n - width):
                if nums[left] <= nums[left + width]:
                    return width

        return 0


'''
sorting approach

sort the nums with index, and find max width with tracking minimum index.
'''


class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        enums = sorted((v, i) for i, v in enumerate(nums))

        min_i = len(nums)
        max_width = 0

        for _, i in enums:
            max_width = max(max_width, i - min_i)
            min_i = min(min_i, i)

        return max_width


'''
monotonic stack approach
'''


class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        n = len(nums)

        for i, v in enumerate(nums):
            if not stack or nums[stack[-1]] > v:
                stack.append(i)

        max_width = 0
        for j in range(n - 1, -1, -1):
            right_val = nums[j]
            while stack and nums[stack[-1]] <= right_val:
                max_width = max(max_width, j - stack[-1])
                stack.pop()

        return max_width

