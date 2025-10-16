'''
2025/10/16 daily challenge

greedy method approach

learnt from official editorial:
https://leetcode.com/problems/smallest-missing-non-negative-integer-after-operations/editorial/#approach-greedy

count nums modulo value and maximize MEX gradually.
'''


import collections


class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        cnt = collections.defaultdict(int)
        for v in nums:
            # add/subtract value to/from v multiple times to
            # make v non-negative and a modulo of value so that we can know
            # if there's enough count for filling current slot
            cnt[v % value] += 1

        mex = 0
        while cnt[mod := mex % value]:
            cnt[mod] -= 1
            mex += 1
        return mex

