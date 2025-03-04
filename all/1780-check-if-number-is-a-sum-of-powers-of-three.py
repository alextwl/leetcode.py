'''
2025/03/04 daily challenge

recursion approach
'''


class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        # cache powers of 3's
        self.powers = []
        curr = 1
        while curr <= n:
            self.powers.append(curr)
            curr *= 3
        return self._check(n, len(self.powers) - 1)
        
    def _check(self, r, i):
        if r == 0:
            return True
        if i < 0 or r < 0 or self.powers[i] > r:
            return False
        i -= 1
        add_pow = self._check(r - self.powers[i], i)
        skip_pow = self._check(r, i)
        return add_pow or skip_pow


'''
math + greedy method approach

always pick the power up in the descending order.

actually we cannot skip any power in each round or we cannot form the sum.
'''


class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        # cache powers of 3's
        powers = []
        curr = 1
        while curr <= n:
            powers.append(curr)
            curr *= 3
        
        while n > 0 and powers:
            next_pow = powers.pop()
            if n >= next_pow:
                n -= next_pow
            if n >= next_pow:
                # the problem asks for **distinct** powers, no duplicates allowed.
                # the remaining powers are impossible to form the current n.
                return False
        return True


'''
bitwise (3-ary, ternary) approach

learnt from official editorial 3:
https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/editorial/#approach-3-ternary-representation

consider the powers of 3 in ternary form:

3**0 = 1
3**1 = 10
3**2 = 100
3**3 = 1000
... and so on.

we can see any valid sum has only 0 or 1's bits in ternary:

e.g. n = 91 = 3**0 + 3**2 + 3**4 = 10101 in ternary

so if we can find any 2's bit, the input number is not a sum of powers of three.
'''


class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n:
            n, rem = divmod(n, 3)
            if rem == 2:
                return False
        return True

