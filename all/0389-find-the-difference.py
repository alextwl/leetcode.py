'''
2023/09/25 daily challenge

XOR approach
'''


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ans = 0
        for c in s:
            ans ^= ord(c)
        for c in t:
            ans ^= ord(c)

        return chr(ans)


'''
Counter approach
'''

import collections


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counter = collections.Counter(t) - collections.Counter(s)
        return counter.most_common(1)[0][0]

