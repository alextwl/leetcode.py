'''
greedy method + prefix/suffix min approach
'''


class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        prefix = []
        current_min = nums[0]
        for v in nums:
            prefix.append(current_min)
            current_min = min(current_min, v)
        suffix = []
        current_min = nums[-1]
        for v in reversed(nums):
            suffix.append(current_min)
            current_min = min(current_min, v)
        suffix.reverse()

        min_sum = float('inf')
        for i in range(1, len(nums) - 1):
            if prefix[i] < nums[i] and nums[i] > suffix[i]:
                min_sum = min(min_sum, prefix[i] + nums[i] + suffix[i])
        
        return -1 if min_sum == float('inf') else min_sum

