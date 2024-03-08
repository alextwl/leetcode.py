'''
2024/03/08 daily challenge

counter approach
'''

import collections


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        c = collections.Counter(nums)
        keyfreq = c.most_common()
        
        max_freq = keyfreq[0][1]
        ans = 0
        for _, f in keyfreq:
            if f != max_freq:
                break
            ans += f
        
        return ans

