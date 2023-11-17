'''
2023/11/17 daily challenge

sorting approach

sort nums[] first, and then find the optimal pairs.

assume [(nums[0], nums[-1]), (nums[i], nums[j])] is a candidate of pairs,
and we try to find a contradiction for a counterexample, that is:

suppose the pairs [(nums[0], nums[i]), (nums[j], nums[-1])] are more optimal,
and we know

nums[0] <= nums[i] <= nums[j] <= nums[-1]

(nums[j] + nums[-1]) is always greater than or equal to (nums[0] + nums[i]),
the maximum pair sum in array is also (nums[j] + nums[-1]),
so we can know (nums[0], nums[-1]) is always smaller than or equal to (nums[j] + nums[-1])
which is not optimal (not minimized).
'''


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        half = len(nums) // 2
        return max(a + b for a, b in zip(nums[:half], reversed(nums[half:])))

