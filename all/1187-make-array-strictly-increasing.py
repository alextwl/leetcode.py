'''
2023/06/17 daily challenge

bottom-up dynamic programming + binary search approach

learnt from official solution 2:
https://leetcode.com/problems/make-array-strictly-increasing/solution/
'''

import bisect
import collections


class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2.sort()
        '''
        dp[previous value] = the minimum number of operations needed to reach the state
        init with dp[-1] = 0 op because -1 < 0 <= arr[i].
        '''
        dp = {-1: 0}
        n2 = len(arr2)
        
        for i, val in enumerate(arr1):
            # assume we need infinite operations to reach new states and try to minimize it.
            new_dp = collections.defaultdict(lambda: float('inf'))
            
            for prev, prev_ops in dp.items():
                if val > prev:
                    '''
                    arr1[i] value can be reached either from
                    (1) a previous smaller value (no operation performed),
                        arr1[i] unchanged, or
                    (2) a new state which changed arr1[i].
                    '''
                    new_dp[val] = min(prev_ops, new_dp[val])
                '''
                try to replace arr1[i] with arr2[j] (which must be greater than prev),
                need 1 operation.
                '''
                j = bisect.bisect_right(arr2, prev)
                if j < n2:
                    new_dp[arr2[j]] = min(new_dp[arr2[j]], 1 + prev_ops)
                dp = new_dp
        
        if dp:
            return min(dp.values())
        
        # couldn't make arr1 strictly increasing
        return -1

