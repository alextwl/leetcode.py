'''
2024/08/06 daily challenge

counter approach
'''

import collections


class Solution:
    def minimumPushes(self, word: str) -> int:
        pushes = 0
        multiplier = 1
        i = 0
        # let letters with higher frequencies be inputted by lower pushes
        for freq in sorted(collections.Counter(word).values(), reverse=True):
            pushes += freq * multiplier
            i += 1
            # only [2..9] total 8 buttons can be remapped
            if i == 8:
                i = 0
                multiplier += 1

        return pushes

