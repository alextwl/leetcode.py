'''
2026/10/03 daily challenge

stack approach
'''


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]  # init with a dummy index for ')' beginning input.
        max_len = 0

        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_len = max(max_len, i - stack[-1])
        return max_len

