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


'''
one-pass ver
'''

import collections


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        keyfreq = collections.defaultdict(int)
        max_freq = 0
        ans = 0
        
        for k in nums:
            keyfreq[k] += 1
            
            if keyfreq[k] > max_freq:
                # reset the max & sum because a newer maxmimum is found
                ans = max_freq = keyfreq[k]
            elif keyfreq[k] == max_freq:
                # one more value with the max frequency
                ans += max_freq

        return ans

