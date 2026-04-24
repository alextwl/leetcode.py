'''
hash map approach
'''


class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        c2i = dict()
        for i, c in enumerate(s):
            c2i[c] = i
        ans = 0
        for i, c in enumerate(t):
            ans += abs(c2i[c] - i)
        return ans

