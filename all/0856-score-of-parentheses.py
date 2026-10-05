'''
2026/10/05 daily challenge

stack approach

double the sum of scores when closing non-empty parentheses.
'''


class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [[]]
        for c in s:
            if c == '(':
                stack.append(list())
            else:
                # closing bracket
                if not stack[-1]:
                    stack.pop()
                    stack[-1].append(1)
                else:
                    score = sum(stack.pop()) * 2
                    stack[-1].append(score)
        return sum(stack[0])

