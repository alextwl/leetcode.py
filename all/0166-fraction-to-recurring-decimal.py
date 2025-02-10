'''
stack approach

implement long division by stack
'''


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        ans = []
        stack = []  # for remainders

        # determine the sign
        negative_flag = (numerator < 0) ^ (denominator < 0)

        denominator = abs(denominator)
        quo, rem = divmod(abs(numerator), denominator)
        # build decimal part
        ans.append(str(quo))

        # build fraction part
        fraction = []
        # long division
        # when we found a duplicate remainder, it starts repeating.
        while rem not in stack:
            stack.append(rem)
            quo, rem = divmod(rem * 10, denominator)
            fraction.append(str(quo))

        # add parentheses
        i = stack.index(rem)
        if i == len(fraction) - 1 and fraction[i] == '0':
            # for repeating '(0)' case (== divided evenly)
            fraction.pop()
        else:
            fraction.insert(i, '(')
            fraction.append(')')

        # build answer
        if fraction:
            ans.append('.')
            ans.extend(fraction)
        
        # prevent '-0' case
        if negative_flag and ans != ['0']:
            ans.insert(0, '-')

        return ''.join(ans)

