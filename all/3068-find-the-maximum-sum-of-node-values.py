'''
2024/05/19 daily challenge

top-down dynamic programming approach

learnt from official solution:
https://leetcode.com/problems/find-the-maximum-sum-of-node-values/solution/

hint: for any pair of non-adjacent nodes u & v,
applying XOR ops for all edges between u & v results in
u & v modified while all nodes between them are unchanged
due to the nature of XOR operation.

[u ^ k, p1 ^ k ^ k, ..., pn ^ k ^ k, v ^ k] = [u ^ k, p1, ..., pn, v ^ k]
'''

import functools


class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        n = len(nums)

        @functools.cache
        def maxSum(i, isEven):
            if i == n:
                # check the parity of the number of modified nodes
                # we need even XOR-modified nodes for effective operation
                return 0 if isEven else float('-inf')
            
            # not to perform XOR on nums[i]
            non_xor_sum = nums[i] + maxSum(i + 1, isEven)
            # to perform XOR on nums[i]
            xor_sum = (nums[i] ^ k) + maxSum(i + 1, isEven ^ 1)
            
            return max(non_xor_sum, xor_sum)
        
        # start from selecting nums[i] as root with no nodes modified (so isEven flag is set)
        return maxSum(0, 1)

