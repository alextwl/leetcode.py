'''
2024/06/05 daily challenge

counter approach
'''

import collections


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        it = iter(words)
        commons = collections.Counter(next(it))
        for w in it:
            curr = collections.Counter(w)
            for c in commons.keys():
                commons[c] = min(commons[c], curr[c])

        ans = []
        for c, v in commons.items():
            for _ in range(v):
                ans.append(c)

        return ans

