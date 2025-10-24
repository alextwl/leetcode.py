'''
2025/10/24 daily challenge

brute force method approach

since the input was smaller than or equal to 10**6,
the last numerically balanced number is 1224444,
so we try to iterate from n+1 to 1224444.
'''


import collections


class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        for i in range(n+1, 1_224_445):
            if all(int(k) == v for k, v in collections.Counter(str(i)).items()):
                return i

