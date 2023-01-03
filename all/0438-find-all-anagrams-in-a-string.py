'''
leetcode 75 lv1 day 12

counter approach
'''

import collections
import functools


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        plen = len(p)
        if len(s) < plen:
            return []

        counts = collections.Counter(p)
        isAnagram = lambda: not(functools.reduce(lambda x,y: x|y, counts.values()))
        ans = []

        siter = enumerate(s)
        # verify initial subsequence
        for _ in range(plen):
            _, c = next(siter)
            counts[c] -= 1
        if isAnagram():
            ans.append(0)
        
        # continue finding anagrams
        for i, c in siter:
            counts[c] -= 1
            counts[s[i-plen]] += 1
            if isAnagram():
                ans.append(i-plen+1)

        return ans

