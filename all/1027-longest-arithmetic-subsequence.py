'''
2023/06/23 daily challenge

dynamic programming approach

learnt from official solution
https://leetcode.com/problems/longest-arithmetic-subsequence/solution/

try to divide the problem into smaller problem by
evaluating from the smallest subsequence to the full sequence.
'''

class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        '''
        dp[(right end, difference)] =
        the length of arithmetic subsequence with step of length=diff
        in the range of nums[0:right+1]
        '''
        dp = {}
        
        for right in range(len(nums)):
            for left in range(right):
                diff = nums[right] - nums[left]
                '''
                the subsequence can be extended
                from [..., nums[left]] to [..., nums[left], nums[right]].
                
                since any single element could be a length-one subsequence,
                any dp[] length defaults to 1.
                '''
                dp[(right, diff)] = dp.get((left, diff), 1) + 1
        
        return max(dp.values())

