'''
2024/08/23 daily challenge

convert all denominators to the LCM,
and convert the sum of fractions to an irreducible fraction
by dividing its numerator and denominator by GCD.
'''


import functools
import math


class Solution:
    def fractionAddition(self, expression: str) -> str:
        numerators = []
        denominators = []

        n = list()
        d = list()

        it = iter(expression)
        # for the first fraction is a negative
        if expression[0] == '-':
            next(it)
            n.append('-')

        # convert expression
        for c in it:
            if c == '/':
                n, d = d, n
            elif c == '+' or c == '-':
                n, d = d, n
                numerators.append(int(''.join(n)))
                denominators.append(int(''.join(d)))
                n = list()
                d = list()
                if c == '-':
                    n.append('-')
            else:
                n.append(c)
        else:
            # push the last fraction
            n, d = d, n
            numerators.append(int(''.join(n)))
            denominators.append(int(''.join(d)))

        # convert all denominators to the least common multiple
        lcm = math.lcm(*denominators)

        @functools.cache
        def multiple_to_lcm(d):
            return lcm // d

        for i, d in enumerate(denominators):
            numerators[i] *= multiple_to_lcm(d)

        numerator_sum = sum(numerators)
        if numerator_sum == 0:
            return "0/1"
        elif numerator_sum == 1 or numerator_sum == -1:
            return str(numerator_sum) + "/" + str(lcm)

        gcd = math.gcd(numerator_sum, lcm)
        numerator_sum //= gcd
        lcm //= gcd

        return str(numerator_sum) + "/" + str(lcm)

