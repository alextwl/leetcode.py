'''
counter approach

do not manipulate the parentheses if it's outermost according to counts.
'''


class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        opened = 0
        for c in s:
            if c == '(':
                if opened:
                    stack.append(c)
                opened += 1
            else:
                if opened > 1:
                    stack.append(c)
                opened -= 1
        return ''.join(stack)

