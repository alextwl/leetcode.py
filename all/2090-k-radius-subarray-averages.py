'''
2023/06/20 daily challenge

sliding window approach
'''

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        diameter = k*2 + 1
        ans = [-1] * n

        if n < diameter:
            return ans

        nums.append(0)  # add an extra zero for the last unconditional prefix_sum += nums[right]
        prefix_sum = 0
        for i in range(0, diameter):
            prefix_sum += nums[i]

        left = 0  # next nums[left] to be popped from subarray
        right = diameter  # next nums[right] to be appended to subarray
        for i in range(k, n-k):
            ans[i] = prefix_sum // diameter
            prefix_sum = prefix_sum - nums[left] + nums[right]
            left += 1
            right += 1

        return ans

