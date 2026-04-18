'''
2026/04/18 daily challenge

string conversion approach
'''


class Solution:
    def mirrorDistance(self, n: int) -> int:
        return abs(n - int(str(n)[::-1]))


'''
base10 division & multiplication approach
'''


class Solution:
    def mirrorDistance(self, n: int) -> int:
        m = n
        rev = 0
        while m:
            m, rem = divmod(m, 10)
            rev = (rev * 10) + rem
        return abs(n - rev)

