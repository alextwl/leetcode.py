'''
2023/12/11 daily challenge

counter approach
'''

import collections


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        cnt = collections.defaultdict(int)        
        threshold = len(arr) // 4

        for num in arr:
            cnt[num] += 1
            if cnt[num] > threshold:
                return num

        # undefined behavior
        return None

