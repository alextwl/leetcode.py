'''
2025/10/13 daily challenge

counter approach
'''

import collections


class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        last_ctr = None
        ans = []
        for w in words:
            ctr = collections.Counter(w)
            if ctr != last_ctr:
                ans.append(w)
                last_ctr = ctr
        return ans

