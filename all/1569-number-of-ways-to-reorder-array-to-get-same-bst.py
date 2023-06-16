'''
2023/06/16 daily challenge

divide and conquer + depth first search approach

learnt from official solution
'''

import math


class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        def dfs(nums):
            m = len(nums)
            if m < 3:
                # only 1 possible permutation for 0, 1, 2 nodes.
                return 1
            '''
            nums[0] is the root node of the current subtree.
            divide it into 2 parts and then conquer it respectively.
            '''
            left_nums = [v for v in nums if v < nums[0]]
            right_nums = [v for v in nums if v > nums[0]]

            '''
                            len(left_nums) or len(right_nums)
            left * right * C
                            m-1 # root node nums[0] excluded.
            '''
            return dfs(left_nums) * dfs(right_nums) * math.comb(m - 1, len(left_nums)) % 1_000_000_007

        # subtract one permutation (the original input) as question asked.
        return (dfs(nums)-1) % 1_000_000_007

