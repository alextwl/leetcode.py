'''
2022/12/17 daily challenge

stack approach
'''

import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []  # store only integers (operands)
        '''
        the problem requires division between two integers should truncate toward zero,
        so x//y will not work when one of the operand is negative (e.g. 6//-132 == -1).

        use math.trunc to truncate the float quotient to nearest integer toward zero.
        '''
        operators = {'+': lambda x, y: x+y,
                     '-': lambda x, y: x-y,
                     '*': lambda x, y: x*y,
                     '/': lambda x, y: math.trunc(x/y)
                    }
        
        for t in tokens:
            fn = operators.get(t)
            if fn is None:
                # current token is an integer
                stack.append(int(t))
            else:
                # current token is an arithmetic operator
                operand2 = stack.pop()
                operand1 = stack.pop()
                stack.append(fn(operand1, operand2))
                #print("%d%s%d = %d" % (operand1, t, operand2, stack[-1]))
        
        return stack[-1]

