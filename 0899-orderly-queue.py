'''
2022/11/06 daily challenge

learnt from the official solution.

for k>=2 case, it's possible to sort the s string
which can be fully lexicographical after many step of moves,
because we can swap one of the first 2 alphabets and the end of alphabet many times.

for k=1 case, we can only rotate the string
by swapping only the first and the end of alphabets,
so we can just find the lexicographically smallest string
from all rotated-only permutation of string.
'''

class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k == 1:
            return min(s[i:] + s[:i] for i in range(len(s)))  # get the minimum of rotated permutations.
        # for k >= 2:
        return ''.join(sorted(s))  # sort the s directly.
