'''
leetcode 75 lv2 day 18

stack approach

always evaulate multiplication/division first,
and then evaulate addition/subtraction later.
'''


class Solution:
    def calculate(self, s: str) -> int:
        opfunc = {'+': lambda a,b: a+b,
                  '-': lambda a,b: a-b,
                  '*': lambda a,b: a*b,
                  '/': lambda a,b: a//b}
        stack = []
        digits = ""  # buffer to build operands
        for c in s:
            if c == ' ':
                continue
            elif c.isdigit():
                digits = digits + c
            else:
                # calculate last multiplication or division if available
                if stack and stack[-1] in ['*', '/']:
                    op = opfunc[stack.pop()]
                    val = op(stack.pop(), int(digits))
                    stack.append(val)
                else:
                    # c == '+' or '-'
                    stack.append(int(digits))
                # always queue current operator
                stack.append(c)
                digits = ""
        
        # calculate last mult/div again if available
        if stack and stack[-1] in ['*', '/']:
            op = opfunc[stack.pop()]
            val = op(stack.pop(), int(digits))
            stack.append(val)
        else:
            stack.append(int(digits))
        
        # proceed add/subtract parts
        stack.reverse()
        opnd1 = stack.pop()
        while(stack):
            op = opfunc[stack.pop()]
            opnd2 = stack.pop()
            opnd1 = op(opnd1, opnd2)

        return opnd1

