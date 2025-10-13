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


'''
oneliner ver (sorting approach)

groupby functions groups consecutive elements which have the same key,
and we use sorted function as key mapped from words, iterate only the
first element returned from each group's iterator.
'''


import itertools


class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        return [next(grp_iter) for _, grp_iter in itertools.groupby(words, key=sorted)]

