'''
sorting + greedy method approach
'''


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        # base case: minimum moves to make the smallest equals to the largest
        ans = nums[-1] - nums[0]
        prev = nums[-1]
        for i in range(n - 2, 0, -1):
            # apply current moves to nums[i]
            curr = nums[i] + ans
            # we need another (nums[i] - nums[i+1]) moves to make nums[i+1] equal
            ans += curr - prev
            prev = curr
        return ans

