'''
2022/10/11 daily challenge

learnt from
https://leetcode.com/problems/increasing-triplet-subsequence/discuss/78993/Clean-and-short-with-comments-C%2B%2B

time=O(n)

note: the problem does not require
the exact triple of indices & values to be returned,
so this solution only checks the existance of a triplet
but does *NOT* track its values & indexes.
'''


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        '''
        the minimum values of possible nums[i] & nums[j].
        
        note the final i & j may *NOT* be the _same_ pair of a triplet,
        it's used only for the later if-condition checking.
        '''
        i = j = float('inf')
        
        for n in nums:
            if n <= i:
                # the minimum number (of left) so far.
                i = n
            elif n <= j:
                # i < n <= j, second number of a triplet exists
                j = n
            else:
                # i < j < n <= k, third number of a triplet exists,
                # so a valid triple is found.
                return True
        
        # triplet not found.
        return False
