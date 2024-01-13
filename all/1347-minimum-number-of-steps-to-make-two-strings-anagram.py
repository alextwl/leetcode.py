'''
2024/01/13 daily challenge

counter approach
'''

import collections


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count_s = collections.Counter(s)
        count_t = collections.Counter(t)
        
        ans = 0
        for c, req in count_s.items():
            if count_t[c] < req:
                ans += req - count_t[c]

        return ans

