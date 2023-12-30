'''
2023/12/30 daily challenge

counter approach
'''

import collections


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n = len(words)
        counter = collections.Counter()

        for w in words:
            counter += Counter(w)

        for v in counter.values():
            if v % n:
                return False

        return True

