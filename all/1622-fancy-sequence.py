'''
2026/03/15 daily challenge

prefix sums/multipliers + modular multiplicative inverse approach

learnt from official editorial:
https://leetcode.com/problems/fancy-sequence/editorial/#introduction
'''


MOD = 1_000_000_007


def quickmul(a, m):
    return pow(a, m, MOD)


def inverse(a):
    # Fermat's little theorem
    # a**(m-1) = 1 (mod m)
    # a**(m-1) * a**(-1) = a**(-1) (mod m)
    # a**(m-2) * a * a**(-1) = a**(-1) (mod m)
    # a**(m-2) = a**(-1) (mod m)
    #
    # so the remainder of multiplicative inverse of 'a' with modulus 10**9+7
    # is (a**(10**9+7 - 2)) % (10**9+7).
    return quickmul(a, MOD - 2)


class Fancy:

    def __init__(self):
        self.x = []
        # prefix components of ax + b
        self.a = [1]
        self.b = [0]

    def append(self, val: int) -> None:
        self.x.append(val)
        self.a.append(self.a[-1])
        self.b.append(self.b[-1])

    def addAll(self, inc: int) -> None:
        self.b[-1] = (self.b[-1] + inc) % MOD

    def multAll(self, m: int) -> None:
        self.a[-1] = self.a[-1] * m % MOD
        self.b[-1] = self.b[-1] * m % MOD

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.x):
            return -1

        # the last state of self.x[idx] is
        # self.x[idx] * (self.a[-1] / self.a[idx]) + \
        # self.b[-1] - self.b[idx] * (self.a[-1] / self.a[idx]).
        #
        # since the components of ax+b might become very large,
        # to cancel multAll ops before idx from self.a[-1] without hassle,
        # convert (self.a[-1] / self.a[idx]) by multiplicative inverse.
        a = inverse(self.a[idx]) * self.a[-1]
        b = self.b[-1] - self.b[idx] * a

        return (a * self.x[idx] + b) % MOD

