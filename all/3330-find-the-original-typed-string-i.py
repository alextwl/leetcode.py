'''
2025/07/01 daily challenge

counter approach
'''


class Solution:
    def possibleStringCount(self, word: str) -> int:
        prev = None
        duplicates = 1
        running_len = 0
        for c in word:
            if prev == c:
                running_len += 1
            else:
                if running_len > 1:
                    duplicates += running_len - 1
                prev = c
                running_len = 1

        # for the last batch
        if running_len > 1:
                duplicates += running_len - 1
        return duplicates


'''
simpler one-pass ver
'''


import itertools


class Solution:
    def possibleStringCount(self, word: str) -> int:
        duplicates = 1
        for prev, curr in itertools.pairwise(word):
            if prev == curr:
                duplicates += 1
        return duplicates

