'''
2025/1/13 daily challenge

math approach

Induction:
the length of each alphabets -> remainings after chars removed
1 -> 1,
2 -> 2,
3 -> 1,
4 -> 2,
5 -> 1,
6 -> 2, ... and so on.
'''


import collections


class Solution:
    def minimumLength(self, s: str) -> int:
        return sum(((v-1) & 1) + 1 for v in collections.Counter(s).values())

