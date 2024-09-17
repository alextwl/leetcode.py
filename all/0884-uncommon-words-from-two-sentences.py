'''
2024/09/17 daily challenge

counter approach
'''

import collections


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        c = collections.Counter(s1.split(' ') + s2.split(' '))
        return [k for k, v in c.items() if v == 1]

