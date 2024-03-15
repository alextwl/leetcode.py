'''
2024/03/15 daily challenge

prefix sum approach
'''


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []

        # build the prefix part
        prev = 1
        for v in nums:
            ans.append(prev)
            prev *= v

        # multiply the suffix part
        prev = 1
        for i in range(len(nums)-1, -1, -1):
            ans[i] *= prev
            prev *= nums[i]

        return ans

