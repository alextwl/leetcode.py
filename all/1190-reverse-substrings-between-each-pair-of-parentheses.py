'''
2024/07/11 daily challenge

stack approach
'''


class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = [[]]

        for c in s:
            if c == '(':
                stack.append(list())
            elif c == ')':
                sub = stack.pop()[::-1]
                stack[-1].extend(sub)
            else:
                stack[-1].append(c)

        return ''.join(stack[0])

