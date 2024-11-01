'''
2024/11/01 daily challenge

stack approach
'''


class Solution:
    def makeFancyString(self, s: str) -> str:
        stack = []
        for c in s:
            if not (len(stack) > 1 and stack[-2] == stack[-1] == c):
                stack.append(c)
        return ''.join(stack)

